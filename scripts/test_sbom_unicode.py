"""Public evidence contains Unicode scalar values in every key and string."""
import json
import unittest
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


class UnicodeTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_lone_surrogates_rejected_in_all_string_locations(self):
        for surrogate in ('\ud800', '\udbff', '\udc00', '\udfff'):
            for location in ('key', 'string', 'array', 'component', 'identity'):
                doc = record('postgres')
                if location == 'key': doc['nested'] = [{surrogate: 'value'}]
                elif location == 'string': doc['nested'] = {'value': surrogate}
                elif location == 'array': doc['nested'] = [0, [surrogate]]
                elif location == 'component': doc['components'][0]['name'] = surrogate
                else: doc['metadata']['component']['name'] += surrogate
                with self.subTest(surrogate=repr(surrogate), location=location):
                    self.path.write_text(json.dumps(doc), encoding='utf-8')
                    self.assertTrue(policy.check_sboms(self.root))
                    with policy.custody_directory(self.images) as directory:
                        with self.assertRaises(UnicodeEncodeError):
                            policy.load_public_json(self.path.name, directory)

    def test_invalid_pairs_and_surrogates_after_valid_pairs_fail(self):
        for escaped in (r'\udc00\ud800', r'\ud800\ud800', r'\udc00\udc00',
                        r'\ud800x\udc00', r'\ud83d\ude00\ud800'):
            doc = record('postgres'); doc['description'] = 'VALUE'
            self.path.write_text(json.dumps(doc).replace('VALUE', escaped))
            with self.subTest(escaped=escaped): self.assertTrue(policy.check_sboms(self.root))

    def test_valid_pairs_literal_unicode_and_escaped_backslashes_pass(self):
        for escaped in (True, False):
            doc = record('postgres')
            doc['components'][0]['name'] = '😀'
            doc['nested'] = {'😀': ['Rúnasmidja', '\U0010ffff', '\u0000', r'\ud800']}
            self.path.write_text(json.dumps(doc, ensure_ascii=escaped), encoding='utf-8')
            with self.subTest(escaped=escaped):
                self.assertEqual(policy.check_sboms(self.root), [])
                with policy.custody_directory(self.images) as directory:
                    self.assertEqual(policy.load_public_json(self.path.name, directory), doc)

    def test_historical_and_noncanonical_json_share_scalar_validation(self):
        for filename, service in (('openbao-official-v0.2.2.cdx.json', 'openbao'),
                                  ('notes.json', 'probe')):
            path = self.images/filename
            doc = record(service); doc['extra'] = {'nested': [{'\udfff': '\ud800'}]}
            path.write_text(json.dumps(doc))
            with self.subTest(filename=filename): self.assertTrue(policy.check_sboms(self.root))
            del doc['extra']; path.write_text(json.dumps(doc))
            self.assertEqual(policy.check_sboms(self.root), [])
            path.unlink()


if __name__ == '__main__': unittest.main()
