# Phase P: Qualification and general-availability readiness

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.372.0 — Scope freeze

**Status:** planned.

**Setup:** baseline 0.371.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Scope freeze.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Freeze the 1.0 reference commit, operation revisions, recipe schema, API and required browser profiles. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Later upstream additions enter a separate backlog; security fixes remain eligible for inclusion. Freeze immutable reference/deltas/schema/API/pack/browser profiles and mandatory inventory; later upstream additions have separate owners, security fixes remain reviewed. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.372.0 implementation stop reached. Run pentest for this exact commit.

## v0.373.0 — Catalogue audit

**Status:** planned.

**Setup:** baseline 0.372.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Catalogue audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Independently reconcile every operation and argument against the pinned baseline and category/source inventories. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No unexplained omissions, duplicate counting or native-only substitutions inflate the compatibility claim. Independent reconciliation finds zero unexplained missing operations/arguments/aliases/defaults or double-counting; native-only substitutions cannot close browser rows. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.373.0 implementation stop reached. Run pentest for this exact commit.

## v0.374.0 — Workflow and UI audit

**Status:** planned.

**Setup:** baseline 0.373.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Workflow and UI audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Verify save/load, links, multiple inputs, breakpoints, offsets, Magic and complete control flow. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Workbench parity is demonstrated beyond unit tests; safety differences are documented prominently. Actual user workflows cover library/sharing/multiple input/debug/offset/Magic/loops with negatives and declared safe differences, beyond unit tests. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.374.0 implementation stop reached. Run pentest for this exact commit.

## v0.375.0 — Cross-target conformance

**Status:** planned.

**Setup:** baseline 0.374.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cross-target conformance.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run native and actual Chromium, Firefox and WebKit suites with and without optional browser features. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Required capabilities work on the published baseline; simulated wasm compilation alone is not sufficient. Exact built artifacts run in supported Chromium/Firefox/WebKit and native profiles with optional APIs both enabled/absent; skipped profiles cannot count as passed. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.375.0 implementation stop reached. Run pentest for this exact commit.

## v0.376.0 — Resource and denial-of-service audit

**Status:** planned.

**Setup:** baseline 0.375.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Resource and denial-of-service audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Fuzz parsers, recipe compilation, regex, queries, archives, images and plugin host interfaces. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Memory/work/depth/output limits hold; discovered crashes and hangs are triaged and fixed before release. Persist parser/query/regex/archive/media/plugin/recipe fuzz regressions; work/depth/output/memory/disk limits and hard-kill cleanup pass adversarial corpora. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.376.0 implementation stop reached. Run pentest for this exact commit.

## v0.377.0 — Unsafe and dependency audit

**Status:** planned.

**Setup:** baseline 0.376.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Unsafe and dependency audit.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Review unsafe islands, crypto providers, build scripts, generated tables and transitive dependency changes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No unreviewed dependency exception or known unmitigated high-severity issue remains in the release profile. Review exact shipped transitive/build/generated/provider graphs and third-party unsafe/security/license risks; first-party unsafe remains forbidden without exception from reference wording. Every admitted dependency/profile has current source and applicable runtime evidence. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.377.0 implementation stop reached. Run pentest for this exact commit.

## v0.378.0 — API and authorization assessment

**Status:** planned.

**Setup:** baseline 0.377.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** API and authorization assessment.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise adversarial authentication, sessions, object permissions, uploads, egress and worker isolation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Confirmed critical/high findings are fixed and regression-tested; accepted lower risks have owners and rationale. Independent API/auth/egress/worker assessment on exact candidate artifacts closes critical/high findings with tested remediation and scoped lower-risk disposition. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.378.0 implementation stop reached. Run pentest for this exact commit.

## v0.379.0 — Data and cache assessment

**Status:** planned.

**Setup:** baseline 0.378.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Data and cache assessment.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Verify secret handling, cache isolation, completed-artifact publication, deletion and backup behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Cross-tenant cache probing and partial-result disclosure tests fail closed; documentation matches actual retention. Sentinel secret/payload and tenant probes across cache/search/staging/retention/backups show no unauthorized disclosure or partial authenticated result publication. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.379.0 implementation stop reached. Run pentest for this exact commit.

