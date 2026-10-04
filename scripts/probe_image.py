"""Verified public Wolfi assembly for the existing static development probe."""
import json
import os
import shutil
from pathlib import Path
from image_gate import ROOT, EVIDENCE, provenance, scan, tool
from image_archive import verify as verify_archive
from postgres_image import bounded_hash
from process_limits import run_bounded
from podman_guard import podman, require_rootless
from stream_archive import save_bounded_archive
from podman_guard import archive as guarded_archive
from image_evidence import evidence_transaction

RECIPE = ROOT / 'deploy/podman/probe'
BINARY = ROOT / 'target/x86_64-unknown-linux-musl/release/runasmidja-server'
MAX_BINARY = 16 * 1024 * 1024


def archive_binding(path, image):
    verify_archive(path, image)
    return bounded_hash(path, 512 * 1024 * 1024)


def build(state):
    require_rootless(run_bounded)
    policy = json.loads((RECIPE / 'image.lock.json').read_text())
    base = policy['probe-base']['image']
    containerfile = (RECIPE / 'Containerfile').read_text()
    if containerfile.splitlines()[1] != 'FROM ' + base:
        raise RuntimeError('Probe base differs from reviewed policy')
    EVIDENCE.mkdir(parents=True, mode=0o700, exist_ok=True)
    provenance('probe-base', base, policy, tool('cosign'))
    scanner = tool('trivy')
    if not scan('probe-base', base, scanner)[0]:
        raise RuntimeError('Probe base vulnerability gate rejected')
    run_bounded('cargo', 'build', '--locked', '-p', 'runasmidja-server', '--release',
                '--target', 'x86_64-unknown-linux-musl', timeout=180)
    digest = bounded_hash(BINARY, MAX_BINARY)
    context = state / 'context'; context.mkdir(mode=0o700)
    shutil.copyfile(BINARY, context / 'runasmidja-server')
    os.chmod(context / 'runasmidja-server', 0o755)
    (context / 'Containerfile').write_text(containerfile)
    if bounded_hash(context / 'runasmidja-server', MAX_BINARY) != digest:
        raise RuntimeError('Probe executable changed during context preparation')
    # Public verified base only. No build execution: this recipe consists of COPY/config.
    podman(run_bounded, 'pull', '--platform', 'linux/amd64', base)
    podman(run_bounded, 'build', '--network', 'none', '--pull=never', '--layers=false',
        '--inherit-labels=false', '--inherit-annotations=false', '--http-proxy=false',
        '--platform', 'linux/amd64', '--iidfile', str(state / 'image.id'),
        '-f', str(context / 'Containerfile'), str(context), timeout=180)
    image = (state / 'image.id').read_text().strip()
    archive = state / 'image.tar'
    guarded_archive(run_bounded, save_bounded_archive, image, archive)
    binding = archive_binding(archive, image)
    component = {'type': 'application', 'name': 'runasmidja-server',
        'version': '0.2.3', 'bom-ref': 'runasmidja-static-probe',
        'hashes': [{'alg': 'SHA-256', 'content': digest}],
        'licenses': [{'license': {'id': 'EUPL-1.2'}}],
        'properties': [{'name': 'runasmidja:inventory-origin',
                        'value': 'first-party build; Cargo SBOM and audit qualify Rust dependencies'}]}
    if not scan('probe', image, scanner, archive=archive,
                archive_check=lambda: archive_binding(archive, image), component=component)[0]:
        raise RuntimeError('Probe image vulnerability gate rejected')
    if archive_binding(archive, image) != binding:
        raise RuntimeError('Probe archive changed after scan')
    return image, digest, binding


def evidence(image, binary, archive):
    """Write nonsecret evidence only after the caller completes actual qualification."""
    from check_release import source_digest
    record = {'schema': 1, 'profile': 'linux/amd64 Wolfi development probe',
        'image': image, 'binary_sha256': binary, 'archive_sha256': archive,
        'source_sha256': source_digest(), 'version': '0.2.3',
        'trust': 'local build/test custody; not distributed publisher signing'}
    with evidence_transaction(EVIDENCE, 'probe', image) as transaction:
        return transaction.publish(record, kind='qualification')
