"""Tests for credential-safe fixture helpers without real service state."""
import os
import tempfile
import unittest
from pathlib import Path
from stack_common import NoRedirect, private

class StackTests(unittest.TestCase):
    def test_private_files_are_exclusive_and_owner_only(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'secret'
            private(path, 'test-only')
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(FileExistsError):
                private(path, 'replace')
            self.assertEqual(path.read_text(), 'test-only')

    def test_authenticated_endpoint_never_redirects(self):
        self.assertIsNone(NoRedirect().redirect_request(None, None, 302, '', {}, 'https://external.invalid'))
