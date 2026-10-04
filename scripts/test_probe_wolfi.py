"""Wolfi admission, kernel restriction, artifact binding and cleanup regressions."""
import copy
import hashlib
import json
import tempfile
import unittest
import podman_guard
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import image_gate as gate
import probe_image as image
import probe_runtime as runtime
from test_postgres_image import archive

IDENTITY = 'a' * 64
IMAGE = 'sha256:' + 'b' * 64


def info():
    return {'Id': IDENTITY, 'Image': IMAGE, 'Config': {'User': '65532:65532',
        'Labels': {runtime.LABEL: 'owner'}, 'Entrypoint': ['/runasmidja-server'],
        'Cmd': ['18080', '--container']}, 'EffectiveCaps': [], 'BoundingCaps': [],
        'Mounts': [], 'State': {'Running': True, 'Pid': 123},
        'HostConfig': {'ReadonlyRootfs': True, 'SecurityOpt': ['no-new-privileges'],
            'Memory': 33554432, 'MemorySwap': 33554432, 'PidsLimit': 16,
            'CpuPeriod': 100000, 'CpuQuota': 100000, 'Privileged': False},
        'NetworkSettings': {'Ports': {'18080/tcp': [{'HostIp': '127.0.0.1', 'HostPort': '34567'}]}}}


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        guard = patch.object(podman_guard, 'require_rootless')
        guard.start(); self.addCleanup(guard.stop)
        entry = patch.object(image, 'require_rootless')
        entry.start(); self.addCleanup(entry.stop)
    def test_resource_identity_and_execution_configuration_denials(self):
        good = info(); runtime.configuration(good, IMAGE)
        prefix_free = copy.deepcopy(good); prefix_free['Image'] = IMAGE[7:]
        runtime.configuration(prefix_free, IMAGE)
        mutations = [('Image', 'wrong'), ('EffectiveCaps', ['CAP_CHOWN']),
                     ('BoundingCaps', ['CAP_CHOWN']), ('Mounts', [{}])]
        for key, value in mutations:
            bad = copy.deepcopy(good); bad[key] = value
            with self.subTest(key=key), self.assertRaises(RuntimeError):
                runtime.configuration(bad, IMAGE)
        for key, value in {'User': '0:0', 'Entrypoint': ['/bin/sh'], 'Cmd': []}.items():
            bad = copy.deepcopy(good); bad['Config'][key] = value
            with self.subTest(key=key), self.assertRaises(RuntimeError):
                runtime.configuration(bad, IMAGE)
        for key in good['HostConfig']:
            bad = copy.deepcopy(good); bad['HostConfig'][key] = True if key == 'Privileged' else None
            with self.subTest(key=key), self.assertRaises(RuntimeError):
                runtime.configuration(bad, IMAGE)

    def test_loopback_single_ephemeral_port_required(self):
        self.assertEqual(runtime.port(info()), 34567)
        for entry in (None, [], [{}, {}], [{'HostIp': '0.0.0.0', 'HostPort': '34567'}],
                      [{'HostIp': '127.0.0.1', 'HostPort': '65536'}],
                      [{'HostIp': '127.0.0.1', 'HostPort': '0'}],
                      [{'HostIp': '127.0.0.1', 'HostPort': '${dynamic}'}]):
            bad = info(); bad['NetworkSettings']['Ports']['18080/tcp'] = entry
            with self.subTest(entry=entry), self.assertRaises(RuntimeError): runtime.port(bad)

    def test_actual_kernel_limits_and_capability_state_required(self):
        files = {'status': 'NoNewPrivs:\t1\nCapEff:\t0000000000000000\nCapPrm:\t0000000000000000\nCapBnd:\t0000000000000000\n',
            'cgroup': '0::/fixture', 'memory.max': '33554432', 'memory.swap.max': '0',
            'pids.max': '16', 'cpu.max': '100000 100000'}
        with patch.object(Path, 'read_text', lambda path: files[path.name]):
            runtime.kernel_limits(info())
            for key in files:
                old = files[key]; files[key] = 'invalid'
                with self.subTest(key=key), self.assertRaises(RuntimeError): runtime.kernel_limits(info())
                files[key] = old

    def test_failures_cleanup_only_captured_owned_container(self):
        for stage in ('copy', 'hash', 'start', 'health', 'exit', 'success'):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as folder:
                state = Path(folder); calls = []; inspections = [0]
                def command(*args, **kwargs):
                    calls.append(args)
                    if args[1] == 'create': return SimpleNamespace(stdout=IDENTITY)
                    if args[1] == 'cp':
                        if stage == 'copy': raise RuntimeError('copy fault')
                        Path(args[-1]).write_text('ID=wolfi\n' if 'os-release' in args[-2] else 'executable')
                    if args[1] == 'start' and stage == 'start': raise RuntimeError('start fault')
                    return SimpleNamespace(stdout='')
                def inspected(_identity):
                    inspections[0] += 1
                    result = info()
                    if stage == 'exit' and inspections[0] == 3: result['State']['Running'] = False
                    return result
                with patch.object(runtime, 'run_bounded', side_effect=command), \
                     patch.object(runtime, 'inspect', side_effect=inspected), \
                     patch.object(runtime, 'bounded_hash', return_value='wrong' if stage == 'hash' else 'digest'), \
                     patch.object(runtime, 'kernel_limits'), \
                     patch.object(runtime, 'verify', side_effect=RuntimeError('health fault') if stage == 'health' else None):
                    if stage == 'success': runtime.qualify(IMAGE, 'digest', state, 'owner')
                    else:
                        with self.assertRaises(RuntimeError): runtime.qualify(IMAGE, 'digest', state, 'owner')
                self.assertEqual(calls[-1], ('podman', 'rm', '-f', IDENTITY))
                if stage in ('copy', 'hash'):
                    self.assertFalse(any(call[1] == 'start' for call in calls))

    def test_unowned_container_is_never_removed(self):
        bad = info(); bad['Config']['Labels'] = {}
        with tempfile.TemporaryDirectory() as folder, \
             patch.object(runtime, 'run_bounded', return_value=SimpleNamespace(stdout=IDENTITY)) as command, \
             patch.object(runtime, 'inspect', return_value=bad):
            with self.assertRaisesRegex(RuntimeError, 'ownership'):
                runtime.qualify(IMAGE, 'digest', Path(folder), 'owner')
            self.assertEqual(command.call_count, 1)


