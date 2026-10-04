#!/usr/bin/env python3
"""Copy an explicitly selected, identity-checked scan snapshot into public evidence."""
import argparse
from pathlib import Path
from image_gate import EVIDENCE
from image_evidence import copy_sbom


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('service')
    parser.add_argument('image')
    parser.add_argument('snapshot', type=Path)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    copy_sbom(EVIDENCE, args.service, args.image, args.snapshot.absolute(), args.destination)
    print('Exact-image/content SBOM export: PASS')


if __name__ == '__main__': main()
