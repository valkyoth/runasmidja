# Bounded Pass Verification

Status: mandatory planning/acceptance contract; enforcement is implemented only
where explicitly listed in [security controls](security-controls.md). Scope
manifests, product suites and trusted distribution attestations are future work.

Each handoff keeps its original acceptance and adds reviewed strict verification.
Source-bundle family gates are checklists for each named split topic; they do not
make one cipher/dialect owner implement all its siblings. Close a source owner
only after all mapped passes qualify. Additional inventory gaps get new minors.

| Gate | Required closure |
| --- | --- |
| G0 Scope/prerequisites | Reviewed manifest names exact variants/arguments/defaults, target/feature profiles, semantic/provider/dataset revisions, numeric resource/deadline ceilings, capability policy, prerequisite evidence, fixture provenance, test IDs and evidence locations. TBD/missing fields block acceptance. |
| G1 Repository/build | Exact candidate passes scripts/checks.sh and applicable reviewed no_std/no-alloc, alloc, browser, native and optional-service graphs. First-party unsafe is forbidden; every executable code file is <=500 lines. Real dependency/feature/lint/API isolation evidence accompanies admission. |
| G2 Semantics | All declared variants/arguments/defaults/errors have independent/reference vectors and target agreement. For selected short streaming corpus cases of lengths 1–12 bytes exhaust nonempty input partitions (2^(n-1), at most 2,048 per 12-byte case); test empty windows separately, output backpressure, large randomized partitions and logical error offsets. A round trip alone is not an independent oracle. |
| G3 Resources/lifecycle | Each limit L has L-1/L/L+1 and unknown-length cases as applicable; checked counters/reservations cannot wrap. Test EOF/error/cancel/repeated finish/stale completion, tiny credits, cleanup and measured hard termination for noncooperative providers. Child work cannot reset whole-run limits. |
| G4 Actual hosts | Execute claimed built browser/native/service/provider profiles plus malformed, permission, fault, revocation, outage, crash and isolation negatives. Compilation/mocks/skips never qualify runtime support. |
| G5 Supply/privacy/docs | Verify freshness, advisories, licenses, source/assets/fixture provenance and SBOM/notices. Update threat controls, limitations, parity, CHANGELOG/notes. Sentinel tests cover unapproved serialization/log/cache/index/URL/persistence boundaries. |
| G6 Assessment | Before each minor/patch/RC/tag, assess exact source with findings, tested remediation/retest, no unresolved critical/high blockers and trusted independent review/identity. Report shape or passing tests do not attest PASS; metadata readiness is separate. |
| G7 Distribution | For distributions/RC/GA, bind reviewed assessment to exact artifacts/packs/models/SBOM/toolchain/provenance/signing and required target/CI/CodeQL Default/settings evidence. Execute applicable upgrade/restore/accessibility/performance and cumulative scope checks. |

Record actual commands, versions, inputs, profiles, hashes, exit status, findings
and limitations. Keep immutable historical evidence dated to its reviewed
source; present summaries link later revisions instead of rewriting old numbers.
Planning status stays planned until an implementation pass records its evidence.
Evolve the current planned-only roadmap test/status schema in that bounded pass;
do not mark a row shipped merely because its handoff exists.

G7 never permits feature security tests to wait for the final release. The
current source/report script verifies report format/digest/lineage and presence
of an SBOM file; it authenticates neither assessor nor distribution artifacts.
Its planned trust-contract and distribution-binding owners must close that gap.
See [release runbook](RELEASE_RUNBOOK.md) and [gap reconciliation](gap-reconciliation-2026-10-03.md).
