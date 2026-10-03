"""Adversarial fixtures for repository gate enforcement."""
import tempfile
import unittest
from pathlib import Path
from check_repository import check

class RepositoryTests(unittest.TestCase):
    def test_limits_and_unpinned_actions_fail(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "crates").mkdir()
            (root / ".github").mkdir()
            (root / "crates/bad.rs").write_text("x\n" * 501)
            (root / ".github/ci.yml").write_text("uses: actions/checkout@main\n")
            self.assertEqual(len(check(root)), 2)

    def test_broken_document_link_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text("[missing](missing.md)")
            self.assertEqual(len(check(root)), 1)

    def test_codeql_workflow_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".github").mkdir()
            (root / ".github/codeql.yml").write_text("name: CodeQL\n")
            self.assertEqual(len(check(root)), 1)

    def test_angle_bracket_links_accept_urls_and_existing_paths(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'local document.md').write_text('Documentation')
            (root / 'README.md').write_text('[source](<https://example.invalid/spec>)\n[local](<local document.md>)')
            self.assertEqual(check(root), [])
            (root / 'README.md').write_text('[missing](<missing document.md>)')
            self.assertEqual(len(check(root)), 1)
