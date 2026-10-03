# Gap Reconciliation and Version Owners

Status: reviewed planning revision after `bc39671`; no runtime remediation,
pentest PASS, browser support or performance claim. The submitted gap analysis
was reviewed and then removed as requested. Its input SHA-256 was
`cb73c62bf560c7dcc79363b3a5284155faebc6c03de62f758bfa9e55c284e7d3`.
This document records decisions/evidence, not a replacement copy of that report.

## Verified scope and corrections

Checked current manifests/source/gates/stack scripts: six scaffold crates,
five empty portable leaves/facade, three Rust probe tests, no runtime third-party
dependencies. The engine/browser/API/providers remain unimplemented. The earlier
plan had 371 planned rows: 345 mapped owners for 240 reference workstreams and
26 extra passes. Reproduced two isolated temporary bypass fixtures: an unpinned
CodeQL `.yaml` file and a comment-spoofed no_std crate both returned no policy
issues. Source inspection confirms local-password-first provisioning, persistent
secret copies, scope-label-only container reuse, missing ownership check on stop,
unqualified volume/network reuse, immediate Valkey deletion before expiry, and
report/SBOM-shape checks that do not authenticate assessment or artifacts.

The analysis's executed service/audit claims are reported historical inputs;
they were not rerun or promoted to new evidence here. The live official freshness
check passed with the existing reviewed product/tool/service pins. Host OS/Podman
drift remains outside that scope. No real service or secret state was mutated.

Corrections applied before adopting the proposed gates:

- X.509 and CRL/CSR parsing stays distinct from signature validity, certificate
  trust and revocation completeness. Parsing owners do not silently acquire
  a full trust validator requirement. Inventoried verification actions get their
  own exact policy/negative evidence.
- Offsets above 2^53 need synthetic DTO/range boundaries and feasible actual
  pages, not an invented physical multi-petabyte browser file qualification.
- JWT decoding may inspect untrusted/historical data. Strict configured
  algorithm/key/issuer/audience/time policy applies to explicit verification and
  live sessions; inspection itself never implies trust.
- Historical YARA-X/Sequoia portability/crypto warnings prompt current exact-version
  qualification; they do not establish permanent impossibility or suitability.
- Reference wording about unsafe islands grants no first-party unsafe exception.
  Review admitted third-party unsafe/build/provider graphs under current policy.
- The original acceptance and every source/split owner remain. Family-wide
  strict gates apply to each scoped topic, rather than making one AES/dialect
  pass ship all siblings. No missing target/provider can be excluded silently.

## Bounded owners

The roadmap now has **386 passes**, through **0.386.0**: the original 345 mapped
owners, the existing 26 extras and 15 new prerequisite/qualification passes.
Each generated handoff retains setup, goal, scope, deliverables, verification
and an exact-source pentest exit. Every reference row has an additive reviewed
gate in [generator input](roadmap-input/reference-verification.json).

