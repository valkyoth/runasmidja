"""Check complete source-workstream coverage and pentest handoffs."""
import json
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import build_plan

ROOT = Path(__file__).resolve().parent.parent

def ordered_rows():
    rows = [row for path in (ROOT / 'docs/roadmap').glob('*.json')
            for row in json.loads(path.read_text())]
    return sorted(rows, key=lambda row: int(row['version'].split('.')[1]))

class PlanTests(unittest.TestCase):
    def test_all_original_versions_have_owners_and_linear_dependencies(self):
        baseline = json.loads((ROOT / 'docs/reference/workbench-plan/roadmap.json').read_text())
        rows = ordered_rows()
        self.assertEqual({item['version'] for item in baseline['releases']}, {row['source_version'] for row in rows if row['source_version']})
        for index, row in enumerate(rows, start=1):
            self.assertEqual(row['version'], f'0.{index}.0')
            self.assertEqual(row['depends_on'], [] if index == 1 else [f'0.{index-1}.0'])
            document = (ROOT / f'docs/releases/phase-{row["phase"].lower()}.md').read_text()
            self.assertIn(f'v{row["version"]} implementation stop reached. Run pentest for this exact commit.', document)
            self.assertEqual(row['status'], 'planned')

    def test_vault_origin_precedes_credential_consumers(self):
        rows = ordered_rows()
        positions = {row['title']: i for i, row in enumerate(rows)}
        self.assertEqual(rows[1]['title'], 'OpenBao-first secret provisioning')
        for consumer in ('PostgreSQL 19 beta 4 test fixture', 'Valkey test fixture'):
            self.assertLess(positions['OpenBao-first secret provisioning'], positions[consumer])
        self.assertLess(positions['Build and release secret delivery'], positions['Executable seed'])
        self.assertLess(positions['Application secret references'], positions['PostgreSQL adapter'])
        self.assertLess(positions['Secret rotation lifecycle'], positions['PostgreSQL adapter'])

    def test_optional_search_is_early_and_follows_authority(self):
        rows = ordered_rows()
        positions = {row['title']: i for i, row in enumerate(rows)}
        self.assertLess(positions['Application contracts'], positions['Search service contracts'])
        self.assertLess(positions['Search service contracts'], positions['First browser workbench'])
        chain = ('PostgreSQL adapter', 'Workspace authorization',
                 'Repository metadata search', 'Search projection and outbox',
                 'Meilisearch Podman fixture', 'Meilisearch metadata adapter',
                 'Search authorization and revocation', 'Search backend switching and recovery',
                 'Shared recipe collections', 'Shared-collection search integration')
        for before, after in zip(chain, chain[1:]):
            self.assertLess(positions[before], positions[after], f'{before} must precede {after}')
        self.assertNotIn('Conditional Meilisearch qualification', positions)

    def test_original_acceptance_and_all_additive_gates_survive(self):
        baseline = json.loads((ROOT / 'docs/reference/workbench-plan/roadmap.json').read_text())
        original = {row['version']: row for row in baseline['releases']}
        strict = json.loads((ROOT / 'docs/roadmap-input/reference-verification.json').read_text())
        self.assertEqual(set(strict), set(original))
        for row in ordered_rows():
            source = row['source_version']
            if source:
                self.assertTrue(row['acceptance'].endswith(original[source]['acceptance']))
                self.assertEqual(row['strict_verification'], strict[source])
                self.assertTrue(strict[source].strip())
                document = (ROOT / f'docs/releases/phase-{row["phase"].lower()}.md').read_text()
                self.assertIn(strict[source], document)

    def test_artifact_pack_and_admission_prerequisites(self):
        positions = {row['title']: i for i, row in enumerate(ordered_rows())}
        chains = (
            ('Feature and target admission gates', 'Seed value and budget vocabulary',
             'Executable seed', 'Application contracts', 'OpenBao SDK admission'),
            ('Fixture ownership and drift', 'PostgreSQL 19 beta 4 test fixture'),
            ('Pack manifest and resource contract', 'Minimal lazy browser pack loader',
             'Regex compatibility feasibility', 'Lossless JSON', 'Crypto provider boundary'),
            ('Native artifact storage', 'Browser artifact storage',
             'Storage transaction discipline', 'Whole-input and seekable adapters'),
            ('Workspace authorization', 'Hosted artifact publication fencing',
             'Repository metadata search'),
            ('Isolated execution workers', 'Worker isolation fault qualification',
             'Admission and quotas', 'Server networking policy',
             'DNS and connection destination binding', 'Redirect and outbound transport policy',
             'Server security gate'),
            ('Logical storage export', 'Migration integrity and canonicalization',
             'MySQL portability prototype', 'PostgreSQL-to-MySQL migration drill',
             'MySQL-to-PostgreSQL reverse drill'),
            ('Release evidence trust contract', 'Release packaging',
             'Distribution assessment and provenance binding', 'Supply-chain release proof'),
        )
        for chain in chains:
            for before, after in zip(chain, chain[1:]):
                self.assertLess(positions[before], positions[after], f'{before} must precede {after}')

    def test_generated_plan_matches_reviewed_files(self):
        with tempfile.TemporaryDirectory() as folder:
            docs = Path(folder)
            inputs = docs / 'roadmap-input'
            inputs.mkdir()
            name = 'reference-verification.json'
            (inputs / name).write_bytes((ROOT / 'docs/roadmap-input' / name).read_bytes())
            with patch.object(build_plan, 'DOCS', docs), contextlib.redirect_stdout(io.StringIO()):
                build_plan.build()
                first = {path.relative_to(docs): path.read_bytes()
                         for path in docs.rglob('*') if path.is_file()}
                build_plan.build()
            second = {path.relative_to(docs): path.read_bytes()
                      for path in docs.rglob('*') if path.is_file()}
            self.assertEqual(first, second)
            for path, content in first.items():
                self.assertEqual(content, (ROOT / 'docs' / path).read_bytes(), path)

    def test_missing_reference_gate_blocks_generation(self):
        with tempfile.TemporaryDirectory() as folder:
            docs = Path(folder)
            inputs = docs / 'roadmap-input'
            inputs.mkdir()
            (inputs / 'reference-verification.json').write_text('{}')
            with patch.object(build_plan, 'DOCS', docs):
                with self.assertRaisesRegex(ValueError, 'Every source workstream'):
                    build_plan.build()
