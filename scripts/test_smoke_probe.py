"""Adversarial smoke evidence tests, including optimized Python and real children."""
import os
import socket
import subprocess
import sys
import threading
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import smoke_probe

ROOT = Path(__file__).resolve().parent.parent
GOOD = b'HTTP/1.1 200 OK\r\nContent-Length: 3\r\n\r\nok\n'
BAD = b'HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n'


class SmokeProbeTests(unittest.TestCase):
    def test_http_failures_and_expected_responses(self):
        for replies, message in (([b'garbage'], 'invalid response'),
                                 ([GOOD, GOOD], 'forbidden route')):
            with self.subTest(message=message), patch.object(smoke_probe, 'request', side_effect=replies):
                with self.assertRaisesRegex(RuntimeError, message):
                    smoke_probe.verify(1)
        with patch.object(smoke_probe, 'request', side_effect=[GOOD, BAD, BAD, BAD]):
            smoke_probe.verify(1)

    def test_container_identity_rejects_root_and_unexpected_users(self):
        for user in ('0:0', '', '65532:0'):
            with self.subTest(user=user), patch.object(smoke_probe, 'podman', return_value=SimpleNamespace(stdout=user)):
                with self.assertRaisesRegex(RuntimeError, 'expected user'):
                    smoke_probe.container_user('test-container')
        with patch.object(smoke_probe, 'podman', return_value=SimpleNamespace(stdout='65532:65532\n')):
            smoke_probe.container_user('test-container')

    def test_checks_remain_active_with_optimization(self):
        cases = (
            ("patch.object(smoke_probe, 'request', return_value=b'garbage')", 'smoke_probe.verify(1)', 'invalid response'),
            ("patch.object(smoke_probe, 'request', return_value=" + repr(GOOD) + ')', 'smoke_probe.verify(1)', 'forbidden route'),
            ("patch.object(smoke_probe, 'podman', return_value=SimpleNamespace(stdout='0:0'))", "smoke_probe.container_user('test')", 'expected user'),
        )
        for mode in ('flag', 'environment'):
            env = os.environ.copy()
            env['PYTHONPATH'] = str(ROOT / 'scripts')
            env['PYTHONOPTIMIZE'] = '1' if mode == 'environment' else '0'
            for mocking, call, message in cases:
                with self.subTest(mode=mode, check=message):
                    code = ('import smoke_probe\nfrom types import SimpleNamespace\nfrom unittest.mock import patch\nwith ' + mocking + ':\n    ' + call + '\n')
                    command = [sys.executable] + (['-O'] if mode == 'flag' else []) + ['-c', code]
                    result = subprocess.run(command, env=env, capture_output=True, text=True, timeout=10)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(message, result.stderr)

    def test_readiness_rejects_bad_addresses_eof_and_timeout(self):
        cases = (
            ('', 'exited'),
            ('not readiness\n', 'invalid listening address'),
            ('Runasmidja development probe on 0.0.0.0:12\n', 'invalid listening address'),
            ('Runasmidja development probe on 127.0.0.1:0\n', 'invalid listening port'),
            ('Runasmidja development probe on 127.0.0.1:65536\n', 'invalid listening port'),
            ('x' * 257, 'exceeds test budget'),
        )
        for line, message in cases:
            with self.subTest(line=line):
                code = 'import sys; sys.stdout.write(' + repr(line) + '); sys.stdout.flush()'
                process = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE)
                try:
                    with self.assertRaisesRegex(RuntimeError, message):
                        smoke_probe.ready_port(process)
                finally:
                    smoke_probe.stop_process(process)
        process = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'], stdout=subprocess.PIPE)
        try:
            with self.assertRaisesRegex(RuntimeError, 'readiness timed out'):
                smoke_probe.ready_port(process, timeout=0.05)
        finally:
            smoke_probe.stop_process(process)

    def test_dead_child_cannot_borrow_responses_from_an_impostor(self):
        # An unrelated listener could answer perfectly; an exited child must fail first.
        process = subprocess.Popen([sys.executable, '-c', 'pass'], stdout=subprocess.PIPE)
        process.wait(timeout=5)
        with patch.object(smoke_probe.subprocess, 'Popen', return_value=process), \
             patch.object(smoke_probe, 'verify') as verify:
            with self.assertRaisesRegex(RuntimeError, 'exited'):
                smoke_probe.native_smoke('ignored')
            verify.assert_not_called()

    def test_child_exit_during_verification_fails_and_is_reaped(self):
        code = "import time; print('Runasmidja development probe on 127.0.0.1:12345', flush=True); time.sleep(30)"
        process = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE)
        def exit_during_verify(_port):
            process.terminate()
            process.wait(timeout=5)
        with patch.object(smoke_probe.subprocess, 'Popen', return_value=process), \
             patch.object(smoke_probe, 'verify', side_effect=exit_during_verify):
            with self.assertRaisesRegex(RuntimeError, 'exited during verification'):
                smoke_probe.native_smoke('ignored')
        self.assertIsNotNone(process.poll())
        self.assertTrue(process.stdout.closed)

    def test_response_reads_fragmented_input_and_rejects_over_budget(self):
        for reply, rejects in ((GOOD, False), (b'x' * 4097, True)):
            with self.subTest(size=len(reply)), socket.socket() as listener:
                listener.bind(('127.0.0.1', 0))
                listener.listen(1)
                def answer():
                    with listener.accept()[0] as stream:
                        stream.recv(4096)
                        stream.sendall(reply[:3])
                        stream.sendall(reply[3:])
                thread = threading.Thread(target=answer)
                thread.start()
                try:
                    if rejects:
                        with self.assertRaisesRegex(RuntimeError, 'response exceeds test budget'):
                            smoke_probe.request(listener.getsockname()[1], b'GET /\r\n\r\n')
                    else:
                        self.assertEqual(smoke_probe.request(listener.getsockname()[1], b'GET /\r\n\r\n'), reply)
                finally:
                    thread.join(timeout=5)
                self.assertFalse(thread.is_alive())


class NativeProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(['cargo', 'build', '--locked', '-p', 'runasmidja-server'], cwd=ROOT,
                       check=True, capture_output=True, timeout=120)

    def test_actual_child_uses_its_bound_ephemeral_port(self):
        process = subprocess.Popen([str(ROOT / 'target/debug/runasmidja-server'), '0'], stdout=subprocess.PIPE)
        try:
            port = smoke_probe.ready_port(process)
            self.assertGreater(port, 0)
            with socket.socket() as collision:
                with self.assertRaises(OSError):
                    collision.bind(('127.0.0.1', port))
            smoke_probe.verify(port)
            self.assertIsNone(process.poll())
        finally:
            smoke_probe.stop_process(process)

    def test_old_fixed_port_impostor_is_never_contacted(self):
        # Keep an unrelated socket bound at the formerly trusted port.
        with socket.socket() as impostor:
            try:
                impostor.bind(('127.0.0.1', 18081))
            except OSError:
                # A pre-existing listener is already a collision; do not mutate it.
                smoke_probe.native_smoke(ROOT / 'target/debug/runasmidja-server')
                return
            impostor.listen(1)
            impostor.settimeout(0.05)
            smoke_probe.native_smoke(ROOT / 'target/debug/runasmidja-server')
            with self.assertRaises(TimeoutError):
                impostor.accept()
