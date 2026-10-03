# Phase O: Portability, collaboration and operations

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.353.0 — Shared recipe collections

**Status:** planned.

**Setup:** baseline 0.352.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Shared recipe collections.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add server-backed folders/tags and permission-aware recipe sharing without default input sharing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Revoking access prevents future reads; links and searches cannot enumerate another workspace. Shared collections preserve separate recipe/payload sharing and current permissions; revoked grants, tenant enumeration and inherited access negatives pass. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.353.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.354.0 — Shared-collection search integration

**Status:** planned.

**Setup:** baseline 0.353.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Shared-collection search integration.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Extend the already-qualified repository and Meilisearch search projections to server collections, sharing and revision policies through the same SearchService contract. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Both backends pass collection-sharing, inherited/revoked grants, revision edits, stale-index and recovery tests; names/tags remain an approved projection and secret-bearing collection metadata is excluded. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.354.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.355.0 — Recipe revisions and conflicts

**Status:** planned.

**Setup:** baseline 0.354.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Recipe revisions and conflicts.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add optimistic revision checks, compare/restore and explicit multi-client conflict handling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two clients cannot silently overwrite each other; no real-time collaboration framework is required. Two-client edits produce explicit conflicts; compare/restore preserves revisions and cannot silently overwrite or recover a revoked secret-bearing record. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.355.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.356.0 — Administrative policy

**Status:** planned.

**Setup:** baseline 0.355.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Administrative policy.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add operation/pack allowlists, egress policy, resource profiles and retention settings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Policy is enforced server-side and reported through capabilities; clients cannot self-authorize forbidden operations. Operation/pack/egress/retention/resource policy is authoritative server state; forged client capabilities and cached policy cannot self-authorize. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.356.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.357.0 — Audit and retention lifecycle

**Status:** planned.

**Setup:** baseline 0.356.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Audit and retention lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded audit export, retention jobs, object deletion and backup-retention documentation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Payloads are absent by default; deleted live records and retained backups are not misleadingly described as immediate erasure everywhere. Retention/deletion/audit jobs are bounded/idempotent and authorized; default audit excludes payloads and backups' remaining retention is stated accurately. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.357.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.358.0 — Logical storage export

**Status:** planned.

**Setup:** baseline 0.357.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Logical storage export.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Export portable recipe, identity-reference, job and artifact manifests using versioned logical records. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Export is independent of PostgreSQL SQL syntax and contains explicit integrity/referential checks. Versioned logical exports include complete IDs/revisions/grants/manifests/digests and referential checks; secrets/payloads follow explicit separate export policy. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.358.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.359.0 — Migration integrity and canonicalization

**Status:** planned.

**Setup:** baseline 0.358.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Migration integrity and canonicalization.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Freeze portable entity/key/revision/grant/timestamp/null/numeric canonicalization and artifact reference semantics before MySQL/cutover drills. Define a maintenance-window job quiesce/fence protocol and rollback that preserves writes after cutover. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two-tenant/revoked-grant/case/Unicode/large-number/tombstone fixtures and corrupt/truncated/duplicate exports reject precisely. Equality requires key sets, canonical digests, byte-read artifact hashes, permissions and revision/idempotency outcomes; missing/duplicate/unexpected records and references are zero. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.359.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.360.0 — MySQL portability prototype

**Status:** planned.

**Setup:** baseline 0.359.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MySQL portability prototype.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement actual MySQL repository methods and backend-specific migrations in a separate adapter. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Shared contracts run against a real MySQL instance; merely compiling a generic driver is insufficient. Actual MySQL adapter/migrations pass the entire repository/use-case suite on a real rootless fixture, with no SQL/provider types in domain APIs. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.360.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.361.0 — SQL semantic parity

**Status:** planned.

**Setup:** baseline 0.360.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SQL semantic parity.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise collation, uniqueness, JSON values, booleans, timestamps, pagination and transaction behavior on both databases. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Results and conflict semantics agree despite different SQL dialects; deviations stay inside adapters. Both databases agree on collation/NULL/JSON/integer/boolean/time/pagination/conflict/transaction semantics using adversarial concurrency fixtures. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.361.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.362.0 — PostgreSQL-to-MySQL migration drill

**Status:** planned.

**Setup:** baseline 0.361.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL-to-MySQL migration drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Import a logical export into MySQL, verify hashes/counts/references, rehearse cutover and rollback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Application use cases work without domain or API changes; failures leave the original deployment recoverable. Quiesce/fence jobs and migrate PostgreSQL to MySQL; zero missing/duplicate records, canonical digest/hash/grant changes, and broken references; cutover/rollback replay succeeds. Quiesce/fence live jobs and verify object hashes by reading bytes; rollback preserves post-cutover writes or explicitly freezes writes, never silently restores stale data. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.362.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.363.0 — MySQL-to-PostgreSQL reverse drill

