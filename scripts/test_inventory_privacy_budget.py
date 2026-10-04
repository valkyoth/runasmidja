"""Known host paths and whole-tree inventory resource ceilings."""
import json
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import sbom_privacy as policy
import inventory_privacy as privacy
import image_gate as gate
from pathlib import Path
import test_sbom_structure as fixtures
from test_public_evidence import record


class PrivacyBudgetTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_known_private_paths_in_keys_and_values(self):
        for value in ('/root/.ssh/id_ed25519', '/tmp/build/session', '/var/tmp/private',
                      r'\\server\share\secret', 'source=\\\\server\\share\\secret',
                      '/private/tmp/session', r'C:\build\secret', 'file:///root/secret',
                      'file://server/share/secret', '/home/person/file', '/Users/person/file',
                      'build: /var/tmp/private', str(self.root)):
            for document in ({'extra': [{'path': value}]}, {'extra': [{value: 'fixture'}]}):
                with self.subTest(value=value, document=document):
                    doc = dict(record('postgres'), **document)
                    self.path.write_text(json.dumps(doc))
                    self.assertTrue(policy.check_sboms(self.root))
                    with self.assertRaises(RuntimeError):
                        policy.public_sbom(doc, 'postgres', 'image', self.root)

    def test_explicit_and_environment_roots_and_public_controls(self):
        for key in ('GITHUB_WORKSPACE', 'RUNNER_TEMP', 'RUNNER_TOOL_CACHE', 'CARGO_HOME', 'XDG_CACHE_HOME'):
            with patch.dict(os.environ, {key: '/opt/private-ci'}):
                with self.assertRaises(RuntimeError):
                    privacy.reject_private_paths({'nested': ['/opt/private-ci/cache']}, self.root)
        with patch.object(privacy.Path, 'home', return_value=privacy.Path('/srv/private-home')), \
             patch.object(privacy.tempfile, 'gettempdir', return_value='/srv/private-temp'):
            for value in ('/srv/private-home/key', '/srv/private-temp/file', '/mnt/extraction/input'):
                with self.assertRaises(RuntimeError):
                    privacy.reject_private_paths({'value': value}, self.root, ['/mnt/extraction'])
        for value in ('https://example.org/path', 'pkg:generic/name@1', '/usr/bin/bao',
                      '/var/lib/postgresql', '/tmp-not-private/file', 'cgr.dev/image@sha256:abc'):
            privacy.reject_private_paths({'value': value}, self.root)
        self.path.write_text(json.dumps(dict(record('postgres'), description='/mnt/extraction/input')))
        self.assertTrue(policy.check_sboms(self.root, extra_roots=['/mnt/extraction']))

    def test_scanner_archive_root_is_supplied_before_publication(self):
        doc = dict(record('probe'), description='/opt/private-archive/input')
        with patch.object(gate, 'EVIDENCE', self.root/'private'), \
             patch.object(gate, 'run_bounded', return_value=SimpleNamespace(stdout=json.dumps(doc))):
            with self.assertRaisesRegex(RuntimeError, 'private filesystem'):
                gate.scan('probe', 'image', 'scanner', archive=Path('/opt/private-archive/input'),
                          archive_check=lambda: 'binding')
        self.assertFalse(list((self.root/'private').glob('*.cdx.json')))

    def test_entry_and_directory_limits_include_nonjson_files(self):
        # The initial tree has one images directory and six canonical reports.
        with patch.object(policy, 'MAX_PUBLIC_ENTRIES', 7):
            self.assertEqual(policy.check_sboms(self.root), [])
            for name in ('extra.txt', 'extra-directory'):
                path = self.images/name
                if name.endswith('.txt'): path.write_text('not parsed')
                else: path.mkdir()
                with self.subTest(name=name):
                    self.assertTrue(any('entry limit' in error for error in policy.check_sboms(self.root)))
                if path.is_dir(): path.rmdir()
                else: path.unlink()
        for n in range(1000): (self.images/f'extra-{n}.json').write_text('{}')
        with patch.object(policy, 'load_public_json', wraps=policy.load_public_json) as reader:
            self.assertTrue(any('entry limit' in error for error in policy.check_sboms(self.root)))
            reader.assert_not_called()

    def test_entry_enumeration_stops_at_limit_plus_one(self):
        visited = []
        def entries():
            for n in range(1000):
                visited.append(n); yield SimpleNamespace(name=str(n))
        context = unittest.mock.MagicMock()
        context.__enter__.return_value = entries()
        with patch.object(policy.os, 'scandir', return_value=context), \
             patch.object(policy, 'MAX_PUBLIC_ENTRIES', 3):
            with self.assertRaises(policy.InventoryBudgetExceeded):
                policy.bounded_names(0, {'entries': 0, 'bytes': 0})
        self.assertEqual(len(visited), 4)

    def test_cumulative_bytes_exact_boundary_and_stop_before_later_reads(self):
        total = sum(path.stat().st_size for path in self.images.iterdir())
        with patch.object(policy, 'MAX_PUBLIC_TOTAL_BYTES', total):
            self.assertEqual(policy.check_sboms(self.root), [])
        with patch.object(policy, 'MAX_PUBLIC_TOTAL_BYTES', total - 1):
            self.assertTrue(any('byte limit' in error for error in policy.check_sboms(self.root)))
        nested = self.root/'sbom/nested'; nested.mkdir()
        (nested/'extra.json').write_text('{}')
        with patch.object(policy, 'MAX_PUBLIC_TOTAL_BYTES', total):
            self.assertTrue(any('byte limit' in error for error in policy.check_sboms(self.root)))
        with policy.custody_directory(self.images) as directory:
            budget = {'entries': 0, 'bytes': 0}
            with patch.object(policy, 'MAX_PUBLIC_TOTAL_BYTES', self.path.stat().st_size):
                policy.load_public_json(self.path.name, directory, budget)
                with self.assertRaises(policy.InventoryBudgetExceeded):
                    policy.load_public_json(self.path.name, directory, budget)

    def test_failed_per_file_growth_still_consumes_aggregate_budget(self):
        self.path.write_text('12345'); info = self.path.stat()
        with policy.custody_directory(self.images) as directory:
            budget = {'entries': 0, 'bytes': 0}
            with patch.object(policy, 'MAX_PUBLIC_SBOM', 4), \
                 patch.object(policy, 'MAX_PUBLIC_TOTAL_BYTES', 8), \
                 patch.object(policy.os, 'fstat', return_value=SimpleNamespace(st_mode=info.st_mode,
                     st_uid=os.getuid(), st_nlink=1, st_size=0)):
                with self.assertRaisesRegex(RuntimeError, 'Public inventory exceeds size'):
                    policy.load_public_json(self.path.name, directory, budget)
                self.assertEqual(budget['bytes'], 5)
                with self.assertRaises(policy.InventoryBudgetExceeded):
                    policy.load_public_json(self.path.name, directory, budget)

    def test_growth_after_stat_cannot_escape_shared_byte_budget(self):
        content = self.path.read_bytes(); info = self.path.stat()
        with policy.custody_directory(self.images) as directory:
            with patch.object(policy, 'MAX_PUBLIC_TOTAL_BYTES', len(content)), \
                 patch.object(policy.os, 'fstat', return_value=SimpleNamespace(st_mode=info.st_mode,
                     st_uid=os.getuid(), st_nlink=1, st_size=0)):
                self.path.write_bytes(content + b' ')
                with self.assertRaises(policy.InventoryBudgetExceeded):
                    policy.load_public_json(self.path.name, directory, {'entries': 0, 'bytes': 0})


if __name__ == '__main__': unittest.main()
