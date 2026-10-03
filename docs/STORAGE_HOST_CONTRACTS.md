# Storage and Host Security Contracts

Status: required design; no product repository, artifact backend, public API or
isolated worker is implemented. See [versioned owners](gap-reconciliation-2026-10-03.md)
and [strict gates](VERIFICATION_GATES.md).

## Metadata, artifacts and publication

Repository commands own atomic recipe revisions, grant changes, optimistic
conflicts, idempotency, deterministic pagination and authoritative job leases/
fencing. Freeze checked numeric/null/boolean/ordering/case/collation/timestamp
semantics. PostgreSQL-specific SQL/JSON/RLS/indexes remain adapter optimizations,
not the only authorization source. Recipes can contain payload literals/secrets:
serialization must inspect sensitivity/size, even when storing recipe metadata.
Bulk input/output belongs to artifact storage, never incidental SQL blobs.

Version ownership: v0.106.0 defines the minimal monotonic per-run fencing/
expiry/revocation/CAS contract; v0.107.0 implements and tests atomic committed
acquisition/reassignment/completion on real PostgreSQL. v0.112.0 consumes that
qualified primitive with v0.111.0 current authorization for hosted SQL publication.
v0.124.0 adds heartbeat/renewal/reclaim/retry/idempotency lifecycle and reruns the
earlier fencing regressions; it does not first introduce fencing.

Artifact ports own immutable IDs/revisions, bounded sequential/range reads,
staged writes, quota reservation, completion/abort, integrity, leases and retention.
Handles are scoped opaque capabilities rather than paths/public content hashes.
Backends qualify traversal/symlinks, durable completion, physical quotas and
confidential staging policy. Nonseekable replay uses bounded explicit spooling;
full seekable/whole-input qualification follows actual native/browser artifacts.

SQL and object storage do not share an ordinary atomic transaction. Reserve
quota/staging under a lease, write/verify and durably finish the immutable object,
then transactionally recheck current authorization/fencing and commit manifest,
run transition and outbox. Only committed authorized manifests expose bytes.
Finalized unreferenced objects remain inaccessible. Reconcile stages/orphans
idempotently after a grace interval; stale indexes cannot delete live objects.
Crash each boundary plus duplicate/failed commit, corrupt bytes, disk full,
expired lease and revoked reader. Read actual bytes to verify hashes.
v0.80.0 crash/transaction tests concern local native manifests and browser
IndexedDB/OPFS/local events only. The SQL run/manifest/outbox sequence above
belongs to v0.112.0 and cannot be claimed from those local tests.

## Database migration and recovery

Freeze the logical schema/authorization/artifact/lease contract before drills.
Begin with a maintenance window, quiesce/fence active jobs and reconcile leases.
Do not claim zero downtime or uncontrolled dual writes. The actual PostgreSQL
and MySQL suites must agree on:

- Entity key sets and canonical entity digests, including IDs/revisions/grants,
  lossless numbers/nulls/order and timestamp precision.
- Artifact size/hash sets, verified by reading bytes, with zero missing or
  duplicate IDs, unexpected records or broken references.
- Authorization decisions, revision/conflict/lease/idempotency outcomes and
  representative restored recipe results.

Use two tenants, revoked/inherited grants, Unicode/case collisions, maximum
offsets, empty/null distinctions, concurrent edits, outbox/tombstones, interrupted
uploads and completed artifacts. Corrupt/truncated/duplicate/partial exports and
target constraints cannot activate a failed import. Rehearse both directions,
coordinated backup restore, replay and rollback. Preserve post-cutover writes by
an explicit freeze/reverse-migration procedure; reverting to a stale snapshot
is not lossless rollback. MySQL remains a proof adapter until separately qualified
for production support. Production PostgreSQL requires reviewed 19 GA.

## Portable seams and real replacement

Business authority, upload/egress policy, quotas and idempotency stay in owned
application commands; framework middleware cannot be their only implementation.
HTTP/browser/native adapters call those use cases. SQL rows, SDK DTOs, framework
requests, Tokio handles, TLS streams and UI signals stay outside domain contracts.
Do not impose native Send/Sync/boxing on fixed-buffer portable operations.

Separate inbound HTTP, outbound egress, native TLS, database negotiation/TLS,
inert HTML and browser-owned Fetch/HTTPS. A second runnable adapter qualifies
host framing/backpressure/disconnect/origin/CSRF/proxy/error behavior; mocks
verify units but never prove replacement. Database TLS tests use real backend
negotiation/channel binding with wrong-name/root/expiry/downgrade negatives.
SDK transports must be inventoried for trust, redirects and deadlines; a SecretRef
wrapper alone does not prove transport substitution. Use real current hooks or
a separately qualified replacement before claiming Vef/Brynja integration.
Default builds require no sibling paths; sibling availability cannot be fabricated.

## Public execution and sandbox

Early API rows are schema/loopback/private integration, never permission to expose
untrusted jobs. Public endpoints remain disabled until identity/object authority,
isolated workers, admission/quota, publication fencing, egress/TLS and recovery
pass together at the server security gate. The development health probe is
disposable: inactivity timeouts are not aggregate request deadlines and a serial
slow client can monopolize it. Production HTTP needs independent framing/body/
aggregate deadline/disconnect tests; do not extend the probe into that claim.

Use a worker security context separate from the control plane. Verify delegated
kernel memory/CPU-rate/PID/FD/scratch quotas, nonroot/no-new-privileges/capability
drop, read-only root, seccomp/applicable MAC/namespaces and bounded IPC. CPU rate
throttling is distinct from cumulative CPU/wall deadline. No home, container
socket, service credentials, unrelated mounts or privileged inherited descriptors.
Default worker networking is absent; granted requests go through an egress broker.

An external supervisor kills the full child tree/cgroup, handles OOM/crash and
fences publication/cleanup. Test CPU spin, OOM, fork/PID/FD/temp exhaustion,
forbidden syscalls/mounts/egress, hostile IPC and surviving descendants. Kernel
control failure rejects the profile. If the threat model requires stronger kernel
separation, qualify a stronger boundary rather than assume rootless implies safe.
Admission runs before expensive work and remains authoritative during cache,
network, storage or quota-service faults. Track fair tenant/global reservations.

## Native outbound destination policy

Use one qualified canonical URL parser with allowed schemes/ports; reject
userinfo, ambiguous numeric/scoped host forms and parser disagreement. The
policy resolver validates all A/AAAA and normalized mapped IPv6 addresses against
public/private/metadata/link-local/reserved policy. Connect only to approved
addresses, preserving original Host/SNI/name verification; validate actual peer.
Retries, pools, TTL refresh, alternative address choices and policy changes
revalidate rather than allowing hidden client re-resolution.

Disable automatic redirects; each approved hop has new destination validation,
finite hops/total deadline/bytes and credential stripping. Disable ambient proxies
and unreviewed Alt-Svc/coalescing routes; an intentional broker/proxy enforces
final destinations. Bound DNS, connection/retry count, headers, request/response
and decompressed bytes/time. Ambient sessions grant no network credentials;
signed URLs and auth headers are secret diagnostics. Network policy supplies an
independent private/metadata destination deny layer. Operator-approved private
network use is explicit and scoped separately from the public default.

Controlled DNS/HTTP/TLS fixtures test rebinding at connect, mixed answers, mapped
and link-local addresses, redirect loops/private hops, proxy variables, wrong
identity, credential forwarding, oversize compression and stale pooled policy.
Browser Fetch uses browser-owned resolver/CORS/trust and cannot promise native
raw-HTTP enforcement; explicit browser effects never silently choose remote mode.
