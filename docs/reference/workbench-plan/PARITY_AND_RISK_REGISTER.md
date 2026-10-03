# Parity, Risk and Release-Evidence Register

**Planning date:** 2 October 2026.  
**Status:** planning controls and templates, not a completed implementation assessment.  
**Reference reviewed:** CyberChef v11.5.0 package and operation categories, with selected operation source files and separately identified moving-branch sources.  
**Immutable baseline commit:** to be resolved and recorded in 0.2.0. No commit hash or exact complete-operation count is invented here.

The attached Gemini draft was reviewed as design input. Its code was not compiled or adopted. This register distinguishes source-backed scope, proposed architecture and work still needed to establish conformance. Source IDs refer to the source register in `ARCHITECTURE.md`.

## 1. What is and is not verified at planning time

The reference contains a broad catalogue beyond encodings: cryptographic and public-key operations, queries and structured formats, compression, flow control, forensic operations, media and networking [S03]. Selected source review establishes concrete compatibility hazards: backward jumps [S05], existing browser workers [S06], XRegExp semantics [S20], a user-triggered HTTP operation [S10], YARA via a Wasm provider [S23], and PDF presentation using a browser surface [S24]. These findings inform the architecture; they are not evidence that a Rust replacement already implements any operation.

Rust 1.99.0 release availability was checked [S01]. Suggested third-party providers and frameworks have not been compiled together for this project. No performance multiplier, audited-security status, validated complete dependency count, or complete per-operation inventory is claimed.

The initial inventory must enumerate the selected immutable checkout, not just copy category labels. Categories can contain the same operation more than once, implementations can have aliases or variants, and a UI feature can be missing despite a complete operation-name list.

## 2. Baseline inventory procedure

At 0.2.0, resolve the selected tag to its commit and retain the source archive or reproducible checkout reference with integrity hashes. Record the exact package version, source paths and relevant upstream notices. Enumerate the registry, categories, operation implementations, argument definitions and tests; compare the sets and flag differences. Review the web features independently: saving/loading, links, inputs, auto/manual execution, breakpoints, selection mapping, rendering, offline packaging and error presentation.

Do not execute arbitrary repository setup scripts just to obtain a list. The reference test runner is a separately isolated development tool, not a production dependency. Import only fixtures and source material whose redistribution conditions have been reviewed; independent small test vectors and attributed specification fixtures are preferred where practical.

A human-reviewed manifest becomes the scope authority. Each missing operation, argument variant, data conversion or required local execution path is an owned task. The already-observed current-branch certificate-bundle parser [S04] enters the initial reconciliation and X.509 delivery, with its adopted source commit recorded. Later upstream additions are recorded in a separate delta manifest. Adopt urgent security corrections deliberately, but do not allow a permanently moving feature baseline to make 1.0 undefinable.

## 3. Required operation record

The following is an **illustrative schema shape**, not an assertion that the example has passed tests:

```json
{
  "reference": {
    "repository": "gchq/CyberChef",
    "tag": "v11.5.0",
    "commit": null,
    "source_path": "src/core/operations/FromBase64.mjs",
    "name": "From Base64"
  },
  "operation_id": "encoding.base64.decode",
  "semantic_revision": 1,
  "status": "not_assessed",
  "arguments": [],
  "input_output_semantics": "to_be_specified",
  "required_targets": ["browser_local", "native"],
  "implemented_targets": [],
  "parity": "gap",
  "fixtures": [],
  "limits": null,
  "capabilities": [],
  "provider": null,
  "license_review": "pending",
  "owner": null,
  "notes": "Argument variants and reference source must be verified at inventory time."
}
```

Add category memberships, aliases, help behavior, invalid-input policy, output formatting, text model, deterministic status, cache sensitivity, data-table/model versions and known safe differences. The required targets express the project’s native/browser goal; upstream availability still needs its own field where behavior differs by host.

Use statuses `not_assessed`, `specified`, `implemented`, `verified`. Track parity independently as `exact`, `equivalent_representation`, `documented_safe_difference`, or `gap`. An implemented operation with unverified arguments is not verified. A native implementation alone does not close browser-local parity. A documented safe difference cannot be used to hide removed analysis functionality.

## 4. Coverage measurements that resist misleading claims

