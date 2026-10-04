"""Admission/publication failures must never mint an accepted OpenBao receipt."""
import json
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import build_openbao_image as build
from custody import read_private


class BuildTests(unittest.TestCase):
    def test_failure_then_retry_never_publishes_unadmitted_candidate(self):
        faults = ('rootless', 'provenance', 'input-scan', 'copy', 'build', 'export',
                  'binding', 'candidate-scan', 'scanner-error', 'recipe-drift',
                  'archive-drift', 'rename', 'fsync', 'receipt', None)
        for fault in faults:
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
                root = Path(directory); state = root/'state'; recipe = root/'recipe'
                recipe.mkdir()
                for name, value in (('Containerfile', '# license\nFROM base\n'),
                                    ('.containerignore', '*'), ('OPENBAO-LICENSE', 'license')):
                    (recipe/name).write_text(value)
                lock = {'upstream': {'image':'upstream'}, 'base':{'image':'base'},
                        'binary_sha256':'binary', 'timestamp':1}
                active = [fault]; scan_calls = [0]; binding_calls = [0]; fingerprints = [0]
                def fail(name):
                    if active[0] == name: raise RuntimeError(name)
                def guard(_run): fail('rootless')
                def provenance(*args): fail('provenance')
                def copy(_image, path, _hash): fail('copy'); path.write_bytes(b'bao')
                def podman(_run, *args):
                    if args[0] == 'build':
                        fail('build'); (state/'image.id').write_text('sha256:image')
                    return SimpleNamespace(stdout='')
                def export(_run, _save, _image, path): fail('export'); path.write_bytes(b'archive')
                def scan(*args, **kwargs):
                    scan_calls[0] += 1
                    if kwargs:
                        fail('scanner-error'); kwargs['archive_check']()
                        return (active[0] != 'candidate-scan', None)
                    return (active[0] != 'input-scan', None)
                def binding(*args):
                    fail('binding'); binding_calls[0] += 1
                    return 'changed' if active[0]=='archive-drift' and binding_calls[0]>1 else 'archive'
                def fingerprint():
                    fingerprints[0] += 1
                    return 'changed' if active[0]=='recipe-drift' and fingerprints[0]>1 else 'recipe'
                original_replace = build.os.replace
                original_receipt = build.replace_private
                def rename(*args): fail('rename'); original_replace(*args)
                def receipt(*args): fail('receipt'); original_receipt(*args)
                for name, value in {'STATE':state, 'EVIDENCE':root/'evidence', 'RECIPE':recipe}.items():
                    stack.enter_context(patch.object(build, name, value))
                functions = {'require_rootless':guard, 'provenance':provenance, 'copied_binary':copy,
                             'podman':podman, 'export_archive':export, 'scan':scan, 'binding':binding,
                             'fingerprint':fingerprint, 'sync_parent':lambda path:fail('fsync'),
                             'replace_private':receipt}
                for name, function in functions.items():
                    stack.enter_context(patch.object(build, name, side_effect=function))
                stack.enter_context(patch.object(build.os, 'replace', side_effect=rename))
                stack.enter_context(patch.object(build, 'pins', return_value=lock))
                stack.enter_context(patch.object(build, 'tool', return_value='tool'))
                if fault:
                    with self.assertRaises(RuntimeError): build.build()
                    self.assertFalse((state/'receipt.json').exists())
                    if fault == 'rootless': self.assertFalse(state.exists())
                active[0] = None; fingerprints[0] = 0; binding_calls[0] = 0
                build.build()
                record = json.loads(read_private(state/'receipt.json'))
                self.assertEqual(record['image'], 'sha256:image')
                self.assertEqual(record['archive_sha256'], 'archive')
                self.assertEqual((state/'image.tar').read_bytes(), b'archive')
                self.assertFalse((state/'candidate.tar').exists())


if __name__ == '__main__': unittest.main()
