"""Fail closed on missing kernel limits and never stop an unowned build unit."""
import tempfile
import unittest
import podman_guard
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import build_sandbox as build


class BuildTests(unittest.TestCase):
    def setUp(self):
        guard = patch.object(podman_guard, 'require_rootless')
        guard.start(); self.addCleanup(guard.stop)
        entry = patch.object(build, 'require_rootless')
        entry.start(); self.addCleanup(entry.stop)
    def test_missing_or_changed_kernel_limits_fail_closed(self):
        parent = '/user.slice/runasmidja-build-fixture.service/supervisor'
        files = {'cgroup': '0::' + parent, 'memory.max': str(build.MEMORY),
                 'memory.swap.max': '0', 'pids.max': '512', 'cpu.max': '200000 100000'}
        def read(path):
            return files[path.name]
        with patch.object(Path, 'read_text', read):
            self.assertEqual(build.cgroup(), parent.rsplit('/', 1)[0] + '/steps')
            for key in ('memory.max', 'memory.swap.max', 'pids.max', 'cpu.max'):
                old = files[key]; files[key] = 'max'
                with self.assertRaises(RuntimeError): build.cgroup()
                files[key] = old
            files['cgroup'] = '0::/user.slice/unrelated.service'
            with self.assertRaises(RuntimeError): build.cgroup()

    def test_cleanup_checks_unique_unit_ownership_before_stop(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(build, 'STATE', Path(folder)), \
             patch.object(build.uuid, 'uuid4', return_value='captured-identity'), \
             patch.object(build, 'run_bounded', side_effect=[RuntimeError('deadline'),
                SimpleNamespace(stdout='Unrelated unit')]) as command:
            with self.assertRaisesRegex(RuntimeError, 'ownership mismatch'):
                build.sandbox('recipe')
            self.assertEqual(command.call_count, 2)
            self.assertFalse(any('stop' in call.args for call in command.call_args_list))

    def test_failed_build_stops_only_its_captured_unit(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(build, 'STATE', Path(folder)), \
             patch.object(build.uuid, 'uuid4', return_value='captured-identity'), \
             patch.object(build, 'run_bounded', side_effect=[RuntimeError('deadline'),
                SimpleNamespace(stdout='Runasmidja public build captured-identity'),
                SimpleNamespace(stdout='')]) as command:
            with self.assertRaisesRegex(RuntimeError, 'deadline'):
                build.sandbox('recipe')
            self.assertEqual(command.call_args.args,
                ('systemctl', '--user', 'stop', 'runasmidja-build-captured-identity.service'))


if __name__ == '__main__':
    unittest.main()
