"""Network-share URI schemes are case-insensitive in public evidence."""
import itertools
import json
import unittest
import inventory_privacy as privacy
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


def casings(word):
    return (''.join(letters) for letters in itertools.product(*[(c, c.upper()) for c in word]))


class ShareUriTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_all_scheme_casings_in_keys_and_values(self):
        for scheme in ('file', 'smb', 'cifs', 'nfs', 'afp', 'sshfs'):
            for spelling in casings(scheme):
                for suffix in ('server/share', 'server'):
                    uri = spelling + '://' + suffix
                    for doc in ({'nested': [uri]}, {'nested': [{uri: 'value'}]}):
                        with self.subTest(uri=uri, doc=doc), self.assertRaises(RuntimeError):
                            privacy.reject_private_paths(doc, self.root)
                    with self.subTest(embedded=uri), self.assertRaises(RuntimeError):
                        privacy.reject_private_paths({'description': 'source=' + uri}, self.root)
        for spelling in casings('file'):
            with self.subTest(local=spelling), self.assertRaises(RuntimeError):
                privacy.reject_private_paths({'path': spelling + ':///root/.ssh/key'}, self.root)

    def test_repository_and_scanner_share_the_rejection(self):
        for uri in ('FILE://server/share', 'File:///tmp/build/session', 'SmB://server/share',
                    'CIFS://server/share', 'NfS://server/share', 'AFP://server/share',
                    'SsHfS://server/share'):
            doc = dict(record('postgres'), description=uri)
            self.path.write_text(json.dumps(doc))
            with self.subTest(uri=uri):
                self.assertTrue(policy.check_sboms(self.root))
                with self.assertRaises(RuntimeError):
                    policy.public_sbom(doc, 'postgres', 'image', self.root)

    def test_https_package_and_nonshare_scheme_controls(self):
        for uri in ('https://example.org/path', 'HTTPS://example.org/path',
                    'pkg:generic/name@1', 'pkg:golang/example.org/module@v1.0.0',
                    'https://example.org/smb/document', 'cgr.dev/image@sha256:abc',
                    'custom-smb://example.org/path', 'profile://example.org/path',
                    'FILE:///usr/bin/bao'):
            doc = dict(record('postgres'), description=uri)
            with self.subTest(uri=uri):
                privacy.reject_private_paths(doc, self.root)
                self.path.write_text(json.dumps(doc))
                self.assertEqual(policy.check_sboms(self.root), [])
                policy.public_sbom(doc, 'postgres', 'image', self.root)


if __name__ == '__main__': unittest.main()
