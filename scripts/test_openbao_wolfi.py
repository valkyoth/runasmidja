"""Static material, local custody, explicit switching and audit failure regressions."""
import copy
import hashlib
import json
import os
import struct
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import openbao_material as material
import openbao_image as image
import switch_openbao as switch
import qualification_openbao as qualify
from custody import replace_private


def elf(kind=1):
    data = bytearray(120); data[:6] = b'\x7fELF\x02\x01'
    struct.pack_into('<H', data, 18, 62); struct.pack_into('<Q', data, 32, 64)
    struct.pack_into('<HH', data, 54, 56, 1); struct.pack_into('<I', data, 64, kind)
    return bytes(data)


class MaterialTests(unittest.TestCase):
    def test_static_hash_platform_and_dynamic_header_denials(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'bao'
            for value, valid in ((elf(), True), (elf(2), False), (elf(3), False),
                                 (b'not-elf', False), (elf()[:70], False)):
                path.write_bytes(value)
                digest = hashlib.sha256(value).hexdigest()
                if valid: material.static_binary(path, digest)
                else:
                    with self.assertRaises(RuntimeError): material.static_binary(path, digest)
            path.write_bytes(elf())
            with self.assertRaises(RuntimeError): material.static_binary(path, '0'*64)

    def test_material_copy_failure_cleans_only_owned_image(self):
        owner = 'test-owner'; identity = 'a'*64
        info = {'Id': identity, 'Image': 'sha256:abc', 'Config': {'Labels': {'io.runasmidja.openbao-material': owner}}}
        for fault in ('copy', 'hash', 'ownership', 'success'):
            calls = []
            def command(_run, *args, **kwargs):
                calls.append(args)
                if args[0] == 'create': return SimpleNamespace(stdout=identity)
                if args[0] == 'inspect':
                    return SimpleNamespace(stdout=json.dumps([{**info, 'Id': 'wrong'} if fault == 'ownership' else info]))
                if args[:2] == ('image', 'inspect'): return SimpleNamespace(stdout='abc')
                if args[0] == 'cp' and fault == 'copy': raise RuntimeError('copy failed')
                return SimpleNamespace(stdout='')
            with patch.object(material.uuid, 'uuid4', return_value=owner), patch.object(material, 'podman', side_effect=command), \
                 patch.object(material, 'static_binary', side_effect=RuntimeError('hash') if fault == 'hash' else None):
                if fault == 'success': material.copied_binary('image', Path('/unused'), 'hash')
                else:
                    with self.assertRaises(RuntimeError): material.copied_binary('image', Path('/unused'), 'hash')
            self.assertEqual(any(c[0] == 'rm' for c in calls), fault != 'ownership')


class CustodyTests(unittest.TestCase):
    def test_receipt_recipe_archive_and_loaded_image_are_bound(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(image, 'STATE', Path(folder)), \
             patch.object(image, 'fingerprint', return_value='recipe'), \
             patch.object(image, 'binding', return_value='archive'), \
             patch.object(image, 'podman', return_value=SimpleNamespace(stdout='a'*64)):
            good = {'image': 'sha256:'+'a'*64, 'recipe': 'recipe', 'archive_sha256': 'archive'}
            for key in (None, 'image', 'recipe', 'archive_sha256'):
                record = {**good}
                if key: record[key] = 'wrong'
                replace_private(Path(folder)/'receipt.json', json.dumps(record))
                if key:
                    with self.assertRaises(RuntimeError): image.validate_image(good['image'])
                else: self.assertEqual(image.validate_image(good['image']), Path(folder)/'image.tar')

    def test_profiles_and_unsigned_arbitrary_override_rejected(self):
        with patch.dict(os.environ, {'RUNASMIDJA_OPENBAO_PROFILE': 'unknown'}):
            with self.assertRaises(RuntimeError): image.profile()
        with patch.dict(os.environ, {'RUNASMIDJA_OPENBAO_PROFILE': 'wolfi'}):
            with self.assertRaises(RuntimeError):
                image.admission_policy({'openbao': image.pins()['upstream']['image']}, {})
        with patch.dict(os.environ, {'RUNASMIDJA_OPENBAO_PROFILE': 'official'}):
            self.assertEqual(image.admission_policy({'openbao': image.pins()['upstream']['image']}, {})['openbao'], image.pins()['upstream'])
        with patch.object(image, 'validate_image', side_effect=RuntimeError('unknown image')):
            with self.assertRaises(RuntimeError): image.admission_policy({'openbao': 'arbitrary'}, {})


class SwitchTests(unittest.TestCase):
    def test_unknown_image_and_data_config_mount_drift_reject(self):
        info = {'Image': 'sha256:abc', 'State': {'Running': False}, 'Mounts': [
            {'Destination': '/data', 'Source': str(switch.STATE/'bao-data'), 'RW': True},
            {'Destination': '/config', 'Source': str(switch.STATE/'bao-config'), 'RW': False}]}
        with patch.object(switch, 'podman', return_value=SimpleNamespace(stdout='abc')):
            switch.removable(info, ['image'])
            for key in ('Image', 'Mounts'):
                bad = {**info, key: 'wrong' if key == 'Image' else []}
                with self.assertRaises(RuntimeError): switch.removable(bad, ['image'])
            for index in (0, 1):
                bad = copy.deepcopy(info); bad['Mounts'][index]['RW'] = not bad['Mounts'][index]['RW']
                with self.assertRaises(RuntimeError): switch.removable(bad, ['image'])

    def test_wrong_instance_or_target_has_no_side_effect(self):
        with patch.object(switch, 'INSTANCE', 'v022-wolfi-valkey'), patch.object(switch, 'selected_image') as image_call:
            with self.assertRaises(RuntimeError): switch.switch('wolfi')
            image_call.assert_not_called()
        with patch.object(switch, 'INSTANCE', 'v023-wolfi-bao'), patch.object(switch, 'selected_image') as image_call:
            with self.assertRaises(RuntimeError): switch.switch('unknown')
            image_call.assert_not_called()

    def test_pending_switch_custody_or_target_drift_blocks_mutation(self):
        with patch.dict(os.environ, {'RUNASMIDJA_OPENBAO_PROFILE':'wolfi'}), \
             tempfile.TemporaryDirectory() as folder, patch.object(switch, 'STATE', Path(folder)), \
             patch.object(switch, 'INSTANCE', 'v023-wolfi-bao'), patch.object(switch, 'selected_image'), \
             patch.object(switch, 'verify_images'), patch.object(switch, 'fixture_images'), \
             patch.object(switch, 'preflight'), patch.object(switch, 'custody', return_value={'hash':'old'}), \
             patch.object(switch, 'stop') as stop:
            for record in ({'target':'official','custody':{'hash':'old'}}, {'target':'wolfi','custody':{'hash':'new'}}):
                replace_private(Path(folder)/'bao-switch.json', json.dumps(record))
                with self.assertRaises(RuntimeError): switch.switch('wolfi')
                stop.assert_not_called()


class AuditTests(unittest.TestCase):
    def test_full_audit_requires_server_refusal_then_recovers_and_cleans(self):
        @contextmanager
        def identity(_role): yield 'fixture-token'
        for fault in ('fill', 'accepted', 'wrong-status', 'changed', 'success'):
            with self.subTest(fault=fault), patch.object(qualify, 'owned', return_value={'Id':'owned'}), \
                 patch.object(qualify, 'runtime_values', return_value={'key':'value'}), \
                 patch.object(qualify, 'identity', identity), \
                 patch.object(qualify, 'podman', return_value=SimpleNamespace(returncode=0 if fault=='fill' else 1)) as run, \
                 patch.object(qualify, 'read_version') as read:
                read.side_effect = [({'key':'value'} if fault=='accepted' else qualify.BaoError(403 if fault=='wrong-status' else 500)),
                                    {'key':'changed' if fault=='changed' else 'value'}]
                if fault == 'success': qualify.audit_full()
                else:
                    with self.assertRaises(RuntimeError): qualify.audit_full()
                self.assertEqual(run.call_args.args[:4], ('exec','owned','rm','-f'))


if __name__ == '__main__': unittest.main()
