#!/usr/bin/env python3
"""Pasang skill OpenCode tanpa menimpa berkas atau konfigurasi yang berbeda."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

NAME = "cloudflare-opencode-terminal"
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".wrangler", ".pytest_cache"}


def excluded(name: str) -> bool:
    return (name in SKIP_DIRS or name.endswith(".pyc")
            or (name.startswith((".env", ".dev.vars"))
                and name not in {".env.example", ".dev.vars.example"}))


def snapshot(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}

    def visit(directory: Path) -> None:
        for item in directory.iterdir():
            if excluded(item.name):
                continue
            if item.is_symlink():
                raise ValueError("Symlink tidak dipasang otomatis: " + str(item))
            if item.is_dir():
                visit(item)
            elif item.is_file():
                result[str(item.relative_to(root))] = hashlib.sha256(item.read_bytes()).hexdigest()
    visit(root)
    return result


def install(source: Path, config: Path, with_agent: bool = False,
            with_commands: bool = False, dry_run: bool = False) -> dict:
    source = source.resolve()
    config = config.expanduser().absolute()
    frontmatter = (source / "SKILL.md").read_text(encoding="utf-8")
    if not re.search(r"(?m)^name: " + re.escape(NAME) + r"\s*$", frontmatter):
        raise ValueError("Source bukan skill cloudflare-opencode-terminal.")
    source_files = snapshot(source)
    target = config / "skills" / NAME
    plan = [{"source": source, "target": target, "directory": True}]
    if with_agent:
        plan.append({"source": source / "assets/opencode/agents/cloudflare-terminal.md",
                     "target": config / "agents/cloudflare-terminal.md", "directory": False})
    if with_commands:
        for name in ("cf-audit.md", "cf-implement.md", "cf-deploy.md"):
            plan.append({"source": source / "assets/opencode/commands" / name,
                         "target": config / "commands" / name, "directory": False})

    def reject_symlink_path(path: Path) -> None:
        for component in (path, *path.parents):
            if component.is_symlink():
                raise ValueError("Path symlink perlu dipilih secara eksplisit sebagai lokasi nyata: " + str(component))

    for entry in plan:
        dest, src = entry["target"], entry["source"]
        reject_symlink_path(dest)
        if not src.exists():
            raise ValueError("Resource pemasangan tidak ditemukan.")
        if dest.resolve() != source and dest.resolve().is_relative_to(source):
            raise ValueError("Tujuan tidak boleh berada di dalam source skill.")
        if dest.exists():
            same = (dest.is_dir() and snapshot(dest) == source_files) if entry["directory"] else (
                dest.is_file() and dest.read_bytes() == src.read_bytes())
            if not same:
                raise FileExistsError("Tujuan sudah berisi file berbeda, tidak ditimpa: " + str(dest))
            entry["action"] = "already_present"
        else:
            entry["action"] = "create"

    output = [{"path": str(item["target"]), "action": item["action"]} for item in plan]
    if dry_run:
        return {"dry_run": True, "items": output}

    # Reservasi semua tujuan dengan mode eksklusif sebelum menyalin bytes.
    created: list[Path] = []
    try:
        for entry in plan:
            if entry["action"] != "create":
                continue
            dest = entry["target"]
            dest.parent.mkdir(parents=True, exist_ok=True)
            if entry["directory"]:
                dest.mkdir()
            else:
                with dest.open("xb"):
                    pass
            created.append(dest)
        for entry in plan:
            if entry["action"] != "create":
                continue
            src, dest = entry["source"], entry["target"]
            if entry["directory"]:
                shutil.copytree(src, dest, dirs_exist_ok=True,
                                ignore=lambda path, names: [n for n in names if excluded(n)])
            else:
                dest.write_bytes(src.read_bytes())
    except Exception:
        for item in reversed(created):
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink(missing_ok=True)
        raise
    return {"dry_run": False, "items": output}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", type=Path, help="Root proyek aplikasi tujuan.")
    group.add_argument("--global", dest="global_scope", action="store_true",
                       help="Pasang ke konfigurasi global OpenCode.")
    parser.add_argument("--config-dir", type=Path, help="Override config global, bukan root proyek.")
    parser.add_argument("--with-agent", action="store_true")
    parser.add_argument("--with-commands", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.config_dir and not args.global_scope:
        parser.error("--config-dir hanya berlaku bersama --global.")
    if args.project and not args.project.expanduser().is_dir():
        parser.error("Folder proyek tidak ada.")
    config = ((args.config_dir or Path.home() / ".config/opencode") if args.global_scope
              else args.project.expanduser().resolve() / ".opencode")
    try:
        result = install(Path(__file__).resolve().parents[1], config,
                         args.with_agent, args.with_commands, args.dry_run)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
