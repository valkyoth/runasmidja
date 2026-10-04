"""Retention and export regressions for private image evidence."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import image_evidence as evidence
import test_image_evidence as helpers


class RetentionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / 'private'
        self.record = helpers.EvidenceTests().record()

    def test_count_boundary_reuse_and_service_isolation(self):
        with evidence.evidence_transaction(self.root, 'probe', 'image') as tx:
            first = tx.publish(self.record)
            for n in range(31):
                tx.publish({'image': 'image', 'serial': n}, 'qualification')
            inode = first.stat().st_ino
            self.assertEqual(tx.publish(self.record), first)
            self.assertEqual(first.stat().st_ino, inode)
            with self.assertRaisesRegex(RuntimeError, 'reviewed pruning'):
                tx.publish({'image': 'image', 'serial': 32}, 'qualification')
            self.assertEqual(len(list(self.root.glob('*.json'))), 32)
            self.assertFalse(list(self.root.glob('*.next')))
        with evidence.evidence_transaction(self.root, 'other', 'image') as tx:
            tx.publish({'image': 'image'}, 'qualification')

    def test_byte_boundary_overfull_and_identical_reuse(self):
        size = len((json.dumps(self.record, indent=2) + '\n').encode())
        with evidence.evidence_transaction(self.root, 'probe', 'image') as tx:
            with patch.object(evidence, 'MAX_SERVICE_EVIDENCE', size - 1):
                with self.assertRaises(RuntimeError): tx.publish(self.record)
            self.assertFalse(list(self.root.glob('*.json*')))
            with patch.object(evidence, 'MAX_SERVICE_EVIDENCE', size):
                path = tx.publish(self.record)
                self.assertEqual(tx.publish(self.record), path)
                with self.assertRaises(RuntimeError):
                    tx.publish({'image': 'image'}, 'qualification')
            with patch.object(evidence, 'MAX_SERVICE_EVIDENCE', size - 1):
                with self.assertRaises(RuntimeError):
                    tx.publish({'image': 'image'}, 'qualification')

    def test_interrupted_publications_consume_budget_and_retry(self):
        with evidence.evidence_transaction(self.root, 'probe', 'image') as tx:
            with patch('custody.os.replace', side_effect=OSError('rename')):
                with self.assertRaises(OSError): tx.publish(self.record)
            pending = list(self.root.glob('*.next'))
            self.assertEqual(len(pending), 1)
            with patch.object(evidence, 'MAX_SERVICE_SNAPSHOTS', 1):
                with self.assertRaisesRegex(RuntimeError, 'retention budget'):
                    tx.publish({'image': 'image'}, 'qualification')
            path = tx.publish(self.record)
            self.assertEqual(tx.read(path), self.record)
            self.assertFalse(list(self.root.glob('*.next')))

    def test_retained_entry_custody_fails_closed(self):
        for kind in ('symlink', 'directory', 'fifo', 'hardlink', 'mode', 'owner'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                entry = root / ('probe-' + 'a'*64 + '-' + 'b'*64 + '.cdx.json')
                if kind == 'symlink': entry.symlink_to(root/'absent')
                elif kind == 'directory': entry.mkdir(mode=0o700)
                elif kind == 'fifo': os.mkfifo(entry, 0o600)
                else:
                    entry.write_text('retained'); entry.chmod(0o600)
                    if kind == 'hardlink': os.link(entry, root/'alias')
                    if kind == 'mode': entry.chmod(0o644)
                if kind == 'owner':
                    real_custody = evidence.custody
                    def wrong_owner(info):
                        real_custody(SimpleNamespace(st_mode=info.st_mode,
                            st_uid=os.getuid()+1, st_nlink=info.st_nlink))
                    with patch.object(evidence, 'custody', side_effect=wrong_owner):
                        with self.assertRaises(RuntimeError):
                            evidence.reserve_snapshot(root, 'probe', 1)
                else:
                    with self.assertRaises(RuntimeError):
                        evidence.reserve_snapshot(root, 'probe', 1)

    def test_export_rejects_private_tree_and_aliases_without_mutation(self):
        with evidence.evidence_transaction(self.root, 'probe', 'image') as tx:
            source = tx.publish(self.record)
            other = tx.publish(dict(self.record, serialNumber='other'))
        nested = self.root/'nested'; nested.mkdir()
        alias = self.root.parent/'directory-alias'; alias.symlink_to(self.root, target_is_directory=True)
        targets = (source, other, self.root/'new.json', nested/'new.json',
                   alias/source.name, alias/'new.json', nested/'..'/'new.json')
        original = {p: (p.read_bytes(), p.stat().st_ino, p.stat().st_mode) for p in (source, other)}
        for target in targets:
            with self.subTest(target=target), self.assertRaises(RuntimeError):
                evidence.copy_sbom(self.root, 'probe', 'image', source, target)
            for path, expected in original.items():
                self.assertEqual((path.read_bytes(), path.stat().st_ino, path.stat().st_mode), expected)
        self.assertFalse(list(self.root.rglob('.evidence-*')))
        self.assertFalse(list(self.root.rglob('new.json')))
        hardlink = self.root.parent/'hardlink.json'; os.link(source, hardlink)
        with self.assertRaisesRegex(RuntimeError, 'aliases'):
            evidence.copy_sbom(self.root, 'probe', 'image', source, hardlink)
        self.assertTrue(os.path.samestat(source.stat(), hardlink.stat()))
        self.assertEqual(source.stat().st_mode & 0o777, 0o600)
        hardlink.unlink()
        public = self.root.parent/'public.json'
        evidence.copy_sbom(self.root, 'probe', 'image', source, public)
        self.assertEqual(json.loads(public.read_text()), self.record)


class ConcurrentRetentionTests(helpers.ConcurrentEvidenceTests):
    # Reuse only the process harness; inherited tests are exercised in their own module.
    test_same_service_different_images_serialize_and_keep_both_results = None
    test_same_image_new_scan_does_not_overwrite_previous_snapshot = None
    test_unrelated_services_scan_concurrently = None
    test_scanner_failure_releases_lock_without_publishing = None

    def test_competing_scans_cannot_exceed_last_slot(self):
        with evidence.evidence_transaction(self.root, 'openbao', 'a') as tx:
            for n in range(31): tx.publish({'image': 'a', 'n': n}, 'qualification')
        first = self.start('openbao', 'a', 'first'); self.assertTrue(first[1].wait(10))
        # The scanner succeeds; publication alone must reject the second scan.
        second = self.start('openbao', 'b', 'second', fault='publication')
        self.assertFalse(second[1].wait(.25))
        self.assertEqual(self.finish(first)[0], 'ok')
        self.assertTrue(second[1].wait(10))
        self.assertEqual(self.finish(second)[0], 'expected-failure')
        self.assertEqual(len(list(self.root.glob('*.json'))), 32)
        self.assertFalse(list(self.root.glob('*.next')))


if __name__ == '__main__': unittest.main()
