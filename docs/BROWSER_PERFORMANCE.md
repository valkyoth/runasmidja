# Browser and Performance Qualification

Status: required design and initial goals, not observed product performance.
See [versioned owners](gap-reconciliation-2026-10-03.md) and
[verification gates](VERIFICATION_GATES.md).

## Worker, UI and cancellation

The owning origin/page remains trusted; a Dedicated Worker cannot prevent a
malicious page reading input or replacing code. Apply the separate local-only,
offline/network-disabled and remote origin contracts, exact document/worker
headers and real browser negatives in
[browser security profiles](BROWSER_SECURITY_PROFILES.md). Pack/Wasm loading
must work under connect-src none rather than widening it for Fetch convenience.

Keep an accessible Rust DOM UI with the linear input/recipe/output workflow,
manual Run, descriptor-generated forms, keyboard editing and bounded pages.
Leptos remains an outer-adapter candidate selected at current reviewed admission.
An optional graph edits the same IR; essential canvas interactions need DOM/
keyboard alternatives. Imports stay inert and secret/history serialization is
checked at the final boundary. Preview is visibly sampled, cheap/pure, capped
at 64 KiB input with separate state/output/work ceilings; partial samples never
claim complete digests/reductions or authenticated plaintext.

The module Dedicated Worker instantiates the engine/packs. Versioned messages
bind engine/pack revision, run/generation/sequence, bounded metadata/byte counts,
transfers, EOF and terminal lifecycle. Negotiate required capabilities; reject
unknown/oversized/duplicate/reordered/mismatched frames. Bound progress events,
page requests and retained responses with credits/coalescing. Transferred buffers
change ownership, while the Wasm bridge can still copy; measure copy bytes.

Long synchronous Wasm calls cannot process ordinary cancel messages. Give
cooperative quanta real task-level yields so a chain of microtasks cannot starve
message handling; check cancellation around provider/credit/I/O/verification/
publication transitions. Shared atomics are optional and the baseline works
without shared memory. The UI supervisor enforces a measured hard deadline and
terminates/recreates noncooperative workers. Host-owned leases/manifests reconcile
staging after termination, since worker cleanup handlers may never execute.
Recheck generations on async page installation and final publication; old success
cannot replace a newer run. Server fencing remains independent authority.

Actual Chromium/Firefox/WebKit workflows test UI responsiveness during jobs,
event floods, starvation, stale messages/pages, hard kill and optional APIs absent.
Default/offline processing requires no account/services/vault and produces no
payload upload or persistence; explicit local storage/network effects are separate.

## Providers and packs

Introduce minimal first-party pack manifests/loading before heavy feasibility
or query/crypto/media admission. Bind hashes, source/license, ABI/semantic revisions,
dependencies, imports, capability/target support and numeric transfer/decompressed/
compile/instance/retained-memory ceilings. Qualify one small actual worker pack;
later extensibility owners broaden the catalogue/plugin model. Failed/tampered/
incompatible activation preserves the previous set. Optional packs stay out of
the initial dependency/bundle profile. Offline distributions include selected
models/fonts/data without hidden CDN traffic or input upload.

Full regex compatibility freezes JS/XRegExp flags, UTF-16/byte offsets, captures,
replacement and Unicode revisions separately from the safe Rust regex subset.
Compile/match/result limits and hard termination cover pathological providers.
YARA parser/compiler/modules and browser runtime need actual independent admission;
using Wasm internally does not prove browser availability. OpenPGP needs backend/
entropy/secret/side-channel qualification and independent interoperability. OCR
needs model/language/license/hash/accuracy/tensor/startup/cancel/offline evidence;
disassembly needs exact architecture/mode/endian vectors without sample execution.
Native components need qualified browser shims/tooling; core-Wasm and components
are separate ABIs. Non-Rust/executable exceptions need an explicit project decision.

Historical YARA-X issues and experimental Sequoia backend flags are risk prompts,
not determinations about current releases. Freeze exact current provider evidence
at admission, keeping unresolved required target/dialect gaps as 1.0 blockers.

## Initial profiles and measurements

| Profile/measure | Initial goal and closure |
| --- | --- |
| Browser engine | 128 MiB tracked-engine profile; separately measure Wasm high-water, JS transfers/UI/decoder/model overhead and retained memory after cancel |
| Native untrusted worker | 512 MiB actual delegated-kernel memory profile; measure RSS/accounting/OOM and inaccessible failed staging |
| Recipe | Initially 512 nodes/2,048 edges, plus manifest-frozen fuel/frame/register/output/artifact caps; early hex seed uses its smaller explicit profile |
| Interaction/cancel | UI p95 <100 ms and cooperative cancel p95 <200 ms on declared device/corpus; also report p99/max, hard deadline and cleanup completion |
| Large stream | 10 GiB native corpus and feasible browser corpus larger than linear memory; verify full bytes/hash and retained-memory plateau, including ingress/export |
| Bundle/pack | Freeze numeric cold/warm transfer/decode/compile/instantiate/retained-memory regression caps after the alpha; no TBD permits acceptance |

These are initial targets and must be measured/reviewed before claims; they do
not impose a fictitious successful result on a weak device/provider. Scope any
revised profile honestly and retain required semantics/security. The seed never
qualifies full large-input/provider performance.

Measure kernels and end-to-end File/worker/Wasm/artifact/viewer paths separately.
Use fixed corpora for expanding/contracting encodings, reductions, tiny chunks,
skewed joins, whole-input rejects, archives, confidential crypto staging, OCR,
regex and event floods. Record hardware/tool/browser, exact source/artifact/input
hashes, repetitions, cold/warm p50/p95/p99/max, throughput, copies, peak/retained
memory and disk, cancellation and result correctness. Compare equivalent correct
semantics against the actual pinned CyberChef build; it already uses workers.
No universal zero-copy, constant-memory or unmeasured speedup claims.

Reviewed upstream basis: [spawn_local](https://docs.rs/wasm-bindgen-futures/latest/wasm_bindgen_futures/fn.spawn_local.html)
runs on the current thread; [worker processing/termination](https://html.spec.whatwg.org/multipage/workers.html#dom-worker-terminate-dev)
defines worker isolation/lifetime. The scheduling and resource gates above are
Runasmidja design requirements. [Regex documentation](https://docs.rs/regex/latest/regex/)
defines the Rust subset; [YARA-X issue](https://github.com/VirusTotal/yara-x/issues/351)
and [Sequoia backend notes](https://gitlab.com/sequoia-pgp/sequoia/-/raw/main/openpgp/README.md)
must be requalified against the admitted versions.
