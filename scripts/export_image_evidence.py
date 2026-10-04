#!/usr/bin/env python3
"""Copy an explicitly selected, identity-checked scan snapshot into public evidence."""
import argparse
from pathlib import Path
from image_gate import EVIDENCE, ROOT
from image_evidence import copy_sbom
from sbom_privacy import PUBLIC_SERVICES


def canonical_destination(service, requested):
    if service not in PUBLIC_SERVICES:
        raise ValueError('Service has no canonical public SBOM')
    expected = ROOT.resolve(strict=True) / 'sbom' / 'images' / f'{service}.cdx.json'
    actual = requested.parent.resolve(strict=True) / requested.name
    if actual != expected:
        raise RuntimeError(f'Destination must be the canonical {service} SBOM')
    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('service')
    parser.add_argument('image')
    parser.add_argument('snapshot', type=Path)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    destination = canonical_destination(args.service, args.destination)
    copy_sbom(EVIDENCE, args.service, args.image, args.snapshot.absolute(), destination)
    print('Exact-image/content SBOM export: PASS')


if __name__ == '__main__': main()
