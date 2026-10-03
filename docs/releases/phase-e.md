# Phase E: Remote API, PostgreSQL and secure server execution

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.103.0 — Public API specification

**Status:** planned.

**Setup:** baseline 0.102.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Public API specification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Stabilize pre-1.0 JSON envelopes, binary artifact routes, pagination, errors and capability negotiation. Current scope: private API schemas and the existing loopback transport, including lossless offsets/errors and bounded commands. Live session/object authority arrives in v0.110.0–v0.111.0, isolated-worker/supervisor proof in v0.119.0–v0.120.0, durable heartbeat/retry in v0.124.0 and egress in v0.125.0–v0.127.0. Those runtime suites remain pending, not schema-test PASS. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Local and HTTP transports pass shared use-case tests; framework request types never enter the application layer. Independent client contract tests exercise version/errors/offsets/capabilities/idempotency; schemas expose no framework/database/provider types. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.103.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.104.0 — Job lifecycle API

**Status:** planned.

**Setup:** baseline 0.103.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Job lifecycle API.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add queued/running/succeeded/failed/cancelled/expired states, progress events and resumable observation. Current scope: lifecycle messages and existing private loopback runs with local generation/cancellation tests; future lease/authorization cases are contract fixtures only. Minimal real SQL fencing is implemented in v0.107.0; deployed object authority qualifies in v0.110.0–v0.111.0, worker supervision in v0.119.0–v0.120.0, durable heartbeat/retry in v0.124.0 and egress in v0.125.0–v0.127.0 before v0.133.0 exposure. Do not claim durable or isolated execution here. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Reconnection and duplicated requests cannot create ambiguous terminal states or leak another principal’s job. Current private loopback lifecycle/contract fixtures cover create/poll/cancel/result terminal states, replay, local generations and disconnect races. Future lease/authority scenarios are schema/contract evidence only; live SQL fencing, sessions, isolated supervisors, heartbeat/retry and egress remain pending at their named owners and must qualify before public exposure. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.104.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.105.0 — Artifact transfer API

**Status:** planned.

**Setup:** baseline 0.104.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Artifact transfer API.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded uploads, integrity checks, range downloads, retention and explicit remote-consent UX. Current scope: bounded private upload/range/checksum/abort behavior on existing local artifact ports with local capability/generation tests. Hosted SQL publication/fencing waits for v0.112.0; live session/object authority for v0.110.0–v0.111.0; worker/supervisor and egress suites for v0.119.0–v0.120.0 and v0.125.0–v0.127.0. Contract fixtures do not qualify absent runtime controls. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Incomplete uploads remain staged; large files do not travel as JSON Base64 payloads by default. Private local upload/download/range/checksum/abort and existing local capability/generation negatives pass; oversized/traversal/partial artifacts stay unreadable. Hosted SQL publication, deployed object authority and worker/egress faults are pending at their named owners; these early tests cannot attest those absent runtime controls. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.105.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.106.0 — Repository contracts

**Status:** planned.

**Setup:** baseline 0.105.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Repository contracts.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define atomic recipe revision saves, job leases, permissions, metadata search and transaction boundaries. Define the minimal authoritative publication lease: per-run monotonic checked fencing generation, committed acquisition/reassignment, expiry/revocation and compare-and-swap completion/publication. Contract fixtures cover duplicate/racing/stale callers. The actual PostgreSQL implementation is required in v0.107.0 before v0.112.0 publication; heartbeat/retry expansion belongs to v0.124.0. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Contracts describe domain semantics instead of generic execute-SQL methods; an in-memory adapter passes the suite. Atomic commands define revision/conflict/idempotency/lease/pagination semantics; rollback and concurrent use-case tests pass before SQL optimization. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.106.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.107.0 — PostgreSQL adapter

**Status:** planned.

**Setup:** baseline 0.106.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL adapter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement parameterized queries, pool configuration and migrations outside core domain packages. Implement the v0.106.0 minimal lease/fencing contract on real PostgreSQL now: atomic committed acquisition/reassignment, checked generation advance, expiry/revocation and conditional completion/publication. Test concurrent claimers, rollback, duplicate completion and stale/expired/revoked tokens with controlled time. Issue tokens only after commit; authorization remains a separate current-state check. This is a prerequisite of v0.112.0, not deferred to v0.124.0. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recipes and jobs pass repository tests on an actual PostgreSQL instance; driver row types stay in the adapter. Real PostgreSQL runs the full repository contract, migrations and runtime least-privilege suite; no input/output payload is silently stored as SQL blobs. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.107.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.108.0 — Database TLS seam

