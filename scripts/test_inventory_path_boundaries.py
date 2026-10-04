"""Embedded traversal uses token boundaries rather than a delimiter allowlist."""
import json
import unittest
import inventory_privacy as privacy
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


class PathBoundaryTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_punctuation_surrounding_relative_paths(self):
        for prefix, suffix in (('(', ')'), ('[', ']'), ('{', '}'), (',', ''),
                               (';', ''), ('|', ''), ('!', ''), ('?', ''), ('—', '')):
            for segment in ('../', './'):
                for path in (segment+'root/.ssh/key', segment+'opt/private-build/secret'):
                    for value in (prefix+path+suffix, 'description='+prefix+path+suffix,
                                  ('description='+prefix+path+suffix).replace('/', '\\')):
                        for doc in ({'description': value}, {'nested': [{value: 'fixture'}]}):
                            with self.subTest(value=value, doc=doc), self.assertRaises(RuntimeError):
                                privacy.reject_private_paths(doc, self.root, ['/opt/private-build'])

    def test_scanner_and_repository_reject_reported_forms(self):
        for value in ('(../root/.ssh/key)', '[../root/.ssh/key]', '{../root/.ssh/key}',
                      ',../root/.ssh/key', ';../root/.ssh/key', '|../root/.ssh/key',
                      'description=(../opt/private-build/secret)',
                      r'description=[..\opt\private-build\secret]'):
            doc = dict(record('postgres'), description=value)
            self.path.write_text(json.dumps(doc))
            with self.subTest(value=value):
                self.assertTrue(policy.check_sboms(self.root, ['/opt/private-build']))
                with self.assertRaises(RuntimeError):
                    policy.public_sbom(doc, 'postgres', 'image', self.root, ['/opt/private-build'])

    def test_module_names_dotted_names_and_prose_remain_supported(self):
        for value in ('./api', './sdk', './internal/helper/stubbolt', '/usr/lib/libexample.so.1',
                      'An input containing a NUL (0).', 'A name such as "example.com".',
                      'https://example.org/releases/v1.2.3/file.json', 'FILE:///usr/bin/bao'):
            doc = dict(record('postgres'), description=value)
            with self.subTest(value=value):
                privacy.reject_private_paths(doc, self.root)
                self.path.write_text(json.dumps(doc))
                self.assertEqual(policy.check_sboms(self.root), [])
                policy.public_sbom(doc, 'postgres', 'image', self.root)


if __name__ == '__main__': unittest.main()
