# Phase P: Qualification and general-availability readiness

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.357.0 — Scope freeze

**Status:** planned.

**Setup:** baseline 0.356.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Scope freeze.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Freeze the 1.0 reference commit, operation revisions, recipe schema, API and required browser profiles. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Later upstream additions enter a separate backlog; security fixes remain eligible for inclusion. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.357.0 implementation stop reached. Run pentest for this exact commit.

## v0.358.0 — Catalogue audit

**Status:** planned.

**Setup:** baseline 0.357.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Catalogue audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Independently reconcile every operation and argument against the pinned baseline and category/source inventories. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No unexplained omissions, duplicate counting or native-only substitutions inflate the compatibility claim. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.358.0 implementation stop reached. Run pentest for this exact commit.

## v0.359.0 — Workflow and UI audit

**Status:** planned.

**Setup:** baseline 0.358.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Workflow and UI audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Verify save/load, links, multiple inputs, breakpoints, offsets, Magic and complete control flow. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Workbench parity is demonstrated beyond unit tests; safety differences are documented prominently. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.359.0 implementation stop reached. Run pentest for this exact commit.

## v0.360.0 — Cross-target conformance

**Status:** planned.

**Setup:** baseline 0.359.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cross-target conformance.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run native and actual Chromium, Firefox and WebKit suites with and without optional browser features. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Required capabilities work on the published baseline; simulated wasm compilation alone is not sufficient. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.360.0 implementation stop reached. Run pentest for this exact commit.

## v0.361.0 — Resource and denial-of-service audit

**Status:** planned.

**Setup:** baseline 0.360.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Resource and denial-of-service audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Fuzz parsers, recipe compilation, regex, queries, archives, images and plugin host interfaces. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Memory/work/depth/output limits hold; discovered crashes and hangs are triaged and fixed before release. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.361.0 implementation stop reached. Run pentest for this exact commit.

## v0.362.0 — Unsafe and dependency audit

**Status:** planned.

**Setup:** baseline 0.361.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Unsafe and dependency audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Review unsafe islands, crypto providers, build scripts, generated tables and transitive dependency changes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No unreviewed dependency exception or known unmitigated high-severity issue remains in the release profile. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.362.0 implementation stop reached. Run pentest for this exact commit.

## v0.363.0 — API and authorization assessment

**Status:** planned.

**Setup:** baseline 0.362.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** API and authorization assessment.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise adversarial authentication, sessions, object permissions, uploads, egress and worker isolation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Confirmed critical/high findings are fixed and regression-tested; accepted lower risks have owners and rationale. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.363.0 implementation stop reached. Run pentest for this exact commit.

## v0.364.0 — Data and cache assessment

**Status:** planned.

**Setup:** baseline 0.363.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Data and cache assessment.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Verify secret handling, cache isolation, completed-artifact publication, deletion and backup behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Cross-tenant cache probing and partial-result disclosure tests fail closed; documentation matches actual retention. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.364.0 implementation stop reached. Run pentest for this exact commit.

## v0.365.0 — Accessibility and usability assessment

**Status:** planned.

**Setup:** baseline 0.364.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Accessibility and usability assessment.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test realistic tasks with keyboard, screen readers, high zoom, narrow layouts and error recovery. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Essential tasks have non-canvas alternatives; accessibility failures are fixed rather than deferred to native apps. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.365.0 implementation stop reached. Run pentest for this exact commit.

## v0.366.0 — Performance characterization

**Status:** planned.

**Setup:** baseline 0.365.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Performance characterization.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Publish reference hardware/browser measurements for startup, interaction, throughput, memory and cancellation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Claims distinguish streaming from whole-input operations and cold from warm caches; no invented speedup multipliers. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.366.0 implementation stop reached. Run pentest for this exact commit.

## v0.367.0 — Supply-chain release proof

**Status:** planned.

**Setup:** baseline 0.366.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Supply-chain release proof.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Produce dependency/asset manifests, license notices, signed checksums and reproducibility evidence for distributed artifacts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Independent clean builds can verify the release process; supplied models/fonts/data are licensed for redistribution. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.367.0 implementation stop reached. Run pentest for this exact commit.

## v0.368.0 — Migration and disaster drill

**Status:** planned.

**Setup:** baseline 0.367.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Migration and disaster drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Re-run PostgreSQL/MySQL portability, schema upgrade/rollback and metadata/artifact restore on release candidates. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recovery preserves recipe revision and authorization invariants; operational instructions are executable. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.368.0 implementation stop reached. Run pentest for this exact commit.

## v0.369.0 — Documentation and SDK freeze

**Status:** planned.

**Setup:** baseline 0.368.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Documentation and SDK freeze.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Finalize API reference, operation docs, extension guide, offline setup, threat model and migration contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Examples are exercised in CI; docs disclose compatibility limits and browser-owned TLS boundaries. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.369.0 implementation stop reached. Run pentest for this exact commit.

## v0.370.0 — Release-candidate rehearsal

**Status:** planned.

**Setup:** baseline 0.369.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Release-candidate rehearsal.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Produce a feature-frozen candidate build and run the full acceptance checklist with representative users. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Blocking issues produce further 0.x releases; the version number cannot waive missing functionality or security gates. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.370.0 implementation stop reached. Run pentest for this exact commit.

## v0.371.0 — GA acceptance decision

**Status:** planned.

**Setup:** baseline 0.370.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GA acceptance decision.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Assemble evidence for all mandatory capabilities, parity matrices, security, accessibility, recovery and provider boundaries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Advance to 1.0.0-rc only when every mandatory gate passes; otherwise continue 0.241.0 and beyond with concrete gap releases. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.371.0 implementation stop reached. Run pentest for this exact commit.
