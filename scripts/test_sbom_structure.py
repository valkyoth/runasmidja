"""Reject placeholder inventories and filesystem aliases before release checks."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sbom_privacy as policy
from test_public_evidence import record


class StructureTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.images = self.root/'sbom/images'; self.images.mkdir(parents=True)
        for service in policy.PUBLIC_SERVICES:
            (self.images/f'{service}.cdx.json').write_text(json.dumps(record(service)))
        self.path = self.images/'postgres.cdx.json'

    def test_minimum_structure_and_supported_specifications(self):
        valid = record('postgres')
        cases = [[], None, {'metadata': valid['metadata']}]
        for field, values in {
            'bomFormat': (None, '', 'SPDX'),
            'specVersion': (None, '', 1.7, [], 'future', '1.999'),
            'components': (None, [], {}, 'library', [None], [{}],
                           [{'name': 'fixture'}], [{'type': 'library', 'name': ''}]),
        }.items():
            missing = dict(valid); del missing[field]; cases.append(missing)
            cases.extend(dict(valid, **{field: value}) for value in values)
        for value in cases:
            with self.subTest(value=value):
                self.path.write_text(json.dumps(value))
                self.assertTrue(policy.check_sboms(self.root))
        for version in ('1.5', '1.7'):
            self.path.write_text(json.dumps(dict(valid, specVersion=version)))
            self.assertEqual(policy.check_sboms(self.root), [])

    def test_symlink_hardlink_fifo_and_directory_are_rejected_without_blocking(self):
        original = self.path.read_bytes()
        for kind in ('symlink', 'broken-symlink', 'hardlink', 'fifo', 'directory'):
            with self.subTest(kind=kind):
                self.path.unlink()
                target = self.root/'target.json'; target.write_bytes(original)
                if kind == 'symlink': self.path.symlink_to(target)
                elif kind == 'broken-symlink': self.path.symlink_to(self.root/'absent')
                elif kind == 'hardlink': os.link(target, self.path)
                elif kind == 'fifo': os.mkfifo(self.path)
                else: self.path.mkdir()
                self.assertTrue(policy.check_sboms(self.root))
                self.assertEqual(target.read_bytes(), original)
                if kind == 'directory': self.path.rmdir()
                else: self.path.unlink()
                self.path.write_bytes(original)
        self.assertEqual(policy.check_sboms(self.root), [])

    def test_size_boundary_and_growth_after_stat(self):
        content = self.path.read_bytes()
        with patch.object(policy, 'MAX_PUBLIC_SBOM', len(content)):
            self.assertEqual(policy.load_canonical_sbom(self.path), record('postgres'))
            self.path.write_bytes(content + b' ')
            with self.assertRaises(RuntimeError): policy.load_canonical_sbom(self.path)
            info = self.path.stat()
            with patch.object(policy.os, 'fstat', return_value=SimpleNamespace(
                    st_mode=info.st_mode, st_nlink=1, st_size=0)):
                with self.assertRaisesRegex(RuntimeError, 'exceeds size'):
                    policy.load_canonical_sbom(self.path)
        # Actual production limit, using a sparse oversized file rather than allocating it.
        with self.path.open('wb') as output: output.truncate(policy.MAX_PUBLIC_SBOM + 1)
        self.assertTrue(policy.check_sboms(self.root))

    def test_invalid_encoding_json_and_nested_reports_fail_closed(self):
        for content in (b'\xff', b'{', b'[' * 2000 + b']' * 2000):
            with self.subTest(content=content[:20]):
                self.path.write_bytes(content)
                self.assertTrue(policy.check_sboms(self.root))

    def test_historical_structure_and_service_bindings(self):
        for filename, prefix in policy.HISTORICAL_IDENTITIES.items():
            path = self.images/filename
            valid = record('fixture'); valid['metadata']['component']['name'] = prefix + 'historical'
            with self.subTest(filename=filename):
                path.write_text(json.dumps(valid)); self.assertEqual(policy.check_sboms(self.root), [])
                path.write_text(json.dumps(record('probe'))); self.assertTrue(policy.check_sboms(self.root))
                path.write_text(json.dumps({'metadata': valid['metadata']}))
                self.assertTrue(policy.check_sboms(self.root))
                path.unlink(); path.symlink_to(self.path); self.assertTrue(policy.check_sboms(self.root))
                path.unlink()
        unknown = self.images/'unreviewed.cdx.json'
        unknown.write_text(json.dumps(record('postgres')))
        self.assertTrue(policy.check_sboms(self.root))

    def test_noncanonical_inventory_privacy_reads_are_also_bounded(self):
        path = self.images/'extra.json'; os.mkfifo(path)
        self.assertTrue(policy.check_sboms(self.root))
        path.unlink(); path.symlink_to(self.path)
        self.assertTrue(policy.check_sboms(self.root))
        path.unlink(); path.write_text(json.dumps({'note': '/home/example/private'}))
        self.assertTrue(policy.check_sboms(self.root))


if __name__ == '__main__': unittest.main()