**Status:** planned.

**Setup:** baseline 0.107.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Database TLS seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Wire tokio-postgres through a replaceable TLS connector and explicit identity/trust configuration. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Certificate validation failures are fatal; a mock provider proves database TLS is not permanently tied to rustls. Real database TLS rejects wrong host/root/expiry/plaintext downgrade; database-specific negotiation/channel binding stays in the adapter. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.108.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.109.0 — OpenBao database leases

**Status:** planned.

**Setup:** baseline 0.108.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenBao database leases.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Evaluate and qualify the current PostgreSQL database plugin; separate migration and runtime identities and map lease revocation to pool behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Real leased login/expiry/revocation fixtures pass; stale pooled credentials are discarded; unsupported beta/plugin compatibility gets a new owned pass. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.109.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.110.0 — Identity and sessions

**Status:** planned.

**Setup:** baseline 0.109.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Identity and sessions.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add server authentication, bounded sessions, token expiry, CSRF defenses and optional identity-provider integration. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Authorization is enforced server-side for every object; browser-local use remains anonymous and database-free. Reviewed identity/session flows pass wrong issuer/audience/nonce, replay, expiry, CSRF/origin and cookie negatives; credentials never appear in URLs/logs. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.110.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.111.0 — Workspace authorization

**Status:** planned.

**Setup:** baseline 0.110.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Workspace authorization.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add owner/editor/viewer roles, tenant scoping and explicit service-account permissions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Cross-workspace and confused-deputy tests fail closed even without database-specific row-security features. Cross-tenant and same-tenant revoked-object denials cover recipes/runs/artifacts/search; opaque IDs and cache/index grants never substitute for authority. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.111.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.112.0 — Hosted artifact publication fencing

**Status:** planned.

**Setup:** baseline 0.111.0; verify current upstream sources and record a bounded scope manifest before coding. Required qualified prerequisites: 0.80.0, 0.106.0, 0.107.0, 0.111.0; PostgreSQL minimal lease/fencing implementation must already pass.

**Goal:** Hosted artifact publication fencing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** With repositories and workspace authority available, qualify object completion followed by manifest/run/outbox transaction. Recheck current authorization and server lease/generation fences; publish only through committed manifests and reconcile inaccessible orphan stages. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Crash each finalize/commit/publish/cleanup cut point; duplicate completion, failed SQL commit, corrupt object, disk full, revoked reader and stale worker cannot publish partial/unauthorized output. Read bytes to verify hashes; cleanup never deletes a live referenced object. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.112.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.113.0 — Repository metadata search

**Status:** planned.

**Setup:** baseline 0.112.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Repository metadata search.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** With PostgreSQL persistence and workspace authorization available, implement bounded saved-recipe metadata search behind SearchService. Approve names, descriptions, tags/categories and collection IDs; exclude secret-bearing or sensitive metadata, operation arguments and all payloads. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Real PostgreSQL tests prove tenant/object permissions, malformed/bounded queries, deterministic pagination and immediate deletion/revocation. The UI/API works with Meilisearch disabled; local browser recipe search stays local. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.113.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.114.0 — Search projection and outbox

**Status:** planned.

**Setup:** baseline 0.113.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Search projection and outbox.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Commit revisioned allowlisted search projections and outbox events atomically with repository changes; add idempotent retry, deletion tombstones, replay watermarks and bounded task/error retention. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Transaction rollback leaves no event; crashes, duplicate/reordered delivery, concurrent edit/delete and poison events cannot resurrect old projections. Projection contains no recipe/input/result/SecretRef values and is fully rebuildable from authorized metadata. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.114.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.115.0 — Meilisearch Podman fixture

**Status:** planned.

**Setup:** baseline 0.114.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Meilisearch Podman fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Admit the latest reviewed Meilisearch image into an explicitly enabled rootless Podman profile with resource bounds, private network and qualified TLS. Obtain its initial master key from OpenBao before startup; persist service-issued scoped API keys in OpenBao before delivery, separating provisioning, index writer and search reader. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Actual optional service start/restart passes; disabled profile starts no Meilisearch container and requests no Meilisearch credentials. Missing/revoked vault secrets, wrong TLS identity, unauthenticated requests and excessive key privileges fail; master keys never reach browser or application readers. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.115.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.116.0 — Meilisearch metadata adapter

**Status:** planned.

