# Image evidence custody

Each service has its own exclusive evidence lock. Scanner execution, archive
binding, finding evaluation and publication form one transaction. Different
services may run concurrently. When an artifact cache lock is needed, acquire
it **before** the evidence lock; evidence code must not acquire artifact locks.

Completed scans return `ScanResult(clean, blocking, snapshot)` and print the
snapshot filename. Blocking vulnerability findings still retain their inventory;
operational failures return no successful result. A snapshot is named:

`SERVICE-IMAGE_SHA256-CONTENT_SHA256.cdx.json`

The first hash covers the complete immutable image reference; the second covers
the serialized report. Different images and different reports cannot overwrite
one another. Repeated identical evidence is checked and resynced before reuse.
Snapshots are immutable by cooperating tooling under trusted local-host custody;
a hostile same-user process is outside this boundary. Content hashes detect
subsequent modification. Snapshot retention is local, not distributed attestation.

Probe first-party inventory is included in the scan transaction, not appended to
a shared output afterward. Reference collisions are rejected. Probe qualification
records use the same lock and image/content-keyed `.qualification.json` files.

## Export the exact snapshot

Use the exact image and snapshot printed by the qualifying command. Replace the
uppercase placeholders below; do not select a report merely by service name:

```sh
python3 scripts/export_image_evidence.py SERVICE IMAGE .local/image-evidence/PRINTED_SNAPSHOT sbom/images/SERVICE.cdx.json
```

Export takes the service lock and validates the snapshot's image, filename,
content hash, regular-file type, ownership and private permissions. It writes
the public destination atomically using a unique temporary file. A mismatched
image, modified snapshot or unkeyed legacy file is rejected rather than relabeled.
Public Git destinations may already be readable; source custody stays private.

Old fixed-name files such as `.local/image-evidence/openbao.cdx.json` and
`probe-qualification.json` are historical, no longer updated, and must not be used
for current release evidence. They are not accepted by the export helper. Public
`sbom/images/SERVICE.cdx.json` names remain stable after explicit verified export.

OpenBao `validate_image()` validates only and returns no archive path. Use its
`artifact()` context manager whenever archive bytes are consumed; it holds the
shared artifact lock through scanning. Evidence snapshots are separate immutable
files and may be referred to after their publication transaction ends.
