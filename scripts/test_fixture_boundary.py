"""Reject rootful engines and out-of-scope rollback before fixture side effects."""
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import stack
import stack_common as common
import stack_files
import stack_resources
import postgres_image
import valkey_image
import qualification_valkey
from test_valkey_wolfi import runtime_info, WOLFI, OFFICIAL, POLICY


class RootlessTests(unittest.TestCase):
    def test_real_or_effective_root_never_invokes_engine(self):
        for uid, euid in ((0, 0), (1000, 0), (0, 1000)):
            with self.subTest(uid=uid, euid=euid), patch.object(os, 'getuid', return_value=uid), \
                 patch.object(os, 'geteuid', return_value=euid), patch.object(common, 'run') as run:
                with self.assertRaisesRegex(RuntimeError, 'root'):
                    common.podman('run', 'image')
                run.assert_not_called()

    def test_engine_false_malformed_or_failure_never_mutates(self):
        for value in ('false', '', 'True', 'unknown', RuntimeError('info failed')):
            with self.subTest(value=value), patch.object(os, 'getuid', return_value=1000), \
                 patch.object(os, 'geteuid', return_value=1000), patch.object(common, 'run') as run:
                if isinstance(value, Exception): run.side_effect = value
                else: run.return_value = SimpleNamespace(stdout=value)
                for operation in ('pull', 'run', 'start', 'stop', 'rm'):
                    run.reset_mock()
                    with self.assertRaises(RuntimeError): common.podman(operation, 'fixture')
                    run.assert_called_once_with('podman', 'info', '--format', '{{.Host.Security.Rootless}}')

    def test_success_is_checked_again_for_next_engine_operation(self):
        with patch.object(os, 'getuid', return_value=1000), patch.object(os, 'geteuid', return_value=1000), \
             patch.object(common, 'run', side_effect=[SimpleNamespace(stdout='true\n'), 'started',
                                                     SimpleNamespace(stdout='false')]) as run:
            self.assertEqual(common.podman('start', 'fixture'), 'started')
            with self.assertRaises(RuntimeError): common.podman('stop', 'fixture')
            self.assertEqual(run.call_count, 3)

    def test_entry_guards_precede_custody_build_and_qualification(self):
        with patch.object(stack, 'require_rootless', side_effect=RuntimeError('rootful')), \
             patch.object(stack, 'files') as files:
            with self.assertRaises(RuntimeError): stack.up()
            files.assert_not_called()
        with patch.object(common, 'require_rootless', side_effect=RuntimeError('rootful')), \
             patch.object(stack_files, 'directory') as directory, \
             patch.object(postgres_image, 'ensure_image') as build, \
             patch.object(qualification_valkey, 'owned') as owned:
            with self.assertRaises(RuntimeError):
                with stack_files.fixture_lock(): self.fail('entered fixture')
            with self.assertRaises(RuntimeError): postgres_image.fixture_images()
            with self.assertRaises(RuntimeError): qualification_valkey.qualify()
            directory.assert_not_called(); build.assert_not_called(); owned.assert_not_called()

    def test_stop_and_upgrade_cannot_mutate_rootful_engine(self):
        with patch.object(os, 'getuid', return_value=1000), patch.object(os, 'geteuid', return_value=1000), \
             patch.object(common, 'run', return_value=SimpleNamespace(stdout='false')) as run:
            for operation in (stack_resources.stop, lambda: stack_resources.upgrade_bounds({})):
                run.reset_mock()
                with self.assertRaises(RuntimeError): operation()
                run.assert_called_once_with('podman', 'info', '--format', '{{.Host.Security.Rootless}}')

    def test_container_root_rejected_even_when_matching_host(self):
        info = runtime_info(); info['Config']['User'] = '0:0'
        with patch.object(os, 'getuid', return_value=0), patch.object(os, 'getgid', return_value=0), \
             patch.object(qualification_valkey, 'podman', return_value=SimpleNamespace(stdout='a'*64)):
            with self.assertRaisesRegex(RuntimeError, 'nonroot'):
                qualification_valkey.configuration(info, WOLFI)


class RollbackTests(unittest.TestCase):
    def test_unsigned_selection_admission_and_arguments_restricted_to_old_instance(self):
        for instance in ('v022-wolfi-valkey', 'new-fixture', ''):
            with self.subTest(instance=instance), patch.dict(os.environ, {'RUNASMIDJA_VALKEY_PROFILE': 'official'}), \
                 patch.object(common, 'INSTANCE', instance):
                with self.assertRaises(RuntimeError): valkey_image.selected_image(instance)
                with self.assertRaises(RuntimeError): valkey_image.admission_policy({'valkey': OFFICIAL}, POLICY)
                with self.assertRaises(RuntimeError): valkey_image.arguments(OFFICIAL)
        with patch.dict(os.environ, {'RUNASMIDJA_VALKEY_PROFILE': 'official'}):
            self.assertEqual(valkey_image.selected_image(valkey_image.ROLLBACK_INSTANCE), OFFICIAL)

    def test_invalid_profile_pair_cannot_create_custody_or_build(self):
        with patch.dict(os.environ, {'RUNASMIDJA_VALKEY_PROFILE': 'official'}), \
             patch.object(common, 'INSTANCE', 'v022-wolfi-valkey'), \
             patch.object(common, 'require_rootless'), patch.object(stack, 'require_rootless'), \
             patch.object(stack_files, 'directory') as directory, patch.object(stack, 'files') as files, \
             patch.object(postgres_image, 'ensure_image') as build:
            with self.assertRaises(RuntimeError): stack.up()
            with self.assertRaises(RuntimeError):
                with stack_files.fixture_lock(): self.fail('created rollback custody')
            with self.assertRaises(RuntimeError): postgres_image.fixture_images()
            directory.assert_not_called(); files.assert_not_called(); build.assert_not_called()


if __name__ == '__main__':
    unittest.main()
