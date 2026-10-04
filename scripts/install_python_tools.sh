#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m venv .local/check-tools
.local/check-tools/bin/python3 -m pip --isolated install --disable-pip-version-check \
  --no-cache-dir --require-hashes --only-binary=:all: --no-deps --index-url https://pypi.org/simple \
  -r scripts/python-tools.lock
.local/check-tools/bin/python3 -c 'import yaml; print("Workflow parser:", yaml.__version__)'
