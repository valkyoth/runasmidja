# Phase M: Complete recipe semantics, Magic and compatibility

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.301.0 — Compatibility interpreter

**Status:** planned.

**Setup:** baseline 0.300.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compatibility interpreter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Complete execution of imported reference recipe sequences using the bounded control-flow IR. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recipes with disabled operations, defaults and mixed data types preserve documented semantics. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.301.0 implementation stop reached. Run pentest for this exact commit.

## v0.302.0 — Fork and Merge compatibility

**Status:** planned.

**Setup:** baseline 0.301.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Fork and Merge compatibility.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Map reference branch/delimiter behavior to typed graph regions and ordered joins. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Empty branches, delimiters and nested forks match fixtures independently of runtime chunking. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.302.0 implementation stop reached. Run pentest for this exact commit.

## v0.303.0 — Subsection processing

**Status:** planned.

**Setup:** baseline 0.302.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Subsection processing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded subsequence selection and reinsertion with exact offset/text semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Boundary, Unicode and changing-output-length cases preserve the required surrounding data. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.303.0 implementation stop reached. Run pentest for this exact commit.

## v0.304.0 — Registers and variables

**Status:** planned.

**Setup:** baseline 0.303.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Registers and variables.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement reference register capture/substitution plus typed native variables and secret references. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Scope, escaping, missing registers and lifetime rules are deterministic; secrets do not leak into recipe serialization. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.304.0 implementation stop reached. Run pentest for this exact commit.

## v0.305.0 — Labels and jumps

**Status:** planned.

**Setup:** baseline 0.304.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Labels and jumps.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver forward/backward and conditional jumps with explicit iteration and total-work limits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Looping reference fixtures pass; exhausted limits return a precise diagnostic rather than hang. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.305.0 implementation stop reached. Run pentest for this exact commit.

## v0.306.0 — Return and nested recipes

**Status:** planned.

**Setup:** baseline 0.305.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Return and nested recipes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add early return, comments, subrecipe calls and reusable parameterized recipe blocks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Return scopes and nested budget inheritance are tested; recursion is bounded or rejected by the declared profile. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.306.0 implementation stop reached. Run pentest for this exact commit.

## v0.307.0 — Compatibility recipe importer

**Status:** planned.

**Setup:** baseline 0.306.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compatibility recipe importer.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Import supported JSON and URL recipe encodings into the canonical model with a diagnostic report. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unknown operations/arguments are preserved for review or rejected, never silently dropped. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.307.0 implementation stop reached. Run pentest for this exact commit.

## v0.308.0 — Compatibility exporter

**Status:** planned.

**Setup:** baseline 0.307.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compatibility exporter.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Export representable recipes to the reference format and native full-fidelity format. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unrepresentable graph features produce an explicit report; no misleading successful export loses behavior. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.308.0 implementation stop reached. Run pentest for this exact commit.

## v0.309.0 — Detection primitives

**Status:** planned.

**Setup:** baseline 0.308.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Detection primitives.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add versioned signature, alphabet, entropy and structure detectors with bounded sampling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Detectors explain evidence and uncertainty; a score is not advertised as a calibrated probability without validation. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.309.0 implementation stop reached. Run pentest for this exact commit.

## v0.310.0 — Magic one-step suggestions

**Status:** planned.

**Setup:** baseline 0.309.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Magic one-step suggestions.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Suggest candidate reversible transforms and display previews without changing the active recipe. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Suggestions require user acceptance; network, secret-revealing or expensive actions are excluded by default. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.310.0 implementation stop reached. Run pentest for this exact commit.

## v0.311.0 — Magic bounded search

**Status:** planned.

**Setup:** baseline 0.310.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Magic bounded search.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add multi-layer transform search with deduplication, depth/work budgets and reproducible ranking. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Adversarial recursive inputs terminate; repeated runs on the same data/revision produce stable candidate ordering. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.311.0 implementation stop reached. Run pentest for this exact commit.

## v0.312.0 — Brute-force analysis

**Status:** planned.

**Setup:** baseline 0.311.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Brute-force analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Complete required XOR/rotation/encoding/language-scoring searches and ranked result presentation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Work estimates, candidate limits and cancellation are effective; heavy searches are never automatic by default. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.312.0 implementation stop reached. Run pentest for this exact commit.

## v0.313.0 — Full regex compatibility

**Status:** planned.

**Setup:** baseline 0.312.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Full regex compatibility.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close remaining XRegExp/JavaScript syntax, Unicode, capture, replacement and formatting gaps through the approved strategy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Reference dialect corpus passes locally and natively; safe-regex mode remains separately identified. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.313.0 implementation stop reached. Run pentest for this exact commit.

## v0.314.0 — End-to-end reference recipes

**Status:** planned.

**Setup:** baseline 0.313.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** End-to-end reference recipes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run a broad versioned corpus combining formats, crypto, loops, archives, media and forensic operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Equality criteria cover bytes, structure, diagnostics and allowed nondeterminism; every mismatch has a tracked disposition. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.314.0 implementation stop reached. Run pentest for this exact commit.

## v0.315.0 — Feature-complete parity candidate

**Status:** planned.

**Setup:** baseline 0.314.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Feature-complete parity candidate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reconcile operation, argument, recipe, UI and browser/native matrices against the frozen reference. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No required capability is missing; any open gap creates additional 0.x releases before qualification. Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.315.0 implementation stop reached. Run pentest for this exact commit.
