"""Ambiguous path segments cannot conceal known private roots in evidence."""
import json
import unittest
import inventory_privacy as privacy
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


class DotSegmentTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_dot_segments_in_paths_keys_values_and_descriptions(self):
        for path in ('/usr/../root/.ssh/key', '/var/../tmp/build/session',
                     '/opt/public/../private-build/secret', '/usr/./bin/bao',
                     './../artifact', './api/../root', './api/./nested', '../artifact', '/usr/bin/.', '/usr/bin/..'):
            for value in (path, 'file://' + path, 'description=' + path,
                          path.replace('/', '\\')):
                for doc in ({'nested': [value]}, {'nested': [{value: 'fixture'}]}):
                    with self.subTest(value=value, doc=doc), self.assertRaises(RuntimeError):
                        privacy.reject_private_paths(doc, self.root, extra_roots=['/opt/private-build'])

    def test_repository_and_scanner_reject_dot_segments(self):
        for value in ('/usr/../root/.ssh/key', 'file:///usr/../root/.ssh/key',
                      '/var/../tmp/build/session', '/opt/public/../private-build/secret',
                      'file:///opt/public/../private-build/secret',
                      r'description=\usr\..\root\.ssh\key'):
            doc = dict(record('postgres'), description=value)
            self.path.write_text(json.dumps(doc))
            with self.subTest(value=value):
                self.assertTrue(policy.check_sboms(self.root, extra_roots=['/opt/private-build']))
                with self.assertRaises(RuntimeError):
                    policy.public_sbom(doc, 'postgres', 'image', self.root,
                                       extra_roots=['/opt/private-build'])

    def test_dotted_names_and_canonical_urls_remain_valid(self):
        for value in ('./sdk', './api', './api/auth/kubernetes', './internal/helper/stubbolt',
                      '/usr/lib/libexample.so.1', '/usr/share/.config/example',
                      '/usr/share/.../example', 'package-1.2.3.tar.gz', 'ordinary prose.', 'An input containing a NUL (0).',
                      'A name such as "example.com".',
                      'https://example.org/releases/v1.2.3/file.json',
                      'pkg:generic/example@1.2.3', 'FILE:///usr/bin/bao'):
            doc = dict(record('postgres'), description=value)
            with self.subTest(value=value):
                privacy.reject_private_paths(doc, self.root)
                self.path.write_text(json.dumps(doc))
                self.assertEqual(policy.check_sboms(self.root), [])
                policy.public_sbom(doc, 'postgres', 'image', self.root)


if __name__ == '__main__': unittest.main()