Report at least five independent matrices: operations, argument/semantic variants, complete recipes, workbench features and execution targets. Keep deterministic byte equivalence separate from useful equivalent representations such as an image/table viewer. Display verified/required totals and the unverified items, rather than a single weighted marketing percentage.

For example, 100 operations with one supported default each do not imply 100 complete operations when those operations expose additional modes and encodings. Categories must not multiply the same operation into multiple successes. A provider that compiles for Wasm but has not been executed in a supported browser is not browser-verified.

For recipe tests, include interactions that isolated operation tests miss: repeated EOF, split UTF sequences, disabled steps, registers, backward jumps, nested forks, multi-input timing, branch joins, truncated compressed data, invalid crypto authentication and side-effect policy. Differential tests compare the selected compatibility profile; safe defaults may intentionally require a user to select that profile rather than inherit historical permissiveness.

## 5. Hard-risk register

All risks below are **open planning risks** until implementation evidence closes them. Release ranges are targets, not assurances that a suitable library already exists. Every row has an early decision point so that a hard dependency is not discovered only near 1.0.

| ID | Risk | Early investigation | Main delivery | Evidence required / fallback |
|---|---|---|---|---|
| R01 | Full catalogue larger than familiar encoders | 0.2.0–0.3.0 | All operation phases; 0.195.0 and 0.227.0 audits | Machine inventory plus reviewed source/argument reconciliation. Extend 0.x for residual operations; never omit them from the denominator. |
| R02 | XRegExp/JavaScript regex is not Rust regex | 0.12.0 and 0.27.0 | 0.193.0, with provider work earlier | Dialect corpus for lookaround, backreferences where required, Unicode, captures, replacement and legacy output. Approve a qualified implementation strategy; keep safe regex distinct. |
| R03 | UTF-16 versus UTF-8/Unicode semantics | 0.3.0, 0.23.0–0.26.0 | All text and language operations | Code-unit/scalar/grapheme and invalid-surrogate fixtures. Explicit compatibility representations; no global lossy conversion. |
| R04 | Query languages are full interpreters | 0.12.0 | 0.77.0–0.79.0 and 0.90.0 | Exact discovered XPath/CSS/JSON query dialects, diagnostics and cost limits. A different query engine is not equivalent by name. |
| R05 | YARA variants/modules differ | 0.12.0 | 0.161.0–0.162.0 | Rule and module corpus on native/browser, match offsets and diagnostics, killability. Resolve actual semantics; YARA-like subset is insufficient. |
| R06 | Long-tail cryptographic provider availability | 0.12.0 | 0.106.0–0.150.0 | Independent vectors, exact modes/parameter sets, provider review and browser builds. More 0.x implementation work if no adequate Rust provider exists. |
| R07 | OpenPGP is broader than packet parsing | 0.12.0 | 0.143.0–0.145.0 | Encrypt/decrypt, signatures, key handling, format variants, integrity staging and interoperability. Parsing-only support cannot close the family. |
| R08 | Compression variants and decompression bombs | 0.12.0 | 0.91.0–0.105.0 | Dictionary, output, nested-member, CPU and disk budgets plus malformed corpus. Limit or reject safely; do not promise every input size works. |
| R09 | Media/OCR/disassembly dependency footprint | 0.12.0 | 0.160.0 and 0.166.0–0.180.0 | Required architectures/codecs/languages, licensed assets, local browser execution and measured memory. Optional loading is allowed; compulsory server upload is not parity. |
| R10 | Cancellation does not stop blocking work | 0.8.0–0.9.0 | 0.31.0–0.45.0, server isolation and qualification | Cooperative checkpoints plus worker/process termination; stale-generation suppression and no successful artifact publication after cancellation. |
| R11 | Bounded DAG queues can deadlock or retain huge memory | 0.31.0–0.35.0 | 0.45.0 and 0.230.0 | Tiny-budget reconverging branch tests, fair readiness rules, explicit join ordering and complete allocation accounting. |
| R12 | Cache identity/sensitivity errors | 0.39.0–0.42.0 | 0.45.0 and 0.233.0 | Chunk-independent hashes, semantic revisions, parameter framing, completed manifests, tenant isolation and secret exclusions. Cache stays optional. |
| R13 | Browser storage/feature differences | 0.8.0 and 0.38.0–0.39.0 | 0.59.0–0.60.0 and 0.229.0 | Actual supported browsers, quota failures, transaction abort, interrupted upgrades and no-SAB/no-OPFS paths. No feature detection result triggers an upload silently. |
| R14 | Database-independent interface hides PostgreSQL behavior | 0.64.0–0.66.0 | 0.216.0–0.219.0 and 0.237.0 | Shared repository suite on real MySQL and PostgreSQL plus logical round-trip migration. Add backend SQL/migrations, not domain branches. |
| R15 | TLS leaks through transitive clients | 0.11.0 and 0.66.0 | 0.206.0–0.210.0 | Inventory inbound/outbound HTTP, identity fetching, database and object-storage TLS. Alternate/mock connectors prove the seam; browser TLS is explicitly excluded. |
| R16 | Vef/Brynja APIs/readiness are unknown | Early interface ADRs | 0.206.0–0.210.0, or later integration | Do not invent sibling APIs. Ship tested boundaries first; real adapters require protocol/security qualification and do not block a working initial provider. |
| R17 | Untrusted Wasm plugin is treated as automatically safe | 0.12.0 feasibility; design before 0.200.0 | 0.200.0–0.205.0 | Allowlisted imports, separate memory/worker, resource controls, capability checks and adversarial host-call tests. Disable third-party plugins where guarantees are insufficient. |
| R18 | Remote API turns a local tool into an exfiltration service | 0.14.0 | 0.61.0–0.75.0 and 0.232.0 | Explicit execution location, per-object authorization, SSRF prevention, restricted workers and no default payload telemetry. Public execution remains off until gates pass. |
| R19 | Recipe interchange loses loops/options | 0.2.0 and 0.43.0 | 0.181.0–0.195.0 | Forward/backward jumps, nested flow, argument defaults and nonrepresentable export diagnostics. Unknown operations never become identity functions. |
| R20 | Licensing/data assets block distribution | 0.2.0 and 0.12.0 | Every provider change; 0.236.0 | Record notices and redistribution review for code, test corpora, Unicode tables, fonts, models and signatures. Replace unsuitable assets or keep the capability open; do not assume all upstream dependencies share one license. |

