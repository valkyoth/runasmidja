# Testing and Evidence

Run `scripts/checks.sh` for format, strict clippy, debug/release/all-feature tests,
rustdoc, no_std bare-metal/Wasm compilation, repository gates and adversarial
Python gate fixtures. No skip silently counts as a pass. Tests validate observable
behavior and failure boundaries rather than copying implementation internals.

Run real service smoke tests with `python3 scripts/stack.py up` and `smoke`, then
repeat after idempotent start and stop/restart. Run the probe locally and in the
provided container test script. This tests foundation behavior; it cannot prove
future product features.

The v0.2 candidate has unit regressions in `test_stack.py` and actual cold-start,
seal/outage/denied/bad-CA, partial-retry, root-revoked restart, version/persistence
and redacted metadata/log/audit checks in `stack_qualification.py`. First-run
empty-state evidence is reported separately from repeated retained-state runs.
`python3 -O -m unittest discover -s scripts -p 'test_*.py'` verifies optimized
Python behavior. Minimum ownership gates protect fixture reuse/stop; complete
fingerprints/races remain v0.5. Persistent delivery/legacy migration are v0.8;
rotation, tmpfs cleanup and private-build/CI wrong-claim/fork denials require
later qualification. Public Rust builds remain secret-free.

The submitted v0.2 review adds actual verified-archive/offline Cargo install
regressions, adversarial child floods/pipe deadlock/timeouts, safe bounded audit
reads/retention, fsync faults and exact-image signature/inventory/scan denials.
`qualification_bounds.py` scans the exact Valkey image before its isolated real
Podman ENOSPC/log-rotation/capture/reuse test and cleans up only its captured
owned container. That test does not qualify the whole three-service stack.
The authorized Wolfi/PostgreSQL source build passes scans and full remediated
service qualification. `qualification_postgres.py` additionally exercises 12
real initialization denials without altering rejected fixture data, verifies
UTF8/C.UTF-8 and excludes compiler/Perl/gosu runtime packages. Archive regressions
bind config/platform/every layer to the image that runs and reject receipt/input
drift, unsafe members and tampering. The original PostgreSQL image remains
rejected; its historical scan is retained. GitHub and maintainer retest remain
pending. See the
[assessment](../security/pentest/v0.2.0.md).

The second review adds binary archive flood/EOF/deadline/stderr/exit and fsync/
rename fault tests, pre-parse outer archive limits, UNKNOWN-advisory image/module/
expiry/evidence denials, SBOM path privacy checks and the reaped-PID regression.
`build_sandbox.py --qualify` checks actual delegated kernel ceilings and a real
bounded build step, and forces ENOSPC on a size-limited tmpfs. The complete
PostgreSQL build runs inside the same checked 3 GiB private storage and owned
cgroup. That remediation's normal and optimized suites had 106 tests. No automated test accepts
the maintainer's pentest; this remains a retest candidate.

The following review adds a real scanner-process regression that emits a valid
reviewed report but exits 1/2/125, plus candidate archive mutation checks.
Build fault injection covers scanner failure, denied findings, load/identity
failure, receipt writes before/after visible publication, and successful automatic
retry. Failed replacement scans/imports preserve previous committed artifacts;
failed publication leaves rebuild possible. Normal and PYTHONOPTIMIZE=2 suites
now have 111 tests. CI checks committed whitespace with `git show --check` and
fetches the parent needed for that diff.

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