**Status:** planned.

**Setup:** baseline 0.362.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MySQL-to-PostgreSQL reverse drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reimport the same logical model and repeat repository and authorization tests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Round trips retain identifiers/revisions; the project makes no unsupported zero-downtime migration guarantee. Reverse the same model to PostgreSQL and repeat exact equality, authorization, revision and recipe-replay checks; active leases cannot survive as unfenced writers. Repeat byte-read hashes/canonical key sets/grants/revisions and representative recipe replay; MySQL is a proof adapter until separately production-qualified, with no zero-downtime claim. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.363.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.364.0 — Artifact backend portability

**Status:** planned.

**Setup:** baseline 0.363.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Artifact backend portability.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise local-disk and an optional object-storage adapter against the same artifact contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Range reads, integrity, leases and orphan cleanup work without tying metadata schema to one cloud provider. Real filesystem/object-store adapters pass ranges/staging/integrity/quotas/cleanup under crash and outage; logical manifests expose no backend-specific paths. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.364.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.365.0 — Backup and disaster recovery

**Status:** planned.

**Setup:** baseline 0.364.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Backup and disaster recovery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Document and test coordinated metadata/artifact backups, schema recovery and corruption detection. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Restore drills actually read and execute restored recipes/artifacts instead of only checking backup file existence. Restore coordinated metadata/artifacts/Bao state then authorize/read/execute representative recipes; corrupt/incomplete backups fail and retained data policy is explicit. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.365.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.366.0 — Release packaging

**Status:** planned.

**Setup:** baseline 0.365.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Release packaging.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Produce versioned static offline bundles, native API binaries and container images with manifests and notices. Package the independently verified signed immutable offline/local-only and separate hosted-local/remote profiles with exact identities and headers. Rerun network-disabled launch, signature/manifest/substitution and profile negatives on the release artifacts; v0.367.0 binds their provenance to assessment. At v0.366.0 and RC/1.0 rerun direct and Fluxheim Wolfi deployment qualification on exact artifacts with reviewed proxy/config versions, notices/inventories and restore/rollback/upgrade evidence; retain both Meilisearch profiles. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Builds identify exact dependency and operation-pack revisions; no desktop/mobile application is shipped yet. Exact offline/static/native/container artifacts include pinned packs/assets/licenses/SBOM and verified hashes; no desktop/mobile support is claimed yet. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.366.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.367.0 — Distribution assessment and provenance binding

**Status:** planned.

**Setup:** baseline 0.366.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Distribution assessment and provenance binding.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Bind trusted reviewed assessment to exact source, toolchain, artifact/pack/model/SBOM hashes, required target evidence and signing/provenance identities. Implement rejection gates distinct from local report metadata, remote CodeQL Default settings and publication authority. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Tampered/substituted artifact, stale SBOM, forged/untrusted PASS, missing target/CI evidence and bad signature/issuer/source bindings reject. Independent clean builds verify manifests; secrets come from OpenBao and no test creates a real assessment PASS or publication authorization. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.367.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.368.0 — Upgrade and rollback

**Status:** planned.

**Setup:** baseline 0.367.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Upgrade and rollback.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add compatible server/browser/pack upgrade rules, migration prechecks and rollback guidance. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** An interrupted upgrade cannot mix incompatible schema/engine assets or corrupt saved recipes. Interrupted browser/server/pack/schema upgrade cannot mix incompatible revisions; rollback/restore preserves authorization and new writes by documented policy. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.368.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.369.0 — Operational load qualification

**Status:** planned.

**Setup:** baseline 0.368.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operational load qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise realistic multi-user mixes, expensive-job fairness, disk pressure and process failure. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Published limits come from measurements; API responsiveness survives isolated worker exhaustion. Measured multi-tenant expensive-job mix with CPU/OOM/disk/network failures preserves API latency/fairness/admission and rejects stale completions. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.369.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.370.0 — Portability and operations gate

**Status:** planned.

**Setup:** baseline 0.369.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Portability and operations gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close deployment docs, actual second-database contract tests and Vef/Brynja replacement rehearsals. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** PostgreSQL is the initial production-supported backend; MySQL support level is stated separately from the proven portability contract. Real second-database and replacement/operational rehearsals pass; support levels remain explicit and executable deployment/rollback documents agree with code. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.370.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.371.0 — Integrated service recovery gate

**Status:** planned.

**Setup:** baseline 0.370.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Integrated service recovery gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Rehearse coordinated PostgreSQL/artifact restore, OpenBao recovery/rotation, Valkey cold start and optional search rebuild. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A restored deployment serves authorized recipes and can run them; cache/search loss does not lose authoritative data; all recovery steps are automated or explicitly custody-gated. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.371.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.
