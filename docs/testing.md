# Testing and Evidence

Run `scripts/checks.sh` for format, strict clippy, debug/release/all-feature tests,
rustdoc, no_std bare-metal/Wasm compilation, repository gates and adversarial
Python gate fixtures. No skip silently counts as a pass. Tests validate observable
behavior and failure boundaries rather than copying implementation internals.

Run real service smoke tests with `python3 scripts/stack.py up` and `smoke`, then
repeat after idempotent start and stop/restart. Run the probe locally and in the
provided container test script. This tests foundation behavior; it cannot prove
future product features.

The next pass must prove OpenBao-first secret origin with actual cold-start and
restart fixtures; the current stack smoke suite proves custody/access only.
Add sealed/unavailable/denied vault, partial provisioning, root-revoked restart,
rotation and tmpfs cleanup tests, with sentinel checks across logs, argv,
environment, container metadata, caches and artifacts. Private build/CI grants
need wrong-claim/fork denial evidence; public Rust builds remain secret-free.

Search qualification runs the same hosted metadata/authorization contracts
against real PostgreSQL and Meilisearch, with the optional feature compiled both
ways and each runtime selector. Test stale index after tenant/object revocation,
secret-bearing metadata rejection, hit/snippet/count/facet privacy, asynchronous
task failures, outbox crash/reorder/delete replay, outage/fallback and backend
cutover. Disabled mode must need no Meilisearch process or credentials; operation
and browser-local recipe search must generate no hosted search traffic.

Future releases add fixtures before their support claims: independent/reference
vectors and all arguments; exhaustive small chunk partitions; property/fuzz
malformed inputs; budgets/EOF/cancellation; browser/native differentials; actual
Chromium/Firefox/WebKit; PostgreSQL/MySQL repositories; TLS trust denials;
crash/restore/upgrade; plugin/provider isolation; accessibility and measured
performance. Every behavior has a test ID in the release scope manifest.

Crypto needs independent known-answer/interoperability evidence, secret-taint
and failure-publication tests, and appropriately scoped side-channel evidence.
Miri/fuzz/model tools are selected for applicable behavior and reviewed/current
before admission, not added as fictitious configured gates.

Permanent evidence records candidate source/artifact digests, commands, tool
versions, inputs, profiles, exit status, findings and limitations. Missing evidence
blocks its support claim and 1.0 acceptance. Every tag, including patches and
RCs, requires an exact-source pentest with remediation and regression retesting.

The [strict gates](VERIFICATION_GATES.md) require reviewed per-pass numeric scope,
selected short-corpus partitions through 12 bytes, every declared resource-bound
edge, real host faults and trusted assessment/distribution identity. Detailed
[execution](EXECUTION_CONTRACTS.md), [browser/performance](BROWSER_PERFORMANCE.md)
and [storage/host](STORAGE_HOST_CONTRACTS.md) rules apply by feature. The current
textual graph/workflow guards, fixture ownership checks and report metadata
validator have verified limits; see [reconciliation](gap-reconciliation-2026-10-03.md).
Their planned hardening is not a claim that current tests enforce those rules.
