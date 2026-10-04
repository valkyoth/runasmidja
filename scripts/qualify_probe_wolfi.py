#!/usr/bin/env python3
"""Local-only Wolfi build, admission and actual health-probe qualification."""
import tempfile
import uuid
from pathlib import Path
from image_gate import ROOT
from process_limits import run_bounded
from podman_guard import require_rootless
from probe_image import build, evidence
from probe_runtime import qualify


def main():
    require_rootless(run_bounded)
    state = ROOT / '.local/probe-wolfi'
    state.mkdir(parents=True, mode=0o700, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='candidate-', dir=state) as folder:
        work = Path(folder)
        image, binary, archive = build(work)
        qualify(image, binary, work, str(uuid.uuid4()))
        evidence(image, binary, archive)
    print('Wolfi exact-image/executable, nonroot/resource limits and health/denied routes: PASS')


if __name__ == '__main__':
    main()
