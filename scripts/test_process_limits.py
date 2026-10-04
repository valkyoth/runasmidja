"""Real child adversaries verify caps during I/O, concurrent draining and cleanup."""
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch
import process_limits
from process_limits import run_bounded
import custody


class ChildTests(unittest.TestCase):
    def test_reaped_leader_is_never_signalled_again(self):
        original = process_limits.subprocess.Popen
        children = []
        def launch(*args, **kwargs):
            child = original(*args, **kwargs)
            children.append(child)
            return child
        for code, allowed in (("pass", (0,)), ("raise SystemExit(3)", (3,))):
            with patch.object(process_limits.subprocess, 'Popen', side_effect=launch), \
                 patch.object(process_limits.os, 'killpg') as kill:
                run_bounded(sys.executable, '-c', code, allowed=allowed)
                kill.assert_not_called()
                self.assertIsNotNone(children[-1].returncode)
        with patch.object(process_limits.os, 'killpg') as kill:
            process_limits._kill_reap(children[-1])
            kill.assert_not_called()

    def test_aggregate_stdout_stderr_limit_and_oversized_line(self):
        for code in ("import os; os.write(1,b'x'*8192)",
                     "import os; os.write(1,b'x'*600); os.write(2,b'y'*600)",
                     "import os;\nwhile True: os.write(2,b'x'*65536)"):
            with self.subTest(code=code), self.assertRaisesRegex(RuntimeError, 'output exceeds'):
                run_bounded(sys.executable, '-c', code, output_limit=1024, timeout=2)

    def test_no_deadlock_when_child_writes_both_pipes_before_reading(self):
        code = "import os,sys; os.write(1,b'o'*65536); os.write(2,b'e'*65536); print(len(sys.stdin.buffer.read()))"
        result = run_bounded(sys.executable, '-c', code, data='i'*65536, timeout=3)
        self.assertTrue(result.stdout.endswith('65536\n'))
        self.assertEqual(result.stderr, 'e'*65536)

    def test_input_and_output_edges(self):
        for size in (0, 1023, 1024):
            result = run_bounded(sys.executable, '-c', "import sys; sys.stdout.buffer.write(sys.stdin.buffer.read())",
                                 data='x'*size, input_limit=1024, output_limit=1024)
            self.assertEqual(len(result.stdout), size)
        with patch.object(process_limits.subprocess, 'Popen') as launch:
            with self.assertRaisesRegex(RuntimeError, 'input exceeds'):
                run_bounded('never-start', data='x'*1025, input_limit=1024)
            launch.assert_not_called()

    def test_timeout_kills_reaps_child_and_pipe_holding_descendant(self):
        child = None
        original = process_limits.subprocess.Popen
        def launch(*args, **kwargs):
            nonlocal child
            child = original(*args, **kwargs)
            return child
        code = "import os,time; os.fork(); time.sleep(30)"
        started = time.monotonic()
        with patch.object(process_limits.subprocess, 'Popen', side_effect=launch):
            with self.assertRaisesRegex(RuntimeError, 'deadline'):
                run_bounded(sys.executable, '-c', code, timeout=0.1)
        self.assertLess(time.monotonic()-started, 2)
        self.assertIsNotNone(child.returncode)
        self.assertTrue(child.stdout.closed and child.stderr.closed)

    def test_flood_failure_kills_and_closes(self):
        original = process_limits.subprocess.Popen
        children = []
        def launch(*args, **kwargs):
            child = original(*args, **kwargs)
            children.append(child)
            return child
        with patch.object(process_limits.subprocess, 'Popen', side_effect=launch):
            with self.assertRaises(RuntimeError):
                run_bounded(sys.executable, '-c', "import os;\nwhile True: os.write(1,b'x'*4096)", output_limit=128)
        self.assertIsNotNone(children[0].returncode)
        self.assertTrue(children[0].stdout.closed)

    def test_failures_never_echo_secret_input_or_output(self):
        with self.assertRaises(RuntimeError) as error:
            run_bounded(sys.executable, '-c', "import sys; print('secret-sentinel');sys.exit(1)", data='secret-sentinel')
        self.assertNotIn('secret-sentinel', str(error.exception))

    def test_explicit_child_environment_is_used(self):
        result = run_bounded(sys.executable, '-c', "import os; print(os.environ.get('TRIVY_IGNORE_UNFIXED', 'absent'))", env={})
        self.assertEqual(result.stdout, 'absent\n')


