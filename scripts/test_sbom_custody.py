"""Descriptor-rooted custody and unambiguous inventory JSON regressions."""
import json
import os
import stat
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import sbom_privacy as policy
import test_sbom_structure as fixtures
from test_public_evidence import record


class CustodyTests(unittest.TestCase):
    setUp = fixtures.StructureTests.setUp

    def test_ancestor_symlinks_and_nested_symlinks_are_rejected(self):
        for path in (self.images, self.root/'sbom'):
            original = path.with_name(path.name + '-original')
            path.rename(original); path.symlink_to(original, target_is_directory=True)
            try:
                self.assertTrue(policy.check_sboms(self.root))
            finally:
                path.unlink(); original.rename(path)
        nested = self.images/'nested'; nested.symlink_to(self.root, target_is_directory=True)
        self.assertTrue(policy.check_sboms(self.root)); nested.unlink()
        self.assertEqual(policy.check_sboms(self.root), [])

    def test_file_and_directory_permissions(self):
        for path in (self.root, self.root/'sbom', self.images, self.path):
            original = path.stat().st_mode & 0o777
            try:
                for mode in ((0o770, 0o777) if path.is_dir() else (0o660, 0o666)):
                    path.chmod(mode)
                    with self.subTest(path=path, mode=mode):
                        self.assertTrue(policy.check_sboms(self.root))
                path.chmod(0o755 if path.is_dir() else 0o644)
                self.assertEqual(policy.check_sboms(self.root), [])
            finally: path.chmod(original)

    def test_wrong_directory_and_file_owners_fail_closed(self):
        real = os.fstat
        for directories in (False, True):
            def wrong_owner(fd):
                info = real(fd)
                return SimpleNamespace(st_uid=os.getuid()+1, st_mode=info.st_mode,
                    st_size=info.st_size, st_nlink=info.st_nlink) if (
                    stat.S_ISDIR(info.st_mode) == directories) else info
            with self.subTest(directories=directories), patch.object(policy.os, 'fstat', side_effect=wrong_owner):
                self.assertTrue(policy.check_sboms(self.root))
        self.assertEqual(policy.check_sboms(self.root), [])

    def test_open_directory_cannot_be_redirected_by_path_replacement(self):
        real_load = policy.load_public_json
        retained = self.root/'retained-images'
        alternate = self.root/'alternate'; alternate.mkdir()
        (alternate/self.path.name).write_text(json.dumps(record('probe')))
        changed = False
        def replace_parent(name, directory):
            nonlocal changed
            if name == self.path.name and not changed:
                self.images.rename(retained)
                self.images.symlink_to(alternate, target_is_directory=True)
                changed = True
            return real_load(name, directory)
        try:
            with patch.object(policy, 'load_public_json', side_effect=replace_parent):
                self.assertEqual(policy.check_sboms(self.root), [])
            self.assertTrue(changed)
            self.assertTrue(policy.check_sboms(self.root))
        finally:
            if changed: self.images.unlink(); retained.rename(self.images)

    def test_duplicate_keys_rejected_at_all_levels(self):
        valid = json.dumps(record('postgres'))
        cases = [
            valid.replace('"metadata":', '"metadata":{"component":{"name":"runasmidja/probe@image"}},"metadata":'),
            valid.replace('"component":', '"component":{"name":"runasmidja/probe@image"},"component":'),
            valid.replace('"components":', '"components":[],"components":'),
            valid.replace('"bomFormat":', '"bomFormat":"SPDX","bomFormat":'),
            valid.replace('"name": "fixture"', '"name":"different","name":"fixture"'),
            valid.replace('"type": "library"', '"type":"application","type":"library"'),
            valid.replace('"specVersion":', '"specVersion":"1.5","specVersion":'),
            valid.replace('"metadata":', '"meta\\u0064ata":{},"metadata":'),
        ]
        for content in cases:
            with self.subTest(content=content):
                self.path.write_text(content)
                self.assertTrue(policy.check_sboms(self.root))
        self.path.write_text(valid)
        self.assertEqual(policy.check_sboms(self.root), [])
        extra = self.images/'extra.json'; extra.write_text('{"a":1,"a":2}')
        self.assertTrue(policy.check_sboms(self.root))

    def test_descriptor_relative_loader_rejects_path_traversal(self):
        with policy.custody_directory(self.images) as directory:
            for name in ('', '.', '..', '../postgres.cdx.json', str(self.path)):
                with self.subTest(name=name), self.assertRaises(ValueError):
                    policy.load_public_json(name, directory)


if __name__ == '__main__': unittest.main()
