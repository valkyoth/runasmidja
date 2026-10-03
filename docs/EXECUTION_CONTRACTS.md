# Execution and Sensitivity Contracts

Status: required design, not implemented engine behavior. Owners and exact
versions are listed in [gap reconciliation](gap-reconciliation-2026-10-03.md)
and the generated [release handoffs](RELEASE_PLAN.md).

## First execution and later kernel

The one-operation hex seed uses an earlier tested no_std/no-alloc vocabulary:
checked IDs/offsets/value kinds/errors and byte/work reservations. Its admission
manifest fixes 32 KiB input, 64 KiB output, 4 KiB windows and 256 KiB tracked
engine state, plus positive finite fuel and measured supervisor deadlines.
Host/JS/Wasm overhead is measured separately, not hidden in that tracked bound.
Minimal version/run/generation/length messages, EOF, error and supervisor kill
are concrete seed prerequisites. General recipe compilation, multi-port credit
scheduling and rich protocol evolution remain later passes; do not assume them
or call the seed full recipe parity. Initial limits apply from the first call.

## Step and execution shape

A step takes bounded input/output windows and budget, returning checked counts
and a fallible NeedInput/NeedOutput/Yield/Finished state. Empty input is not EOF.
EOF/finish is explicit; define repeated finish, truncation, error and cancellation
as state transitions. Validate consumed/produced against each window before use;
publish only the produced range. No borrowed window survives a call. Owned
carry/scratch is separately reserved before growth/provider invocation.

Zero output credit cannot discard input; zero-progress yield/retry consumes fuel
or trips a bounded no-progress rule. Finished follows all final output and can
publish once. Terminal paths release reservations once. Multi-input operations
report indexed windows/counts and explicit skew/join/EOF rules.

Separate execution shape from capabilities. Streaming, reduction, bounded-window,
seekable/two-pass and whole-input-bounded shapes can each need network, secrets,
persistence or entropy. The sixth reference category, capability dependence, is
an orthogonal declaration rather than an alternative that hides streaming shape.
Portable synchronous steps do not conceal asynchronous host waits: the host
owns bounded cancellable readiness and returns owned scoped results.

Chunk invariance compares ordered output, terminal success/error and logical
error position across feasible transport partitions; progress frequency and
per-call counts may differ. Charge logical work consistently across partitions,
with transport overhead separately bounded. Deadline/OOM rejection is an
operational failure, never a differently labeled successful transformation.

| Shape | Required evidence |
| --- | --- |
| Streaming | Exact independent results/errors/absolute offsets across input/output partitions, tiny/empty windows and every tail/EOF state; carry and expansion bounds |
| Reduction | Checked accumulators, fixed empty/final semantics, partition-invariant update order or declared float tolerance; provisional samples are not final reductions |
| Bounded window | Window/record L-1/L/L+1, split delimiters/codepoints, hostile long lines/combining sequences; exact above-limit behavior |
| Seekable/two-pass | Immutable revision/hash identity, mutation rejection, bounded source ranges/spool/disk and cancellation; actual artifact prerequisites precede qualification |
| Whole input | Preflight known length and cumulatively bound unknown length, state/provider scratch/output; reject before unreserved allocation/invocation |
| Capability requirement | Missing/revoked/wrong-scope grants deny, retries have explicit side-effect idempotency, imports stay inert, local failure never uploads |

## Scheduler and control flow

Reserve byte credit before enqueueing; message-count bounds alone are inadequate.
Charge allocation capacity, carry/provider scratch, Wasm pages, queues, frames,
previews/indexes/provenance, spool/output/artifacts and fan-out retention. Shared
buffers stay charged until their final consumer releases them. Tiny-credit
diamonds, failed/stalled branches, join skew, fairness and terminal races have
stress fixtures; content hashing/cache lookup cannot hide full-stream buffering.

Dataflow is acyclic within a typed region. Control transfers connect regions;
bounded loop-carried bindings and an explicit frame/program-counter interpreter
handle backward/irreducible compatibility jumps. Do not put cyclic stream
queues into a DAG scheduler. Full Jump/Return/counter-reset/default semantics
need pinned whole-recipe differentials, not assumptions from operation names.

Bound compilation nodes/edges/depth/schema/arguments independently. Runtime uses
monotonic positive global fuel, cumulative output/spool bytes, peak memory,
branch/node counts, register bytes, frame depth and artifact count. Jumps,
subrecipes, cache hits and resumptions never reset them. Checked static nested
loop estimates help admission; expansion and dynamic jumps still need runtime
limits. A finite quantum count proves no termination of a blocking provider
call: browser/process supervisors enforce separate hard deadlines.

## Values, disclosure and publication

Keep bytes, explicitly encoded text, lossless records/tables, artifact collections
and secret capabilities distinct. Exact 64-bit wire offsets use validated decimal
strings/binary values; checked JS indexing rejects out-of-range sizes. Logical
offsets beyond 2^53 use synthetic boundary vectors plus feasible real range tests;
they never claim a physical multi-petabyte browser file worked.

Sensitivity joins relevant inputs, arguments and SecretRefs conservatively.
Declassification is an explicitly reviewed rule; hashing a low-entropy secret
does not make it public. Field/container aggregates inherit sensitivity. Secret
material has no ordinary formatting/serialization/clone/history/cache/index path;
worker/provider buffers and scoped handles carry lifecycle. Reveal/export/copy
requires an explicit disclosure grant and current-generation/permission checks.

Sentinels cover URLs, undo/history, clipboard, IndexedDB, OPFS, CacheStorage,
service-worker caches, searches, diagnostics and output pages. Recipes may carry
payload literals or key parameters, so serialization checks the document itself.
Browser key entry can create DOM/JS/GC copies; minimize them and use a qualified
zeroization provider for owned mutable buffers without claiming total erasure.
Explicit encrypted persistence needs its own authenticated custody/recovery pass.

Authenticated decryption stays in inaccessible bounded confidential staging.
Final tag, generation/lease and current authorization checks precede publication.
Failure/cancel/quota/crash produces no readable result handle or preview; cleanup
is idempotent and large disk staging has declared encryption/retention rules.

The pinned [CyberChef Jump implementation](https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/src/core/operations/Jump.mjs)
contains backward transfers/counter state. Runasmidja's bounded-region rules above
are design decisions; frozen differential fixtures must establish exact parity.