## v0.380.0 — Accessibility and usability assessment

**Status:** planned.

**Setup:** baseline 0.379.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Accessibility and usability assessment.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test realistic tasks with keyboard, screen readers, high zoom, narrow layouts and error recovery. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Essential tasks have non-canvas alternatives; accessibility failures are fixed rather than deferred to native apps. Realistic tasks pass manual keyboard/screen-reader/zoom/narrow-layout/error recovery, with essential graph/canvas alternatives and resolved blockers. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.380.0 implementation stop reached. Run pentest for this exact commit.

## v0.381.0 — Performance characterization

**Status:** planned.

**Setup:** baseline 0.380.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Performance characterization.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Publish reference hardware/browser measurements for startup, interaction, throughput, memory and cancellation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Claims distinguish streaming from whole-input operations and cold from warm caches; no invented speedup multipliers. Publish reproducible cold/warm startup/interaction/throughput/copy/memory/disk/cancel distributions on declared corpus/hardware; claims use equivalent correct results. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.381.0 implementation stop reached. Run pentest for this exact commit.

## v0.382.0 — Supply-chain release proof

**Status:** planned.

**Setup:** baseline 0.381.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Supply-chain release proof.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Produce dependency/asset manifests, license notices, signed checksums and reproducibility evidence for distributed artifacts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Independent clean builds can verify the release process; supplied models/fonts/data are licensed for redistribution. Clean independent build verifies exact artifact/SBOM/model/pack hashes, notices and trusted signing/provenance; mutable or unidentified assets block release. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.382.0 implementation stop reached. Run pentest for this exact commit.

## v0.383.0 — Migration and disaster drill

**Status:** planned.

**Setup:** baseline 0.382.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Migration and disaster drill.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Re-run PostgreSQL/MySQL portability, schema upgrade/rollback and metadata/artifact restore on release candidates. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recovery preserves recipe revision and authorization invariants; operational instructions are executable. Rehearse both database directions, schema upgrades/rollback and coordinated recovery on exact RC artifacts; hashes/grants/revisions and runnable restored recipes agree. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.383.0 implementation stop reached. Run pentest for this exact commit.

## v0.384.0 — Documentation and SDK freeze

**Status:** planned.

**Setup:** baseline 0.383.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Documentation and SDK freeze.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Finalize API reference, operation docs, extension guide, offline setup, threat model and migration contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Examples are exercised in CI; docs disclose compatibility limits and browser-owned TLS boundaries. Compile/run public SDK/API/extension/offline examples against exact artifacts; docs disclose limits/support/trust/browser-owned TLS and match schemas. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.384.0 implementation stop reached. Run pentest for this exact commit.

## v0.385.0 — Release-candidate rehearsal

**Status:** planned.

**Setup:** baseline 0.384.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Release-candidate rehearsal.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Produce a feature-frozen candidate build and run the full acceptance checklist with representative users. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Blocking issues produce further 0.x releases; the version number cannot waive missing functionality or security gates. Freeze feature-complete candidate and run cumulative acceptance plus user rehearsal; any missing mandatory capability receives a further bounded 0.x owner. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.385.0 implementation stop reached. Run pentest for this exact commit.

## v0.386.0 — GA acceptance decision

**Status:** planned.

**Setup:** baseline 0.385.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GA acceptance decision.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Assemble evidence for all mandatory capabilities, parity matrices, security, accessibility, recovery and provider boundaries. The retained reference acceptance mentions 0.241.0 as historical reference numbering. Actual additional Runasmidja passes start at v0.387.0; do not reuse historical reference versions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Advance to 1.0.0-rc only when every mandatory gate passes; otherwise continue 0.241.0 and beyond with concrete gap releases. All mandatory five-matrix, resource/security/privacy/accessibility/recovery/provider/artifact gates close before RC; otherwise add 0.x passes, never waive blockers. Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.386.0 implementation stop reached. Run pentest for this exact commit.