**Setup:** baseline 0.115.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Meilisearch metadata adapter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement runasmidja-search-meilisearch outside portable defaults using a current reviewed minimal client/SDK. Consume outbox projections, track asynchronous task completion/failure and expose bounded search candidates through the owned contract. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Real server tests cover task acceptance versus completion, failed indexing, retry, queue ceilings, malformed queries, deadlines, scoped reader/writer credentials and exact projection fields. Shared repository/Meilisearch conformance passes without backend DTOs leaking into API types. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.116.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.117.0 — Search authorization and revocation

**Status:** planned.

**Setup:** baseline 0.116.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Search authorization and revocation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Enforce server-owned tenant filters and authoritative current database permission/revision checks before returning metadata. Derive visible snippets, facets, counts and pagination only from authorized current state; keep browsers behind the application API. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two-tenant and same-tenant revoked-reader tests with a deliberately stale index reveal no hit, title, snippet, facet, count or object existence. Forged filter/cursor, stale edit/delete/revoke, permissions changed during a request and database outage deny access without trusting index grants. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.117.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.118.0 — Search backend switching and recovery

**Status:** planned.

**Setup:** baseline 0.117.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Search backend switching and recovery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Qualify explicit repository/meilisearch runtime selection, std-only optional feature and an authorized repository fallback on Meilisearch outage. Rebuild/switch using outbox watermarks without data/schema/UI migration; declare ranking/freshness differences and enforce bounded recovery. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Run website/API tests in both compiled profiles and both runtime modes; disabled mode needs no search service/secrets. Outage, task failure, key rotation, corrupted/lost index, pagination across switches and cutover/replay drills preserve current permissions and database truth; performance measurements tune deployment choice rather than cancel adapter work. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.118.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.119.0 — Isolated execution workers

**Status:** planned.

**Setup:** baseline 0.118.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Isolated execution workers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Move remotely submitted CPU work into restricted processes with memory, CPU, disk and egress policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A parser crash or non-cooperative job can be killed without taking down API or other tenants. Real isolated processes reject forbidden syscalls/mounts/network; CPU/memory/PID/temp/FD exhaustion and hard kill of descendants leave inaccessible staging. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.119.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.120.0 — Worker isolation fault qualification

**Status:** planned.

**Setup:** baseline 0.119.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Worker isolation fault qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Qualify actual delegated cgroup/namespace/seccomp/MAC, nonroot/capability/descriptor policies and bounded scratch for isolated untrusted jobs. Keep supervisor/deadline enforcement outside the worker and kill the complete process tree. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** CPU spin, OOM, PID/fork/FD/temp exhaustion, forbidden mounts/syscalls/egress and malformed IPC are tested on the deployment kernel. Descendants stop after kill and staged output remains inaccessible; missing kernel controls reject the profile rather than silently weaken it. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.120.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.121.0 — Admission and quotas

**Status:** planned.

**Setup:** baseline 0.120.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Admission and quotas.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add principal/workspace job quotas, maximum artifacts, rate limits and queue backpressure. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Repeated tiny requests and large expanding jobs cannot bypass aggregate resource accounting. Admission precedes expensive work; concurrent tenant/global limits, rate limits and quota-service outage cannot oversubscribe or bypass resource reservations. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.121.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.122.0 — Valkey application adapter

**Status:** planned.

**Setup:** baseline 0.121.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Valkey application adapter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement bounded optional metadata/cache access behind application-owned CacheStore with scoped keys and revision-aware identities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Cache miss, outage, poison, stale revision and cross-tenant probes pass against Valkey; authoritative data and permissions survive without cache. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.122.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.123.0 — Valkey invalidation and outage

**Status:** planned.

**Setup:** baseline 0.122.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Valkey invalidation and outage.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Prove TTL, revocation invalidation, resource ceilings and eviction behavior without giving cache authority over authorization. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Revoked grants are checked against authoritative state; connection failures do not bypass quotas; cache poisoning and invalidation races have regressions. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.123.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.124.0 — Durable jobs and leases

**Status:** planned.

**Setup:** baseline 0.123.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Durable jobs and leases.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add job leases, fencing tokens, worker heartbeat, retry eligibility and idempotency records. Expand the minimal SQL lease/fencing primitive already qualified in v0.107.0 and used by v0.112.0. Add durable queue/heartbeat/renewal/reclaim, retry eligibility and idempotency lifecycle; rerun the earlier concurrent/stale/expiry/publication suite. This pass does not introduce fencing for the first time. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Expired workers cannot finalize duplicate results; retry is prohibited for unsafe external side effects. Crash/reassign/duplicate completion tests enforce authoritative fencing; stale/expired workers cannot renew or publish newer run output. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.124.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.125.0 — Server networking policy

**Status:** planned.

