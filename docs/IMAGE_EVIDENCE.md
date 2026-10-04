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

## Retention budget and maintenance

Each service may retain at most 32 keyed files and 128 MiB in total. SBOM and
qualification snapshots share that budget across all images. Interrupted `.next`
publications count too, so repeated failed writes cannot escape the limit. The
existing 16 MiB single-file cap remains. New publication checks regular-file
custody, current ownership, private permissions and single links while holding
the service lock. Exceeding either budget fails closed with “reviewed pruning
required”; it never silently discards evidence. Identical completed snapshots
can still be verified/reused without consuming another slot.

When the limit is reached, stop starting scans, builds, fixture operations and
exports, and wait for all existing callers to finish. Review which exact reports
are still referenced by release/advisory records or pending retests. Export and
retain those records first, then manually remove only reviewed obsolete keyed
snapshots or abandoned `.next` files. Never delete `.locks` or a lock inode.
Resume operations only after maintenance finishes. There is no automatic pruning
or lease system: quiescence protects paths returned to earlier callers. Historical
unkeyed reports are outside this budget and are no longer produced; review their
retention separately. The budget covers managed evidence per service, not the
whole workspace or hostile same-user writes. One bounded scanner report may be
in memory during admission; publication does not start when the budget is full.

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
The resolved destination parent must be outside the private evidence tree. Source
and other snapshot destinations, new private-tree paths, symlink-parent aliases,
leaf symlinks and hard links to the source are rejected before writing. A trusted
maintainer must not concurrently rearrange destination directories during export;
this is protection from accidental misuse, not a hostile same-user sandbox.

Old fixed-name files such as `.local/image-evidence/openbao.cdx.json` and
`probe-qualification.json` are historical, no longer updated, and must not be used
for current release evidence. They are not accepted by the export helper. Public
`sbom/images/SERVICE.cdx.json` names remain stable after explicit verified export.

OpenBao `validate_image()` validates only and returns no archive path. Use its
`artifact()` context manager whenever archive bytes are consumed; it holds the
shared artifact lock through scanning. Evidence snapshots are separate immutable
files and may be referred to after their publication transaction ends.
