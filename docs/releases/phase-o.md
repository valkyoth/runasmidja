# Phase O: Portability, collaboration and operations

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.340.0 — Shared recipe collections

**Status:** planned.

**Setup:** baseline 0.339.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Shared recipe collections.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add server-backed folders/tags and permission-aware recipe sharing without default input sharing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Revoking access prevents future reads; links and searches cannot enumerate another workspace. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.340.0 implementation stop reached. Run pentest for this exact commit.

## v0.341.0 — Shared-collection search integration

**Status:** planned.

**Setup:** baseline 0.340.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Shared-collection search integration.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Extend the already-qualified repository and Meilisearch search projections to server collections, sharing and revision policies through the same SearchService contract. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Both backends pass collection-sharing, inherited/revoked grants, revision edits, stale-index and recovery tests; names/tags remain an approved projection and secret-bearing collection metadata is excluded. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.341.0 implementation stop reached. Run pentest for this exact commit.

## v0.342.0 — Recipe revisions and conflicts

**Status:** planned.

**Setup:** baseline 0.341.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Recipe revisions and conflicts.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add optimistic revision checks, compare/restore and explicit multi-client conflict handling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two clients cannot silently overwrite each other; no real-time collaboration framework is required. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.342.0 implementation stop reached. Run pentest for this exact commit.

## v0.343.0 — Administrative policy

**Status:** planned.

**Setup:** baseline 0.342.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Administrative policy.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add operation/pack allowlists, egress policy, resource profiles and retention settings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Policy is enforced server-side and reported through capabilities; clients cannot self-authorize forbidden operations. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.343.0 implementation stop reached. Run pentest for this exact commit.

## v0.344.0 — Audit and retention lifecycle

**Status:** planned.

**Setup:** baseline 0.343.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Audit and retention lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded audit export, retention jobs, object deletion and backup-retention documentation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Payloads are absent by default; deleted live records and retained backups are not misleadingly described as immediate erasure everywhere. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.344.0 implementation stop reached. Run pentest for this exact commit.

## v0.345.0 — Logical storage export

**Status:** planned.

**Setup:** baseline 0.344.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Logical storage export.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Export portable recipe, identity-reference, job and artifact manifests using versioned logical records. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Export is independent of PostgreSQL SQL syntax and contains explicit integrity/referential checks. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.345.0 implementation stop reached. Run pentest for this exact commit.

## v0.346.0 — MySQL portability prototype

**Status:** planned.

**Setup:** baseline 0.345.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MySQL portability prototype.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement actual MySQL repository methods and backend-specific migrations in a separate adapter. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Shared contracts run against a real MySQL instance; merely compiling a generic driver is insufficient. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.346.0 implementation stop reached. Run pentest for this exact commit.

## v0.347.0 — SQL semantic parity

**Status:** planned.

**Setup:** baseline 0.346.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SQL semantic parity.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise collation, uniqueness, JSON values, booleans, timestamps, pagination and transaction behavior on both databases. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Results and conflict semantics agree despite different SQL dialects; deviations stay inside adapters. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.347.0 implementation stop reached. Run pentest for this exact commit.

## v0.348.0 — PostgreSQL-to-MySQL migration drill

**Status:** planned.

**Setup:** baseline 0.347.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL-to-MySQL migration drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Import a logical export into MySQL, verify hashes/counts/references, rehearse cutover and rollback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Application use cases work without domain or API changes; failures leave the original deployment recoverable. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.348.0 implementation stop reached. Run pentest for this exact commit.

## v0.349.0 — MySQL-to-PostgreSQL reverse drill

**Status:** planned.

**Setup:** baseline 0.348.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MySQL-to-PostgreSQL reverse drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reimport the same logical model and repeat repository and authorization tests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Round trips retain identifiers/revisions; the project makes no unsupported zero-downtime migration guarantee. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.349.0 implementation stop reached. Run pentest for this exact commit.

## v0.350.0 — Artifact backend portability

**Status:** planned.

**Setup:** baseline 0.349.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Artifact backend portability.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise local-disk and an optional object-storage adapter against the same artifact contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Range reads, integrity, leases and orphan cleanup work without tying metadata schema to one cloud provider. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.350.0 implementation stop reached. Run pentest for this exact commit.

## v0.351.0 — Backup and disaster recovery

**Status:** planned.

**Setup:** baseline 0.350.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Backup and disaster recovery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Document and test coordinated metadata/artifact backups, schema recovery and corruption detection. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Restore drills actually read and execute restored recipes/artifacts instead of only checking backup file existence. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.351.0 implementation stop reached. Run pentest for this exact commit.

## v0.352.0 — Release packaging

**Status:** planned.

**Setup:** baseline 0.351.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Release packaging.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Produce versioned static offline bundles, native API binaries and container images with manifests and notices. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Builds identify exact dependency and operation-pack revisions; no desktop/mobile application is shipped yet. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.352.0 implementation stop reached. Run pentest for this exact commit.

## v0.353.0 — Upgrade and rollback

**Status:** planned.

**Setup:** baseline 0.352.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Upgrade and rollback.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add compatible server/browser/pack upgrade rules, migration prechecks and rollback guidance. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** An interrupted upgrade cannot mix incompatible schema/engine assets or corrupt saved recipes. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.353.0 implementation stop reached. Run pentest for this exact commit.

## v0.354.0 — Operational load qualification

**Status:** planned.

**Setup:** baseline 0.353.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operational load qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise realistic multi-user mixes, expensive-job fairness, disk pressure and process failure. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Published limits come from measurements; API responsiveness survives isolated worker exhaustion. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.354.0 implementation stop reached. Run pentest for this exact commit.

## v0.355.0 — Portability and operations gate

**Status:** planned.

**Setup:** baseline 0.354.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Portability and operations gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close deployment docs, actual second-database contract tests and Vef/Brynja replacement rehearsals. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** PostgreSQL is the initial production-supported backend; MySQL support level is stated separately from the proven portability contract. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.355.0 implementation stop reached. Run pentest for this exact commit.

## v0.356.0 — Integrated service recovery gate

**Status:** planned.

**Setup:** baseline 0.355.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Integrated service recovery gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Rehearse coordinated PostgreSQL/artifact restore, OpenBao recovery/rotation, Valkey cold start and optional search rebuild. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A restored deployment serves authorized recipes and can run them; cache/search loss does not lose authoritative data; all recovery steps are automated or explicitly custody-gated. Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.356.0 implementation stop reached. Run pentest for this exact commit.
