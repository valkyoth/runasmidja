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

The production exporter accepts only `openbao`, `postgres`, `probe`, `probe-base`,
`valkey` and `wolfi-base`, each at `sbom/images/SERVICE.cdx.json` in this repository.
The destination's resolved parent must match that canonical location. Unknown
services, cross-service names and arbitrary public paths fail before publication.
Repository checks independently require all six files and verify their internal
service identity plus a nonempty image reference, catching manual swaps as well.
Historical inventories keep their existing filenames and are not export targets.
The lower-level `copy_sbom` helper remains a general identity-checked copy utility;
canonical publication must use the production CLI. These checks bind service
identity, not acceptance of a newer image or authorization to release it.

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


## Repository inventory validation

All public JSON is read once through a no-follow, nonblocking descriptor. It must
be a regular single-link file no larger than 16 MiB; reads also enforce the limit
after `fstat` to reject growth. Public Git-readable permissions are allowed.
Rejected symlinks, FIFOs, directories or oversized files are never reopened by
the privacy check. Invalid encoding, malformed/deeply nested JSON fail closed.

All `.cdx.json` files, including Cargo and historical inventories, must declare
CycloneDX and a supported `specVersion` (currently 1.5 and 1.7, matching the
reviewed producers), with a nonempty component list. Each component needs a
nonempty string name and type. New producer formats require a reviewed update.
This is a bounded minimum evidence profile, not full CycloneDX schema validation,
inventory completeness proof, signature verification or release authorization.

Canonical service bindings remain required. Historical OpenBao/Valkey names map
to their original services; the blocked official PostgreSQL report retains its
original `docker.io/library/postgres@sha256:` identity. These three filenames have
explicit bindings in the validator. Unknown image `.cdx.json` filenames fail
until reviewed into that mapping, so manual cross-service historical swaps cannot
silently become accepted evidence. Historical records remain historical; passing
these checks never admits a blocked image or makes an old scan current.


The selected repository root is the custody trust anchor. The checker opens it
as a no-follow directory and verifies current-user ownership and no group/world
write permissions. It then traverses `sbom`, `images` and any nested directories
using descriptor-relative no-follow opens, retaining each verified descriptor
through its children's reads. Symlinks anywhere in the inventory tree fail.
Directories must have the same ownership/write restrictions; public files also
require current-user ownership and no group/world writes. Modes 0755 for directories
and 0644 for files are accepted; shared-writable 0770/0777 or 0660/0666 are not.
Paths above the explicitly selected repository root remain trusted host setup.
Traversal is bounded to 32 nested inventory directories and does not change modes
or ownership automatically. An opened directory cannot be redirected by replacing
its pathname; this is point-in-time validation, not protection from a malicious
owner or a guarantee that a later consumer reads unchanged files.

JSON parsing rejects duplicate object keys at every nesting level, including
escaped spellings that decode to the same key. This applies to canonical,
historical and other public JSON alike; privacy, structure and service checks
all consume the same unambiguous parsed record.


Image service binding applies to `.cdx.json` files at every depth beneath
`sbom/images`, not only direct children. Nested directories do not create an
exception: any image inventory without an explicit reviewed relative-path binding
fails, including a canonical filename copied into a subdirectory.

Public JSON must be strictly UTF-8 encoded without a leading byte-order mark.
UTF-16/UTF-32, malformed UTF-8, `NaN`, `Infinity`, `-Infinity` and floating-point
exponents overflowing to infinity fail before structural/service checks. Duplicate
key rejection still applies at every level. Ordinary finite JSON numbers, Unicode
text and quoted strings such as `"Infinity"` remain supported. This is an accepted
input profile, not canonical serialization or an arbitrary-precision number API;
it does not establish signature or inventory completeness guarantees.
