#!/usr/bin/env python3
"""Exercise the actual native process and scratch/non-root container probe."""
import argparse
import os
import re
import selectors
import socket
import subprocess
import time
from pathlib import Path
from process_limits import run_bounded
from podman_guard import podman, require_rootless

ROOT = Path(__file__).resolve().parent.parent
NAME = 'runasmidja-test-probe'

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def request(port, content):
    with socket.create_connection(('127.0.0.1', port), timeout=5) as stream:
        stream.sendall(content)
        reply = bytearray()
        while True:
            part = stream.recv(4097 - len(reply))
            if not part:
                return bytes(reply)
            reply.extend(part)
            require(len(reply) <= 4096, 'probe response exceeds test budget')

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
    require(reply.startswith(b'HTTP/1.1 200 OK\r\n') and reply.endswith(b'ok\n'),
            'health probe returned an invalid response')
    for content in (b'POST /healthz HTTP/1.1\r\n\r\n', b'GET /api/v1/operations HTTP/1.1\r\n\r\n', b'GET / HTTP/1.1\r\n\r\n'):
        require(request(port, content).startswith(b'HTTP/1.1 400 Bad Request\r\n'),
                'health probe accepted a forbidden route')

def container_user(name):
    user = podman(run_bounded, 'inspect', '--format', '{{.Config.User}}', name).stdout.strip()
    require(user == '65532:65532', 'container is not running as the expected user')

def ready_port(process, timeout=5):
    deadline = time.monotonic() + timeout
    line = bytearray()
    with selectors.DefaultSelector() as selector:
        selector.register(process.stdout, selectors.EVENT_READ)
        while b'\n' not in line:
            remaining = deadline - time.monotonic()
            require(remaining > 0, 'probe readiness timed out')
            require(selector.select(remaining), 'probe readiness timed out')
            part = os.read(process.stdout.fileno(), 257 - len(line))
            require(part, 'probe exited before becoming ready')
            line.extend(part)
            require(len(line) <= 256, 'probe readiness exceeds test budget')
    match = re.fullmatch(rb'Runasmidja development probe on 127\.0\.0\.1:([0-9]+)\n', line)
    require(match is not None, 'probe reported an invalid listening address')
    port = int(match[1])
    require(0 < port <= 65535, 'probe reported an invalid listening port')
    require(process.poll() is None, 'probe exited before verification')
    return port

def stop_process(process):
    if process.poll() is None:
        process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)
    if process.stdout is not None:
        process.stdout.close()

def native_smoke(binary):
    process = subprocess.Popen([str(binary), '0'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    try:
        port = ready_port(process)
        require(process.poll() is None, 'probe exited before verification')
        verify(port)
        require(process.poll() is None, 'probe exited during verification')
    finally:
        stop_process(process)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--container', action='store_true')
    args = parser.parse_args()
    if args.container:
        require_rootless(run_bounded)
        subprocess.run(['cargo', 'build', '--locked', '-p', 'runasmidja-server', '--release', '--target', 'x86_64-unknown-linux-musl'], cwd=ROOT, check=True)
        podman(run_bounded, 'build', '--network', 'none', '-t', 'localhost/runasmidja:foundation', '-f', str(ROOT / 'Containerfile'), str(ROOT))
        # No replacement of an existing name; only remove a container created by this run.
        podman(run_bounded, 'run', '-d', '--name', NAME, '--init', '--read-only', '--cap-drop', 'ALL',
            '--security-opt', 'no-new-privileges', '--memory', '32m', '--pids-limit', '16',
            '-p', '127.0.0.1:18082:18080', 'localhost/runasmidja:foundation')
        try:
            container_user(NAME)
            verify(18082)
        finally:
            podman(run_bounded, 'rm', '-f', NAME)
        print('Scratch/non-root/read-only container health and rejected routes: PASS')
    else:
        subprocess.run(['cargo', 'build', '--locked', '-p', 'runasmidja-server'], cwd=ROOT, check=True)
        native_smoke(ROOT / 'target/debug/runasmidja-server')
        print('Native loopback health and rejected routes: PASS')

if __name__ == '__main__':
    main()