### What happens when a provider does not exist?

There is no honest universal promise that every required Rust/no_std provider is already mature, feature-complete and browser-ready. Use the feasibility release to establish that evidence. Implement a bounded, independently tested Rust provider where the work is tractable; extend the roadmap when it is substantial. Minimal dependencies is a preference constrained by correctness and security, not a mandate to handwrite cryptographic primitives casually.

A non-Rust runtime or translated foreign-code provider is a separate explicit architecture decision requiring acknowledgement of its effect on the Rust-first goal, attack surface, licenses and distribution. It must not be silently added and then advertised as an entirely Rust implementation. This plan does not preapprove that exception. A server-only workaround likewise remains a browser parity gap.

## 6. Quantitative test targets, not measured achievements

The architecture proposes conservative initial profiles: 64 KiB automatic previews, 128 MiB tracked browser-engine memory plus separately measured host/UI overhead, and a 512 MiB example native worker profile. Adjust from measured workloads and make limits visible. These are not universal maximum file sizes or claims about what the current code already achieves.

Measure responsiveness, cooperative cancellation latency, worker hard-stop behavior, throughput, peak retained bytes, total temporary storage and cold/warm startup separately. Test large streaming fixtures that exceed Wasm linear memory using bounded windows, and test whole-input operations against their explicit lower input limits. A virtual viewer’s small visible-byte window is not the whole application memory footprint.

Security and correctness tests run throughout development. Final assessments repeat them on exact distribution artifacts; they do not replace early review.

## 7. Evidence bundle required for 1.0.0

The release owner assembles the pinned inventory and semantic mapping; complete operation/argument/workflow/target reports; differential fixture provenance; browser and native results; limit/fuzz/crash reports; security assessment and fixes; public API/recipe compatibility policy; current dependency and asset manifests; offline package verification; PostgreSQL deployment/restore evidence; real second-database portability results; HTTP/TLS replacement contract reports; and accessibility/performance measurements.

An unresolved required operation, missing argument behavior, browser-local gap, severe unmitigated vulnerability, broken restore process or silently incompatible recipe migration prevents 1.0.0. A future sibling provider not being ready does not prevent 1.0 when the initial provider is qualified and the replacement boundary is proven. Desktop/mobile packaging is intentionally absent until after this gate.
