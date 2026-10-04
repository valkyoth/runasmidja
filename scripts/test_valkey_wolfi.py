"""Exact cache profile admission, command adaptation and runtime policy regressions."""
import copy
import hashlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import image_gate
import valkey_image as images
import qualification_valkey as qualify
from valkey_probe_wire import CacheProbe

POLICY = images.rules()
WOLFI = POLICY['valkey']['image']
OFFICIAL = POLICY['valkey-official']['image']


def runtime_info():
    return {'Image': 'a' * 64, 'Config': {'User': f'{os.getuid()}:{os.getgid()}'},
        'HostConfig': {'Memory': 536870912, 'PidsLimit': 128, 'CpuPeriod': 100000,
            'CpuQuota': 100000, 'ReadonlyRootfs': True, 'Privileged': False,
            'SecurityOpt': ['no-new-privileges']}, 'EffectiveCaps': [], 'BoundingCaps': [],
        'NetworkSettings': {'Ports': {'6379/tcp': [{'HostIp': '127.0.0.1', 'HostPort': '16379'}]}},
        'Mounts': [{'Destination': '/config/valkey.conf', 'Source': str(qualify.STATE / 'valkey.conf'), 'RW': False}]}


class ImageTests(unittest.TestCase):
    def test_only_explicit_reviewed_profiles_are_selectable(self):
        for profile, expected in (('wolfi', WOLFI), ('official', OFFICIAL)):
            with patch.dict(os.environ, {'RUNASMIDJA_VALKEY_PROFILE': profile}):
                self.assertEqual(images.selected_image(), expected)
        for invalid in ('', 'latest', 'arbitrary:tag', '../official'):
            with patch.dict(os.environ, {'RUNASMIDJA_VALKEY_PROFILE': invalid}):
                with self.assertRaises(RuntimeError): images.selected_image()

    def test_policy_and_entrypoint_do_not_transfer_unsigned_exception(self):
        self.assertEqual(images.admission_policy({'valkey': WOLFI}, POLICY)['valkey']['method'], 'signed-index')
        self.assertEqual(images.admission_policy({'valkey': OFFICIAL}, POLICY)['valkey']['method'], 'maintainer-exception')
        self.assertEqual(images.arguments(WOLFI), ['/config/valkey.conf'])
        self.assertEqual(images.arguments(OFFICIAL), ['valkey-server', '/config/valkey.conf'])
        for unknown in (WOLFI + 'bad', OFFICIAL + 'bad', 'unreviewed'):
            with self.assertRaises(RuntimeError): images.admission_policy({'valkey': unknown}, POLICY)
            with self.assertRaises(RuntimeError): images.arguments(unknown)
        self.assertEqual(POLICY['valkey']['method'], 'signed-index')

    def test_signature_index_platform_and_digest_are_required(self):
        raw = json.dumps({'manifests': [{'digest': WOLFI.split('@')[1],
            'platform': {'os': 'linux', 'architecture': 'amd64'}}]})
        digest = 'sha256:' + hashlib.sha256(raw.encode()).hexdigest()
        rule = {**POLICY['valkey'], 'index': 'cgr.dev/chainguard/valkey@' + digest}
        policy = {**POLICY, 'valkey': rule}
        sig = json.dumps([{'critical': {'image': {'docker-manifest-digest': digest}}}])
        for contents, valid in ((raw, True), (raw + ' ', False), (raw.replace('amd64', 'arm64'), False)):
            with patch.object(image_gate, 'run_bounded', side_effect=[SimpleNamespace(stdout=sig), SimpleNamespace(stdout=contents)]) as command:
                if valid:
                    self.assertEqual(image_gate.provenance('valkey', WOLFI, policy, 'cosign'), 'signed-index')
                    self.assertIn(rule['identity'], command.call_args_list[0].args)
                else:
                    with self.assertRaises(RuntimeError): image_gate.provenance('valkey', WOLFI, policy, 'cosign')
        with patch.object(image_gate, 'run_bounded', side_effect=RuntimeError('signature rejected')):
            with self.assertRaises(RuntimeError): image_gate.provenance('valkey', WOLFI, POLICY, 'cosign')