**Setup:** baseline 0.124.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Server networking policy.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Centralize outbound connections, redirects, destination restrictions, credentials and HTTP limits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** SSRF, rebinding, private/metadata destinations and mapped-address cases are covered before user HTTP operations are public. Controlled DNS/connect/redirect fixtures deny rebinding, all forbidden A/AAAA/mapped/link-local destinations, credential forwarding and decompression excess. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.125.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.126.0 — DNS and connection destination binding

**Status:** planned.

**Setup:** baseline 0.125.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DNS and connection destination binding.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement canonical native destination admission with all A/AAAA validation, IPv4-mapped IPv6 normalization, policy-owned resolution and connection to approved addresses while preserving Host/SNI. Revalidate retry/pool/TTL/policy changes and peer identity. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Controlled DNS/TLS fixtures reject mixed public/private answers, rebinding between resolve/connect, metadata/private/link-local/reserved addresses, scoped/ambiguous forms and unknown peers. No SDK/client re-resolution bypass remains; explicit private-network operator policy is separately scoped. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.126.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.127.0 — Redirect and outbound transport policy

**Status:** planned.

**Setup:** baseline 0.126.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Redirect and outbound transport policy.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Qualify each redirect/credential/timeout/decompression decision in the native broker; disable ambient proxy/Alt-Svc/coalescing bypasses. Inventory SDK/identity/search/object-store transports and isolate any client lacking required transport hooks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Private redirects, loops, retry/deadline/byte excess, signed-URL/header leaks, cross-origin credentials, ambient proxy and stale pooled-policy tests fail. An intentional proxy enforces final destinations; browser Fetch limitations are explicit and cannot trigger silent remote fallback. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.127.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.128.0 — Metadata-only observability

**Status:** planned.

**Setup:** baseline 0.127.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Metadata-only observability.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add health, readiness, redacted audit events, bounded metrics and structured operational errors. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Default logs contain no raw inputs, outputs, secrets or high-cardinality user payload labels. Sentinel payloads/keys/query bodies never enter default logs/metrics/traces; bounded IDs/counters still diagnose failures without sensitive labels. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.128.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.129.0 — Server deployment profile

**Status:** planned.

**Setup:** baseline 0.128.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Server deployment profile.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Ship a hardened single-node deployment with reverse-proxy and direct-TLS options, backups and cleanup jobs. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Restart and restore drills preserve metadata/artifact consistency; insecure development defaults cannot silently become public. Reproducible rootless deployment checks all actual isolation/secret/TLS/admission policies; public endpoints exclude administrative services and dev shortcuts. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.129.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.130.0 — Service TLS deployment policy

**Status:** planned.

**Setup:** baseline 0.129.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Service TLS deployment policy.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Qualify native PostgreSQL/Valkey/OpenBao TLS, certificate identity, trust roots and private service networks independently of local fixture shortcuts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Wrong names, unknown roots, expired certificates, missing TLS and unauthorized service clients fail; deployment never publishes administrative endpoints. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.130.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.131.0 — OpenBao production recovery custody

**Status:** planned.

**Setup:** baseline 0.130.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenBao production recovery custody.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Separate production recovery shares, initial bootstrap identity and app credentials; automate operational configuration and rehearse restore and rotation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Independent custody/recovery, audit-disk failure, snapshot restore and expired bootstrap identity are tested; one-share local test material is rejected in production. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.131.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.132.0 — PostgreSQL beta-to-GA upgrade drill

**Status:** planned.

**Setup:** baseline 0.131.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL beta-to-GA upgrade drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** When available admit PostgreSQL 19 GA after upstream review; rehearse dump/restore or documented upgrade from the beta baseline. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Restore and repository/authorization fixtures pass on pinned GA; no beta data directory is reused blindly; rollback is executable and 1.0 uses GA. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.132.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.133.0 — Server security gate

**Status:** planned.

**Setup:** baseline 0.132.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Server security gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test authentication, object authorization, uploads, worker isolation, cancellation and resource abuse. Expose remote execution only through a separate origin/application with distinct session, storage, worker, CORS/CSRF and opener boundaries. Local-only origins have no network-capable transform or automatic payload bridge/fallback. Explicit disclosure changes the trust profile; run the browser security-profile negatives. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Public remote execution stays disabled until isolation and quota tests pass; local web mode remains independently releasable. Adversarial API/auth/worker/egress/storage assessment passes on the exact deployment; remediation/retest and operational recovery evidence precede exposure. All public untrusted-job routes stay disabled until authority, admission, isolation, fencing, egress, TLS and recovery gates pass together; earlier API rows are local/private integration only. Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.133.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.
