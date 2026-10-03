#!/usr/bin/env python3
"""Exercise the actual native process and scratch/non-root container probe."""
import argparse
import socket
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = 'runasmidja-test-probe'

def request(port, content):
    with socket.create_connection(('127.0.0.1', port), timeout=5) as stream:
        stream.sendall(content)
        return stream.recv(4096)

def verify(port):
    deadline = time.monotonic() + 20
    while True:
        try:
            reply = request(port, b'GET /healthz HTTP/1.1\r\nHost: localhost\r\n\r\n')
            break
        except OSError:
            if time.monotonic() > deadline:
                raise
            time.sleep(0.1)
    assert reply.startswith(b'HTTP/1.1 200 OK\r\n') and reply.endswith(b'ok\n')
    for content in (b'POST /healthz HTTP/1.1\r\n\r\n', b'GET /api/v1/operations HTTP/1.1\r\n\r\n', b'GET / HTTP/1.1\r\n\r\n'):
        assert request(port, content).startswith(b'HTTP/1.1 400 Bad Request\r\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--container', action='store_true')
    args = parser.parse_args()
    if args.container:
        subprocess.run(['cargo', 'build', '--locked', '-p', 'runasmidja-server', '--release', '--target', 'x86_64-unknown-linux-musl'], cwd=ROOT, check=True)
        subprocess.run(['podman', 'build', '--network', 'none', '-t', 'localhost/runasmidja:foundation', '-f', 'Containerfile', '.'], cwd=ROOT, check=True)
        # No replacement of an existing name; only remove a container created by this run.
        subprocess.run(['podman', 'run', '-d', '--name', NAME, '--init', '--read-only', '--cap-drop', 'ALL',
            '--security-opt', 'no-new-privileges', '--memory', '32m', '--pids-limit', '16',
            '-p', '127.0.0.1:18082:18080', 'localhost/runasmidja:foundation'], check=True, stdout=subprocess.DEVNULL)
        try:
            user = subprocess.check_output(['podman', 'inspect', '--format', '{{.Config.User}}', NAME], text=True).strip()
            assert user == '65532:65532'
            verify(18082)
        finally:
            subprocess.run(['podman', 'rm', '-f', NAME], check=True, stdout=subprocess.DEVNULL)
        print('Scratch/non-root/read-only container health and rejected routes: PASS')
    else:
        subprocess.run(['cargo', 'build', '--locked', '-p', 'runasmidja-server'], cwd=ROOT, check=True)
        process = subprocess.Popen([str(ROOT / 'target/debug/runasmidja-server'), '18081'], stdout=subprocess.DEVNULL)
        try:
            verify(18081)
        finally:
            process.terminate()
            process.wait(timeout=5)
        print('Native loopback health and rejected routes: PASS')

if __name__ == '__main__':
    main()
