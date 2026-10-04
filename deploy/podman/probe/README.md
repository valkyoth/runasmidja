# Wolfi static probe — v0.2.1 candidate

`python3 scripts/qualify_probe_wolfi.py` verifies the pinned public base,
compiles the locked Rust 1.99.0 static musl probe, assembles a COPY-only image,
scans/binds its archive, checks the copied executable and runs health/denial
checks in a restricted owned rootless container. It uses a private temporary
context with only the executable and recipe; no secrets or package installation.
Native and scratch tests remain `python3 scripts/smoke_probe.py` and
`python3 scripts/smoke_probe.py --container`. All container work is local.

The [static starter](https://images.chainguard.dev/directory/image/static/overview)
is Wolfi-based, unlike paid Chainguard OS images. Its signed index and selected
Linux/amd64 digest are in `image.lock.json`; qualification copies `/etc/os-release`
and requires `ID=wolfi`. The reviewed inventory contains Wolfi baselayout, CA
certificates and timezone data, without a shell, package manager or libc.
Our executable is fully static; no musl/glibc ABI mixing is introduced.

Base package license identifiers are retained in the public
[image inventories](../../../sbom/images/README.md); project code is EUPL-1.2.
The independently generated Cargo inventory/audit covers first-party Rust.
The application component's executable hash is appended to the container SBOM;
Trivy does not independently inventory the internals of a stripped Rust binary.
No upstream publisher signature is claimed for our locally assembled image.

Temporary containers and archive contexts are removed; image store content may
remain for inspection. No service volumes/networks or existing fixture containers
are replaced. Reverting to native/scratch needs no migration: run the retained
commands above. The new profile is optional and changes no default deployment.
No container registry publication is performed. The serial development HTTP
probe and inherited network behavior are not a production API or worker sandbox.
See [scope](../../../docs/releases/v0.2.1-scope.md) for limits and pending pentest.

License inventory at admission: Wolfi baselayout MIT; CA certificate bundle
MPL-2.0/MIT; timezone data CC-PDDC; Runasmidja EUPL-1.2. These remain separate
licenses, not relicensed by the project. The retained source/package purls and
scanner license fields accompany any later distribution review.
