# Phase M: Complete recipe semantics, Magic and compatibility

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.323.0 — Compatibility interpreter

**Status:** planned.

**Setup:** baseline 0.322.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compatibility interpreter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Complete execution of imported reference recipe sequences using the bounded control-flow IR. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recipes with disabled operations, defaults and mixed data types preserve documented semantics. Bounded compatibility VM executes immutable reference semantics with global fuel, frame/register/output/artifact limits and deterministic errors. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.323.0 implementation stop reached. Run pentest for this exact commit.

## v0.324.0 — Fork and Merge compatibility

**Status:** planned.

**Setup:** baseline 0.323.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Fork and Merge compatibility.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Map reference branch/delimiter behavior to typed graph regions and ordered joins. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Empty branches, delimiters and nested forks match fixtures independently of runtime chunking. Fork/Merge separators/order/branch scopes pass whole-recipe differentials; nested fan-out shares aggregate limits and cannot deadlock joins. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.324.0 implementation stop reached. Run pentest for this exact commit.

## v0.325.0 — Subsection processing

**Status:** planned.

**Setup:** baseline 0.324.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Subsection processing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded subsequence selection and reinsertion with exact offset/text semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Boundary, Unicode and changing-output-length cases preserve the required surrounding data. Subsection selection/replacement uses exact byte/text/regex semantics and scoped state; overlapping/empty/unbounded selections have precise limits. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.325.0 implementation stop reached. Run pentest for this exact commit.

## v0.326.0 — Registers and variables

**Status:** planned.

**Setup:** baseline 0.325.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Registers and variables.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement reference register capture/substitution plus typed native variables and secret references. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Scope, escaping, missing registers and lifetime rules are deterministic; secrets do not leak into recipe serialization. Register substitution/types/lifetimes/defaults match reference; scopes cannot retain unlimited values or expose secret parameters in UI/exports. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.326.0 implementation stop reached. Run pentest for this exact commit.

## v0.327.0 — Labels and jumps

**Status:** planned.

**Setup:** baseline 0.326.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Labels and jumps.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver forward/backward and conditional jumps with explicit iteration and total-work limits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Looping reference fixtures pass; exhausted limits return a precise diagnostic rather than hang. Forward/backward/conditional jumps, missing/duplicate labels and reference counter reset behavior have differential fixtures; global fuel never resets. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.327.0 implementation stop reached. Run pentest for this exact commit.

## v0.328.0 — Return and nested recipes

**Status:** planned.

**Setup:** baseline 0.327.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Return and nested recipes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add early return, comments, subrecipe calls and reusable parameterized recipe blocks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Return scopes and nested budget inheritance are tested; recursion is bounded or rejected by the declared profile. Return/subrecipe semantics pass nested differentials; direct/indirect recursion and frame-depth/output amplification terminate without host-stack overflow. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.328.0 implementation stop reached. Run pentest for this exact commit.

## v0.329.0 — Compatibility recipe importer

**Status:** planned.

**Setup:** baseline 0.328.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compatibility recipe importer.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Import supported JSON and URL recipe encodings into the canonical model with a diagnostic report. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unknown operations/arguments are preserved for review or rejected, never silently dropped. Versioned imports preserve exact names/arguments/control flow/revisions; unknown or malicious operations fail visibly and never autorun. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.329.0 implementation stop reached. Run pentest for this exact commit.

## v0.330.0 — Compatibility exporter

**Status:** planned.

**Setup:** baseline 0.329.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compatibility exporter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Export representable recipes to the reference format and native full-fidelity format. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unrepresentable graph features produce an explicit report; no misleading successful export loses behavior. Export/reimport preserves representable semantics; unsupported native features return a precise error rather than silently flatten loops or drop arguments. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.330.0 implementation stop reached. Run pentest for this exact commit.

## v0.331.0 — Detection primitives

**Status:** planned.

**Setup:** baseline 0.330.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Detection primitives.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add versioned signature, alphabet, entropy and structure detectors with bounded sampling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Detectors explain evidence and uncertainty; a score is not advertised as a calibrated probability without validation. Detectors pin signatures/datasets, validity checks and ordering; bounded scans explain evidence and avoid payload/secret network lookups. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.331.0 implementation stop reached. Run pentest for this exact commit.

## v0.332.0 — Magic one-step suggestions

**Status:** planned.

**Setup:** baseline 0.331.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Magic one-step suggestions.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Suggest candidate reversible transforms and display previews without changing the active recipe. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Suggestions require user acceptance; network, secret-revealing or expensive actions are excluded by default. One-step Magic suggestions are deterministic and explain detector/arguments/cost/capabilities; suggestions never execute effects automatically. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.332.0 implementation stop reached. Run pentest for this exact commit.

## v0.333.0 — Magic bounded search

**Status:** planned.

**Setup:** baseline 0.332.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Magic bounded search.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add multi-layer transform search with deduplication, depth/work budgets and reproducible ranking. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Adversarial recursive inputs terminate; repeated runs on the same data/revision produce stable candidate ordering. Magic search caps depth/candidates/state/output/global fuel; adversarial ambiguous inputs terminate and ordered suggestions reproduce across targets. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.333.0 implementation stop reached. Run pentest for this exact commit.

## v0.334.0 — Brute-force analysis

**Status:** planned.

**Setup:** baseline 0.333.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Brute-force analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Complete required XOR/rotation/encoding/language-scoring searches and ranked result presentation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Work estimates, candidate limits and cancellation are effective; heavy searches are never automatic by default. Brute force declares alphabet/search space/verification/work caps; cancellation and output count limits hold, and legacy search cannot consume unbounded resources. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.334.0 implementation stop reached. Run pentest for this exact commit.

## v0.335.0 — Full regex compatibility

**Status:** planned.

**Setup:** baseline 0.334.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Full regex compatibility.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close remaining XRegExp/JavaScript syntax, Unicode, capture, replacement and formatting gaps through the approved strategy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Reference dialect corpus passes locally and natively; safe-regex mode remains separately identified. Full required JS/XRegExp semantics pass pinned differentials and pathological kill tests; UTF-16/byte offsets and replacements are mapped explicitly. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.335.0 implementation stop reached. Run pentest for this exact commit.

## v0.336.0 — End-to-end reference recipes

**Status:** planned.

**Setup:** baseline 0.335.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** End-to-end reference recipes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run a broad versioned corpus combining formats, crypto, loops, archives, media and forensic operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Equality criteria cover bytes, structure, diagnostics and allowed nondeterminism; every mismatch has a tracked disposition. Complete frozen reference recipes pass all arguments/control flow and target profiles; failures report exact unsupported semantics rather than count operations. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.336.0 implementation stop reached. Run pentest for this exact commit.

## v0.337.0 — Feature-complete parity candidate

**Status:** planned.

**Setup:** baseline 0.336.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Feature-complete parity candidate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reconcile operation, argument, recipe, UI and browser/native matrices against the frozen reference. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No required capability is missing; any open gap creates additional 0.x releases before qualification. Five matrices for operations, arguments/semantics, recipes, UI and targets have zero mandatory gaps; a feature-complete candidate still needs final qualification. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.337.0 implementation stop reached. Run pentest for this exact commit.
