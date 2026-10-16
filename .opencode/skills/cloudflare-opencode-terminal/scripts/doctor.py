#!/usr/bin/env python3
"""Audit konfigurasi lokal, tanpa membaca nilai secret atau mengubah file."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import tomllib
from pathlib import Path


def parse_jsonc(source: str) -> dict:
    """Parse JSONC dengan komentar dan trailing comma tanpa merusak string."""
    out: list[str] = []
    i, in_string, escaped = 0, False, False
    while i < len(source):
        ch = source[i]
        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue
        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
        elif source.startswith("//", i):
            end = source.find("\n", i)
            i = len(source) if end < 0 else end
        elif source.startswith("/*", i):
            end = source.find("*/", i + 2)
            if end < 0:
                raise ValueError("Komentar JSONC tidak ditutup.")
            out.append(" ")
            out.extend("\n" for c in source[i:end + 2] if c == "\n")
            i = end + 2
        else:
            out.append(ch)
            i += 1
    cleaned = "".join(out)
    out, i, in_string, escaped = [], 0, False, False
    while i < len(cleaned):
        ch = cleaned[i]
        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
            if ch == ",":
                nxt = i + 1
                while nxt < len(cleaned) and cleaned[nxt].isspace():
                    nxt += 1
                if nxt < len(cleaned) and cleaned[nxt] in "]}":
                    i += 1
                    continue
            out.append(ch)
        i += 1
    value = json.loads("".join(out))
    if not isinstance(value, dict):
        raise ValueError("Config harus berupa object.")
    return value


def inspect(project: Path) -> dict:
    project = project.resolve()
    findings: list[dict[str, str]] = []

    def add(level: str, code: str, message: str) -> None:
        findings.append({"level": level, "code": code, "message": message})

    configs = [project / name for name in
               ("wrangler.jsonc", "wrangler.json", "wrangler.toml")
               if (project / name).is_file()]
    if not configs:
        add("error", "CONFIG_MISSING", "Konfigurasi Wrangler tidak ditemukan.")
        return {"config": None, "findings": findings}
    if len(configs) > 1:
        add("warning", "MULTIPLE_CONFIGS",
            "Ada beberapa config. Pastikan CLI memakai satu sumber yang benar.")
    config_file = configs[0]
    try:
        raw = config_file.read_text(encoding="utf-8-sig")
        config = tomllib.loads(raw) if config_file.suffix == ".toml" else parse_jsonc(raw)
    except (ValueError, OSError):
        add("error", "CONFIG_INVALID", "Config tidak dapat diparse. Nilainya tidak ditampilkan.")
        return {"config": config_file.name, "findings": findings}

    if not config.get("name"):
        add("error", "NAME_MISSING", "Nama Worker belum diatur.")
    try:
        date = dt.date.fromisoformat(config.get("compatibility_date", ""))
        if date > dt.datetime.now(dt.timezone.utc).date():
            add("warning", "FUTURE_DATE", "Tanggal kompatibilitas berada di masa depan UTC.")
    except (ValueError, TypeError):
        add("error", "DATE_INVALID", "compatibility_date harus berformat YYYY-MM-DD.")

    if not config.get("main") and not config.get("assets"):
        add("error", "ENTRY_MISSING", "Config memerlukan main atau direktori assets.")
    main = config.get("main")
    if isinstance(main, str) and not (project / main).is_file():
        add("error", "MAIN_MISSING", "Entrypoint yang disebut config tidak ada.")
    assets = config.get("assets", {})
    if isinstance(assets, dict) and assets:
        directory = assets.get("directory")
        if not isinstance(directory, str) or not (project / directory).is_dir():
            add("warning", "ASSETS_MISSING", "Folder assets belum ada. Jalankan build yang benar.")
        if assets.get("not_found_handling") == "single-page-application":
            add("warning", "SPA_ROUTING",
                "Uji API typo dan callback agar tidak menjadi HTML 200 dari fallback SPA.")
        if assets.get("run_worker_first") is True:
            add("warning", "ALL_ASSETS_INVOKE",
                "Semua aset masuk Worker. Pastikan kebutuhan auth atau transformasinya jelas.")

    resource_fields = ("d1_databases", "kv_namespaces", "r2_buckets", "durable_objects",
                       "queues", "ai", "vectorize", "workflows")

    def check_section(section: dict, label: str) -> None:
        variables = section.get("vars", {})
        if isinstance(variables, dict):
            for key in variables:
                if re.search(r"(SECRET|PASSWORD|TOKEN|PRIVATE_KEY|API_KEY)", str(key), re.I):
                    add("error", "SECRET_IN_VARS",
                        label + ": ada nama variabel rahasia dalam vars. Pindahkan ke secrets.")
        for field in ("d1_databases", "kv_namespaces", "r2_buckets"):
            entries = section.get(field, [])
            if not isinstance(entries, list):
                add("error", "BINDING_SHAPE", label + ": bentuk daftar binding salah.")
                continue
            for entry in entries:
                if not isinstance(entry, dict):
                    add("error", "BINDING_SHAPE", label + ": entri binding harus object.")
                    continue
                for value in entry.values():
                    if isinstance(value, str) and (
                        "<" in value or "REPLACE_" in value or "YOUR_" in value
                    ):
                        add("error", "PLACEHOLDER_BINDING",
                            label + ": binding masih memuat placeholder.")
                        break
        triggers = section.get("triggers", {})
        if isinstance(triggers, dict):
            for cron in triggers.get("crons", []):
                if isinstance(cron, str) and cron.split()[:1] == ["*"]:
                    add("warning", "FREQUENT_CRON",
                        label + ": cron setiap menit tetap aktif saat tidak ada pengguna.")
        if section.get("ai"):
            add("info", "REMOTE_AI", label + ": AI binding dapat memakai layanan/kuota remote.")

    check_section(config, "root")
    environments = config.get("env", {})
    if isinstance(environments, dict):
        for name, section in environments.items():
            if not isinstance(section, dict):
                add("error", "ENV_SHAPE", "Environment harus berupa object.")
                continue
            check_section(section, "env")
            if any(config.get(field) and field not in section for field in resource_fields):
                add("warning", "ENV_BINDINGS",
                    "Environment memiliki binding root yang belum dideklarasikan ulang. Periksa inheritance.")

    obs = config.get("observability", {})
    if not isinstance(obs, dict) or not obs.get("enabled"):
        add("info", "OBSERVABILITY", "Periksa kebutuhan log terstruktur dan observability.")
    ignore = project / ".gitignore"
    ignore_text = ignore.read_text(encoding="utf-8") if ignore.is_file() else ""
    if not any(line.strip() in {".dev.vars", ".dev.vars*", ".dev.vars.*"}
               for line in ignore_text.splitlines()):
        add("warning", "SECRET_IGNORE", "Pastikan .dev.vars dan variasinya tidak masuk git.")
    if not any((project / f).is_file() for f in
               ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb")):
        add("info", "LOCKFILE", "Lockfile belum ada. Buat setelah memasang dependency proyek.")
    return {"config": config_file.name, "findings": findings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--json", action="store_true", help="Keluarkan hasil JSON.")
    parser.add_argument("--strict", action="store_true", help="Warning juga memberi exit code 1.")
    args = parser.parse_args()
    if not args.project.is_dir():
        parser.error("Folder proyek tidak ditemukan.")
    result = inspect(args.project)
    result["scope"] = "Audit statis lokal. Tidak memverifikasi schema resmi, secret remote, DNS atau billing."
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Config:", result["config"] or "tidak ada")
        for row in result["findings"]:
            print(f'{row["level"].upper()} {row["code"]}: {row["message"]}')
        print(result["scope"])
    failed = any(f["level"] == "error" or (args.strict and f["level"] == "warning")
                 for f in result["findings"])
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