| Gap/context | Actual revised owner(s) | Required closure |
| --- | --- | --- |
| SEC-01 secret origin | 0.2.0 OpenBao-first provisioning | Vault credentials precede consumers; current owned-resource checks are concrete prerequisites; scoped restart/version reuse, seal/outage/deny/partial/root-revoked and custody-preserving migration tests |
| GATE-01 workflow policy | 0.3.0 | Both YAML suffixes; qualified remote/local/container reference forms and quoted/dynamic negatives; CodeQL Default only |
| GATE-02 / PORT-01 graph admission | 0.4.0 | Reviewed normal/build/dev/target/optional graphs and lint inheritance, actual no-alloc/alloc/Wasm/native builds, no comment-spoof or feature-unification leakage |
| OPS-01 ownership/drift | 0.5.0 | Verify container/network/volume ownership and nonsecret desired configuration before every mutation, including stop; collision/drift tests preserve state |
| EVID-01 cache expiration | 0.7.0 fixture; 0.11.0 lifecycle; 0.122.0–0.123.0 product | Observe TTL/countdown and actual expiry, plus cold restart, eviction/revocation/outage; current EX-option smoke is not expiration proof |
| SEC-02 secret delivery/custody | 0.8.0, 0.9.0, 0.131.0 | Ephemeral delivery/cleanup, private-build/release identity and independent production recovery; OpenBao source policy unchanged |
| REL-01 evidence authority | 0.10.0 trust contract; 0.367.0 distribution binding; 0.382.0 final supply proof | Trusted assessment/reviewer and exact source/artifact/pack/model/SBOM/toolchain/target/CI/signing bindings; formatted PASS alone cannot publish |
| ENG-01 seed prerequisites | 0.13.0 vocabulary before 0.14.0 seed; 0.21.0–0.26.0 full contracts | Checked values/byte-work ceilings and minimal explicit worker messages first; seed is one bounded hex operation, not a future scheduler claim |
| DATA-01 browser sensitivity | 0.27.0 before rich viewers/crypto; 0.285.0 expanded key UX | Conservative sensitivity, scoped disclosure, sentinels across pages/history/storage/network and crash/cancel staging; honest erasure limitations |
| Early heavy pack admission | 0.30.0 manifest, 0.31.0 loader; 0.340.0 expanded lazy catalogue | Actual small worker pack first, verified identity/imports/budgets/offline activation before heavy feasibility/providers |
| Performance evidence | 0.42.0 initial profiles; 0.87.0 engine stress; 0.381.0 cumulative characterization | Declared hardware/corpora/targets; numeric caps and correct cold/warm latency/copy/memory/disk/cancel distributions; no invented speedups |
| Replay/source ordering | 0.78.0–0.80.0 storage before 0.81.0 full seekable adapters | Immutable source/ranges, quota/spool and real artifacts precede full replay; tiny earlier feasibility remains explicitly in-memory bounded |
| ENG-02 loops/amplification | 0.13.0 seed budget, 0.73.0 expanded ledger, 0.85.0 regions; phase M full compatibility | Positive monotonic global fuel/cumulative bytes/registers/frames; region control differs from cyclic stream queues, hard provider deadlines remain required |
| Cross-store publication | 0.112.0 after repository/authority | Real object-finalize/manifest/run/outbox crash cuts with current permissions/fencing and inaccessible orphan reconciliation |
| Remote isolation | 0.119.0 worker, 0.120.0 fault qualification; 0.133.0 exposure gate | Actual kernel restrictions/delegation and descendant kill/cleanup; public routes wait for authority/admission/fencing/egress/TLS/recovery |
| SSRF/hidden transports | 0.125.0 policy, 0.126.0 DNS/connect, 0.127.0 redirect/client qualification | All A/AAAA/peer and retry/pool checks, scoped proxies, total byte/deadline/credential limits, controlled rebinding fixtures |
| Lossless migration | 0.358.0 export, 0.359.0 canonicalization, 0.360.0–0.363.0 actual second DB/drills | Canonical keys/digests/grants/revisions and byte-read artifact hashes match; quiesce/fence, bad export and post-cutover rollback tests; no zero-downtime claim |
| EVID-02 history/status | Every handoff and evidence document | Preserve dated source-specific records; evolve planned-only status tests before recording implementation evidence, never infer shipped behavior from plans |

Existing optional search and vault integration remain mandatory planned work:
SearchService is now **0.20.0**, OpenBao SDK/references/rotation **0.17.0–0.19.0**,
and hosted search **0.113.0–0.118.0**. Both repository/Meilisearch implementations
qualify before 1.0; deployment may disable Meilisearch, and local search stays
local. Shared-collection integration is 0.354.0. Secrets include service initial
admin/master keys, private Rust/build, CI and release; vault startup/recovery
trust retains only the enumerated independent-custody boundary.

## Source distinctions and acceptance

The preserved 240-row reference is unchanged. Reference 0.240.0 maps to actual
0.386.0 GA acceptance; actual version numbers are not reference numbers. The
[earlier search/secret revision](plan-revision-2026-10-03.md) and
[foundation evidence](verification-2026-10-03.md) retain their historical numbers.
Use the generated phase JSON source_version fields for current ownership.

The [execution](EXECUTION_CONTRACTS.md), [browser/performance](BROWSER_PERFORMANCE.md),
[storage/host](STORAGE_HOST_CONTRACTS.md) and [G0–G7 gates](VERIFICATION_GATES.md)
make this additive contract explicit. Small further passes close new inventory
or qualification gaps; neither a count/date nor family title waives 1.0 scope.
Vef/Brynja require current runnable APIs before real integration claims. MySQL
is a pre-1.0 proof adapter until separately supported; PostgreSQL 19 GA remains
a production prerequisite. Desktop/mobile/Aesynx horizons stay post-1.0.

## Verification of this revision

Repository bypasses were reproduced only in temporary fixtures. All 240 reference
gates were reconciled against the baseline and all original owners retained.
`scripts/checks.sh` passed: repository/link/500-line gates, formatting, strict
clippy, debug/release/all-feature Rust tests, rustdoc, bare-metal/Wasm checks and
20 Python tests. New tests prove original acceptance preservation, complete
additive gate coverage, prerequisite ordering, deterministic generated files and
rejection of missing source gates. The original reference bytes remain unchanged.
The official freshness check passed. Pentest remains NOT RUN; no tag, publishing
or runtime-control remediation follows from these planning checks.
