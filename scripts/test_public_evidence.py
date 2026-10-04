"""Canonical public SBOM publication and independent repository binding."""
import json
import multiprocessing
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import export_image_evidence as exporter
from image_evidence import evidence_transaction
from sbom_privacy import PUBLIC_SERVICES, check_sboms


def record(service, image='image'):
    return {'bomFormat': 'CycloneDX', 'specVersion': '1.7', 'components': [{'type': 'library', 'name': 'fixture'}],
            'metadata': {'component': {'name': f'runasmidja/{service}@{image}'}}}


def export(root, service, snapshot, destination):
    with patch.object(exporter, 'ROOT', root), patch.object(exporter, 'EVIDENCE', root/'private'), \
         patch('sys.argv', ['export', service, 'image', str(snapshot), str(destination)]):
        exporter.main()


def worker(folder, service, snapshot, destination, ready, go, result):
    ready.set()
    if not go.wait(10): raise RuntimeError('test deadline')
    try:
        export(Path(folder), service, Path(snapshot), Path(destination))
        result.put('ok')
    except RuntimeError as error:
        if 'canonical' not in str(error): raise
        result.put('rejected')


class PublicEvidenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.images = self.root/'sbom/images'; self.images.mkdir(parents=True)
        for service in PUBLIC_SERVICES:
            (self.images/f'{service}.cdx.json').write_text(json.dumps(record(service)))
        with evidence_transaction(self.root/'private', 'probe', 'image') as tx:
            self.snapshot = tx.publish(record('probe'))

    def test_cli_canonical_success_and_source_symlink_rejection(self):
        target = self.images/'probe.cdx.json'
        export(self.root, 'probe', self.snapshot, target)
        self.assertEqual(json.loads(target.read_text()), record('probe'))
        self.assertEqual(check_sboms(self.root), [])
        alias = self.snapshot.parent/'alias'; alias.symlink_to(self.snapshot)
        before = target.read_bytes()
        with self.assertRaises(RuntimeError): export(self.root, 'probe', alias, target)
        self.assertEqual(target.read_bytes(), before)

    def test_wrong_destinations_and_unknown_services_do_not_write(self):
        target = self.images/'postgres.cdx.json'
        before = (target.read_bytes(), target.stat().st_ino)
        for destination in (target, self.root/'probe.cdx.json', self.images/'other.json'):
            with self.subTest(destination=destination), patch.object(exporter, 'copy_sbom') as copy:
                with self.assertRaises(RuntimeError): export(self.root, 'probe', self.snapshot, destination)
                copy.assert_not_called()
        for service in ('openbao-wolfi', '../probe', 'unknown'):
            with self.subTest(service=service), self.assertRaises(ValueError):
                export(self.root, service, self.snapshot, target)
        self.assertEqual((target.read_bytes(), target.stat().st_ino), before)

    def test_destination_aliases_cannot_select_another_service(self):
        alias = self.root/'alias'; alias.symlink_to(self.images, target_is_directory=True)
        with self.assertRaises(RuntimeError):
            export(self.root, 'probe', self.snapshot, alias/'postgres.cdx.json')
        leaf = self.images/'probe.cdx.json'; leaf.unlink(); leaf.symlink_to(self.images/'postgres.cdx.json')
        before = (self.images/'postgres.cdx.json').read_bytes()
        with self.assertRaises(RuntimeError): export(self.root, 'probe', self.snapshot, leaf)
        self.assertEqual((self.images/'postgres.cdx.json').read_bytes(), before)

    def test_repository_rejects_swapped_missing_and_malformed_canonical_reports(self):
        path = self.images/'postgres.cdx.json'
        for value in (record('probe'), record('postgres', ''), {}, [],
                      {'metadata': None}, {'metadata': {'component': {'name': 42}}}):
            with self.subTest(value=value):
                path.write_text(json.dumps(value)); self.assertTrue(check_sboms(self.root))
        path.write_text('{'); self.assertTrue(check_sboms(self.root))
        path.unlink(); self.assertTrue(check_sboms(self.root))
        path.write_text(json.dumps(record('postgres')))
        self.assertEqual(check_sboms(self.root), [])
        # Historical inventories retain their own service identity, not a fabricated suffix identity.
        (self.images/'postgres-official-blocked-2026-10-03.cdx.json').write_text(json.dumps(dict(record('postgres'), metadata={'component': {'name': 'docker.io/library/postgres@sha256:original'}})))
        self.assertEqual(check_sboms(self.root), [])

    def test_concurrent_exports_cannot_cross_service_destinations(self):
        ctx = multiprocessing.get_context('spawn'); go = ctx.Event(); result = ctx.Queue()
        processes = []
        before = (self.images/'postgres.cdx.json').read_bytes()
        try:
            for destination in ('probe.cdx.json', 'probe.cdx.json', 'postgres.cdx.json'):
                ready = ctx.Event()
                process = ctx.Process(target=worker, args=(str(self.root), 'probe', str(self.snapshot),
                    str(self.images/destination), ready, go, result))
                process.start(); processes.append(process); self.assertTrue(ready.wait(10))
            go.set()
            for process in processes:
                process.join(15); self.assertFalse(process.is_alive()); self.assertEqual(process.exitcode, 0)
            self.assertEqual(sorted(result.get(timeout=2) for _ in processes), ['ok', 'ok', 'rejected'])
            self.assertEqual((self.images/'postgres.cdx.json').read_bytes(), before)
            self.assertEqual(check_sboms(self.root), [])
            self.assertFalse(list(self.images.glob('.evidence-*')))
        finally:
            for process in processes:
                if process.is_alive(): process.terminate()
                process.join(5)
                if process.is_alive(): process.kill(); process.join(5)
            result.close(); result.join_thread()


if __name__ == '__main__': unittest.main()
