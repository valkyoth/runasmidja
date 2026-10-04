"""Host build/probe denial, namespace entry and static bypass regressions."""
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch
import podman_guard as guard
import podman_policy
import build_sandbox
import build_postgres_image
import probe_image
import probe_runtime
import postgres_image
import smoke_probe
import qualify_probe_wolfi


class GuardTests(unittest.TestCase):
    def test_all_host_workflows_reject_rootful_engine_before_work(self):
        operations = [
            (probe_image, lambda: probe_image.build(Path('/unused'))),
            (probe_runtime, lambda: probe_runtime.qualify('image', 'digest', Path('/unused'), 'owner')),
            (postgres_image, lambda: postgres_image.verify_loaded_image('image')),
            (build_postgres_image, build_postgres_image.build),
            (build_sandbox, lambda: build_sandbox.sandbox('recipe')),
            (qualify_probe_wolfi, qualify_probe_wolfi.main),
        ]
        for module, invoke in operations:
            with self.subTest(module=module.__name__), patch.object(os, 'getuid', return_value=1000), \
                 patch.object(os, 'geteuid', return_value=1000), \
                 patch.object(module, 'run_bounded', return_value=SimpleNamespace(stdout='false')) as run, \
                 patch.object(Path, 'mkdir') as mkdir:
                with self.assertRaisesRegex(RuntimeError, 'rootless'): invoke()
                self.assertEqual(run.call_count, 1)
                self.assertIn('info', run.call_args.args)
                mkdir.assert_not_called()

    def test_scratch_rejects_before_cargo_build(self):
        with patch('sys.argv', ['smoke_probe.py', '--container']), \
             patch.object(smoke_probe, 'run_bounded', return_value=SimpleNamespace(stdout='false')), \
             patch.object(smoke_probe.subprocess, 'run') as cargo:
            with self.assertRaisesRegex(RuntimeError, 'rootless'): smoke_probe.main()
            cargo.assert_not_called()

    def test_streamed_archive_denial_does_not_create_file(self):
        run = Mock(return_value=SimpleNamespace(stdout='false')); save = Mock()
        with self.assertRaisesRegex(RuntimeError, 'rootless'):
            guard.archive(run, save, 'image', Path('/unused'))
        save.assert_not_called()
        run.return_value.stdout = 'true'
        guard.archive(run, save, 'image', Path('/unused'))
        save.assert_called_once_with(['podman', 'save', '--format', 'docker-archive', 'image'], Path('/unused'))

    def test_unshare_checks_local_engine_before_supervisor(self):
        run = Mock(side_effect=[SimpleNamespace(stdout='true'), 'started'])
        self.assertEqual(guard.unshare(run, ['systemd-run', '--user'], ['python3', 'worker']), 'started')
        self.assertEqual(run.call_args_list[0].args,
                         ('podman', '--remote=false', 'info', '--format', '{{.Host.Security.Rootless}}'))
        self.assertEqual(run.call_args_list[1].args[:5],
                         ('systemd-run', '--user', 'podman', '--remote=false', 'unshare'))
        for value in ('false', '', 'True'):
            run = Mock(return_value=SimpleNamespace(stdout=value))
            with self.assertRaises(RuntimeError): guard.unshare(run, ['systemd-run'], ['worker'])
            self.assertEqual(run.call_count, 1)

    def test_operation_env_matches_guard_and_global_flags_are_rejected(self):
        run = Mock(return_value=SimpleNamespace(stdout='true'))
        env = {'CONTAINER_HOST': 'unix:///test-engine'}
        guard.podman(run, 'image', 'inspect', 'image', env=env)
        self.assertEqual([call.kwargs['env'] for call in run.call_args_list], [env, env])
        run.reset_mock()
        with self.assertRaises(ValueError): guard.podman(run, '--remote=false', 'run', 'image')
        run.assert_not_called()

    def test_worker_requires_nonroot_host_mapping_before_mount(self):
        for value in ('', '0 0 4294967295', '0 0 1', '0 1000 2', '1 1000 1'):
            with patch.object(os, 'geteuid', return_value=0), patch.object(Path, 'read_text', return_value=value), \
                 patch.object(build_sandbox, 'run_bounded') as run:
                with self.assertRaisesRegex(RuntimeError, 'mapping'):
                    build_sandbox.worker('/unused', 'recipe', 'qualify')
                run.assert_not_called()
        with patch.object(os, 'geteuid', return_value=0), \
             patch.object(Path, 'read_text', return_value='0 1000 1\n1 100000 65536\n'):
            build_sandbox.require_worker_namespace()
        with patch.object(os, 'geteuid', return_value=1000), \
             patch.object(Path, 'read_text', return_value='0 1000 1'):
            with self.assertRaises(RuntimeError): build_sandbox.require_worker_namespace()


class PolicyTests(unittest.TestCase):
    def test_direct_alias_absolute_and_shell_command_forms_are_rejected(self):
        for source in ("run_bounded('podman', 'load', 'archive')", "subprocess.run(['podman', 'run', 'image'])",
                       "cmd = ['/usr/bin/podman', 'save']; run(*cmd)",
                       "engine = 'podman'; subprocess.Popen([engine, 'build'])",
                       "subprocess.run('podman run image', shell=True)"):
            self.assertTrue(podman_policy.violations(source, 'new_workflow.py'))
        self.assertFalse(podman_policy.violations("podman(run_bounded, 'run', 'image')", 'probe.py'))
        self.assertTrue(podman_policy.violations("def sandbox():\n run('podman')", 'build_sandbox.py'))
        self.assertFalse(podman_policy.violations("def worker():\n run('podman')", 'build_sandbox.py'))

    def test_repository_has_only_reviewed_raw_command_owners(self):
        self.assertEqual(podman_policy.check(Path(__file__).resolve().parent.parent), [])


if __name__ == '__main__':
    unittest.main()
