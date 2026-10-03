"""Bounded retention and mandatory container logging/audit settings."""
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import audit_evidence as audit
import custody
import stack_resources as resources
import stack_files


class AuditTests(unittest.TestCase):
    def test_snapshots_rotate_to_two_bounded_private_regular_files(self):
        info = {'HostConfig': {'Tmpfs': {'/audit': 'size=16777216'}}}
        with tempfile.TemporaryDirectory() as folder, patch.object(audit, 'STATE', Path(folder)), \
             patch.object(audit, 'podman', side_effect=[SimpleNamespace(stdout='first'),
                 SimpleNamespace(stdout='second'), SimpleNamespace(stdout='third')]) as call:
            (Path(folder) / 'bao-audit').mkdir(mode=0o700)
            for _ in range(3): audit.snapshot_audit(info)
            self.assertEqual(audit.audit_text(), 'secondthird')
            self.assertEqual(call.call_args.kwargs['output_limit'], custody.MAX_AUDIT)
            self.assertEqual(call.call_args.kwargs['timeout'], 30)
            for path in (Path(folder) / 'bao-audit').iterdir():
                self.assertEqual(path.stat().st_mode & 0o777, 0o600)

    def test_snapshot_symlink_or_budget_failure_preserves_old_evidence(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(audit, 'STATE', Path(folder)):
            directory = Path(folder) / 'bao-audit'; directory.mkdir(mode=0o700)
            target = directory / 'audit.log'; custody.private(target, 'retained')
            with patch.object(audit, 'podman', side_effect=RuntimeError('output exceeds budget')):
                with self.assertRaises(RuntimeError): audit.snapshot_audit({'HostConfig': {'Tmpfs': {'/audit': ''}}})
            self.assertEqual(custody.read_private(target), 'retained')
            target.unlink(); target.symlink_to('/dev/zero')
            with self.assertRaises(OSError): audit.audit_text()

    def test_unbounded_existing_container_requires_explicit_upgrade(self):
        for service in ('postgres', 'valkey', 'openbao'):
            info = {'Image': 'reviewed', 'State': {'Running': False}, 'HostConfig': {'LogConfig': {'Type': 'journald'}}}
            with patch.object(resources, 'owned', return_value=info), \
                 patch.object(resources, 'podman', return_value=SimpleNamespace(stdout='reviewed')) as call:
                with self.assertRaises(RuntimeError): resources.start_container(service, 'image', [])
                self.assertEqual(call.call_count, 1)

    def test_upgrade_mount_drift_blocks_all_stop_remove_operations(self):
        info = {'Image': 'reviewed', 'Mounts': [{'Destination': '/var/lib/postgresql', 'Name': 'wrong-volume'}]}
        with patch.object(resources, 'preflight'), patch.object(resources, 'owned', return_value=info), \
             patch.object(resources, 'podman', return_value=SimpleNamespace(stdout='reviewed')) as call, \
             patch.object(resources, 'stop') as stop:
            with self.assertRaises(RuntimeError): resources.upgrade_bounds({'postgres': 'image'})
            stop.assert_not_called()
            self.assertEqual(call.call_count, 1)

    def test_effective_log_and_audit_caps_are_required_on_reuse(self):
        host = {'LogConfig': {'Type': 'k8s-file', 'Config': None, 'Size': '1.049MB'},
                'Tmpfs': {'/audit': 'rw,noexec,nosuid,nodev,size=16777216'}}
        info = {'Image': 'reviewed', 'State': {'Running': True}, 'HostConfig': host}
        with patch.object(resources, 'owned', return_value=info), \
             patch.object(resources, 'podman', return_value=SimpleNamespace(stdout='reviewed')) as call:
            resources.start_container('openbao', 'image', [])
            self.assertEqual(call.call_count, 1)
            host['Tmpfs']['/audit'] = 'rw,noexec,nosuid,nodev,size=167772160'
            with self.assertRaises(RuntimeError): resources.start_container('openbao', 'image', [])
            host['LogConfig']['Size'] = '-1B'
            with self.assertRaises(RuntimeError): resources.start_container('valkey', 'image', [])

    def test_upgrade_retains_data_and_removes_only_verified_containers(self):
        infos = {
            'postgres': {'Image': 'reviewed', 'Mounts': [{'Destination': '/var/lib/postgresql', 'Name': resources.NAMES['postgres']}]},
            'openbao': {'Image': 'reviewed', 'Mounts': [{'Destination': '/data', 'Source': str(resources.STATE / 'bao-data')}]},
            'valkey': {'Image': 'reviewed', 'Mounts': []}}
        with patch.object(resources, 'preflight'), \
             patch.object(resources, 'owned', side_effect=lambda _kind, _name, service: infos[service]), \
             patch.object(resources, 'podman', return_value=SimpleNamespace(stdout='reviewed')) as call, \
             patch.object(resources, 'stop') as stop:
            resources.upgrade_bounds({service: 'image' for service in infos})
            stop.assert_called_once()
            mutations = [args.args for args in call.call_args_list if args.args[0] != 'image']
            self.assertEqual(mutations, [('rm', resources.NAMES[service]) for service in resources.NAMES])

    def test_new_directories_are_private_and_parent_synced(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(stack_files, 'sync_parent') as sync:
            path = Path(folder) / 'parent/child'
            stack_files.directory(path)
            self.assertEqual([args.args[0] for args in sync.call_args_list], [path.parent, path])
            self.assertEqual(path.parent.stat().st_mode & 0o777, 0o700)
            self.assertEqual(path.stat().st_mode & 0o777, 0o700)

    def test_file_fsync_failure_is_not_reported_as_success(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(custody.os, 'fsync', side_effect=OSError('fault')):
            with self.assertRaises(OSError): custody.private(Path(folder) / 'secret', 'fixture')


if __name__ == '__main__':
    unittest.main()
