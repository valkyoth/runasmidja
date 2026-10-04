"""Real cross-process cache locking around build publication and readers."""
import hashlib
import json
import multiprocessing
import os
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from openbao_lock import artifact_lock


def digest(path, _image):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def builder(folder, identity, started, entered, release, result, automatic=False, publication=False):
    import build_openbao_image as build
    import openbao_image as image
    from custody import sync_parent
    state = Path(folder)/'state'; recipe = Path(folder)/'recipe'
    def command(_run, *args):
        if args[0] == 'build':
            if not publication:
                entered.set()
                if not release.wait(15): raise RuntimeError('test release deadline')
            (state/'image.id').write_text(identity)
        return SimpleNamespace(stdout='')
    def copy(_image, path, _hash): path.write_bytes(b'binary')
    def export(_run, _save, name, path): path.write_bytes(name.encode())
    def sync(path):
        if publication:
            entered.set()
            if not release.wait(15): raise RuntimeError('test publication deadline')
        sync_parent(path)
    lock = {'upstream':{'image':'upstream'}, 'base':{'image':'base'},
            'binary_sha256':'binary', 'timestamp':1}
    try:
        with ExitStack() as patches:
            for module in (build, image):
                patches.enter_context(patch.object(module, 'STATE', state))
                patches.enter_context(patch.object(module, 'fingerprint', return_value='recipe'))
                patches.enter_context(patch.object(module, 'binding', side_effect=digest))
            patches.enter_context(patch.object(image, 'podman', side_effect=lambda _run,*args:SimpleNamespace(stdout=args[2])))
            for name,value in {'EVIDENCE':Path(folder)/'evidence', 'RECIPE':recipe}.items():
                patches.enter_context(patch.object(build,name,value))
            for name in ('require_rootless','provenance','tool'):
                patches.enter_context(patch.object(build,name))
            patches.enter_context(patch.object(build,'pins',return_value=lock))
            patches.enter_context(patch.object(build,'scan',return_value=(True,0)))
            for name,function in {'podman':command, 'copied_binary':copy, 'export_archive':export, 'sync_parent':sync}.items():
                patches.enter_context(patch.object(build,name,side_effect=function))
            started.set()
            build.build(if_missing=automatic)
            result.put(('ok', image.cached_image()))
    except Exception as error:
        result.put(('error', type(error).__name__))
        raise


def reader(folder, started, entered, release, result):
    import openbao_image as image
    try:
        with patch.object(image,'STATE',Path(folder)/'state'), \
             patch.object(image,'fingerprint',return_value='recipe'), \
             patch.object(image,'binding',side_effect=digest), \
             patch.object(image,'podman',side_effect=lambda _run,*args:SimpleNamespace(stdout=args[2])):
            started.set()
            with image.artifact() as (identity,archive):
                entered.set()
                if not release.wait(15): raise RuntimeError('test reader deadline')
                if digest(archive,identity) != hashlib.sha256(identity.encode()).hexdigest():
                    raise RuntimeError('incoherent receipt/archive pair')
                result.put(('ok', identity))
    except Exception as error:
        result.put(('error',type(error).__name__))
        raise


class LockTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(); self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.context = multiprocessing.get_context('spawn')
        recipe = self.root/'recipe'; recipe.mkdir()
        for name,value in (('Containerfile','# license\nFROM base\n'),('.containerignore','*'),('OPENBAO-LICENSE','license')):
            (recipe/name).write_text(value)

    def launch(self, target, *args):
        started,entered,release = [self.context.Event() for _ in range(3)]
        result = self.context.Queue()
        process = self.context.Process(target=target,args=(self.folder.name,*args,started,entered,release,result))
        def cleanup():
            # A killed waiter may leave its Event internals locked; never reuse it.
            if process.is_alive(): process.terminate()
            process.join(5)
            if process.is_alive(): process.kill(); process.join(5)
            result.close(); result.join_thread()
        self.addCleanup(cleanup)
        process.start()
        self.assertTrue(started.wait(10),'child did not attempt operation')
        return process,entered,release,result

    def build(self, identity, automatic=False, publication=False):
        from functools import partial
        return self.launch(partial(builder,automatic=automatic,publication=publication),identity)

    def finish(self, child):
        process,_,release,result = child; release.set(); process.join(15)
        self.assertFalse(process.is_alive(),'worker deadlocked')
        self.assertEqual(process.exitcode,0)
        record=result.get(timeout=2); self.assertEqual(record[0],'ok')
        return record[1]

    def seed(self):
        child=self.build('first'); self.assertTrue(child[1].wait(10)); self.finish(child)

    def test_two_direct_builds_serialize_and_publish_coherent_pair(self):
        first=self.build('first'); self.assertTrue(first[1].wait(10))
        second=self.build('second')
        self.assertFalse(second[1].wait(.25),'second writer entered occupied cache')
        first[2].set(); self.assertTrue(second[1].wait(10)); self.finish(second); self.finish(first)
        state=self.root/'state'; record=json.loads((state/'receipt.json').read_text())
        self.assertEqual(record['image'],'second')
        self.assertEqual(record['archive_sha256'],digest(state/'image.tar','second'))
        self.assertTrue((state/'artifact.lock').exists())

    def test_automatic_build_rechecks_receipt_after_waiting(self):
        first=self.build('first',automatic=True); self.assertTrue(first[1].wait(10))
        second=self.build('second',automatic=True)
        self.assertFalse(second[1].wait(.25))
        self.finish(first)
        self.assertEqual(self.finish(second),'first')
        self.assertFalse(second[1].is_set(),'unnecessary second cold-start build')

    def test_reader_cannot_observe_interrupted_publication(self):
        self.seed()
        writer=self.build('second',publication=True); self.assertTrue(writer[1].wait(10))
        self.assertFalse((self.root/'state/receipt.json').exists())
        child=self.launch(reader)
        self.assertFalse(child[1].wait(.25),'reader observed incomplete publication')
        self.finish(writer); self.assertTrue(child[1].wait(10))
        self.assertEqual(self.finish(child),'second')

    def test_shared_readers_hold_archive_until_both_finish(self):
        self.seed()
        first=self.launch(reader); self.assertTrue(first[1].wait(10))
        second=self.launch(reader); self.assertTrue(second[1].wait(10))
        writer=self.build('second')
        self.assertFalse(writer[1].wait(.25))
        self.finish(first); self.assertFalse(writer[1].wait(.25))
        self.finish(second); self.assertTrue(writer[1].wait(10)); self.finish(writer)

    def test_killed_writer_releases_lock_and_retry_repairs_publication(self):
        self.seed()
        first=self.build('interrupted',publication=True); self.assertTrue(first[1].wait(10))
        first[0].terminate(); first[0].join(5)
        self.assertFalse(first[0].is_alive())
        second=self.build('retry',automatic=True); self.assertTrue(second[1].wait(10))
        self.assertEqual(self.finish(second),'retry')

    def test_invalid_directory_and_lock_custody_fail_closed(self):
        for fault in ('state-mode','state-link','state-file','lock-mode','lock-link','lock-fifo','lock-directory','lock-hardlink','owner'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as folder:
                root=Path(folder); state=root/'state'; real=root/'real'; real.mkdir(mode=0o700)
                if fault=='state-link': state.symlink_to(real,target_is_directory=True)
                elif fault=='state-file': state.write_text('bad')
                else: state.mkdir(mode=0o700)
                if fault=='state-mode': state.chmod(0o755)
                lock=state/'artifact.lock'
                if fault=='lock-mode': lock.write_text(''); lock.chmod(0o644)
                if fault=='lock-link': lock.symlink_to(root/'missing')
                if fault=='lock-fifo': os.mkfifo(lock,0o600)
                if fault=='lock-directory': lock.mkdir()
                if fault=='lock-hardlink':
                    lock.write_text(''); lock.chmod(0o600); os.link(lock,root/'alias')
                with patch('openbao_lock.os.getuid',return_value=os.getuid()+1 if fault=='owner' else os.getuid()):
                    with self.assertRaises((RuntimeError,OSError)):
                        with artifact_lock(state,exclusive=True): self.fail('invalid custody admitted')

class AdmissionLockTests(unittest.TestCase):
    def test_image_gate_retains_read_scope_through_scan_and_unwinds_failures(self):
        from contextlib import contextmanager
        import image_gate as gate
        import openbao_image as image
        active = []
        @contextmanager
        def artifact(identity):
            active.append(identity)
            try: yield identity, Path('/fixture/image.tar')
            finally: active.pop()
        images={'openbao':'local-test','postgres':'pg','valkey':'vk'}
        policy={'openbao':{'method':'local-build'},'postgres':{},'valkey':{}}
        for failure in (False,True):
            def scan(service, identity, scanner, **kwargs):
                if service=='openbao':
                    self.assertEqual(active,[identity])
                    self.assertEqual(kwargs['archive'],Path('/fixture/image.tar'))
                    kwargs['archive_check']()
                    if failure: raise RuntimeError('scanner failure')
                return True,0
            with tempfile.TemporaryDirectory() as folder, \
                 patch.object(gate,'EVIDENCE',Path(folder)), patch.object(gate,'tool'), \
                 patch.object(gate,'provenance'), patch('valkey_image.admission_policy',return_value=policy), \
                 patch.object(image,'admission_policy',return_value=policy), \
                 patch.object(image,'artifact',artifact), patch.object(image,'binding',return_value='hash'), \
                 patch.object(gate,'scan',side_effect=scan):
                if failure:
                    with self.assertRaisesRegex(RuntimeError,'scanner failure'): gate.verify_images(images)
                else: gate.verify_images(images)
            self.assertEqual(active,[])


if __name__ == '__main__': unittest.main()
