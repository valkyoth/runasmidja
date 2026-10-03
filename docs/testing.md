# Testing and Evidence

Run `scripts/checks.sh` for format, strict clippy, debug/release/all-feature tests,
rustdoc, no_std bare-metal/Wasm compilation, repository gates and adversarial
Python gate fixtures. No skip silently counts as a pass. Tests validate observable
behavior and failure boundaries rather than copying implementation internals.

Run real service smoke tests with `python3 scripts/stack.py up` and `smoke`, then
repeat after idempotent start and stop/restart. Run the probe locally and in the
provided container test script. This tests foundation behavior; it cannot prove
future product features.

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
