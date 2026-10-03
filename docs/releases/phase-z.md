# Phase Z: Repository and service foundation

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.1.0 — Repository foundation

**Status:** planned.

**Setup:** baseline empty initialized repository; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Repository foundation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Initialize EUPL-1.2 workspace, copied and adapted GitHub files, Rust 1.99.0, no_std facade, 500-line gates, reference provenance and pending release evidence. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Default/release tests, bare-metal and Wasm checks, policy rejection fixtures, documentation links and dependency audits pass; no product parity is claimed. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.1.0 implementation stop reached. Run pentest for this exact commit.

## v0.2.0 — PostgreSQL 19 beta 4 test fixture

**Status:** planned.

**Setup:** baseline 0.1.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL 19 beta 4 test fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Pin PostgreSQL 19 beta 4 by digest; automate rootless Podman, private credentials, readiness and a separate runtime role. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A real container reports 19beta4, transaction rollback works, runtime role has no superuser or role-management powers, and only loopback ports are published. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.2.0 implementation stop reached. Run pentest for this exact commit.

## v0.3.0 — OpenBao test bootstrap

**Status:** planned.

**Setup:** baseline 0.2.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenBao test bootstrap.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Automate TLS identity, persistent single-node storage, declarative audit, KV v2, scoped AppRole, root-token revocation and private recovery material. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Initialization and restart work; AppRole reads only runtime secrets; mounts and other secret paths return 403; no credential is printed or tracked. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.3.0 implementation stop reached. Run pentest for this exact commit.

## v0.4.0 — Valkey test fixture

**Status:** planned.

**Setup:** baseline 0.3.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Valkey test fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Automate digest-pinned rootless Valkey with application ACL, prefix isolation, TTLs and memory limits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Authenticated set/get/delete works; unauthenticated access and foreign key prefixes fail; eviction cannot become authoritative application state. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.4.0 implementation stop reached. Run pentest for this exact commit.

## v0.5.0 — Service lifecycle harness

**Status:** planned.

**Setup:** baseline 0.4.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Service lifecycle harness.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise idempotent start, stop/restart, readiness deadlines and failed provisioning recovery without touching unrelated containers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two starts converge; sealed OpenBao is unsealed from local test recovery material; PostgreSQL persists; cache can be empty; failures return nonzero. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.5.0 implementation stop reached. Run pentest for this exact commit.

## v0.6.0 — Freshness and supply-chain controls

**Status:** planned.

**Setup:** baseline 0.5.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Freshness and supply-chain controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Schedule weekly upstream checks, pin tool archive hashes and action commits, monitor SDK/services and record review decisions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Newer stable, yanked, unavailable and prerelease metadata fixtures fail as specified; exact current upstream versions are verified before dependency changes. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.6.0 implementation stop reached. Run pentest for this exact commit.
