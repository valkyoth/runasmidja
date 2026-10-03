# Phase N: Extensibility and replacement-adapter proof

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.338.0 — Operation SDK

**Status:** planned.

**Setup:** baseline 0.337.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operation SDK.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Publish first-party operation scaffolding, descriptor validators, fixture templates and threat-review guidance. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A sample operation is added without modifying scheduler, HTTP routes, database schema or handwritten UI forms. Independent operation author implements descriptor/step/tests/limits without editing transport/UI/domain plumbing; conformance failure catches missing metadata. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.338.0 implementation stop reached. Run pentest for this exact commit.

## v0.339.0 — Operation pack manifests

**Status:** planned.

**Setup:** baseline 0.338.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operation pack manifests.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Group operation implementations by capability, version, dependency footprint and platform support. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Required dependencies are explicit; removing a pack cannot produce silently incomplete loaded recipes. Pack manifests bind operation/revision/ABI/dependencies/capabilities/assets/licenses/sizes; malformed/incompatible packs reject before execution. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.339.0 implementation stop reached. Run pentest for this exact commit.

## v0.340.0 — Lazy browser packs

**Status:** planned.

**Setup:** baseline 0.339.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lazy browser packs.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add on-demand loading and an explicit complete offline-pack catalogue. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** App, engine and pack versions are verified before activation; failed downloads leave a usable previous state. Large browser packs load only on explicit need/installation, with verified identity and resource budgets; absent/offline packs never upload input. Extend the already-qualified minimal first-party loader/catalogue rather than delaying initial provider isolation to this milestone. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.340.0 implementation stop reached. Run pentest for this exact commit.

## v0.341.0 — Provider replacement tests

**Status:** planned.

**Setup:** baseline 0.340.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Provider replacement tests.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run selected operations against alternate providers behind stable semantic descriptors. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Replacement requires byte/behavior conformance and security review; provider identity participates where it affects reproducibility. Swap a real qualified provider and rerun shared independent vectors/error/resource/secret suites; mock compilation alone cannot claim interchangeability. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.341.0 implementation stop reached. Run pentest for this exact commit.

## v0.342.0 — Core-Wasm plugin ABI

**Status:** planned.

**Setup:** baseline 0.341.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Core-Wasm plugin ABI.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Specify a narrow versioned ABI for memory, metadata, bounded I/O, errors and capability requests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** The ABI contains no host pointers, unrestricted syscalls or implicit network/file access. Core-Wasm ABI validates handles/lengths/versions/imports/exports; malformed modules, memory growth and host-call amplification fail under limits. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.342.0 implementation stop reached. Run pentest for this exact commit.

## v0.343.0 — Browser plugin sandbox

**Status:** planned.

**Setup:** baseline 0.342.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser plugin sandbox.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Load plugins in a separate worker/instance with allowlisted imports, resource limits and explicit grants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** An infinite loop, memory growth or hostile output can be terminated without accessing app state or persistent secrets. Untrusted plugins execute in isolated worker/memory with no arbitrary origin JS authority; forbidden imports, network/storage and runaway execution are denied/terminated. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.343.0 implementation stop reached. Run pentest for this exact commit.

## v0.344.0 — Native plugin sandbox

**Status:** planned.

**Setup:** baseline 0.343.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Native plugin sandbox.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add a reviewed Wasm runtime adapter with fuel/epoch or equivalent limits and constrained host calls. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Resource and capability tests cover malicious modules; signatures are not treated as proof of safety. Native plugin runtime enforces fuel/epoch or process deadlines, memory/table/stack/host-call limits and capability denial with real hostile guests. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.344.0 implementation stop reached. Run pentest for this exact commit.

## v0.345.0 — Plugin package integrity

**Status:** planned.

**Setup:** baseline 0.344.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Plugin package integrity.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add manifests, hashes, optional signatures, provenance, revocation and administrator policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unknown publishers are not automatically trusted; rollback protection and offline integrity checks have tests. Tampered/rollback/oversized/incompatible packages reject; trusted identity/integrity never substitutes for sandbox restrictions or safe-code review. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.345.0 implementation stop reached. Run pentest for this exact commit.

## v0.346.0 — Plugin conformance kit

**Status:** planned.

**Setup:** baseline 0.345.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Plugin conformance kit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Publish ABI vectors, boundary fuzzing, malformed-module tests and example portable operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Plugin authors can validate behavior without depending on the web framework or database. Public plugin vectors/malformed ABI/import/memory/work tests run independently in browser/native; example plugins meet the same limits as third-party guests. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.346.0 implementation stop reached. Run pentest for this exact commit.

## v0.347.0 — Component-model evaluation

**Status:** planned.

**Setup:** baseline 0.346.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Component-model evaluation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Evaluate a WIT/component adapter using the required JavaScript shims/transpilation where needed. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Keep it optional unless browser/native portability and resource enforcement match the established plugin contract. Actual WIT/component adapter plus generated JS passes browser/native semantics/import/resource/copy tests; optional tooling remains outside the baseline ABI. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.347.0 implementation stop reached. Run pentest for this exact commit.

## v0.348.0 — HTTP server replacement seam

**Status:** planned.

**Setup:** baseline 0.347.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTTP server replacement seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement a second minimal/mock HTTP adapter and route conformance suite for a future Vef provider. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** All application endpoints run without importing the original framework outside its adapter package. Second runnable HTTP adapter serves the same use cases; framing/backpressure/disconnect/origin/error/security suites pass without domain changes. Mocks remain useful unit fixtures but do not close runnable host replacement support. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.348.0 implementation stop reached. Run pentest for this exact commit.

## v0.349.0 — Outbound HTTP replacement seam

**Status:** planned.

**Setup:** baseline 0.348.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Outbound HTTP replacement seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Centralize identity, user HTTP, object-storage and other outbound clients behind application-owned gateway policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No native subsystem opens an unreviewed HTTP/TLS path; destination and trust policies survive provider substitution. All native outbound consumers are inventoried and routed/isolated under owned egress policy; alternate transport preserves DNS/connect/redirect/trust limits. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.349.0 implementation stop reached. Run pentest for this exact commit.

## v0.350.0 — TLS replacement seam

**Status:** planned.

**Setup:** baseline 0.349.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TLS replacement seam.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test inbound/outbound TLS and database TLS connectors with alternate/mock providers for future Brynja integration. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Trust, hostname verification, ALPN, timeouts and errors remain explicit; browser-owned TLS is documented as outside this seam. Alternate native and database TLS providers pass real identity/trust/ALPN/mTLS/negotiation negatives; browser TLS is explicitly outside replacement scope. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.350.0 implementation stop reached. Run pentest for this exact commit.

## v0.351.0 — Conditional sibling integrations

**Status:** planned.

**Setup:** baseline 0.350.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Conditional sibling integrations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add real Vef/Brynja adapter packages only when their APIs and security properties are usable; otherwise ship contract harnesses. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** The default build works without sibling paths; integration is not claimed complete when only a placeholder exists. Real Vef/Brynja integration is claimed only against current runnable APIs with target/security evidence; default builds require no sibling directory. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.351.0 implementation stop reached. Run pentest for this exact commit.

## v0.352.0 — Extensibility qualification

**Status:** planned.

**Setup:** baseline 0.351.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Extensibility qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Demonstrate a new operation, new pack, provider swap and transport replacement through the public contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No domain/database/UI rewrite is needed; every accepted extra dependency has a documented purpose and feature budget. Demonstrate operation/pack/provider/transport additions through public contracts with actual execution and documented dependency/size costs. Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.352.0 implementation stop reached. Run pentest for this exact commit.
