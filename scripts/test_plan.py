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
            self.assertIn(f'v{row["version"]} implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.', document)
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

    def test_blank_or_nonstring_gate_rejects_before_output_mutation(self):
        original = json.loads((ROOT / 'docs/roadmap-input/reference-verification.json').read_text())
        for invalid in ('', ' \n\t', '\u2003', None, False, 17, [], {}):
            with self.subTest(value=invalid), tempfile.TemporaryDirectory() as folder:
                docs = Path(folder)
                inputs = docs / 'roadmap-input'
                inputs.mkdir()
                gates = dict(original)
                gates['0.240.0'] = invalid
                (inputs / 'reference-verification.json').write_text(json.dumps(gates))
                (docs / 'RELEASE_PLAN.md').write_text('previous reviewed output')
                before = {p.relative_to(docs): p.read_bytes() for p in docs.rglob('*') if p.is_file()}
                with patch.object(build_plan, 'DOCS', docs):
                    with self.assertRaisesRegex(ValueError, 'nonblank string'):
                        build_plan.build()
                self.assertEqual(before, {p.relative_to(docs): p.read_bytes()
                                         for p in docs.rglob('*') if p.is_file()})
                self.assertFalse((docs / 'releases').exists())
                self.assertFalse((docs / 'roadmap').exists())

    def test_minimal_fencing_and_local_publication_have_explicit_owners(self):
        rows = {row['title']: row for row in ordered_rows()}
        publication = rows['Hosted artifact publication fencing']
        self.assertIn(rows['PostgreSQL adapter']['version'], publication['prerequisites'])
        self.assertIn(rows['Repository contracts']['version'], publication['prerequisites'])
        self.assertIn(rows['Workspace authorization']['version'], publication['prerequisites'])
        self.assertIn(rows['Storage transaction discipline']['version'], publication['prerequisites'])
        self.assertIn('Implement the v0.106.0 minimal lease/fencing contract',
                      rows['PostgreSQL adapter']['scope_context'])
        self.assertIn('does not introduce fencing for the first time',
                      rows['Durable jobs and leases']['scope_context'])
        self.assertIn('Hosted SQL', rows['Storage transaction discipline']['scope_context'])
        for title in ('Public API specification', 'Job lifecycle API', 'Artifact transfer API'):
            self.assertIn('v0.119.0', rows[title]['scope_context'])
            self.assertIn('v0.125.0', rows[title]['scope_context'])
        phase = (ROOT / 'docs/releases/phase-e.md').read_text()
        self.assertNotIn('Run real PostgreSQL/OpenBao/Valkey tests, cross-principal object denials, lease races, egress and supervisor failures.', phase)
        self.assertIn('contract fixtures never attest their runtime PASS', phase)

    def test_actual_continuation_does_not_replace_historical_acceptance(self):
        rows = ordered_rows()
        continuation = f'v0.{len(rows) + 1}.0'
        ga = next(row for row in rows if row['source_version'] == '0.240.0')
        self.assertIn('continue 0.241.0', ga['acceptance'])
        self.assertIn(continuation, ga['scope_context'])
        for path in ('docs/RELEASE_PLAN.md', 'docs/VERSION_PLAN.md', 'docs/releases/phase-p.md'):
            self.assertIn(continuation, (ROOT / path).read_text())

    def test_browser_origin_controls_have_early_and_release_owners(self):
        rows = {row['title']: row for row in ordered_rows()}
        required = {
            'Executable seed': ('0.14.0', ('document/worker CSP', 'connect-src none')),
            'Browser privacy and secret publication': ('0.27.0', ('origin compromise', 'automatic remote bridges')),
            'First browser workbench': ('0.28.0', ('Trusted Types', 'COOP/COEP/CORP', 'Permissions Policy', 'Chromium/Firefox/WebKit')),
            'Minimal lazy browser pack loader': ('0.31.0', ('connect-src none', 'no policy widening')),
            'Offline packaging': ('0.101.0', ('independent pre-launch', 'network-disabled host', 'untrusted signer')),
            'Server security gate': ('0.133.0', ('separate origin/application', 'CORS/CSRF', 'automatic payload bridge')),
            'Release packaging': ('0.366.0', ('signed immutable', 'network-disabled launch', 'v0.367.0')),
        }
        for title, (version, controls) in required.items():
            with self.subTest(owner=title):
                row = rows[title]
                self.assertEqual(row['version'], version)
                contract = ' '.join(str(row.get(key, '')) for key in ('deliverable', 'acceptance', 'scope_context'))
                for control in controls:
                    self.assertIn(control, contract)
        self.assertEqual(len(rows), 386)
