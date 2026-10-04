#!/usr/bin/env python3
"""Read live repository policy; never mutate settings or request credentials in CI."""
import json
import subprocess

ENDPOINT = 'repos/valkyoth/runasmidja/actions/permissions'


def validate(data):
    if not isinstance(data, dict) or data.get('enabled') is not True:
        raise ValueError('GitHub Actions must be explicitly enabled')
    if data.get('sha_pinning_required') is not True:
        raise ValueError('GitHub platform full-SHA action enforcement is missing or disabled')
    if data.get('allowed_actions') not in ('all', 'local_only', 'selected'):
        raise ValueError('GitHub allowed-actions policy is missing or unknown')


def check():
    result = subprocess.run(['gh', 'api', '--hostname', 'github.com', ENDPOINT],
                            capture_output=True, text=True, timeout=30, check=True)
    validate(json.loads(result.stdout))
    print('Live GitHub action SHA-pinning policy: PASS')


if __name__ == '__main__':
    check()
