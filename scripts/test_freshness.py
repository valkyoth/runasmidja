"""Registry ordering, prerelease and yanked-version rejection."""
import unittest
from check_freshness import crate_version, postgres_version

class FreshnessTests(unittest.TestCase):
    def test_highest_stable_non_yanked(self):
        data = {'versions': [{'num': '2.0.0'}, {'num': '9.0.0-beta.1'}, {'num': '3.0.0', 'yanked': True}, {'num': '2.10.0'}, {'num': '2.9.0'}]}
        self.assertEqual(crate_version(data), '2.10.0')
    def test_unavailable_stable_fails(self):
        with self.assertRaises(ValueError):
            crate_version({'versions': [{'num': '1.0.0-rc.1'}]})

    def test_postgres_beta_rc_ga_and_patch_order(self):
        self.assertEqual(postgres_version('/ftp/source/v19beta4/ /ftp/source/v19beta3/'), '19beta4')
        self.assertEqual(postgres_version('/ftp/source/v19beta4/ /ftp/source/v19rc1/'), '19rc1')
        self.assertEqual(postgres_version('/ftp/source/v19rc2/ /ftp/source/v19/ /ftp/source/v19.1/'), '19.1')
    def test_postgres_empty_source_fails(self):
        with self.assertRaises(ValueError):
            postgres_version('<html>missing</html>')

    def test_postgres_relative_directory_links(self):
        self.assertEqual(postgres_version('<a href="v19beta4/">v19beta4</a>'), '19beta4')
