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
`qualification_bounds.py` verifies and scans the exact signed Wolfi base image before its isolated real
Podman ENOSPC/log-rotation/capture/reuse test and cleans up only its captured
owned container. That test does not qualify the whole three-service stack.
The authorized Wolfi/PostgreSQL source build passes scans and full remediated
service qualification. `qualification_postgres.py` additionally exercises 12
real initialization denials without altering rejected fixture data, verifies
UTF8/C.UTF-8 and excludes compiler/Perl/gosu runtime packages. Archive regressions
bind config/platform/every layer to the image that runs and reject receipt/input
drift, unsafe members and tampering. The original PostgreSQL image remains
rejected; its historical scan is retained. The maintainer accepted the final
retest; GitHub remains pending. See the
[assessment](../security/pentest/v0.2.0.md).

The second review adds binary archive flood/EOF/deadline/stderr/exit and fsync/
rename fault tests, pre-parse outer archive limits, UNKNOWN-advisory image/module/
expiry/evidence denials, SBOM path privacy checks and the reaped-PID regression.
`build_sandbox.py --qualify` checks actual delegated kernel ceilings and a real
bounded build step, and forces ENOSPC on a size-limited tmpfs. The complete
PostgreSQL build runs inside the same checked 3 GiB private storage and owned
cgroup. That remediation's normal and optimized suites had 106 tests. No automated test accepts
the maintainer's pentest; acceptance is recorded separately in the assessment.

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
textual graph guards, fixture ownership checks and report metadata
validator have verified limits; see [reconciliation](gap-reconciliation-2026-10-03.md).
Their planned hardening is not a claim that current tests enforce those rules.

Host-side Podman calls use `podman_guard.py`, with negative regressions for
build/probe/streaming/namespace entry. `check_repository.py` includes an AST
command guardrail; the already-isolated build worker is the reviewed exception
and requires UID-map and cgroup verification. CI runs these mocked policy tests
without invoking Podman. Real builds, image scans and runtime checks remain local.


## Wolfi OpenBao packaging (v0.2.3)

Developer qualification covers fresh vault-first initialization and retained
same-version official/Wolfi switching, actual audit ENOSPC and recovery, binary/
base/version identity, scoped auth/storage and kernel limits. Regression tests
cover static ELF/hash rejection, owned material cleanup, recipe/archive/receipt
binding, scanner and publication failures followed by successful retries, and
switch checkpoint/identity/custody failure recovery. Freshness detects drift
between the packaging lock and monitored upstream/base pins. Heavy tests remain
local; see the [handoff](releases/v0.2.3-handoff.md). Automated success does not
attest maintainer pentest acceptance.

## Workflow reference admission (v0.3.0)

Install the hash-pinned tooling parser with `scripts/install_python_tools.sh`;
`scripts/checks.sh` selects `.local/check-tools/bin/python3` when installed.
Direct Python tests should use that interpreter (or the exact reviewed system
PyYAML version). `test_workflow_policy.py`, `test_workflow_local.py` and
`test_workflow_bounds.py` cover syntax, context, recursive local admission and
resource/ambiguity boundaries. Repository regressions exercise integration.
See [policy](WORKFLOW_POLICY.md) for the deliberately limited YAML/reference
profile. Tests cannot authenticate remote action content or a maintainer review.
