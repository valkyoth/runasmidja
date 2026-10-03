# Phase N: Extensibility and replacement-adapter proof

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.325.0 — Operation SDK

**Status:** planned.

**Setup:** baseline 0.324.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operation SDK.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Publish first-party operation scaffolding, descriptor validators, fixture templates and threat-review guidance. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A sample operation is added without modifying scheduler, HTTP routes, database schema or handwritten UI forms. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.325.0 implementation stop reached. Run pentest for this exact commit.

## v0.326.0 — Operation pack manifests

**Status:** planned.

**Setup:** baseline 0.325.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operation pack manifests.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Group operation implementations by capability, version, dependency footprint and platform support. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Required dependencies are explicit; removing a pack cannot produce silently incomplete loaded recipes. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.326.0 implementation stop reached. Run pentest for this exact commit.

## v0.327.0 — Lazy browser packs

**Status:** planned.

**Setup:** baseline 0.326.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lazy browser packs.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add on-demand loading and an explicit complete offline-pack catalogue. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** App, engine and pack versions are verified before activation; failed downloads leave a usable previous state. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.327.0 implementation stop reached. Run pentest for this exact commit.

## v0.328.0 — Provider replacement tests

**Status:** planned.

**Setup:** baseline 0.327.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Provider replacement tests.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run selected operations against alternate providers behind stable semantic descriptors. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Replacement requires byte/behavior conformance and security review; provider identity participates where it affects reproducibility. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.328.0 implementation stop reached. Run pentest for this exact commit.

## v0.329.0 — Core-Wasm plugin ABI

**Status:** planned.

**Setup:** baseline 0.328.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Core-Wasm plugin ABI.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Specify a narrow versioned ABI for memory, metadata, bounded I/O, errors and capability requests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** The ABI contains no host pointers, unrestricted syscalls or implicit network/file access. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.329.0 implementation stop reached. Run pentest for this exact commit.

## v0.330.0 — Browser plugin sandbox

**Status:** planned.

**Setup:** baseline 0.329.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser plugin sandbox.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Load plugins in a separate worker/instance with allowlisted imports, resource limits and explicit grants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** An infinite loop, memory growth or hostile output can be terminated without accessing app state or persistent secrets. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.330.0 implementation stop reached. Run pentest for this exact commit.

## v0.331.0 — Native plugin sandbox

**Status:** planned.

**Setup:** baseline 0.330.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Native plugin sandbox.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add a reviewed Wasm runtime adapter with fuel/epoch or equivalent limits and constrained host calls. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Resource and capability tests cover malicious modules; signatures are not treated as proof of safety. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.331.0 implementation stop reached. Run pentest for this exact commit.

## v0.332.0 — Plugin package integrity

**Status:** planned.

**Setup:** baseline 0.331.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Plugin package integrity.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add manifests, hashes, optional signatures, provenance, revocation and administrator policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unknown publishers are not automatically trusted; rollback protection and offline integrity checks have tests. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.332.0 implementation stop reached. Run pentest for this exact commit.

## v0.333.0 — Plugin conformance kit

**Status:** planned.

**Setup:** baseline 0.332.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Plugin conformance kit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Publish ABI vectors, boundary fuzzing, malformed-module tests and example portable operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Plugin authors can validate behavior without depending on the web framework or database. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.333.0 implementation stop reached. Run pentest for this exact commit.

## v0.334.0 — Component-model evaluation

**Status:** planned.

**Setup:** baseline 0.333.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Component-model evaluation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Evaluate a WIT/component adapter using the required JavaScript shims/transpilation where needed. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Keep it optional unless browser/native portability and resource enforcement match the established plugin contract. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.334.0 implementation stop reached. Run pentest for this exact commit.

## v0.335.0 — HTTP server replacement seam

**Status:** planned.

**Setup:** baseline 0.334.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTTP server replacement seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement a second minimal/mock HTTP adapter and route conformance suite for a future Vef provider. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** All application endpoints run without importing the original framework outside its adapter package. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.335.0 implementation stop reached. Run pentest for this exact commit.

## v0.336.0 — Outbound HTTP replacement seam

**Status:** planned.

**Setup:** baseline 0.335.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Outbound HTTP replacement seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Centralize identity, user HTTP, object-storage and other outbound clients behind application-owned gateway policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No native subsystem opens an unreviewed HTTP/TLS path; destination and trust policies survive provider substitution. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.336.0 implementation stop reached. Run pentest for this exact commit.

## v0.337.0 — TLS replacement seam

**Status:** planned.

**Setup:** baseline 0.336.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TLS replacement seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test inbound/outbound TLS and database TLS connectors with alternate/mock providers for future Brynja integration. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Trust, hostname verification, ALPN, timeouts and errors remain explicit; browser-owned TLS is documented as outside this seam. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.337.0 implementation stop reached. Run pentest for this exact commit.

## v0.338.0 — Conditional sibling integrations

**Status:** planned.

**Setup:** baseline 0.337.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Conditional sibling integrations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add real Vef/Brynja adapter packages only when their APIs and security properties are usable; otherwise ship contract harnesses. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** The default build works without sibling paths; integration is not claimed complete when only a placeholder exists. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.338.0 implementation stop reached. Run pentest for this exact commit.

## v0.339.0 — Extensibility qualification

**Status:** planned.

**Setup:** baseline 0.338.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Extensibility qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Demonstrate a new operation, new pack, provider swap and transport replacement through the public contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No domain/database/UI rewrite is needed; every accepted extra dependency has a documented purpose and feature budget. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.339.0 implementation stop reached. Run pentest for this exact commit.
