#!/usr/bin/env python3
"""Test installer tanpa menyentuh config global atau akun nyata."""
import json
import tempfile
import unittest
from pathlib import Path

from install_opencode import NAME, install
from terminal_preflight import inspect_terminal


def make_source(parent: Path) -> Path:
    source = parent / NAME
    source.mkdir()
    (source / "SKILL.md").write_text("---\nname: " + NAME + "\ndescription: test\n---\nIsi")
    for directory, names in {
        "agents": ["cloudflare-terminal.md"],
        "commands": ["cf-audit.md", "cf-implement.md", "cf-deploy.md"],
    }.items():
        dest = source / "assets/opencode" / directory
        dest.mkdir(parents=True)
        for name in names:
            (dest / name).write_text("template " + name)
    return source


class InstallerTests(unittest.TestCase):
    def test_install_semua_dan_idempoten(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = make_source(base)
            config = base / "proyek dengan spasi/.opencode"
            first = install(source, config, True, True)
            self.assertEqual(len(first["items"]), 5)
            self.assertTrue((config / "skills" / NAME / "SKILL.md").is_file())
            self.assertTrue((config / "agents/cloudflare-terminal.md").is_file())
            self.assertFalse((config / "opencode.json").exists())
            again = install(source, config, True, True)
            self.assertTrue(all(item["action"] == "already_present" for item in again["items"]))

    def test_conflict_agent_tidak_memasang_sebagian(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = make_source(base)
            config = base / "config"
            (config / "agents").mkdir(parents=True)
            old = config / "agents/cloudflare-terminal.md"
            old.write_text("milik pengguna")
            with self.assertRaises(FileExistsError):
                install(source, config, True, True)
            self.assertEqual(old.read_text(), "milik pengguna")
            self.assertFalse((config / "skills" / NAME).exists())

    def test_dry_run_tidak_menulis(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = make_source(base)
            config = base / "belum-ada"
            self.assertTrue(install(source, config, True, True, True)["dry_run"])
            self.assertFalse(config.exists())

    def test_file_rahasia_dan_cache_tidak_disalin(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = make_source(base)
            (source / ".dev.vars").write_text("SAMPLE=private")
            (source / ".env.example").write_text("SAMPLE=")
            (source / "__pycache__").mkdir()
            (source / "__pycache__/x.pyc").write_bytes(b"cache")
            config = base / "config"
            install(source, config)
            target = config / "skills" / NAME
            self.assertFalse((target / ".dev.vars").exists())
            self.assertFalse((target / "__pycache__").exists())
            self.assertTrue((target / ".env.example").exists())

    def test_symlink_ditolak(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = make_source(base)
            outside = base / "file.txt"
            outside.write_text("tidak ikut")
            (source / "alias.txt").symlink_to(outside)
            with self.assertRaises(ValueError):
                install(source, base / "config")

    def test_tujuan_di_dalam_source_ditolak(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = make_source(Path(tmp))
            with self.assertRaises(ValueError):
                install(source, source / "nested")

    def test_konflik_skill_tidak_ditimpa(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = make_source(base)
            config = base / "config"
            target = config / "skills" / NAME
            target.mkdir(parents=True)
            (target / "SKILL.md").write_text("versi pengguna")
            with self.assertRaises(FileExistsError):
                install(source, config)
            self.assertEqual((target / "SKILL.md").read_text(), "versi pengguna")


class PreflightTests(unittest.TestCase):
    def test_config_bermasalah_tidak_membuka_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = {"provider": {"x": {"apiKey": "SAMPLE_SECRET"}},
                    "permission": {"skill": {NAME: "deny"}}}
            (root / "opencode.json").write_text(json.dumps(data))
            result = inspect_terminal(root)
            self.assertIn("SKILL_DENIED", {x["code"] for x in result["findings"]})
            self.assertNotIn("SAMPLE_SECRET", json.dumps(result))
            self.assertEqual(result["probes"], {})

    def test_jsonc_dan_disabled(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "opencode.jsonc").write_text('{"tools":{"skill":false}, // catatan\n}')
            result = inspect_terminal(root)
            self.assertIn("SKILL_DISABLED", {x["code"] for x in result["findings"]})

    def test_config_rusak(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "opencode.json").write_text('{"provider":')
            self.assertIn("CONFIG_INVALID", {x["code"] for x in inspect_terminal(root)["findings"]})


if __name__ == "__main__":
    unittest.main()
