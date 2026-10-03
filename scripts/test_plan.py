"""Check complete source-workstream coverage and pentest handoffs."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class PlanTests(unittest.TestCase):
    def test_all_original_versions_have_owners_and_linear_dependencies(self):
        baseline = json.loads((ROOT / 'docs/reference/workbench-plan/roadmap.json').read_text())
        rows = [row for path in (ROOT / 'docs/roadmap').glob('*.json') for row in json.loads(path.read_text())]
        rows.sort(key=lambda row: int(row['version'].split('.')[1]))
        self.assertEqual({item['version'] for item in baseline['releases']}, {row['source_version'] for row in rows if row['source_version']})
        for index, row in enumerate(rows, start=1):
            self.assertEqual(row['version'], f'0.{index}.0')
            self.assertEqual(row['depends_on'], [] if index == 1 else [f'0.{index-1}.0'])
            document = (ROOT / f'docs/releases/phase-{row["phase"].lower()}.md').read_text()
            self.assertIn(f'v{row["version"]} implementation stop reached. Run pentest for this exact commit.', document)
            self.assertEqual(row['status'], 'planned')
