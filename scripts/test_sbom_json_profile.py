"""Nested service binding and strict public JSON encoding/number regressions."""
import json
import unittest
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


class JsonProfileTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_unknown_image_inventory_at_every_depth_is_rejected(self):
        for relative in ('foreign.cdx.json', 'unreviewed/foreign.cdx.json',
                         'a/b/probe.cdx.json', 'a/b/openbao-official-v0.2.2.cdx.json'):
            with self.subTest(relative=relative):
                path = self.images/relative; path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(record('probe')))
                self.assertTrue(policy.check_sboms(self.root))
                path.unlink()
                self.assertEqual(policy.check_sboms(self.root), [])

    def test_utf16_utf32_and_boms_are_rejected(self):
        document = json.dumps(record('postgres'))
        for encoding in ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le',
                         'utf-32-be', 'utf-8-sig'):
            with self.subTest(encoding=encoding):
                self.path.write_bytes(document.encode(encoding))
                self.assertTrue(policy.check_sboms(self.root))
        valid = dict(record('postgres'), description='Rúnasmidja ✓')
        self.path.write_bytes(json.dumps(valid, ensure_ascii=False).encode('utf-8'))
        self.assertEqual(policy.check_sboms(self.root), [])

    def test_nonfinite_constants_and_exponent_overflow_at_any_depth(self):
        # Exercise canonical, historical and other JSON through the shared loader.
        historical = self.images/'openbao-official-v0.2.2.cdx.json'
        extra = self.images/'notes.json'
        for path, service in ((self.path, 'postgres'), (historical, 'openbao'), (extra, 'probe')):
            for token in ('NaN', 'Infinity', '-Infinity', '1e9999', '-1e9999', '1.8e308'):
                for nested in (False, True):
                    with self.subTest(path=path, token=token, nested=nested):
                        doc = record(service)
                        doc['evidence'] = {'nested': ['NUMBER']} if nested else 'NUMBER'
                        path.write_text(json.dumps(doc).replace('"NUMBER"', token))
                        self.assertTrue(policy.check_sboms(self.root))
            if path == self.path: path.write_text(json.dumps(record('postgres')))
            else: path.unlink()
        self.assertEqual(policy.check_sboms(self.root), [])

    def test_finite_numbers_and_literal_strings_remain_supported(self):
        doc = record('postgres')
        doc['evidence'] = {'numbers': [0, -1, 1.25, 1e100, -1.7976931348623157e308],
                           'text': ['NaN', 'Infinity', '1e9999', '\ufeff']}
        self.path.write_text(json.dumps(doc, ensure_ascii=False), encoding='utf-8')
        self.assertEqual(policy.check_sboms(self.root), [])
        with policy.custody_directory(self.images) as directory:
            self.assertEqual(policy.load_public_json(self.path.name, directory), doc)


if __name__ == '__main__': unittest.main()
