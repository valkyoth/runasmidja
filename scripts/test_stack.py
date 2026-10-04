"""Fail-closed fixture sequencing, version reuse, custody and mutation regression tests."""
import json
import os
import tempfile
import unittest
import urllib.error
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import stack
import stack_common as common
import stack_files
import stack_resources as resources
import stack_vault as vault

VALUES = {key: str(n) * 64 for n, key in enumerate(vault.KEYS, 1)}


def record(values, version=1):
    return {'data': {'data': values, 'metadata': {'version': version, 'destroyed': False, 'deletion_time': ''}}}


class VaultTests(unittest.TestCase):
    def test_audit_missing_blocks_bootstrap_issuance(self):
        with patch.object(vault, 'bao', return_value={'data': {}}) as call:
            with self.assertRaises(RuntimeError):
                vault.configure('root-fixture')
            self.assertEqual(call.call_count, 1)

    def test_initialized_without_custody_is_not_reset(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(vault, 'STATE', Path(folder)), \
             patch.object(vault, 'wait_for'), patch.object(vault, 'bao', return_value={'initialized': True}) as call:
            with self.assertRaises(RuntimeError):
                vault.bootstrap()
            self.assertEqual(call.call_count, 1)

    def test_lost_data_with_recovery_custody_is_not_reinitialized(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(vault, 'STATE', Path(folder)), \
             patch.object(vault, 'wait_for'), patch.object(vault, 'bao', return_value={'initialized': False}) as call:
            common.private(Path(folder) / 'recovery.json', '{}')
            with self.assertRaises(RuntimeError):
                vault.bootstrap()
            self.assertEqual(call.call_count, 1)

    def test_interrupted_revoked_root_only_resumes_after_confirmed_denial(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(vault, 'STATE', Path(folder)), \
             patch.object(vault, 'wait_for'), patch.object(vault, 'configure', side_effect=common.BaoError(403)):
            common.private(Path(folder) / 'recovery.json', '{}')
            common.private(Path(folder) / 'bootstrap.json', '{"root_token":"fixture"}')
            for response, expect_error in (({}, True), (common.BaoError(403), False)):
                with patch.object(vault, 'bao', side_effect=[{'initialized': True}, {'sealed': False}, {'sealed': False}, response]):
                    if expect_error:
                        with self.assertRaises(common.BaoError):
                            vault.bootstrap()
                    else:
                        self.assertEqual(vault.bootstrap(), 'fixture')

    def test_existing_versions_do_not_generate_or_overwrite(self):
        def api(path, payload=None, token=None, method=None):
            self.assertIsNone(payload)
            self.assertEqual(token, 'root-fixture')
            return record(VALUES if path.endswith('/provisioning') else {k: VALUES[k] for k in vault.KEYS[1:]})
        with patch.object(vault, 'bao', side_effect=api) as call:
            vault.issue_credentials('root-fixture')
            self.assertEqual(call.call_count, 2)

    def test_empty_state_uses_vault_random_and_cas_zero(self):
        stored = {}
        random_calls = []
        def api(path, payload=None, token=None, method=None):
            if path == 'sys/tools/random':
                random_calls.append(payload)
                return {'data': {'random_bytes': str(len(random_calls)) * 64}}
            if payload:
                self.assertEqual(payload['options'], {'cas': 0})
                self.assertNotIn(path, stored)
                stored[path] = payload['data']
                return {}
            if path not in stored:
                raise common.BaoError(404)
            return record(stored[path])
        with patch.object(vault, 'bao', side_effect=api):
            vault.issue_credentials('root-fixture')
        self.assertEqual(random_calls, [{'bytes': 32, 'format': 'hex'}] * 3)
        self.assertEqual(stored['runasmidja/data/provisioning'], VALUES)

    def test_denial_never_becomes_generation(self):
        for status in (403, 500, 503):
            with self.subTest(status=status), patch.object(vault, 'bao', side_effect=common.BaoError(status)) as call:
                with self.assertRaises(common.BaoError):
                    vault.issue_credentials('root-fixture')
                self.assertEqual(call.call_count, 1)

    def test_deleted_wrong_version_or_malformed_credentials_refuse(self):
        for document in (record(VALUES, 2), record(VALUES, True), record({}), record({**VALUES, 'database_password': "'attack"}),
                         {'data': {'data': VALUES, 'metadata': {'version': 1, 'destroyed': True}}}):
            with self.subTest(document=document), patch.object(vault, 'bao', return_value=document):
                with self.assertRaises(RuntimeError):
                    vault.read_version('provisioning', 'fixture', vault.KEYS)

    def test_deleted_record_cannot_be_recreated(self):
        with patch.object(vault, 'bao', side_effect=[common.BaoError(404), common.BaoError(400)]) as call:
            with self.assertRaises(common.BaoError):
                vault.create_once('provisioning', VALUES, 'fixture')
            self.assertEqual(call.call_args.args[1]['options'], {'cas': 0})

    def test_projection_mismatch_refuses(self):
        with patch.object(vault, 'read_version', return_value=VALUES), \
             patch.object(vault, 'create_once', return_value={k: 'f' * 64 for k in vault.KEYS[1:]}):
            with self.assertRaises(RuntimeError):
                vault.issue_credentials('fixture')

    def test_scoped_token_revoked_even_after_failure(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(vault, 'STATE', Path(folder)):
            common.private(Path(folder) / 'runtime-role.json', '{"role_id":"role", "secret_id":"sentinel"}')
            with patch.object(vault, 'bao', side_effect=[{'auth': {'client_token': 'test-token'}}, {}]) as call:
                with self.assertRaisesRegex(RuntimeError, 'work failure'):
                    with vault.identity('runtime'):
                        raise RuntimeError('work failure')
                self.assertEqual(call.call_args.args, ('auth/token/revoke-self', {}, 'test-token'))

    def test_revocation_checkpoint_recovery_requires_confirmed_invalid_root(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(vault, 'STATE', Path(folder)):
            file = Path(folder) / 'bootstrap.json'
            common.private(file, '{"root_token":"fixture"}')
            with patch.object(vault, 'bao', side_effect=[common.BaoError(403), common.BaoError(403)]):
                vault.revoke_root('fixture')
            self.assertFalse(file.exists())
            common.private(file, '{"root_token":"fixture"}')
            with patch.object(vault, 'bao', side_effect=[{}, {}]):
                with self.assertRaises(RuntimeError):
                    vault.revoke_root('fixture')
            self.assertTrue(file.exists())


class SequencingTests(unittest.TestCase):
    def execute(self, failure=None):
        events = []
        def step(name, result=None):
            def run(*args, **kwargs):
                events.append(name)
                if name == failure:
                    raise RuntimeError('deliberate interruption')
                return result
            return run
        from contextlib import ExitStack
        with ExitStack() as patches:
            for name, result in (('require_rootless', None), ('files', None), ('preflight', None), ('infrastructure', None),
                                 ('fixture_images', {'postgres': 'reviewed', 'openbao': 'reviewed', 'valkey': 'reviewed'}),
                                 ('verify_images', None),
                                 ('bootstrap', 'fixture'), ('provisioning_values', VALUES),
                                 ('runtime_values', {k: VALUES[k] for k in vault.KEYS[1:]}),
                                 ('delivery', None), ('revoke_root', None)):
                patches.enter_context(patch.object(stack, name, side_effect=step(name, result)))
            patches.enter_context(patch.object(stack, 'start_container', side_effect=lambda service, *args: events.append('start-' + service)))
            patches.enter_context(patch.object(stack, 'podman', return_value=SimpleNamespace(returncode=0)))
            patches.enter_context(patch.object(stack, 'wait_for'))
            patches.enter_context(patch.object(stack, 'owned'))
            if failure:
                with self.assertRaises(RuntimeError):
                    stack.up()
            else:
                stack.up()
        return events

    def test_vault_and_scoped_reads_precede_consumers_root_revoke_last(self):
        events = self.execute()
        self.assertLess(events.index('verify_images'), events.index('start-openbao'))
        for event in ('bootstrap', 'provisioning_values', 'runtime_values', 'delivery'):
            self.assertLess(events.index(event), events.index('start-postgres'))
        self.assertLess(events.index('start-openbao'), events.index('bootstrap'))
        self.assertEqual(events[-1], 'revoke_root')

    def test_unavailable_sealed_or_denied_vault_starts_no_consumer(self):
        for failure in ('bootstrap', 'provisioning_values', 'runtime_values', 'delivery', 'preflight', 'verify_images'):
            events = self.execute(failure)
            self.assertNotIn('start-postgres', events)
            self.assertNotIn('start-valkey', events)
            self.assertNotIn('revoke_root', events)
            if failure == 'verify_images':
                self.assertNotIn('start-openbao', events)


class OwnershipTests(unittest.TestCase):
    def test_unowned_container_network_volume_refuse(self):
        expected = {'io.runasmidja.project': 'runasmidja', 'io.runasmidja.instance': 'owner'}
        for kind in ('container', 'network', 'volume'):
            for actual in ({}, {**expected, 'io.runasmidja.instance': 'other'}):
                info = {'Config': {'Labels': actual}, 'Labels': actual, 'labels': actual}
                with patch.object(resources, 'labels', return_value=expected), \
                     patch.object(resources, 'podman', side_effect=[SimpleNamespace(returncode=0), SimpleNamespace(stdout=json.dumps([info]))]) as call:
                    with self.assertRaises(RuntimeError):
                        resources.owned(kind, 'name', 'postgres')
                    self.assertEqual(call.call_count, 2)

    def test_stop_preflights_before_any_mutation(self):
        with patch.object(resources, 'preflight', side_effect=RuntimeError('collision')), patch.object(resources, 'podman') as call:
            with self.assertRaises(RuntimeError):
                resources.stop()
            call.assert_not_called()

    def test_image_drift_refuses_start(self):
        with patch.object(resources, 'owned', return_value={'Image': 'wrong'}), \
             patch.object(resources, 'podman', return_value=SimpleNamespace(stdout='reviewed')) as call:
            with self.assertRaises(RuntimeError):
                resources.start_container('postgres', 'reviewed', [])
            self.assertEqual(call.call_args.args[:2], ('image', 'inspect'))


class CustodyTests(unittest.TestCase):
    def test_child_error_never_echoes_secret_output(self):
        with self.assertRaises(RuntimeError) as caught:
            common.run(sys.executable, '-c', "print('sentinel'); raise SystemExit(1)", data='sentinel')
        self.assertNotIn('sentinel', str(caught.exception))

    def test_http_error_never_echoes_body_path_or_token(self):
        error = urllib.error.HTTPError('https://sentinel.invalid', 403, 'sentinel', {}, None)
        with patch.object(common.ssl, 'create_default_context'), patch.object(common.urllib.request, 'build_opener') as opener:
            opener.return_value.open.side_effect = error
            with self.assertRaises(common.BaoError) as caught:
                common.bao('sentinel-path', {'value': 'sentinel'}, 'sentinel-token')
            self.assertNotIn('sentinel', str(caught.exception))
            self.assertEqual(caught.exception.status, 403)

    def test_private_files_are_exclusive_and_owner_only(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'secret'
            common.private(path, 'test-only')
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(FileExistsError):
                common.private(path, 'replace')
            self.assertEqual(path.read_text(), 'test-only')

    def test_authenticated_endpoint_never_redirects(self):
        self.assertIsNone(common.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://external.invalid'))

    def test_nonregular_and_oversize_custody_refuse(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'fifo'
            os.mkfifo(path, 0o600)
            with self.assertRaises(RuntimeError):
                common.read_private(path)
            large = Path(folder) / 'large'
            large.write_text('x' * 65537)
            large.chmod(0o600)
            with self.assertRaises(RuntimeError):
                common.read_private(large)

    def test_private_reads_reject_symlink_and_broad_mode(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'secret'
            common.private(path, 'sentinel')
            link = Path(folder) / 'link'
            link.symlink_to(path)
            with self.assertRaises(OSError):
                common.read_private(link)
            os.chmod(path, 0o644)
            with self.assertRaises(RuntimeError):
                common.read_private(path)

    def test_delivery_drift_refuses_rekey(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(stack_files, 'STATE', Path(folder)):
            stack_files.delivery(VALUES)
            stack_files.delivery(VALUES)
            with self.assertRaises(RuntimeError):
                stack_files.delivery({**VALUES, 'postgres_admin_password': 'f' * 64})
            self.assertEqual(common.read_private(Path(folder) / 'postgres.password'), VALUES['postgres_admin_password'])

    def test_no_service_credentials_before_vault(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(stack_files, 'STATE', Path(folder)):
            for name in ('bao.key', 'bao.crt'):
                common.private(Path(folder) / name, 'public-test-placeholder')
            stack_files.files()
            self.assertFalse(list(Path(folder).glob('*.password')))
            self.assertFalse((Path(folder) / 'valkey.conf').exists())


if __name__ == '__main__':
    unittest.main()
