"""Exact archive compilation: corrupt bytes reject; registry root is never re-fetched."""
import hashlib
import io
import os
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path
import tool_archive

ROOT=Path(__file__).resolve().parent.parent


class ToolInstallTests(unittest.TestCase):
    def archive(self, root, bad_path=None):
        crate=root/'original.crate'
        files={'Cargo.toml': '[package]\nname="runasmidja-integrity-fixture"\nversion="0.0.0"\nedition="2024"\n',
               'Cargo.lock': 'version = 4\n[[package]]\nname="runasmidja-integrity-fixture"\nversion="0.0.0"\n',
               'src/main.rs':'fn main() { println!("verified-archive-source"); }'}
        with tarfile.open(crate,'w:gz') as output:
            for path,content in files.items():
                info=tarfile.TarInfo('runasmidja-integrity-fixture-0.0.0/'+path)
                data=content.encode();info.size=len(data);output.addfile(info,io.BytesIO(data))
            if bad_path:
                info=tarfile.TarInfo(bad_path);info.size=1;output.addfile(info,io.BytesIO(b'x'))
        return crate

    def fixture(self, root, corrupt=False):
        scripts=root/'scripts';scripts.mkdir()
        for name in ('install_ci_tools.sh','tool_archive.py'):
            (scripts/name).write_bytes((ROOT/'scripts'/name).read_bytes())
        crate=self.archive(root)
        digest=hashlib.sha256(crate.read_bytes()).hexdigest()
        (scripts/'ci-tools.lock').write_text('runasmidja-integrity-fixture 0.0.0 '+digest+'\n')
        if corrupt: crate.write_bytes(crate.read_bytes()+b'corrupted')
        fakebin=root/'fakebin';fakebin.mkdir()
        # The only root-package download available is this one verified archive.
        curl=fakebin/'curl'
        curl.write_text('#!/usr/bin/env python3\nimport os,sys,shutil\nshutil.copyfile(os.environ["FIXTURE_ARCHIVE"],sys.argv[-1])\n')
        curl.chmod(0o700)
        env=dict(os.environ,PATH=str(fakebin)+os.pathsep+os.environ['PATH'],
                 CARGO_NET_OFFLINE='true', CARGO_INSTALL_ROOT=str(root/'installed'), FIXTURE_ARCHIVE=str(crate))
        return env

    def test_corrupt_download_never_installs(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);env=self.fixture(root,corrupt=True)
            result=subprocess.run(['bash','scripts/install_ci_tools.sh'],cwd=root,env=env,capture_output=True,timeout=30)
            self.assertNotEqual(result.returncode,0)
            self.assertFalse((root/'installed/bin/runasmidja-integrity-fixture').exists())

    def test_installs_verified_root_with_registry_unavailable(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);env=self.fixture(root)
            result=subprocess.run(['bash','scripts/install_ci_tools.sh'],cwd=root,env=env,capture_output=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr.decode())
            actual=subprocess.check_output([str(root/'installed/bin/runasmidja-integrity-fixture')])
            self.assertEqual(actual,b'verified-archive-source\n')

    def test_archive_traversal_or_wrong_identity_rejects(self):
        for path in ('../escape', '/absolute', 'runasmidja-integrity-fixture-0.0.0/../../escape'):
            with self.subTest(path=path), tempfile.TemporaryDirectory() as folder:
                root=Path(folder);crate=self.archive(root,path)
                with self.assertRaises(ValueError):
                    tool_archive.extract(crate,root/'extracted','runasmidja-integrity-fixture','0.0.0')
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);crate=self.archive(root)
            with self.assertRaises(ValueError):
                tool_archive.extract(crate,root/'extracted','different-root','0.0.0')


if __name__=='__main__': unittest.main()
