#!/usr/bin/env python3
"""Verify reviewed publishers and scan exact fixture images before execution."""
import hashlib
import json
import os
import platform
import stat
from pathlib import Path
from custody import MAX_AUDIT, replace_private
from process_limits import run_bounded
from advisory_review import BLOCKING_SEVERITIES, disposition
from sbom_privacy import public_sbom

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / '.local/image-evidence'


def tool(name):
    pin = json.loads((ROOT / 'scripts/image-tools.lock.json').read_text())[name]
    path = ROOT / '.local/tools' / name
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, 'rb') as source:
        info = os.fstat(source.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > 256 * 1024 * 1024:
            raise RuntimeError('Image tool is not a bounded regular file')
        digest = hashlib.file_digest(source, 'sha256').hexdigest()
    if digest != pin['binary_sha256']:
        raise RuntimeError('Image tool digest rejected; run scripts/install_image_tools.py')
    return str(path)


def provenance(service, image, policy, cosign):
    rule = policy[service]
    if policy.get('platform') != 'linux/amd64':
        raise RuntimeError('Image platform has no reviewed provenance policy')
    if service == 'openbao' and rule.get('method') == 'local-build' and rule.get('image') == 'local:openbao-wolfi':
        from openbao_image import validate_image, pins
        validate_image(image)
        lock = pins()
        upstream = {**policy, 'openbao': lock['upstream'], 'wolfi-base': lock['base']}
        provenance('openbao', lock['upstream']['image'], upstream, cosign)
        provenance('wolfi-base', lock['base']['image'], upstream, cosign)
        return 'local assembly (verified static upstream binary and signed Wolfi base)'
    if service == 'postgres' and rule.get('method') == 'local-build' and rule.get('image') == 'local:postgres-wolfi':
        from postgres_image import validate_image
        validate_image(image)
        provenance('wolfi-base', policy['wolfi-base']['image'], policy, cosign)
        return 'local-build (trusted host custody; verified base/source)'
    if rule.get('image') != image or policy.get('platform') != 'linux/amd64':
        raise RuntimeError('Image/platform has no reviewed provenance policy')
    if rule.get('method') == 'maintainer-exception':
        if service not in ('postgres', 'valkey') or not all(rule.get(key) for key in
                ('approved_by', 'approved_on', 'reason', 'scope')):
            raise RuntimeError('Unsigned image exception incomplete or out of scope')
        return 'maintainer-exception'
    if service not in ('openbao', 'wolfi-base', 'probe-base', 'valkey') or rule.get('method') != 'signed-index':
        raise RuntimeError('Unsupported image provenance policy')
    result = run_bounded(cosign, 'verify', '--certificate-identity', rule['identity'],
        '--certificate-oidc-issuer', rule['issuer'], rule['index'], timeout=180)
    index_digest = rule['index'].split('@', 1)[1]
    signatures = json.loads(result.stdout)
    if not signatures or any(item['critical']['image']['docker-manifest-digest'] != index_digest
                             for item in signatures):
        raise RuntimeError('Signature did not bind reviewed index digest')
    raw = run_bounded('skopeo', 'inspect', '--raw', 'docker://' + rule['index']).stdout
    if 'sha256:' + hashlib.sha256(raw.encode()).hexdigest() != index_digest:
        raise RuntimeError('Signed index bytes failed digest verification')
    selected = [item for item in json.loads(raw)['manifests']
                if item.get('platform', {}).get('os') == 'linux'
                and item.get('platform', {}).get('architecture') == 'amd64']
    if len(selected) != 1 or selected[0]['digest'] != image.split('@', 1)[1]:
        raise RuntimeError('Signed index does not authorize selected platform image')
    return 'signed-index'


def scan(service, image, scanner, archive=None, candidate_recipe=None, archive_check=None):
    target = EVIDENCE / (service + '.cdx.json')
    before = None
    if archive_check is not None:
        if archive is None or candidate_recipe is not None:
            raise ValueError('Ambiguous archive binding')
        before = archive_check()
    elif archive and candidate_recipe is not None:
        from postgres_image import candidate_receipt
        before = candidate_receipt(archive, image, candidate_recipe)
    # Never consume stale evidence after a failed scanner run or follow an output link.
    result = run_bounded(scanner, 'image', '--image-src', 'remote', '--platform', 'linux/amd64',
        '--cache-dir', str(ROOT / '.local/trivy'), '--scanners', 'vuln', '--format', 'cyclonedx',
        '--severity', BLOCKING_SEVERITIES, '--exit-code', '0', '--quiet', '--ignore-unfixed=false',
        '--config', '', '--ignorefile', '/dev/null', '--ignore-policy', '', '--ignore-status', '',
        '--vex', '', '--skip-db-update=false', '--disable-telemetry',
        *(['--input', str(archive)] if archive else [image]),
        allowed=(0,), timeout=900, output_limit=MAX_AUDIT,
        env={key: value for key, value in os.environ.items() if not key.startswith('TRIVY_')})
    evidence = json.loads(result.stdout)
    if evidence.get('bomFormat') != 'CycloneDX' or not evidence.get('components'):
        raise RuntimeError('Image SBOM is missing dependency inventory')
    if archive:
        if archive_check is not None:
            if archive_check() != before:
                raise RuntimeError('Archive changed during scan')
        elif before is not None:
            if candidate_receipt(archive, image, candidate_recipe) != before:
                raise RuntimeError('Candidate changed during scan')
        else:
            from postgres_image import validate_image
            validate_image(image, require_local=False)
    if archive and service == 'postgres':
        source = json.loads((ROOT / 'deploy/podman/postgres/source.lock.json').read_text())
        evidence['components'].append({'type': 'application', 'name': 'PostgreSQL',
            'version': source['version'], 'bom-ref': 'runasmidja-postgresql-source',
            'purl': 'pkg:generic/postgresql@' + source['version'],
            'licenses': [{'license': {'id': 'PostgreSQL'}}],
            'externalReferences': [{'type': 'distribution', 'url': source['url'],
                                    'hashes': [{'alg': 'SHA-256', 'content': source['sha256']}]}]})
    public_sbom(evidence, service, image, ROOT)
    reviews = json.loads((ROOT / 'deploy/podman/advisory-reviews.json').read_text())
    from advisory_evidence import verified_reviews
    reviews = verified_reviews(reviews, ROOT)
    components = {item.get('bom-ref'): (item.get('name'), item.get('version')) for item in evidence['components']}
    findings = evidence.get('vulnerabilities', [])
    statuses = [disposition(item, image, reviews, components) for item in findings]
    reviewed = statuses.count('reviewed_not_affected')
    if reviewed:
        evidence.setdefault('metadata', {}).setdefault('properties', []).append(
            {'name': 'runasmidja:unknown-not-affected-reviews', 'value': str(reviewed)})
    replace_private(target, json.dumps(evidence, indent=2) + '\n', limit=MAX_AUDIT)
    clean = 'blocked' not in statuses
    return clean, statuses.count('blocked')


def verify_images(images):
    if platform.system() != 'Linux' or platform.machine() not in ('x86_64', 'amd64'):
        raise RuntimeError('Fixture image qualification is limited to Linux/amd64')
    if set(images) != {'openbao', 'postgres', 'valkey'}:
        raise RuntimeError('Fixture image set differs from reviewed policy')
    policy = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())
    from valkey_image import admission_policy
    policy = admission_policy(images, policy)
    from openbao_image import admission_policy as bao_policy
    policy = bao_policy(images, policy)
    EVIDENCE.mkdir(parents=True, mode=0o700, exist_ok=True)
    scanner, cosign = tool('trivy'), tool('cosign')
    blocked = []
    for service, image in images.items():
        method = provenance(service, image, policy, cosign)
        if service == 'openbao' and policy[service].get('method') == 'local-build':
            from openbao_image import artifact, binding
            with artifact(image) as (_, archive):
                clean, count = scan(service, image, scanner, archive=archive,
                                    archive_check=lambda: binding(archive, image))
        elif policy[service].get('method') == 'local-build':
            from postgres_image import validate_image
            clean, count = scan(service, image, scanner, archive=validate_image(image))
        else:
            clean, count = scan(service, image, scanner)
        print(f'{service}: {method}; exact-image SBOM; {count} blocking UNKNOWN/HIGH/CRITICAL findings', flush=True)
        if not clean:
            blocked.append(service)
    if blocked:
        raise RuntimeError('Image vulnerability gate rejected: ' + ', '.join(blocked))


if __name__ == '__main__':
    try:
        from postgres_image import fixture_images
        verify_images(fixture_images())
    except (RuntimeError, ValueError, KeyError, OSError) as error:
        raise SystemExit(f'Image gate failed ({type(error).__name__}); no execution authorized') from None
