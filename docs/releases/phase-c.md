# Phase C: Streaming, artifacts and execution foundations

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.73.0 — Resource ledger

**Status:** planned.

**Setup:** baseline 0.72.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Resource ledger.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Account for input windows, queued bytes, operation state, output, cache, artifacts and provider allocations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A deliberately expanding operation hits the declared budget; reported totals do not omit retained branch buffers. Allocation capacity, provider scratch, queue retention, previews, fan-out, and disk reservations are charged; failures refund correctly and counters cannot wrap. Whole-run positive fuel and cumulative output/disk/branch/frame/register limits cannot reset on jumps, cache hits or child recipes; each noncooperative provider quantum has a hard host deadline. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.73.0 implementation stop reached. Run pentest for this exact commit.

## v0.74.0 — Backpressure scheduler

**Status:** planned.

**Setup:** baseline 0.73.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Backpressure scheduler.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add deterministic ready queues, bounded channels or equivalent credits and partial-output resumption. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Slow consumers cannot grow memory indefinitely; synchronous CPU work does not depend on an async task per node. Tiny-credit diamonds and stalled/failed joins complete or fail deterministically; no deadlock, starvation, unbounded queue, or credit leak remains. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.74.0 implementation stop reached. Run pentest for this exact commit.

## v0.75.0 — Stream state machines

**Status:** planned.

**Setup:** baseline 0.74.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Stream state machines.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Standardize EOF, truncation, cancellation, errors, logical record boundaries and output completion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every state transition is tested; EOF is neither duplicated nor inferred from an arbitrary chunk boundary. Enumerate input/output/EOF/error/cancel terminal transitions; duplicate EOF/finish and truncated tails cannot busy-loop or produce duplicate completion. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.75.0 implementation stop reached. Run pentest for this exact commit.

## v0.76.0 — Multi-input ports

**Status:** planned.

**Setup:** baseline 0.75.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Multi-input ports.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add constant parameters, immutable keys and synchronized data inputs with explicit joining policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Arrival order cannot change XOR/key semantics; unresolved inputs block safely and never grow unbounded buffers. Multi-port skew, missing/failed input, ordering, and unequal EOF cases follow typed port rules under bounded per-port and aggregate credit. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.76.0 implementation stop reached. Run pentest for this exact commit.

## v0.77.0 — Branches and joins

**Status:** planned.

**Setup:** baseline 0.76.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Branches and joins.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement graph regions, ordered fork/join, fan-out reference sharing and explicit merge policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Reconverging branches, slow consumers and early exits do not deadlock or lose output. Fork/join output ordering is invariant under scheduling; failed branches cancel dependents, and shared buffers stay charged until the last reference releases them. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.77.0 implementation stop reached. Run pentest for this exact commit.

## v0.78.0 — Native artifact storage

**Status:** planned.

**Setup:** baseline 0.77.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Native artifact storage.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Introduce staged artifacts, immutable manifests, range reads, leases and verified finalization on local disk. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Crash simulation cannot expose a partial artifact as complete; offsets and lengths are checked. Real filesystem ranges/staging/integrity pass; traversal/symlink attempts, disk full, partial write, crash, and orphan cleanup cannot expose unfinished payloads. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.78.0 implementation stop reached. Run pentest for this exact commit.

## v0.79.0 — Browser artifact storage

**Status:** planned.

**Setup:** baseline 0.78.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser artifact storage.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement IndexedDB metadata and optional OPFS chunk storage with memory/file fallbacks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Firefox and other supported browsers work without optional APIs; quota failures never trigger silent upload. Real worker IndexedDB/OPFS tests cover transaction completion/abort, quota, schema upgrade, denied persistence, and secret-sentinel exclusion. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.79.0 implementation stop reached. Run pentest for this exact commit.

## v0.80.0 — Storage transaction discipline

**Status:** planned.

