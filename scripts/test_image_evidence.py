"""Evidence writers serialize; immutable scan snapshots cannot cross image/run identity."""
import json
import multiprocessing
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import image_gate as gate
import image_evidence as evidence


def scanner_worker(folder, service, image, serial, fault, started, entered, release, output):
    def scanner(*args, **kwargs):
        entered.set()
        if not release.wait(15): raise RuntimeError('test scanner deadline')
        if fault: raise RuntimeError('scanner operational failure')
        return SimpleNamespace(stdout=json.dumps({'bomFormat':'CycloneDX', 'serialNumber':serial,
            'components':[{'name':'fixture'}]}))
    with patch.object(gate,'EVIDENCE',Path(folder)), patch.object(gate,'run_bounded',side_effect=scanner):
        started.set()
        try:
            result=gate.scan(service,image,'scanner')
            output.put(('ok',str(result.snapshot)))
        except RuntimeError:
            if not fault: raise
            output.put(('expected-failure',None))


class ConcurrentEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary=tempfile.TemporaryDirectory(); self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name); self.context=multiprocessing.get_context('spawn')

    def start(self, service, image, serial, fault=False):
        started,entered,release=[self.context.Event() for _ in range(3)]
        output=self.context.Queue()
        process=self.context.Process(target=scanner_worker,
            args=(self.temporary.name,service,image,serial,fault,started,entered,release,output))
        def cleanup():
            if process.is_alive(): process.terminate()
            process.join(5)
            if process.is_alive(): process.kill(); process.join(5)
            output.close(); output.join_thread()
        self.addCleanup(cleanup); process.start()
        self.assertTrue(started.wait(10))
        return process,entered,release,output

    def finish(self, child):
        process,_,release,output=child; release.set(); process.join(15)
        self.assertFalse(process.is_alive(),'scan/publication deadlock')
        self.assertEqual(process.exitcode,0)
        return output.get(timeout=2)

    def test_same_service_different_images_serialize_and_keep_both_results(self):
        first=self.start('openbao','image-a','run-a'); self.assertTrue(first[1].wait(10))
        second=self.start('openbao','image-b','run-b'); self.assertFalse(second[1].wait(.25))
        a=self.finish(first); self.assertTrue(second[1].wait(10)); b=self.finish(second)
        self.assertNotEqual(a[1],b[1])
        for record,image,serial in ((a,'image-a','run-a'),(b,'image-b','run-b')):
            self.assertEqual(record[0],'ok')
            with evidence.evidence_transaction(self.root,'openbao',image) as tx:
                self.assertEqual(tx.read(Path(record[1]))['serialNumber'],serial)
        self.assertFalse((self.root/'openbao.cdx.json').exists())
        self.assertFalse(list(self.root.glob('*.next')))

    def test_same_image_new_scan_does_not_overwrite_previous_snapshot(self):
        first=self.start('openbao','same','run-a'); self.assertTrue(first[1].wait(10))
        second=self.start('openbao','same','run-b'); self.assertFalse(second[1].wait(.25))
        a=self.finish(first); before=Path(a[1]).read_bytes()
        self.assertTrue(second[1].wait(10)); b=self.finish(second)
        self.assertNotEqual(a[1],b[1]); self.assertEqual(Path(a[1]).read_bytes(),before)

    def test_unrelated_services_scan_concurrently(self):
        first=self.start('openbao','a','a'); self.assertTrue(first[1].wait(10))
        second=self.start('valkey','b','b'); self.assertTrue(second[1].wait(10))
        self.assertEqual(self.finish(first)[0],'ok'); self.assertEqual(self.finish(second)[0],'ok')

    def test_scanner_failure_releases_lock_without_publishing(self):
        first=self.start('openbao','a','a',fault=True); self.assertTrue(first[1].wait(10))
        second=self.start('openbao','b','b'); self.assertFalse(second[1].wait(.25))
        self.assertEqual(self.finish(first)[0],'expected-failure')
        self.assertTrue(second[1].wait(10)); self.assertEqual(self.finish(second)[0],'ok')
        self.assertEqual(len(list(self.root.glob('*.cdx.json'))),1)


