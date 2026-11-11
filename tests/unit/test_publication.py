"""Standalone project publication metadata and notice checks."""
import pathlib
import tomllib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]

class PublicationTests(unittest.TestCase):
    def test_project_identity_and_entry_point(self):
        data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertEqual(data["project"]["name"], "elucidary")
        self.assertEqual(data["project"]["scripts"], {"elucidary": "verifier_lab.elucidary_desktop:main"})
        self.assertEqual(data["project"]["license"]["file"], "LICENSE")

    def test_project_notices_exist(self):
        for name in ("LICENSE", "NOTICE", "OPEN_CANOPY_CONTRACT.md", "THIRD_PARTY_NOTICES.md"):
            self.assertTrue((ROOT / name).is_file(), name)
        license = (ROOT / "LICENSE").read_text()
        self.assertIn("Version 2.0, January 2004", license)
        self.assertIn("9. Accepting Warranty or Additional Liability", license)

    def test_no_browser_or_cli_in_desktop_source(self):
        package = ROOT / "src" / "verifier_lab"
        for name in ("server.py", "cli.py", "web"):
            self.assertFalse((package / name).exists(), name)
        self.assertTrue((package / "third_party" / "tree-sitter-LICENSE.txt").is_file())
