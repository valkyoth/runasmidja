#!/usr/bin/env python3
"""Fail on upstream drift or unavailable metadata; never auto-admit new code."""
import json
import sys
import re
import subprocess
import tomllib
import urllib.request
from pathlib import Path
from process_limits import run_bounded

ROOT = Path(__file__).resolve().parent.parent

def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'runasmidja-freshness/0.1 (https://github.com/valkyoth/runasmidja)'})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read(4 * 1024 * 1024 + 1)
        if len(raw) > 4 * 1024 * 1024:
            raise ValueError('metadata too large')
        return raw

def crate_version(data):
    # Explicit stable-only selection, independent of registry ordering.
    versions = [item['num'] for item in data['versions'] if not item.get('yanked') and '-' not in item['num']]
    if not versions:
        raise ValueError('no non-yanked stable release')
    return max(versions, key=lambda value: tuple(int(part) for part in value.split('.')))

def postgres_version(document):
    versions = set(re.findall(r'\bv(19(?:\.\d+|beta\d+|rc\d+)?)/', document))
    if not versions:
        raise ValueError('PostgreSQL 19 release absent from official source directory')
    def order(version):
        if 'beta' in version:
            return (0, int(version.split('beta')[1]))
        if 'rc' in version:
            return (1, int(version.split('rc')[1]))
        return (2, int(version.split('.')[1]) if '.' in version else 0)
    return max(versions, key=order)

def main():
    issues = []
    def compare(label, expected, read):
        try:
            actual = read()
            if actual != expected:
                issues.append(f'{label}: pinned {expected}; upstream {actual}; review required')
            else:
                print(f'{label}: current ({actual})')
        except Exception as error:
            issues.append(f'{label}: verification unavailable ({type(error).__name__})')
    rust = tomllib.loads((ROOT / 'rust-toolchain.toml').read_text())['toolchain']['channel']
    compare('Rust stable', rust, lambda: tomllib.loads(fetch('https://static.rust-lang.org/dist/channel-rust-stable.toml').decode())['pkg']['rust']['version'].split()[0])
    for line in (ROOT / 'scripts/ci-tools.lock').read_text().splitlines():
        name, version, _digest = line.split()
        compare(name, version, lambda name=name: crate_version(json.loads(fetch(f'https://crates.io/api/v1/crates/{name}'))))
    metadata = json.loads((ROOT / 'docs/upstream-lock.json').read_text())
    for repo, version in metadata['github_releases'].items():
        compare(repo, version, lambda repo=repo: json.loads(fetch(f'https://api.github.com/repos/{repo}/releases/latest'))['tag_name'])
    compare('OpenBao SDK (planned adapter)', metadata['openbao_sdk'], lambda: crate_version(json.loads(fetch('https://crates.io/api/v1/crates/openbao'))))
    compare('PostgreSQL 19 release', metadata['postgres'], lambda: postgres_version(fetch('https://www.postgresql.org/ftp/source/').decode()))
    source = json.loads((ROOT / 'deploy/podman/postgres/source.lock.json').read_text())
    compare('PostgreSQL source checksum', source['sha256'], lambda: fetch(source['checksum_source']).decode().split()[0])
    base = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())['wolfi-base']['index']
    compare('Wolfi base index', base.split('@')[1], lambda: run_bounded('skopeo', 'inspect', '--no-tags',
        '--format', '{{.Digest}}', 'docker://cgr.dev/chainguard/wolfi-base:latest').stdout.strip())
    probe = json.loads((ROOT / 'deploy/podman/probe/image.lock.json').read_text())['probe-base']['index']
    compare('Wolfi static probe index', probe.split('@')[1], lambda: run_bounded('skopeo', 'inspect', '--no-tags',
        '--format', '{{.Digest}}', 'docker://cgr.dev/chainguard/static:latest').stdout.strip())
    valkey = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())['valkey']['index']
    compare('Wolfi Valkey index', valkey.split('@')[1], lambda: run_bounded('skopeo', 'inspect', '--no-tags',
        '--format', '{{.Digest}}', 'docker://cgr.dev/chainguard/valkey:latest').stdout.strip())
    for repo, version in metadata.get('optional_github_releases', {}).items():
        compare(repo + ' (optional, not admitted)', version, lambda repo=repo: json.loads(fetch(f'https://api.github.com/repos/{repo}/releases/latest'))['tag_name'])
    workspace = json.loads(__import__('subprocess').check_output(['cargo', 'metadata', '--locked', '--offline', '--format-version', '1'], cwd=ROOT))
    for package in workspace['packages']:
        if package['source'] is not None:
            compare(package['name'], package['version'], lambda name=package['name']: crate_version(json.loads(fetch(f'https://crates.io/api/v1/crates/{name}'))))
    if issues:
        raise SystemExit('\n'.join(issues))

if __name__ == '__main__':
    main()