class EvidenceTests(unittest.TestCase):
    def record(self, image='image'):
        return {'bomFormat':'CycloneDX','metadata':{'component':{'name':'runasmidja/probe@'+image}},
                'components':[{'name':'fixture'}]}

    def test_publication_export_identity_integrity_and_immutable_reuse(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); record=self.record()
            with evidence.evidence_transaction(root,'probe','image') as tx:
                path=tx.publish(record); inode=path.stat().st_ino
                self.assertEqual(tx.publish(record),path); self.assertEqual(path.stat().st_ino,inode)
                with self.assertRaises(RuntimeError): tx.publish(self.record('wrong'))
            with self.assertRaises(RuntimeError): tx.publish(record)
            with self.assertRaises(RuntimeError): tx.read(path)
            destination=root/'public.json'
            evidence.copy_sbom(root,'probe','image',path,destination)
            self.assertEqual(json.loads(destination.read_text()),record)
            destination.chmod(0o644)
            evidence.copy_sbom(root,'probe','image',path,destination)
            link=root/'symlink.json'; link.symlink_to(destination)
            with self.assertRaises(RuntimeError): evidence.copy_sbom(root,'probe','image',path,link)
            import export_image_evidence as exporter
            with patch.object(exporter,'EVIDENCE',root), patch('sys.argv',
                    ['export','probe','image',str(path),str(destination)]): exporter.main()
            alias=root/'alias-snapshot.json'; alias.symlink_to(path)
            with patch.object(exporter,'EVIDENCE',root), patch('sys.argv',
                    ['export','probe','image',str(alias),str(destination)]):
                with self.assertRaises(RuntimeError): exporter.main()
            with self.assertRaises(RuntimeError): evidence.copy_sbom(root,'probe','wrong',path,destination)
            with evidence.evidence_transaction(root,'probe','image') as tx:
                with self.assertRaises(RuntimeError): tx.read(destination)
                path.write_text(json.dumps(self.record('changed')))
                with self.assertRaises(RuntimeError): tx.read(path)
                with self.assertRaises(RuntimeError): tx.publish(record)

    def test_invalid_service_fails_before_scanner_or_filesystem_mutation(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(gate,'EVIDENCE',Path(folder)/'unused'), \
             patch.object(gate,'run_bounded') as scanner:
            for service in ('../escape','','UPPER','a/b','a'*65):
                with self.assertRaises(ValueError): gate.scan(service,'image','scanner')
            scanner.assert_not_called(); self.assertFalse((Path(folder)/'unused').exists())

    def test_failed_publication_retry_and_existing_snapshot_durability(self):
        for fault in ('write','sync'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as folder:
                root=Path(folder)
                with evidence.evidence_transaction(root,'probe','image') as tx:
                    if fault=='write':
                        with patch.object(evidence,'replace_private',side_effect=RuntimeError('write')):
                            with self.assertRaises(RuntimeError): tx.publish(self.record())
                    else:
                        with patch('custody.sync_parent',side_effect=RuntimeError('sync')):
                            with self.assertRaises(RuntimeError): tx.publish(self.record())
                    path=tx.publish(self.record())
                    with patch.object(evidence,'sync_parent',side_effect=RuntimeError('sync')):
                        with self.assertRaises(RuntimeError): tx.publish(self.record())
                    self.assertEqual(tx.read(path),self.record())

    def test_probe_annotation_publishes_atomically_and_rejects_colliding_reference(self):
        report={'bomFormat':'CycloneDX','components':[{'name':'fixture','bom-ref':'os'}]}
        component={'name':'runasmidja-server','bom-ref':'probe','hashes':[{'alg':'SHA-256','content':'a'*64}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(gate,'EVIDENCE',Path(folder)), \
             patch.object(gate,'run_bounded',return_value=SimpleNamespace(stdout=json.dumps(report))):
            result=gate.scan('probe','image','scanner',component=component)
            with evidence.evidence_transaction(Path(folder),'probe','image') as tx:
                self.assertEqual(tx.read(result.snapshot)['components'][-1],component)
            with self.assertRaises(RuntimeError): gate.scan('probe','image','scanner',component={'bom-ref':'os'})
            with self.assertRaises(RuntimeError): gate.scan('valkey','image','scanner',component=component)
            self.assertEqual(len(list(Path(folder).glob('*.cdx.json'))),1)

    def test_export_publication_failure_keeps_whole_files_and_retries(self):
        for fault in ('rename','directory-sync'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as folder:
                root=Path(folder); target=root/'public.json'; target.write_text('previous')
                with evidence.evidence_transaction(root,'probe','image') as tx:
                    snapshot=tx.publish(self.record())
                sync=evidence.sync_parent
                def failed_sync(path):
                    if path==target: raise RuntimeError('directory sync')
                    sync(path)
                if fault=='rename':
                    failure=patch.object(evidence.os,'replace',side_effect=RuntimeError('rename'))
                else: failure=patch.object(evidence,'sync_parent',side_effect=failed_sync)
                with failure, self.assertRaises(RuntimeError):
                    evidence.copy_sbom(root,'probe','image',snapshot,target)
                if fault=='rename': self.assertEqual(target.read_text(),'previous')
                else: self.assertEqual(json.loads(target.read_text()),self.record())
                self.assertFalse(list(root.glob('.evidence-*')))
                evidence.copy_sbom(root,'probe','image',snapshot,target)
                self.assertEqual(json.loads(target.read_text()),self.record())

    def test_qualification_is_image_and_content_bound(self):
        import probe_image
        with tempfile.TemporaryDirectory() as folder, patch.object(probe_image,'EVIDENCE',Path(folder)), \
             patch('check_release.source_digest',return_value='source'):
            a=probe_image.evidence('a','binary','archive'); b=probe_image.evidence('b','binary','archive')
            self.assertNotEqual(a,b)
            with evidence.evidence_transaction(Path(folder),'probe','a') as tx:
                self.assertEqual(tx.read(a,'qualification')['image'],'a')
                with self.assertRaises(RuntimeError): tx.read(b,'qualification')
                with self.assertRaises(RuntimeError): tx.publish({'image':'wrong'},'qualification')


if __name__ == '__main__': unittest.main()
