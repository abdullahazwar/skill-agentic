#!/usr/bin/env python3
"""Validasi struktur dan tautan lokal skill dengan pustaka standar Python."""
import json
import re
import sys
from pathlib import Path


def validate(root: Path) -> list[str]:
    errors = []
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        return ["SKILL.md tidak ditemukan."]
    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not match:
        return ["Frontmatter tidak valid."]
    fields = {}
    for line in match.group(1).splitlines():
        if ": " not in line:
            errors.append("Frontmatter harus berisi field satu baris.")
            continue
        key, value = line.split(": ", 1)
        fields[key] = value
    if set(fields) != {"name", "description"}:
        errors.append("Frontmatter harus memiliki name dan description saja.")
    # Work Mode dapat memakai ID folder canonical saat skill disimpan.
    canonical_work_folder = bool(re.fullmatch(r"skill-[a-f0-9]{32}", root.name))
    if fields.get("name") != root.name and not canonical_work_folder:
        errors.append("Nama folder dan name berbeda.")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", fields.get("name", "")):
        errors.append("Nama skill tidak valid.")
    if len(content.splitlines()) > 500:
        errors.append("SKILL.md melebihi 500 baris.")
    if not 1 <= len(fields.get("description", "")) <= 1024:
        errors.append("Description harus 1 sampai 1024 karakter.")
    if "TODO" in content:
        errors.append("SKILL.md masih memiliki TODO.")
    for file in root.rglob("*.md"):
        if any(part in {"node_modules", ".wrangler"} for part in file.parts):
            continue
        text = file.read_text(encoding="utf-8")
        if "\u2014" in text:
            errors.append(str(file.relative_to(root)) + ": mengandung tanda pisah panjang.")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                continue
            target = (file.parent / link.split("#")[0]).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(str(file.relative_to(root)) + ": tautan keluar folder skill.")
            elif not target.exists():
                errors.append(str(file.relative_to(root)) + ": tautan lokal tidak ada: " + link)
    for required in ("agents/openai.yaml", "scripts/doctor.py", "scripts/estimasi.py",
                     "scripts/install_opencode.py", "scripts/terminal_preflight.py",
                     "assets/opencode/agents/cloudflare-terminal.md",
                     "assets/opencode/commands/cf-audit.md",
                     "assets/opencode/commands/cf-implement.md",
                     "assets/opencode/commands/cf-deploy.md",
                     "assets/opencode/opencode.minimal.json",
                     "assets/worker-starter/package.json", "assets/sql/0001_initial.sql"):
        if not (root / required).is_file():
            errors.append("Resource wajib tidak ada: " + required)
    try:
        json.loads((root / "assets/worker-starter/package.json").read_text())
    except (ValueError, OSError):
        errors.append("package.json starter tidak valid.")
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    problems = validate(root)
    for problem in problems:
        print("ERROR:", problem)
    if not problems:
        print("Skill valid: frontmatter, struktur dan tautan lokal.")
    sys.exit(bool(problems))
