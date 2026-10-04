"""Actual build transaction/custody with small archives and injected external faults."""
import hashlib
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import build_postgres_image as build
import postgres_image as image
from custody import replace_private
from test_postgres_image import archive


class BuildRetryTests(unittest.TestCase):
    def environment(self, folder, patches, fault):
        state = Path(folder)
        source = b'public source fixture'
        (state / 'postgresql-19beta4.tar.bz2').write_bytes(source)
        progress = {'builds': 0, 'loaded': False, 'image': None}
        def sandbox(recipe):
            progress['builds'] += 1
            progress['image'] = archive(state / 'candidate.tar')
            replace_private(state / 'contained-image.id', progress['image'])
            return SimpleNamespace(returncode=0, stdout='', stderr='')
        def scan(service, *args, **kwargs):
            if service == 'postgres':
                self.assertFalse((state / 'receipt.json').exists())
                if fault[0] == 'scanner': raise RuntimeError('scanner failed')
                if fault[0] == 'findings': return False, 1
                if fault[0] == 'changed':
                    with (state / 'candidate.tar').open('ab') as output:
                        output.write(b'changed')
            return True, 0
        def load(*args, **kwargs):
            self.assertFalse((state / 'receipt.json').exists())
            if fault[0] == 'load': raise RuntimeError('load failed')
            progress['loaded'] = True
        def inspect(*args, **kwargs):
            if not progress['loaded'] or fault[0] == 'identity':
                raise RuntimeError('loaded identity unavailable')
            return SimpleNamespace(stdout=progress['image'])
        def write(path, value):
            if fault[0] == 'receipt': raise OSError('receipt write failed')
            replace_private(path, value)
            if fault[0] == 'receipt-visible': raise OSError('post-rename sync failed')
        for module in (build, image):
            patches.enter_context(patch.object(module, 'STATE', state))
            patches.enter_context(patch.object(module, 'fingerprint', return_value='fixture-recipe'))
        patches.enter_context(patch.object(build, 'EVIDENCE', state))
        patches.enter_context(patch.object(build, 'SOURCE_SHA', hashlib.sha256(source).hexdigest()))
        patches.enter_context(patch.object(build, 'provenance'))
        patches.enter_context(patch.object(build, 'tool', return_value='fixture-tool'))
        patches.enter_context(patch.object(build, 'sandbox', side_effect=sandbox))
        patches.enter_context(patch.object(build, 'scan', side_effect=scan))
        patches.enter_context(patch.object(build, 'run_bounded', side_effect=load))
        patches.enter_context(patch.object(image, 'run_bounded', side_effect=inspect))
        patches.enter_context(patch.object(image, 'replace_private', side_effect=write))
        return progress

    def test_each_failed_admission_can_retry_without_manual_custody_repair(self):
        for name in ('scanner', 'findings', 'load', 'identity', 'receipt', 'receipt-visible', 'changed'):
            with self.subTest(fault=name), tempfile.TemporaryDirectory() as folder, ExitStack() as patches:
                fault = [name]
                progress = self.environment(folder, patches, fault)
                with self.assertRaises((RuntimeError, OSError)):
                    image.ensure_image()
                self.assertEqual((Path(folder) / 'receipt.json').exists(), name == 'receipt-visible')
                fault[0] = None
                self.assertEqual(image.ensure_image(), progress['image'])
                self.assertTrue(progress['loaded'])
                self.assertEqual(image.validate_image(progress['image']), Path(folder) / 'image.tar')
                self.assertEqual(progress['builds'], 1 if name == 'receipt-visible' else 2)

    def test_failed_replacement_preserves_previous_committed_artifacts_until_publication(self):
        for name in ('scanner', 'load'):
            with self.subTest(fault=name), tempfile.TemporaryDirectory() as folder, ExitStack() as patches:
                fault = [None]
                progress = self.environment(folder, patches, fault)
                image.ensure_image()
                state = Path(folder)
                before = [(state / filename).read_bytes() for filename in ('receipt.json', 'image.tar')]
                # Replacement scans/imports must also tolerate the previous final receipt.
                def rescan(service, *args, **kwargs):
                    if service == 'postgres' and name == 'scanner':
                        raise RuntimeError('scan failed')
                    return True, 0
                patches.enter_context(patch.object(build, 'scan', side_effect=rescan))
                patches.enter_context(patch.object(build, 'run_bounded', side_effect=RuntimeError('load failed')))
                with self.assertRaises(RuntimeError): build.build()
                self.assertEqual(before, [(state / filename).read_bytes() for filename in ('receipt.json', 'image.tar')])
                self.assertEqual(image.ensure_image(), progress['image'])

    def test_replacement_publication_failures_allow_automatic_rebuild(self):
        for boundary in ('receipt', 'archive-rename', 'archive-sync'):
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as folder, ExitStack() as patches:
                fault = [None]
                progress = self.environment(folder, patches, fault)
                image.ensure_image()
                candidate = Path(folder) / 'candidate.tar'
                archive(candidate)
                admitted = image.candidate_receipt(candidate, progress['image'], 'fixture-recipe')
                with ExitStack() as failure:
                    if boundary == 'receipt': fault[0] = 'receipt'
                    elif boundary == 'archive-rename':
                        failure.enter_context(patch.object(image.os, 'replace', side_effect=OSError('rename failed')))
                    else:
                        failure.enter_context(patch.object(image, 'sync_parent', side_effect=OSError('sync failed')))
                    with self.assertRaises(OSError): image.commit_candidate(admitted)
                self.assertFalse((Path(folder) / 'receipt.json').exists())
                fault[0] = None
                self.assertEqual(image.ensure_image(), progress['image'])
                self.assertEqual(progress['builds'], 2)


if __name__ == '__main__':
    unittest.main()
