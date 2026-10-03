"""Check complete source-workstream coverage and pentest handoffs."""
import json
import unittest
from pathlib import Path

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