class AdmissionTests(unittest.TestCase):
    def setUp(self):
        guard = patch.object(podman_guard, 'require_rootless')
        guard.start(); self.addCleanup(guard.stop)
        entry = patch.object(image, 'require_rootless')
        entry.start(); self.addCleanup(entry.stop)
    def test_probe_archive_scans_bind_bytes_without_postgres_metadata(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(gate, 'EVIDENCE', Path(folder)):
            path = Path(folder) / 'image.tar'; identity = archive(path)
            report = json.dumps({'bomFormat': 'CycloneDX', 'components': [{'name': 'wolfi-baselayout'}]})
            def scanner(*args, **kwargs): return SimpleNamespace(stdout=report)
            check = lambda: image.archive_binding(path, identity)
            with patch.object(gate, 'run_bounded', side_effect=scanner):
                result = gate.scan('probe', identity, 'scanner', archive=path, archive_check=check)
                self.assertEqual(result[:2], (True, 0))
            evidence = result.snapshot.read_text()
            self.assertNotIn('PostgreSQL', evidence)
            def mutated(*args, **kwargs):
                with path.open('ab') as target: target.write(b'changed')
                return SimpleNamespace(stdout=report)
            with patch.object(gate, 'run_bounded', side_effect=mutated), self.assertRaisesRegex(RuntimeError, 'changed during scan'):
                gate.scan('probe', identity, 'scanner', archive=path, archive_check=check)
            self.assertEqual(result.snapshot.read_text(), evidence)
            for kwargs in ({}, {'archive': path, 'candidate_recipe': 'ambiguous'}):
                with self.assertRaises(ValueError):
                    gate.scan('probe', identity, 'scanner', archive_check=check, **kwargs)

    def test_probe_base_index_signature_and_platform_binding(self):
        policy = json.loads((image.RECIPE / 'image.lock.json').read_text())
        base = policy['probe-base']['image']
        raw = json.dumps({'manifests': [{'digest': base.split('@')[1],
            'platform': {'os': 'linux', 'architecture': 'amd64'}}]})
        digest = 'sha256:' + hashlib.sha256(raw.encode()).hexdigest()
        policy['probe-base']['index'] = 'cgr.dev/chainguard/static@' + digest
        signature = json.dumps([{'critical': {'image': {'docker-manifest-digest': digest}}}])
        for payload, valid in ((raw, True), (raw + ' ', False), (raw.replace('amd64', 'arm64'), False)):
            with patch.object(gate, 'run_bounded', side_effect=[SimpleNamespace(stdout=signature), SimpleNamespace(stdout=payload)]):
                if valid: self.assertEqual(gate.provenance('probe-base', base, policy, 'cosign'), 'signed-index')
                else:
                    with self.assertRaises(RuntimeError): gate.provenance('probe-base', base, policy, 'cosign')

class BuildTests(unittest.TestCase):
    def setUp(self):
        guard = patch.object(podman_guard, 'require_rootless')
        guard.start(); self.addCleanup(guard.stop)
        entry = patch.object(image, 'require_rootless')
        entry.start(); self.addCleanup(entry.stop)
    def test_build_admission_stops_on_provenance_scan_and_archive_failures(self):
        from contextlib import ExitStack
        for fault in ('provenance', 'base-scan', 'build', 'archive', 'image-scan', 'success'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as folder, ExitStack() as patches:
                state = Path(folder); binary = state / 'binary'; binary.write_bytes(b'fixture executable')
                commands = []
                def command(*args, **kwargs):
                    commands.append(args)
                    if args[:2] == ('podman', 'build'):
                        if fault == 'build': raise RuntimeError('build fault')
                        (state / 'image.id').write_text(IMAGE)
                    return SimpleNamespace(stdout='')
                def save(_args, path):
                    if fault == 'archive': raise RuntimeError('archive fault')
                    identity = archive(path)
                    (state / 'archive-identity').write_text(identity)
                def scan(service, *args, **kwargs):
                    if service == 'probe-base': return fault != 'base-scan', 0
                    (state / 'probe.cdx.json').write_text(json.dumps({'components': [kwargs['component']]}))
                    (state / 'probe.cdx.json').chmod(0o600)
                    return fault != 'image-scan', 0
                patches.enter_context(patch.object(image, 'BINARY', binary))
                patches.enter_context(patch.object(image, 'EVIDENCE', state))
                patches.enter_context(patch.object(image, 'tool', return_value='tool'))
                patches.enter_context(patch.object(image, 'provenance', side_effect=RuntimeError('signature fault') if fault == 'provenance' else None))
                patches.enter_context(patch.object(image, 'scan', side_effect=scan))
                patches.enter_context(patch.object(image, 'run_bounded', side_effect=command))
                patches.enter_context(patch.object(image, 'save_bounded_archive', side_effect=save))
                patches.enter_context(patch.object(image, 'archive_binding', return_value='fixture archive hash'))
                if fault == 'success':
                    result = image.build(state)
                    self.assertEqual(result[1], hashlib.sha256(binary.read_bytes()).hexdigest())
                    self.assertEqual(set(path.name for path in (state / 'context').iterdir()), {'Containerfile', 'runasmidja-server'})
                    evidence = json.loads((state / 'probe.cdx.json').read_text())
                    self.assertEqual(evidence['components'][-1]['hashes'][0]['content'], result[1])
                else:
                    with self.assertRaises(RuntimeError): image.build(state)
                if fault in ('provenance', 'base-scan'): self.assertEqual(commands, [])
                self.assertFalse(any(command[:2] in (('podman', 'run'), ('podman', 'start')) for command in commands))


if __name__ == '__main__':
    unittest.main()
