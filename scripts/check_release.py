#!/usr/bin/env python3
"""Reject missing or fabricated readiness; bind assessment to exact source."""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = {'.git', '.local', 'target', '__pycache__', '.cargo-deny-advisory-dbs',
    '.agents', '.codex', 'AGENTS.md', 'AGENTS.override.md', 'README.internal.md'}

def source_digest(root=ROOT):
    digest = hashlib.sha256()
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if not path.is_file() or any(part in EXCLUDED for part in rel.parts):
            continue
        if rel.parts[:2] == ('security', 'pentest') or path.name == 'PENTEST.md':
            continue
        data = path.read_bytes()
        name = rel.as_posix().encode()
        digest.update(len(name).to_bytes(8, 'big') + name + len(data).to_bytes(8, 'big') + data)
    return digest.hexdigest()

def validate_report(content):
    errors = []
    if not re.search(r'^Status: PASS$', content, re.MULTILINE):
        errors.append('assessment must explicitly be PASS')
    for heading in ('Findings', 'Commands', 'Results', 'Remediation', 'Retest', 'Limitations'):
        if not re.search(r'^## ' + heading + r'\n\n\S', content, re.MULTILINE):
            errors.append('missing nonempty report section: ' + heading)
    for field in ('Reviewed commit', 'Source SHA256'):
        length = 40 if field == 'Reviewed commit' else 64
        if not re.search('^' + field + r': [0-9a-f]{' + str(length) + '}$', content, re.MULTILINE):
            errors.append('missing exact ' + field)
    if re.search(r'^Unresolved (?:critical|high): (?!0$)', content, re.MULTILINE):
        errors.append('unresolved critical/high finding')
    for severity in ('critical', 'high'):
        if f'Unresolved {severity}: 0' not in content:
            errors.append('missing zero unresolved ' + severity + ' finding count')
    return errors

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def main(version):
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-rc\.\d+)?', version):
        raise SystemExit('invalid version')
    report_path = ROOT / f'security/pentest/v{version}.md'
    if not report_path.exists():
        raise SystemExit('release blocked: pentest report missing (NOT RUN)')
    content = report_path.read_text()
    errors = validate_report(content)
    if errors:
        raise SystemExit('release blocked: ' + '; '.join(errors))
    reviewed = re.search(r'^Reviewed commit: (.+)$', content, re.MULTILINE)[1]
    digest = re.search(r'^Source SHA256: (.+)$', content, re.MULTILINE)[1]
    if git('status', '--porcelain'):
        raise SystemExit('release blocked: uncommitted source')
    if git('rev-parse', 'HEAD^') != reviewed:
        raise SystemExit('release blocked: report must be direct child of reviewed commit')
    changes = git('diff', '--name-only', reviewed, 'HEAD').splitlines()
    if changes != [f'security/pentest/v{version}.md']:
        raise SystemExit('release blocked: report commit changed reviewed source')
    if source_digest() != digest:
        raise SystemExit('release blocked: source digest differs from assessment')
    if not (ROOT / f'release-notes/v{version}.md').exists() or not list((ROOT / 'sbom').glob('*.json')):
        raise SystemExit('release blocked: release notes or SBOM missing')
    if (ROOT / 'PENTEST.md').exists():
        raise SystemExit('release blocked: private pentest scratch remains')
    print('Local source/report readiness: PASS; review GitHub checks and signing separately')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: check_release.py X.Y.Z')
    main(sys.argv[1])
