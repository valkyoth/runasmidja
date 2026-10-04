"""URI normalization cannot remove private-root evidence from distinct schemes."""
import json
import unittest
import inventory_privacy as privacy
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


class NormalizationTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_distinct_schemes_cannot_hide_known_roots(self):
        for scheme, root in (('profile', '/root'), ('custom-file', '/tmp'), ('notfile', '/var/tmp')):
            for spelling in (scheme, scheme.upper(), scheme.title()):
                for value in (spelling + '://' + root, 'source=' + spelling + '://' + root + '/secret'):
                    for doc in ({'nested': [value]}, {'nested': [{value: 'fixture'}]}):
                        with self.subTest(value=value, doc=doc), self.assertRaises(RuntimeError):
                            privacy.reject_private_paths(doc, self.root)

    def test_scanner_and_repository_reject_normalization_collisions(self):
        for value in ('profile:///root/.ssh/key', 'custom-file:///tmp/build/secret',
                      'notfile:///var/tmp/private'):
            doc = dict(record('postgres'), description=value)
            self.path.write_text(json.dumps(doc))
            with self.subTest(value=value):
                self.assertTrue(policy.check_sboms(self.root))
                with self.assertRaises(RuntimeError):
                    policy.public_sbom(doc, 'postgres', 'image', self.root)

    def test_file_normalization_preserves_distinct_schemes_and_public_controls(self):
        for value in ('profile:///usr/bin/bao', 'custom-file:///usr/bin/bao', 'notfile:///usr/bin/bao'):
            self.assertEqual(privacy.FILE_URI.sub('', value), value)
        self.assertEqual(privacy.FILE_URI.sub('', 'source=FILE:///usr/bin/bao'), 'source=/usr/bin/bao')
        for value in ('profile://example.org/root/path', 'FILE:///usr/bin/bao',
                      'https://example.org/path', 'pkg:generic/name@1'):
            doc = dict(record('postgres'), description=value)
            with self.subTest(value=value):
                privacy.reject_private_paths(doc, self.root)
                policy.public_sbom(doc, 'postgres', 'image', self.root)
                self.path.write_text(json.dumps(doc))
                self.assertEqual(policy.check_sboms(self.root), [])


if __name__ == '__main__': unittest.main()