**Setup:** baseline 0.79.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Storage transaction discipline.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add transaction-completion waits, chunk manifests, orphan cleanup and storage schema migrations. This pass qualifies local native artifact manifests and browser IndexedDB/OPFS transaction completion, local event/outbox records and orphan recovery only. Hosted SQL manifest/run/outbox publication is owned by v0.112.0, not assumed here. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Aborted transactions and interrupted writes are reported; no successful-write result precedes commit confirmation. Crash local native object-finalize/manifest and browser IndexedDB/OPFS transaction/local-event cut points; idempotent recovery exposes only completed locally authorized artifacts. This proves local storage discipline, not hosted SQL run/manifest/outbox publication, which qualifies in v0.112.0. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.80.0 implementation stop reached. Run pentest for this exact commit.

## v0.81.0 — Whole-input and seekable adapters

**Status:** planned.

**Setup:** baseline 0.80.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Whole-input and seekable adapters.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Support bounded accumulation, two-pass operations and seekable artifact readers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Non-streaming operations declare their class and reject oversized jobs before uncontrolled allocation. Whole-input L-1/L/L+1 and unknown-length cases fail closed; seekable two-pass source mutation rejects, and spooling has real disk/work ceilings. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.81.0 implementation stop reached. Run pentest for this exact commit.

## v0.82.0 — Semantic content identities

**Status:** planned.

**Setup:** baseline 0.81.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Semantic content identities.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define canonical typed parameters, ordered ports, operation revision and chunk-independent input digests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Repartitioning input leaves identity unchanged; different parameters or operation semantics never reuse an entry accidentally. Canonical identities include type, ordered inputs, arguments, semantic/provider/dataset revisions; chunk partition changes no identity and ambiguous framing collides nowhere in fixtures. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.82.0 implementation stop reached. Run pentest for this exact commit.

## v0.83.0 — Selective computation cache

**Status:** planned.

**Setup:** baseline 0.82.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Selective computation cache.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Cache only deterministic, completed, permitted jobs using immutable input identities or completed spool hashes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unknown streams are not fully buffered merely to attempt an early hit; secrets and failed jobs are excluded by default. Only complete deterministic nonsensitive authorized results cache; secret/effectful/staged outputs deny, and cache identity includes current scope/revisions. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.83.0 implementation stop reached. Run pentest for this exact commit.

## v0.84.0 — Cache lifecycle

**Status:** planned.

**Setup:** baseline 0.83.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cache lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add per-workspace quotas, reference pinning, eviction, cancellation cleanup and encrypted-at-rest hooks where configured. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Eviction cannot delete a live artifact; cache misses and storage failures do not corrupt authoritative recipes. TTL/eviction/revocation/poison/outage cases preserve truth and permissions; pending writers or stale grants cannot resurrect entries. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.84.0 implementation stop reached. Run pentest for this exact commit.

## v0.85.0 — Bounded control-flow IR

**Status:** planned.

**Setup:** baseline 0.84.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bounded control-flow IR.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Represent labels, conditional branches, bounded repeats, registers and subrecipes separately from DAG regions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Graph-cycle rejection does not mistakenly eliminate required recipe loops; iteration/work budgets are enforced. Bound compilation, SCC/region structure, frame depth, fuel, registers, output and artifacts; self/nested loops and amplification exhaust budgets predictably. Cyclic control transfers connect bounded regions, not cyclic stream queues; checked static loop estimates supplement monotonic runtime fuel, and irreducible compatibility jumps use a bounded frame/program-counter model. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.85.0 implementation stop reached. Run pentest for this exact commit.

## v0.86.0 — Execution provenance

**Status:** planned.

**Setup:** baseline 0.85.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Execution provenance.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Record operation revisions, argument redactions, input references, diagnostics and exact reproducibility conditions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Sensitive arguments stay out of logs; nondeterministic jobs cannot masquerade as reproducible cached results. Provenance preserves exact source/operation revisions and offset availability; debug/event growth is bounded and records exclude payload/secret values. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.86.0 implementation stop reached. Run pentest for this exact commit.

## v0.87.0 — Engine stress qualification

**Status:** planned.

**Setup:** baseline 0.86.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Engine stress qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Exercise huge streams, joins, cancellation, expansion bombs, temporary storage exhaustion and corrupt artifacts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Measured memory stays within each declared profile and errors remain recoverable; no universal constant-memory claim. Large streaming plateaus in retained memory; adversarial partitions, queue interleavings, cancellation, and all execution classes pass stress/resource fixtures. Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.87.0 implementation stop reached. Run pentest for this exact commit.
