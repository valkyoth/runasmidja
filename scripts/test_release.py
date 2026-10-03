"""Negative fixtures for assessment status and exact-source binding."""
import tempfile
import unittest
from pathlib import Path
from check_release import source_digest, validate_report

class ReleaseTests(unittest.TestCase):
    def test_test_results_do_not_qualify_as_assessment(self):
        self.assertTrue(validate_report('Status: NOT RUN\nTests passed\n'))

    def test_complete_report_shape(self):
        report = 'Status: PASS\nReviewed commit: ' + 'a' * 40 + '\nSource SHA256: ' + 'b' * 64 + '\nUnresolved critical: 0\nUnresolved high: 0\n'
        for heading in ('Findings', 'Commands', 'Results', 'Remediation', 'Retest', 'Limitations'):
            report += '\n## ' + heading + '\n\nEvidence.\n'
        self.assertEqual(validate_report(report), [])
        self.assertTrue(validate_report(report.replace('Unresolved high: 0', 'Unresolved high: 1')))

    def test_digest_changes_on_source_but_not_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'source.rs').write_text('original')
            original = source_digest(root)
            (root / 'security/pentest').mkdir(parents=True)
            (root / 'security/pentest/v0.1.0.md').write_text('report')
            self.assertEqual(original, source_digest(root))
            (root / 'AGENTS.md').write_text('Local instructions')
            (root / '.codex').mkdir()
            (root / '.codex/settings.toml').write_text('local = true')
            self.assertEqual(original, source_digest(root))
            (root / 'source.rs').write_text('changed')
            self.assertNotEqual(original, source_digest(root))
