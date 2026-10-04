"""Only exact, unexpired not-affected UNKNOWN reviews may satisfy admission."""
from datetime import date, datetime, timezone

BLOCKING_SEVERITIES = 'UNKNOWN,HIGH,CRITICAL'


def disposition(finding, image, reviews, components, *, today=None):
    severities = {rating.get('severity', 'unknown').lower() for rating in finding.get('ratings', [])}
    if not severities:
        severities = {'unknown'}
    if severities & {'high', 'critical'}:
        return 'blocked'
    if severities - {'unknown', 'low', 'medium', 'info', 'none'}:
        return 'blocked'
    if 'unknown' not in severities:
        return 'nonblocking'
    today = today or datetime.now(timezone.utc).date()
    for review in reviews:
        if review.get('id') != finding.get('id') or review.get('image') != image:
            continue
        try:
            first, last = date.fromisoformat(review['reviewed_on']), date.fromisoformat(review['expires_on'])
        except (ValueError, KeyError, TypeError):
            continue
        if not first <= today < last or not 0 < (last - first).days <= 30:
            continue
        if review.get('status') != 'not_affected' or not review.get('reason') or not review.get('evidence_sha256'):
            continue
        affected = finding.get('affects', [])
        if affected and all(components.get(item.get('ref')) ==
                (review.get('module'), review.get('version')) for item in affected):
            return 'reviewed_not_affected'
    return 'blocked'
