"""Negative supply-chain cases must reject before any service execution."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import image_gate as gate
import install_image_tools as installer

POLICY = json.loads((gate.ROOT / 'deploy/podman/image-policy.json').read_text())
IMAGES = {key: POLICY[key]['image'] for key in ('openbao', 'postgres', 'valkey')}


class ImageTests(unittest.TestCase):
    def test_exceptions_are_exact_digest_platform_and_service_scoped(self):
        for service in ('valkey',):
            self.assertEqual(gate.provenance(service, IMAGES[service], POLICY, 'cosign'), 'maintainer-exception')
            for image in ('other@sha256:' + '0' * 64, IMAGES[service] + 'changed'):
                with self.assertRaises(RuntimeError):
                    gate.provenance(service, image, POLICY, 'cosign')
        invalid = {**POLICY, 'platform': 'linux/arm64'}
        with self.assertRaises(RuntimeError):
            gate.provenance('valkey', IMAGES['valkey'], invalid, 'cosign')
        with self.assertRaises(RuntimeError):
            gate.provenance('postgres', POLICY['historical_postgres']['image'], POLICY, 'cosign')
        invalid = {**POLICY, 'openbao': {**POLICY['openbao'], 'method': 'maintainer-exception'}}
        with self.assertRaises(RuntimeError):
            gate.provenance('openbao', IMAGES['openbao'], invalid, 'cosign')

    def test_signed_index_binds_publisher_digest_and_exact_platform_leaf(self):
        raw = json.dumps({'manifests': [{'digest': IMAGES['openbao'].split('@')[1],
                                        'platform': {'os': 'linux', 'architecture': 'amd64'}}]})
        digest = 'sha256:' + hashlib.sha256(raw.encode()).hexdigest()
        rule = {**POLICY['openbao'], 'index': 'ghcr.io/openbao/openbao@' + digest}
        policy = {**POLICY, 'openbao': rule}
        signature = json.dumps([{'critical': {'image': {'docker-manifest-digest': digest}}}])
        with patch.object(gate, 'run_bounded', side_effect=[SimpleNamespace(stdout=signature), SimpleNamespace(stdout=raw)]) as call:
            self.assertEqual(gate.provenance('openbao', IMAGES['openbao'], policy, 'cosign'), 'signed-index')
            self.assertIn(rule['identity'], call.call_args_list[0].args)
            self.assertIn(rule['issuer'], call.call_args_list[0].args)
        for altered in (raw + ' ', raw.replace('amd64', 'arm64')):
            with patch.object(gate, 'run_bounded', side_effect=[SimpleNamespace(stdout=signature), SimpleNamespace(stdout=altered)]):
                with self.assertRaises(RuntimeError):
                    gate.provenance('openbao', IMAGES['openbao'], policy, 'cosign')
        with patch.object(gate, 'run_bounded', return_value=SimpleNamespace(stdout='[]')):
            with self.assertRaises(RuntimeError):
                gate.provenance('openbao', IMAGES['openbao'], policy, 'cosign')

    def test_vulnerable_return_code_ratings_and_missing_inventory_block(self):
        base = {'bomFormat': 'CycloneDX', 'components': [{'name': 'fixture'}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(gate, 'EVIDENCE', Path(folder)), \
             patch.dict(gate.os.environ, {'TRIVY_IGNORE_UNFIXED': 'true', 'TRIVY_VEX': 'fixture-vex'}):
            for code, report, clean in ((0, base, True), (1, base, False),
                    (0, {**base, 'vulnerabilities': [{'ratings': [{'severity': 'critical'}]}]}, False)):
                with patch.object(gate, 'run_bounded', return_value=SimpleNamespace(returncode=code, stdout=json.dumps(report))) as call:
                    self.assertEqual(gate.scan('postgres', IMAGES['postgres'], 'trivy')[0], clean)
                    self.assertIn('--ignore-unfixed=false', call.call_args.args)
                    self.assertIn('/dev/null', call.call_args.args)
                    self.assertFalse(any(key.startswith('TRIVY_') for key in call.call_args.kwargs['env']))
                    self.assertEqual(call.call_args.kwargs['output_limit'], gate.MAX_AUDIT)
            with patch.object(gate, 'run_bounded', return_value=SimpleNamespace(returncode=0, stdout='{}')):
                with self.assertRaises(RuntimeError):
                    gate.scan('postgres', IMAGES['postgres'], 'trivy')

    def test_preserves_all_three_sboms_then_rejects_any_unclean_image(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(gate, 'EVIDENCE', Path(folder)), \
             patch.object(gate, 'tool'), patch.object(gate, 'provenance'), \
             patch('postgres_image.validate_image', return_value=Path(folder) / 'image.tar'), \
             patch.object(gate, 'scan', side_effect=[(True, 0), (False, 3), (True, 0)]) as scans:
            with self.assertRaisesRegex(RuntimeError, 'postgres'):
                gate.verify_images(IMAGES)
            self.assertEqual(scans.call_count, 3)

    def test_tool_tampering_and_symlinks_reject(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(gate, 'ROOT', Path(folder)):
            root = Path(folder)
            (root / 'scripts').mkdir()
            (root / '.local/tools').mkdir(parents=True)
            pin = {'cosign': {'binary_sha256': hashlib.sha256(b'reviewed').hexdigest()}}
            (root / 'scripts/image-tools.lock.json').write_text(json.dumps(pin))
            binary = root / '.local/tools/cosign'
            binary.write_bytes(b'reviewed')
            self.assertEqual(gate.tool('cosign'), str(binary))
            binary.write_bytes(b'tampered')
            with self.assertRaises(RuntimeError): gate.tool('cosign')
            binary.unlink(); binary.symlink_to('/dev/zero')
            with self.assertRaises(OSError): gate.tool('cosign')

    def test_tool_download_rejects_corrupt_or_oversized_artifact(self):
        from io import BytesIO
        for data in (b'wrong', b'x' * (150 * 1024 * 1024 + 1)):
            with patch.object(installer.urllib.request, 'urlopen', return_value=BytesIO(data)):
                with self.assertRaises(RuntimeError): installer.download('https://fixture.invalid', '0' * 64)


if __name__ == '__main__':
    unittest.main()
