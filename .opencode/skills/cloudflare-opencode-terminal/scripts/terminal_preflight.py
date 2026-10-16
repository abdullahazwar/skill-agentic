#!/usr/bin/env python3
"""Audit lokal OpenCode dan terminal. Tidak login, install atau deploy."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

from doctor import parse_jsonc

NAME = "cloudflare-opencode-terminal"


def inspect_terminal(project: Path, probe: bool = False) -> dict:
    project = project.expanduser().resolve()
    findings: list[dict[str, str]] = []

    def add(level: str, code: str, message: str) -> None:
        findings.append({"level": level, "code": code, "message": message})

    executables = {name: shutil.which(name) for name in ("opencode", "node", "npm", "git", "gh")}
    if not executables["opencode"]:
        add("warning", "OPENCODE_MISSING", "OpenCode tidak ditemukan di PATH.")
    if not executables["node"] or not executables["npm"]:
        add("warning", "NODE_TOOLCHAIN", "Node/npm belum lengkap pada PATH.")
    config_paths = [project / name for name in ("opencode.jsonc", "opencode.json")
                    if (project / name).is_file()]
    if len(config_paths) > 1:
        add("warning", "MULTIPLE_CONFIG", "Ada dua config OpenCode. Periksa precedence.")
    for path in config_paths:
        try:
            config = parse_jsonc(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError):
            add("error", "CONFIG_INVALID", "Config OpenCode tidak dapat diparse. Isi tidak ditampilkan.")
            continue
        if "permissions" in config and "permission" not in config:
            add("warning", "SCHEMA_VARIANT", "Config memakai permissions. Cocokkan dengan versi/schema lokal.")
        permission = config.get("permission")
        if permission == "deny":
            add("warning", "PERMISSION_DENY", "Permission umum deny. Periksa kebijakan efektif.")
        if isinstance(permission, dict):
            skill = permission.get("skill")
            if skill == "deny" or (isinstance(skill, dict) and skill.get(NAME) == "deny"):
                add("warning", "SKILL_DENIED", "Rule lokal menolak skill ini.")
        tools = config.get("tools")
        if isinstance(tools, dict) and tools.get("skill") is False:
            add("warning", "SKILL_DISABLED", "Tool skill dinonaktifkan pada config lokal.")
    if not (project / ".opencode/skills" / NAME / "SKILL.md").is_file():
        add("info", "NO_PROJECT_SKILL", "Skill tidak berada di proyek. Instalasi global mungkin tetap tersedia.")
    if not any((project / n).is_file() for n in ("wrangler.jsonc", "wrangler.json", "wrangler.toml")):
        add("info", "NO_WRANGLER_CONFIG", "Folder ini belum memiliki config Wrangler.")

    probes = {}
    if probe:
        for name in ("opencode", "node", "npm", "git"):
            if not executables[name]:
                continue
            try:
                result = subprocess.run([executables[name], "--version"], cwd=project,
                                        capture_output=True, text=True, timeout=15)
                match = re.search(r"\b\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?\b",
                                  result.stdout + result.stderr)
                probes[name] = {"exit_code": result.returncode,
                                "version": match.group(0) if match else None}
            except (OSError, subprocess.TimeoutExpired):
                probes[name] = {"error": "VERSION_UNAVAILABLE"}
        if executables["opencode"]:
            try:
                result = subprocess.run([executables["opencode"], "--help"], cwd=project,
                                        capture_output=True, text=True, timeout=15)
                text = result.stdout + result.stderr
                probes["opencode_help"] = {
                    "exit_code": result.returncode,
                    "has_agent_flag": "--agent" in text,
                    "has_run_command": bool(re.search(r"\b(?:opencode )?run\b", text)),
                }
            except (OSError, subprocess.TimeoutExpired):
                probes["opencode_help"] = {"error": "HELP_UNAVAILABLE"}
    return {"executables": {name: bool(path) for name, path in executables.items()},
            "probes": probes, "findings": findings,
            "scope": "Pemeriksaan statis lokal. Tidak mengevaluasi seluruh policy gabungan atau autentikasi akun."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--probe", action="store_true", help="Jalankan version/help dengan timeout.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.project.is_dir():
        parser.error("Folder proyek tidak ditemukan.")
    result = inspect_terminal(args.project, args.probe)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Tools:", ", ".join(k for k, present in result["executables"].items() if present) or "tidak ada")
        for row in result["findings"]:
            print(row["level"].upper(), row["code"] + ":", row["message"])
        if args.probe:
            print(json.dumps(result["probes"], ensure_ascii=False))
        print(result["scope"])
    raise SystemExit(any(row["level"] == "error" for row in result["findings"]))
