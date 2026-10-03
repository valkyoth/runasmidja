# Phase Z: Repository and service foundation

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.1.0 — Repository foundation

**Status:** planned.

**Setup:** baseline empty initialized repository; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Repository foundation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Initialize EUPL-1.2 workspace, copied and adapted GitHub files, Rust 1.99.0, no_std facade, 500-line gates, reference provenance and pending release evidence. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Default/release tests, bare-metal and Wasm checks, policy rejection fixtures, documentation links and dependency audits pass; no product parity is claimed. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.1.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.2.0 — OpenBao-first secret provisioning

**Status:** planned.

**Setup:** baseline 0.1.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenBao-first secret provisioning.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Remediate the current local-password-first harness: start and initialize TLS OpenBao before credential-consuming services; generate project-owned credentials through OpenBao, persist references/versions there and separate minimal vault trust/recovery custody. Configure audit, scoped provisioning/runtime identities and bootstrap root revocation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** An empty-state run obtains PostgreSQL admin/runtime and Valkey credentials from OpenBao before service initialization; sealed/unavailable/denied OpenBao prevents dependent startup without local generation or fallback. Partial failure/retry preserves vault credential versions and data; bootstrap root is revoked only after scoped provisioning succeeds; diagnostics never expose secrets. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.2.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.3.0 — Workflow reference policy

**Status:** planned.

**Setup:** baseline 0.2.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Workflow reference policy.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Harden workflow admission for both .yml and .yaml, quoted/block/expression forms and action/reusable-workflow references. Define separate full-commit remote, reviewed same-repository local and digest-pinned container policies; preserve CodeQL Default setup. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unpinned, dynamic, malformed and advanced-CodeQL references reject in both suffixes; approved remote/local/container fixtures pass. Do not mistake comments or unrelated YAML strings for executed references; current bypass regressions are exercised. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.3.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.4.0 — Feature and target admission gates

**Status:** planned.

**Setup:** baseline 0.3.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Feature and target admission gates.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Replace scaffold-only dependency/no_std heuristics with reviewed package profiles and normal/build/dev/optional/target dependency graphs. Require inherited unsafe-forbid/lint policy, real target/feature builds and public contract isolation; keep dependency admission explicit. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Comment-spoofed no_std, target/build dependency leakage, default-feature std/alloc and feature-unification leaks reject. Reviewed std adapters and portable providers can be admitted without disabling checks; bare-metal no-alloc, alloc, Wasm and native graphs are tested separately. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.4.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.5.0 — Fixture ownership and drift

**Status:** planned.

**Setup:** baseline 0.4.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Fixture ownership and drift.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Require project/service ownership before every container/network/volume mutation, including stop; verify immutable image and nonsecret resource/mount/port/network/config fingerprints before reuse. Reconcile only documented safe differences and refuse destructive replacement. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Name collisions, wrong labels/digests, changed mounts/ports/limits and unowned volume/network tests refuse mutation. Partial startup and drift preserve owned database/vault state; fingerprints/logs contain no secret values and no unrelated object is stopped. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.5.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.6.0 — PostgreSQL 19 beta 4 test fixture

**Status:** planned.

**Setup:** baseline 0.5.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PostgreSQL 19 beta 4 test fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Pin PostgreSQL 19 beta 4 by digest; automate rootless Podman, OpenBao-sourced initial admin and runtime credentials, readiness and a separate runtime role. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A real container reports 19beta4, transaction rollback works, runtime role has no superuser or role-management powers, wrong passwords fail, and only loopback ports are published. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.6.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.7.0 — Valkey test fixture

**Status:** planned.

**Setup:** baseline 0.6.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Valkey test fixture.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Automate digest-pinned rootless Valkey with OpenBao-sourced application ACL credentials, prefix isolation, TTLs and memory limits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Authenticated set/get/delete, TTL/countdown and observed expiration pass; unauthenticated access and foreign key prefixes fail; eviction cannot become authoritative application state. Grant only the additional TTL-test command permissions needed; the current EX-option smoke does not establish expiry. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.7.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.8.0 — Initialization secret delivery

