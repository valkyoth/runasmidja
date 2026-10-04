"""Bind each narrowly scoped advisory review to its retained evidence bytes."""
import hashlib
import json
import re


def verified_reviews(reviews, root):
    accepted = []
    for review in reviews:
        name = review.get('evidence', '')
        if not re.fullmatch(r'security/advisories/[a-zA-Z0-9_.-]+\.json', name):
            continue
        path = root / name
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 65536:
            continue
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != review.get('evidence_sha256'):
            continue
        data = json.loads(raw)
        if data.get('image') != review.get('image') or data.get('id') != review.get('id'):
            continue
        if data.get('analysis') != 'affected packages absent from complete binary symbol inventory':
            continue
        if not re.fullmatch(r'[0-9a-f]{64}', data.get('binary_sha256', '')) or not data.get('symbol_count'):
            continue
        if not data.get('affected_packages') or data.get('affected_package_symbols') != 0:
            continue
        accepted.append(review)
    return accepted