class EvidenceTests(unittest.TestCase):
    def test_retry_resyncs_visible_custody_before_using_it(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'checkpoint'
            with patch.object(custody, 'sync_parent', side_effect=OSError('fault')):
                with self.assertRaises(OSError): custody.private(path, 'retained')
            events = []
            original = custody.os.fsync
            def sync(fd):
                events.append(__import__('stat').S_ISDIR(os.fstat(fd).st_mode))
                original(fd)
            with patch.object(custody.os, 'fsync', side_effect=sync):
                self.assertEqual(custody.read_private(path), 'retained')
            self.assertEqual(events, [False, True])
            with patch.object(custody.os, 'fsync', side_effect=OSError('fault')):
                with self.assertRaises(OSError): custody.read_private(path)

    def test_creation_and_replacement_enforce_utf8_byte_budgets_before_mutation(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'secret'
            with self.assertRaises(RuntimeError): custody.private(path, 'é' * 32769)
            self.assertFalse(path.exists())
            custody.private(path, 'retained')
            with self.assertRaises(RuntimeError): custody.replace_private(path, 'é' * 32769)
            self.assertEqual(custody.read_private(path), 'retained')
            with self.assertRaises(ValueError): custody.replace_private(path, 'new', limit=-1)

    def test_audit_symlink_device_fifo_and_oversize_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            actual = root/'audit'
            custody.private(actual, 'x'*1025)
            link = root/'link'; link.symlink_to(actual)
            fifo = root/'fifo'; os.mkfifo(fifo, 0o600)
            for path in (link, Path('/dev/zero'), fifo, actual):
                with self.subTest(path=path), self.assertRaises((RuntimeError, OSError)):
                    custody.read_owned_regular_bounded(path, limit=1024)
            self.assertEqual(custody.read_owned_regular_bounded(actual, limit=1025), 'x'*1025)

    def test_file_and_parent_sync_order_for_create_replace_unlink(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'secret'
            events=[]
            original_sync=custody.os.fsync
            original_replace=custody.os.replace
            def sync(fd):
                events.append('sync-directory' if __import__('stat').S_ISDIR(os.fstat(fd).st_mode) else 'sync-file')
                original_sync(fd)
            def replace(a,b):
                events.append('rename');original_replace(a,b)
            with patch.object(custody.os,'fsync',side_effect=sync), patch.object(custody.os,'replace',side_effect=replace):
                custody.private(path,'first')
                self.assertEqual(events, ['sync-file','sync-directory'])
                events.clear();custody.replace_private(path,'second')
                self.assertEqual(events, ['sync-file','sync-directory','rename','sync-directory'])
                events.clear();custody.durable_unlink(path)
                self.assertEqual(events, ['sync-directory'])

    def test_create_rename_unlink_faults_preserve_or_fail_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'secret'
            for boundary in ('create-parent','temporary-parent','rename','rename-parent','unlink-parent'):
                with self.subTest(boundary=boundary):
                    if path.exists(): path.unlink()
                    temporary=path.with_name('secret.next')
                    if temporary.exists(): temporary.unlink()
                    if boundary=='create-parent':
                        with patch.object(custody,'sync_parent',side_effect=OSError('fault')):
                            with self.assertRaises(OSError): custody.private(path,'new')
                        self.assertEqual(custody.read_private(path),'new')
                        continue
                    custody.private(path,'old')
                    if boundary=='unlink-parent':
                        with patch.object(custody,'sync_parent',side_effect=OSError('fault')):
                            with self.assertRaises(OSError): custody.durable_unlink(path)
                        self.assertFalse(path.exists());continue
                    if boundary=='rename':
                        with patch.object(custody.os,'replace',side_effect=OSError('fault')):
                            with self.assertRaises(OSError): custody.replace_private(path,'new')
                        self.assertEqual(custody.read_private(path),'old')
                    else:
                        effects=[OSError('fault')] if boundary=='temporary-parent' else [None,OSError('fault')]
                        with patch.object(custody,'sync_parent',side_effect=effects):
                            with self.assertRaises(OSError): custody.replace_private(path,'new')
                        self.assertEqual(custody.read_private(path),'old' if boundary=='temporary-parent' else 'new')
                    # Retry accepts only bounded verified custody, never silently discards the old target.
                    custody.replace_private(path,'new')
                    self.assertEqual(custody.read_private(path),'new')


if __name__ == '__main__':
    unittest.main()
