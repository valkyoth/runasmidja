"""Real binary producers prove disk caps, atomic publication and failure cleanup."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import stream_archive as stream


class ArchiveWriterTests(unittest.TestCase):
    def test_binary_boundary_and_durable_publication(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'image.tar'
            payload = bytes(range(256)) * 4
            events = []
            original = stream.os.fsync
            def sync(fd):
                events.append('file' if not __import__('stat').S_ISDIR(os.fstat(fd).st_mode) else 'parent')
                original(fd)
            with patch.object(stream.os, 'fsync', side_effect=sync):
                stream.save_bounded_archive([sys.executable, '-c', 'import os;os.write(1,bytes(range(256))*4)'],target,limit=1024)
            self.assertEqual(target.read_bytes(), payload)
            self.assertEqual(target.stat().st_mode & 0o777, 0o600)
            self.assertEqual(events, ['file', 'parent'])

    def test_flood_timeout_stderr_and_failed_exit_keep_old_archive(self):
        codes = ["import os;\nwhile True: os.write(1,b'x'*65536)",
                 "import os;os.write(2,b'e'*2048)", "import time;time.sleep(30)",
                 "import os,time;os.close(1);os.close(2);time.sleep(30)",
                 "pass", "import os;os.write(1,b'partial');raise SystemExit(1)"]
        original = stream.subprocess.Popen
        for code in codes:
            with self.subTest(code=code), tempfile.TemporaryDirectory() as folder:
                target = Path(folder) / 'image.tar'; target.write_bytes(b'old')
                children = []
                def launch(*args, **kwargs):
                    child = original(*args, **kwargs); children.append(child); return child
                with patch.object(stream.subprocess, 'Popen', side_effect=launch), self.assertRaises(RuntimeError):
                    stream.save_bounded_archive([sys.executable,'-c',code],target,limit=1024,stderr_limit=1024,timeout=.1)
                self.assertEqual(target.read_bytes(),b'old')
                self.assertFalse(target.with_name('image.tar.next').exists())
                self.assertIsNotNone(children[0].returncode)
                self.assertTrue(children[0].stdout.closed and children[0].stderr.closed)

    def test_never_writes_over_budget_even_temporarily(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'image.tar'
            largest=[]
            original=stream.durable_unlink
            def unlink(path):
                largest.append(path.stat().st_size); original(path)
            with patch.object(stream,'durable_unlink',side_effect=unlink), self.assertRaises(RuntimeError):
                stream.save_bounded_archive([sys.executable,'-c',"import os;os.write(1,b'x'*1025)"],target,limit=1024)
            self.assertLessEqual(max(largest),1024)
            self.assertFalse(target.exists())

    def test_symlink_fifo_stale_temporary_and_sync_failure_fail_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); target=root/'image.tar'
            for kind in ('symlink','fifo','temporary'):
                with self.subTest(kind=kind):
                    if kind=='symlink': target.symlink_to('/dev/zero')
                    elif kind=='fifo': os.mkfifo(target,0o600)
                    else: target.with_name('image.tar.next').symlink_to('/dev/zero')
                    with patch.object(stream.subprocess,'Popen') as child, self.assertRaises((OSError,RuntimeError)):
                        stream.save_bounded_archive(['never-start'],target,limit=1024)
                    child.assert_not_called()
                    if target.is_symlink() or target.exists(): target.unlink()
                    temporary=target.with_name('image.tar.next')
                    if temporary.is_symlink(): temporary.unlink()
            target.write_bytes(b'old')
            with patch.object(stream.os,'fsync',side_effect=OSError('fault')), self.assertRaises(OSError):
                stream.save_bounded_archive([sys.executable,'-c',"import os;os.write(1,b'new')"],target,limit=1024)
            self.assertEqual(target.read_bytes(),b'old')

    def test_rename_and_directory_sync_faults_are_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'image.tar'; target.write_bytes(b'old')
            command = [sys.executable, '-c', "import os;os.write(1,b'new')"]
            with patch.object(stream.os, 'replace', side_effect=OSError('rename fault')), self.assertRaises(OSError):
                stream.save_bounded_archive(command, target, limit=1024)
            self.assertEqual(target.read_bytes(), b'old')
            self.assertFalse(target.with_name('image.tar.next').exists())
            with patch.object(stream, 'sync_parent', side_effect=OSError('directory fault')), self.assertRaises(OSError):
                stream.save_bounded_archive(command, target, limit=1024)
            # Rename is already visible; durability failure must never report success.
            self.assertEqual(target.read_bytes(), b'new')
            self.assertFalse(target.with_name('image.tar.next').exists())


if __name__=='__main__': unittest.main()
