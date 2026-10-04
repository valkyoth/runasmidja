"""Serialized per-service publication of image- and content-bound evidence."""
import hashlib
import json
import os
import re
import stat
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import NamedTuple
from custody import MAX_AUDIT, read_owned_regular_bounded, replace_private, sync_parent
from openbao_lock import artifact_lock, custody

MAX_SERVICE_SNAPSHOTS = 32
MAX_SERVICE_EVIDENCE = 128 * 1024 * 1024


def reserve_snapshot(root, service, incoming):
    """Caller holds the service lock; include interrupted publication files."""
    pattern = re.compile(re.escape(service) +
                         r'-[0-9a-f]{64}-[0-9a-f]{64}\.(?:cdx|qualification)\.json(?:\.next)?')
    count = total = 0
    with os.scandir(root) as entries:
        for entry in entries:
            if not pattern.fullmatch(entry.name):
                continue
            info = entry.stat(follow_symlinks=False)
            custody(info)
            count += 1
            total += info.st_size
    if (count >= MAX_SERVICE_SNAPSHOTS or total > MAX_SERVICE_EVIDENCE or
            incoming > MAX_SERVICE_EVIDENCE - total):
        raise RuntimeError('Evidence retention budget exhausted; reviewed pruning required')


def checked_export_target(root, snapshot, target):
    destination = target.parent.resolve(strict=True) / target.name
    if destination.is_relative_to(root.resolve(strict=True)):
        raise RuntimeError('Public evidence destination must be outside private evidence custody')
    if destination.exists() or destination.is_symlink():
        info = destination.lstat()
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid():
            raise RuntimeError('Public evidence destination has invalid custody')
        if os.path.samestat(info, snapshot.lstat()):
            raise RuntimeError('Public destination aliases the source snapshot')
    return destination


class ScanResult(NamedTuple):
    clean: bool
    blocking: int
    snapshot: Path


def service_name(service):
    if not isinstance(service, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', service):
        raise ValueError('Invalid evidence service name')


class Evidence:
    def __init__(self, root, service, image):
        self.root, self.service, self.image = root, service, image
        self.active = True
        self.key = hashlib.sha256(image.encode()).hexdigest()

    def check(self, record, kind):
        if not self.active:
            raise RuntimeError('Evidence transaction has ended')
        if kind == 'cdx':
            if (record.get('bomFormat') != 'CycloneDX' or not record.get('components') or
                    record.get('metadata', {}).get('component', {}).get('name') !=
                    f'runasmidja/{self.service}@{self.image}'):
                raise RuntimeError('SBOM is not bound to the expected image')
        elif kind == 'qualification':
            if record.get('image') != self.image:
                raise RuntimeError('Qualification is not bound to the expected image')
        else:
            raise ValueError('Unknown evidence kind')

    def publish(self, record, kind='cdx'):
        self.check(record, kind)
        content = json.dumps(record, indent=2) + '\n'
        digest = hashlib.sha256(content.encode()).hexdigest()
        target = self.root / f'{self.service}-{self.key}-{digest}.{kind}.json'
        # Reuse identical evidence without replacing its inode. Interrupted .next
        # publication is repaired only while holding the service writer lock.
        if target.exists() or target.is_symlink():
            if read_owned_regular_bounded(target, MAX_AUDIT, durable=True) != content:
                raise RuntimeError('Immutable evidence content changed')
            sync_parent(target)
        else:
            reserve_snapshot(self.root, self.service, len(content.encode('utf-8')))
            replace_private(target, content, limit=MAX_AUDIT)
        return target

    def read(self, snapshot, kind='cdx'):
        snapshot = Path(snapshot)
        if (not self.active or kind not in ('cdx', 'qualification') or snapshot.parent != self.root or
                not re.fullmatch(re.escape(f'{self.service}-{self.key}-') + r'[0-9a-f]{64}\.' + kind + r'\.json', snapshot.name)):
            raise RuntimeError('Evidence path/transaction rejected')
        content = read_owned_regular_bounded(snapshot, MAX_AUDIT, durable=True)
        digest = hashlib.sha256(content.encode()).hexdigest()
        expected = self.root / f'{self.service}-{self.key}-{digest}.{kind}.json'
        if snapshot != expected:
            raise RuntimeError('Evidence path/content identity mismatch')
        record = json.loads(content)
        self.check(record, kind)
        sync_parent(snapshot)
        return record


@contextmanager
def evidence_transaction(root, service, image):
    service_name(service)
    if not isinstance(image, str) or not image or len(image) > 2048:
        raise ValueError('Invalid evidence image identity')
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        custody(os.fstat(descriptor), directory=True)
    finally:
        os.close(descriptor)
    with artifact_lock(root / '.locks' / service, exclusive=True):
        transaction = Evidence(root, service, image)
        try:
            yield transaction
        finally:
            transaction.active = False


def copy_sbom(root, service, image, snapshot, target):
    """Export only the explicitly selected immutable scan, under the same lock."""
    with evidence_transaction(root, service, image) as transaction:
        report = transaction.read(snapshot)
        target = checked_export_target(root, Path(snapshot), Path(target))
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=target.parent,
                                             prefix='.evidence-', delete=False) as output:
                temporary = Path(output.name)
                output.write(json.dumps(report, indent=2) + '\n')
                output.flush(); os.fchmod(output.fileno(), 0o644); os.fsync(output.fileno())
            os.replace(temporary, target); sync_parent(target)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
