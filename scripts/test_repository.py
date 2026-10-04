"""Adversarial fixtures for repository gate enforcement."""
import json
import tempfile
import unittest
from pathlib import Path
from check_repository import check
from sbom_privacy import PUBLIC_SERVICES

class RepositoryTests(unittest.TestCase):
    def canonical_inventories(self, root):
        images = root / 'sbom/images'
        images.mkdir(parents=True)
        for service in PUBLIC_SERVICES:
            (images / f'{service}.cdx.json').write_text(json.dumps(
                {'bomFormat': 'CycloneDX', 'specVersion': '1.7', 'components': [{'type': 'library', 'name': 'fixture'}], 'metadata': {'component': {'name': f'runasmidja/{service}@image'}}}))

    def test_container_recipes_have_the_same_code_limit(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.canonical_inventories(root)
            for name in ('Containerfile', 'Dockerfile'):
                (root / name).write_text('# recipe\n' * 501)
            self.assertEqual(len(check(root)), 2)

    def test_limits_and_unpinned_actions_fail(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.canonical_inventories(root)
            (root / "crates").mkdir()
            (root / ".github/workflows").mkdir(parents=True)
            (root / ".github/workflow-policy.toml").write_text("version = 1\n[local_actions]\n[local_workflows]\n")
            (root / "crates/bad.rs").write_text("x\n" * 501)
            (root / ".github/workflows/ci.yaml").write_text("jobs: {check: {steps: [{uses: actions/checkout@main}]}}")
            self.assertEqual(len(check(root)), 2)

    def test_broken_document_link_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.canonical_inventories(root)
            (root / "README.md").write_text("[missing](missing.md)")
            self.assertEqual(len(check(root)), 1)

    def test_codeql_workflow_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.canonical_inventories(root)
            (root / ".github/workflows").mkdir(parents=True)
            (root / ".github/workflow-policy.toml").write_text("version = 1\n[local_actions]\n[local_workflows]\n")
            (root / ".github/workflows/codeql.yaml").write_text("jobs: {check: {steps: [{uses: github/codeql-action/init@" + "a" * 40 + "}]}}")
            self.assertEqual(len(check(root)), 1)

    def test_angle_bracket_links_accept_urls_and_existing_paths(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.canonical_inventories(root)
            (root / 'local document.md').write_text('Documentation')
            (root / 'README.md').write_text('[source](<https://example.invalid/spec>)\n[local](<local document.md>)')
            self.assertEqual(check(root), [])
            (root / 'README.md').write_text('[missing](<missing document.md>)')
            self.assertEqual(len(check(root)), 1)
