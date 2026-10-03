# Phase C: Streaming, artifacts and execution foundations

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.58.0 — Resource ledger

**Status:** planned.

**Setup:** baseline 0.57.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Resource ledger.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Account for input windows, queued bytes, operation state, output, cache, artifacts and provider allocations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A deliberately expanding operation hits the declared budget; reported totals do not omit retained branch buffers. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.58.0 implementation stop reached. Run pentest for this exact commit.

## v0.59.0 — Backpressure scheduler

**Status:** planned.

**Setup:** baseline 0.58.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Backpressure scheduler.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add deterministic ready queues, bounded channels or equivalent credits and partial-output resumption. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Slow consumers cannot grow memory indefinitely; synchronous CPU work does not depend on an async task per node. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.59.0 implementation stop reached. Run pentest for this exact commit.

## v0.60.0 — Stream state machines

**Status:** planned.

**Setup:** baseline 0.59.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Stream state machines.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Standardize EOF, truncation, cancellation, errors, logical record boundaries and output completion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every state transition is tested; EOF is neither duplicated nor inferred from an arbitrary chunk boundary. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.60.0 implementation stop reached. Run pentest for this exact commit.

## v0.61.0 — Multi-input ports

**Status:** planned.

**Setup:** baseline 0.60.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Multi-input ports.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add constant parameters, immutable keys and synchronized data inputs with explicit joining policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Arrival order cannot change XOR/key semantics; unresolved inputs block safely and never grow unbounded buffers. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.61.0 implementation stop reached. Run pentest for this exact commit.

## v0.62.0 — Branches and joins

**Status:** planned.

**Setup:** baseline 0.61.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Branches and joins.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement graph regions, ordered fork/join, fan-out reference sharing and explicit merge policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Reconverging branches, slow consumers and early exits do not deadlock or lose output. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.62.0 implementation stop reached. Run pentest for this exact commit.

## v0.63.0 — Whole-input and seekable adapters

**Status:** planned.

**Setup:** baseline 0.62.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Whole-input and seekable adapters.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Support bounded accumulation, two-pass operations and seekable artifact readers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Non-streaming operations declare their class and reject oversized jobs before uncontrolled allocation. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.63.0 implementation stop reached. Run pentest for this exact commit.

## v0.64.0 — Native artifact storage

**Status:** planned.

**Setup:** baseline 0.63.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Native artifact storage.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Introduce staged artifacts, immutable manifests, range reads, leases and verified finalization on local disk. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Crash simulation cannot expose a partial artifact as complete; offsets and lengths are checked. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.64.0 implementation stop reached. Run pentest for this exact commit.

## v0.65.0 — Browser artifact storage

**Status:** planned.

**Setup:** baseline 0.64.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser artifact storage.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement IndexedDB metadata and optional OPFS chunk storage with memory/file fallbacks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Firefox and other supported browsers work without optional APIs; quota failures never trigger silent upload. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.65.0 implementation stop reached. Run pentest for this exact commit.

## v0.66.0 — Storage transaction discipline

**Status:** planned.

**Setup:** baseline 0.65.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Storage transaction discipline.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add transaction-completion waits, chunk manifests, orphan cleanup and storage schema migrations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Aborted transactions and interrupted writes are reported; no successful-write result precedes commit confirmation. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.66.0 implementation stop reached. Run pentest for this exact commit.

## v0.67.0 — Semantic content identities

**Status:** planned.

**Setup:** baseline 0.66.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Semantic content identities.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define canonical typed parameters, ordered ports, operation revision and chunk-independent input digests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Repartitioning input leaves identity unchanged; different parameters or operation semantics never reuse an entry accidentally. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.67.0 implementation stop reached. Run pentest for this exact commit.

## v0.68.0 — Selective computation cache

**Status:** planned.

**Setup:** baseline 0.67.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Selective computation cache.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Cache only deterministic, completed, permitted jobs using immutable input identities or completed spool hashes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unknown streams are not fully buffered merely to attempt an early hit; secrets and failed jobs are excluded by default. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.68.0 implementation stop reached. Run pentest for this exact commit.

## v0.69.0 — Cache lifecycle

**Status:** planned.

**Setup:** baseline 0.68.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cache lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add per-workspace quotas, reference pinning, eviction, cancellation cleanup and encrypted-at-rest hooks where configured. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Eviction cannot delete a live artifact; cache misses and storage failures do not corrupt authoritative recipes. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.69.0 implementation stop reached. Run pentest for this exact commit.

## v0.70.0 — Bounded control-flow IR

**Status:** planned.

**Setup:** baseline 0.69.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bounded control-flow IR.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Represent labels, conditional branches, bounded repeats, registers and subrecipes separately from DAG regions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Graph-cycle rejection does not mistakenly eliminate required recipe loops; iteration/work budgets are enforced. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.70.0 implementation stop reached. Run pentest for this exact commit.

## v0.71.0 — Execution provenance

**Status:** planned.

**Setup:** baseline 0.70.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Execution provenance.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Record operation revisions, argument redactions, input references, diagnostics and exact reproducibility conditions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Sensitive arguments stay out of logs; nondeterministic jobs cannot masquerade as reproducible cached results. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.71.0 implementation stop reached. Run pentest for this exact commit.

## v0.72.0 — Engine stress qualification

**Status:** planned.

**Setup:** baseline 0.71.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Engine stress qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise huge streams, joins, cancellation, expansion bombs, temporary storage exhaustion and corrupt artifacts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Measured memory stays within each declared profile and errors remain recoverable; no universal constant-memory claim. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.72.0 implementation stop reached. Run pentest for this exact commit.