class RuntimeTests(unittest.TestCase):
    def test_configuration_denials(self):
        good = runtime_info()
        config = 'save ""\nappendonly no\nmaxmemory 64mb\nmaxmemory-policy allkeys-lru\nuser default off\n'
        with patch.object(qualify, 'podman', return_value=SimpleNamespace(stdout='a' * 64)), \
             patch.object(qualify, 'read_private', return_value=config):
            qualify.configuration(good, WOLFI)
            for key, value in (('Image', 'wrong'), ('EffectiveCaps', ['CAP_CHOWN']),
                               ('BoundingCaps', ['CAP_CHOWN']), ('Mounts', []), ('NetworkSettings', {})):
                bad = copy.deepcopy(good); bad[key] = value
                with self.subTest(key=key), self.assertRaises(RuntimeError): qualify.configuration(bad, WOLFI)
            for key in good['HostConfig']:
                bad = copy.deepcopy(good); bad['HostConfig'][key] = True if key == 'Privileged' else None
                with self.subTest(key=key), self.assertRaises(RuntimeError): qualify.configuration(bad, WOLFI)
            bad = copy.deepcopy(good); bad['Config']['User'] = '0:0'
            with self.assertRaises(RuntimeError): qualify.configuration(bad, WOLFI)
        with patch.object(qualify, 'podman', return_value=SimpleNamespace(stdout='a' * 64)), \
             patch.object(qualify, 'read_private', return_value=config.replace('64mb', '640mb')):
            with self.assertRaises(RuntimeError): qualify.configuration(good, WOLFI)

    def test_kernel_limits_fail_closed(self):
        files = {'status': 'NoNewPrivs:\t1\nCapEff:\t0000000000000000\nCapPrm:\t0000000000000000\nCapBnd:\t0000000000000000\n',
            'cgroup': '0::/fixture', 'memory.max': '536870912', 'pids.max': '128', 'cpu.max': '100000 100000'}
        with patch.object(Path, 'read_text', lambda path: files[path.name]):
            qualify.kernel({'State': {'Pid': 123}})
            for key in files:
                old = files[key]; files[key] = 'invalid'
                with self.subTest(key=key), self.assertRaises(RuntimeError): qualify.kernel({'State': {'Pid': 123}})
                files[key] = old

    def test_missing_eviction_and_acl_auth_failures_reject_and_close(self):
        for fault in ('auth', 'acl', 'eviction', 'corruption', 'success'):
            with self.subTest(fault=fault):
                calls = [0]
                def request(*parts):
                    calls[0] += 1
                    if parts[0] == 'AUTH':
                        if parts[-1] == 'invalid-public-negative-fixture': return b'+OK' if fault == 'auth' else b'-WRONGPASS rejected'
                        return b'+OK'
                    if calls[0] <= 9: return b'+OK' if fault == 'acl' else b'-NOPERM denied'
                    if parts[0] == 'SET': return b'+OK'
                    if parts[0] == 'DEL': return b':1'
                    index = int(parts[1].rsplit(':', 1)[-1])
                    if fault == 'corruption': return b'corrupt'
                    if fault != 'eviction' and index < 512: return None
                    return b'x' * 65500
                with patch.object(qualify, 'CacheProbe') as client, \
                     patch.object(qualify, 'runtime_values', return_value={'valkey_password': 'test'}):
                    client.return_value.request.side_effect = request
                    if fault == 'success': qualify.memory_and_denials()
                    else:
                        with self.assertRaises(RuntimeError): qualify.memory_and_denials()
                    client.return_value.close.assert_called_once()


class WireTests(unittest.TestCase):
    def probe(self, data):
        value = CacheProbe.__new__(CacheProbe)
        value.stream = SimpleNamespace(settimeout=lambda _value: None, sendall=lambda _data: None)
        value.reader = io.BytesIO(data); value.deadline = float('inf'); value.commands = 0
        return value

    def test_resp_reply_types_and_bounds(self):
        for data, expected in ((b'+OK\r\n', b'+OK'), (b'-NOPERM denied\r\n', b'-NOPERM denied'),
                               (b':1\r\n', b':1'), (b'$-1\r\n', None), (b'$3\r\nabc\r\n', b'abc')):
            self.assertEqual(self.probe(data).request('PING'), expected)
        for data in (b'+bad\n', b'$65537\r\n', b'$-2\r\n', b'$3\r\nabcXX', b'$5\r\nab', b'*1\r\n', b'x'*4097):
            with self.subTest(data=data[:20]), self.assertRaises(RuntimeError): self.probe(data).request('PING')

    def test_fragmented_replies_and_total_deadline(self):
        probe = self.probe(b'$3\r\nabc\r\n')
        original = probe.reader
        probe.reader = SimpleNamespace(read1=lambda _size: original.read(1))
        self.assertEqual(probe.request('GET', 'key'), b'abc')
        probe = self.probe(b'+slow\r\n'); probe.deadline = 3
        with patch('valkey_probe_wire.time.monotonic', side_effect=[0, 1, 2, 3]):
            with self.assertRaisesRegex(RuntimeError, 'deadline'): probe.request('PING')

    def test_request_and_total_work_limits(self):
        with self.assertRaises(RuntimeError): self.probe(b'').request('SET', 'key', b'x'*65537)
        with self.assertRaises(RuntimeError): self.probe(b'').request()
        value = self.probe(b'+OK\r\n'); value.commands = 5000
        with self.assertRaises(RuntimeError): value.request('PING')
        value = self.probe(b'+OK\r\n'); value.deadline = 0
        with self.assertRaises(RuntimeError): value.request('PING')


if __name__ == '__main__':
    unittest.main()
