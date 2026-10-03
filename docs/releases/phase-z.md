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

## v0.2.0 — OpenBao-first secret provisioning

**Status:** planned.

**Setup:** baseline 0.1.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenBao-first secret provisioning.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Remediate the current local-password-first harness: start and initialize TLS OpenBao before credential-consuming services; generate project-owned credentials through OpenBao, persist references/versions there and separate minimal vault trust/recovery custody. Configure audit, scoped provisioning/runtime identities and bootstrap root revocation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** An empty-state run obtains PostgreSQL admin/runtime and Valkey credentials from OpenBao before service initialization; sealed/unavailable/denied OpenBao prevents dependent startup without local generation or fallback. Partial failure/retry preserves vault credential versions and data; bootstrap root is revoked only after scoped provisioning succeeds; diagnostics never expose secrets. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.2.0 implementation stop reached. Run pentest for this exact commit.

## v0.3.0 — PostgreSQL 19 beta 4 test fixture

**Status:** planned.

**Setup:** baseline 0.2.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL 19 beta 4 test fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Pin PostgreSQL 19 beta 4 by digest; automate rootless Podman, OpenBao-sourced initial admin and runtime credentials, readiness and a separate runtime role. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A real container reports 19beta4, transaction rollback works, runtime role has no superuser or role-management powers, wrong passwords fail, and only loopback ports are published. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.3.0 implementation stop reached. Run pentest for this exact commit.

## v0.4.0 — Valkey test fixture

**Status:** planned.

**Setup:** baseline 0.3.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Valkey test fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Automate digest-pinned rootless Valkey with OpenBao-sourced application ACL credentials, prefix isolation, TTLs and memory limits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Authenticated set/get/delete works; unauthenticated access and foreign key prefixes fail; eviction cannot become authoritative application state. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.4.0 implementation stop reached. Run pentest for this exact commit.

## v0.5.0 — Initialization secret delivery

**Status:** planned.

**Setup:** baseline 0.4.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Initialization secret delivery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Inventory every fixture/provisioning secret; deliver OpenBao-issued values through bounded memory/IPC or private short-lived tmpfs files when a service requires files. Replace persistent plaintext password/ACL copies and scope restart grants independently from runtime grants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No project credential remains in .local plaintext custody, argv, container metadata, environment dumps or logs; interruption cleans delivery files. Restart after root revocation resolves the same vault-owned credential version; expiry, denied provisioning identity and missing TLS fail closed. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.5.0 implementation stop reached. Run pentest for this exact commit.

## v0.6.0 — Build and release secret delivery

**Status:** planned.

**Setup:** baseline 0.5.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Build and release secret delivery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Make public Rust initialization/builds secret-free. For private registries, publishing, signing and deployment, authenticate a bounded developer/workload identity to OpenBao and resolve project secrets there; qualify GitHub OIDC claim binding and secret-free pull-request workflows. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Public rustup/Cargo/checks need no secret or vault. Credential-requiring jobs deny sealed vault, wrong repository/ref/environment/audience and fork PRs; no project secret is stored in GitHub Secrets, committed Cargo credentials, artifacts or build caches. Short-lived delivery and cleanup/renewal are tested. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.6.0 implementation stop reached. Run pentest for this exact commit.

## v0.7.0 — Service lifecycle harness

**Status:** planned.

**Setup:** baseline 0.6.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Service lifecycle harness.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise idempotent start, stop/restart, readiness deadlines and failed provisioning recovery without touching unrelated containers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two starts converge; sealed OpenBao is unsealed from local test recovery material; PostgreSQL persists; cache can be empty; failures return nonzero. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.7.0 implementation stop reached. Run pentest for this exact commit.

## v0.8.0 — Freshness and supply-chain controls

**Status:** planned.

**Setup:** baseline 0.7.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Freshness and supply-chain controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Schedule weekly upstream checks, pin tool archive hashes and action commits, monitor SDK/services and record review decisions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Newer stable, yanked, unavailable and prerelease metadata fixtures fail as specified; exact current upstream versions are verified before dependency changes. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.8.0 implementation stop reached. Run pentest for this exact commit.
