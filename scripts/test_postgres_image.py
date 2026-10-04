"""Adversarial archive/material/receipt binding for the public-source image."""
import hashlib
import io
import json
import os
import tarfile
import tempfile
import unittest
import podman_guard
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import image_archive
import postgres_image as image
from custody import replace_private


def archive(path, attack=None):
    payload = b'independently specified layer bytes'
    layer = hashlib.sha256(payload).hexdigest()
    config = json.dumps({'os': 'linux', 'architecture': 'amd64',
                         'rootfs': {'diff_ids': ['sha256:' + layer]}}).encode()
    identity = hashlib.sha256(config).hexdigest()
    manifest = [{'Config': identity + '.json', 'Layers': [layer + '.tar']}]
    if attack == 'config-name': manifest[0]['Config'] = '0' * 64 + '.json'
    if attack == 'platform':
        config = config.replace(b'amd64', b'arm64')
        identity = hashlib.sha256(config).hexdigest(); manifest[0]['Config'] = identity + '.json'
    entries = {'manifest.json': json.dumps(manifest).encode(), identity + '.json': config,
               layer + '.tar': payload if attack != 'layer-bytes' else b'tampered'}
    with tarfile.open(path, 'w') as output:
        for name, data in entries.items():
            member = tarfile.TarInfo(name); member.size = len(data)
            output.addfile(member, io.BytesIO(data))
        if attack in ('link', 'fifo', 'duplicate'):
            member = tarfile.TarInfo('manifest.json' if attack == 'duplicate' else 'unexpected')
            member.type = tarfile.SYMTYPE if attack == 'link' else tarfile.FIFOTYPE if attack == 'fifo' else tarfile.REGTYPE
            member.linkname = '/dev/zero'
            output.addfile(member)
    return 'sha256:' + identity


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        guard = patch.object(podman_guard, 'require_rootless')
        guard.start(); self.addCleanup(guard.stop)
    def test_outer_archive_budget_and_special_files_reject_before_parsing(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'large'
            with path.open('wb') as output:
                output.truncate(512 * 1024 * 1024 + 1)
            fifo = Path(folder) / 'fifo'; os.mkfifo(fifo, 0o600)
            link = Path(folder) / 'link'; link.symlink_to(path)
            with patch.object(image_archive.tarfile, 'open') as parser:
                for target in (path, fifo, Path('/dev/zero'), link):
                    with self.assertRaises((RuntimeError, OSError)):
                        image_archive.verify(target, 'sha256:' + '0' * 64)
                parser.assert_not_called()

    def test_binds_config_layers_and_platform_without_extraction(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'image.tar'
            identity = archive(path)
            image_archive.verify(path, identity)
            with self.assertRaises(RuntimeError): image_archive.verify(path, 'sha256:' + '0' * 64)
            for attack in ('config-name', 'layer-bytes', 'platform', 'link', 'fifo', 'duplicate'):
                with self.subTest(attack=attack):
                    identity = archive(path, attack)
                    with self.assertRaises((RuntimeError, KeyError)): image_archive.verify(path, identity)

    def test_invalid_input_blob_custody_and_size_fail_without_following(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'blob'; path.write_bytes(b'12345')
            self.assertEqual(image.bounded_hash(path, 5), hashlib.sha256(b'12345').hexdigest())
            with self.assertRaises(RuntimeError): image.bounded_hash(path, 4)
            link = Path(folder) / 'link'; link.symlink_to('/dev/zero')
            with self.assertRaises(OSError): image.bounded_hash(link, 1024)
            fifo = Path(folder) / 'fifo'; os.mkfifo(fifo, 0o600)
            with self.assertRaises(RuntimeError): image.bounded_hash(fifo, 1024)

    def test_receipt_recipe_and_scanned_archive_are_not_interchangeable(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(image, 'STATE', Path(folder)), \
             patch.object(image, 'fingerprint', return_value='reviewed-inputs'):
            root = Path(folder); identity = archive(root / 'image.tar')
            image.record(identity)
            with patch.object(image, 'run_bounded', return_value=SimpleNamespace(stdout=identity)):
                self.assertEqual(image.validate_image(identity), root / 'image.tar')
            with patch.object(image, 'fingerprint', return_value='changed-recipe'), patch.object(image, 'run_bounded') as child:
                with self.assertRaises(RuntimeError): image.validate_image(identity)
                child.assert_not_called()
            other = archive(root / 'other.tar', 'platform')
            receipt = json.loads(image.read_private(root / 'receipt.json'))
            receipt['image'] = other
            replace_private(root / 'receipt.json', json.dumps(receipt))
            with self.assertRaises(RuntimeError): image.validate_image(identity)
            image.record(identity)
            (root / 'image.tar').write_bytes(b'tampered')
            with self.assertRaises(RuntimeError): image.validate_image(identity)

    def test_rootless_entrypoint_is_valid_shell(self):
        from process_limits import run_bounded
        run_bounded('sh', '-n', str(image.ROOT / 'deploy/podman/postgres/entrypoint.sh'))


if __name__ == '__main__':
    unittest.main()