**Status:** planned.

**Setup:** baseline 0.7.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Initialization secret delivery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Inventory every fixture/provisioning secret; deliver OpenBao-issued values through bounded memory/IPC or private short-lived tmpfs files when a service requires files. Replace persistent plaintext password/ACL copies and scope restart grants independently from runtime grants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No project credential remains in .local plaintext custody, argv, container metadata, environment dumps or logs; interruption cleans delivery files. Restart after root revocation resolves the same vault-owned credential version; expiry, denied provisioning identity and missing TLS fail closed. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.8.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.9.0 — Build and release secret delivery

**Status:** planned.

**Setup:** baseline 0.8.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Build and release secret delivery.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Make public Rust initialization/builds secret-free. For private registries, publishing, signing and deployment, authenticate a bounded developer/workload identity to OpenBao and resolve project secrets there; qualify GitHub OIDC claim binding and secret-free pull-request workflows. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Public rustup/Cargo/checks need no secret or vault. Credential-requiring jobs deny sealed vault, wrong repository/ref/environment/audience and fork PRs; no project secret is stored in GitHub Secrets, committed Cargo credentials, artifacts or build caches. Short-lived delivery and cleanup/renewal are tested. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.9.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.10.0 — Release evidence trust contract

**Status:** planned.

**Setup:** baseline 0.9.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Release evidence trust contract.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define scope/evidence schemas and reviewed assessor/reviewer identity, exact-source lineage, severity disposition and artifact evidence references. Describe check_release as metadata validation, not assessment authentication; plan trusted attestation enforcement before distribution. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Report-shape PASS alone cannot authorize publishing; missing assessment identity/review/target evidence blocks the reviewed release checklist. Define tampered/fabricated evidence regressions and keep no-report NOT RUN rejection; no signing provider is invented. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.10.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.11.0 — Service lifecycle harness

**Status:** planned.

**Setup:** baseline 0.10.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Service lifecycle harness.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise idempotent start, stop/restart, readiness deadlines and failed provisioning recovery without touching unrelated containers. At v0.11.0 add an actual rootless Fluxheim Wolfi proxy fixture for the bounded health probe, using only the official published proxy-wolfi image pinned by digest; do not build or repackage Fluxheim. Verify current version, publisher/platform, scans and inventory before admission. Test direct native/container backends and real proxy routing/rejections, outage/restart, timeout bounds and spoofed forwarding headers; freeze the minimal HTTP/TLS trust scope. Automate owned private-network configuration and cleanup without exposing admin services. This is health-fixture evidence only, not production/browser/session/upload qualification. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Two starts converge; sealed OpenBao is unsealed from local test recovery material; PostgreSQL persists; cache can be empty; failures return nonzero. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.11.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.12.0 — Freshness and supply-chain controls

**Status:** planned.

**Setup:** baseline 0.11.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Freshness and supply-chain controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Schedule weekly upstream checks, pin tool archive hashes and action commits, monitor SDK/services and record review decisions. Include the admitted Fluxheim image/release, exact proxy/base/source identities and per-image scan/SBOM evidence. Review current accessible Wolfi service images; same-base packaging never replaces publisher, runtime or vulnerability checks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Newer stable, yanked, unavailable and prerelease metadata fixtures fail as specified; exact current upstream versions are verified before dependency changes. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.12.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.13.0 — Seed value and budget vocabulary

**Status:** planned.

**Setup:** baseline 0.12.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Seed value and budget vocabulary.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement the smallest no_std/no-alloc checked ID/offset/value-kind/error and byte/work reservation vocabulary for a one-operation hex seed. Define explicit EOF and terminal counts without requiring the later compiler/scheduler. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Checked conversions, reserve/refund, overflow, zero limits and L-1/L/L+1 have unit tests on native/bare-metal/Wasm. Freeze a seed manifest: 32 KiB input, 64 KiB output, 4 KiB windows and 256 KiB tracked engine state; choose finite fuel and host deadlines before admission, with no hidden dynamic growth. Exercise real services, startup failure, authorization denials, restart and redacted diagnostics. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.13.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.
