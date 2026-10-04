# Security Policy

Runasmidja is security-sensitive data-transformation software. Inputs, imported
recipes, crypto, rendering, secrets, caching, database access, HTTP/TLS, plugins,
workers and supply-chain changes require threat review and executable tests.
The repository has a tagged v0.1.0 foundation and a v0.2.0 remediation candidate;
neither is a production service. The maintainer accepted the v0.2.0 retest with
no new findings; GitHub checks and tagging remain pending. The authorized
Wolfi/PostgreSQL fixture passes scans and actual service qualification; this
does not establish production security or a pentest PASS. See the
[assessment](security/pentest/v0.2.0.md).

Runasmidja targets a normal public website. Review findings against its actual
supported behavior, exploitability and trust boundaries, and choose controls
that a solo maintainer can operate. Rigorous reviews do not establish a separate
military assurance profile. Document not-affected and out-of-scope determinations
with evidence rather than silently disabling relevant security checks.

Report vulnerabilities privately through [GitHub private advisories](https://github.com/valkyoth/runasmidja/security/advisories/new).
Do not disclose exploitable details in public issues before remediation.

Run scripts/checks.sh, current freshness checks, cargo deny check and cargo audit
--deny warnings before releases; real service/browser/provider/fault tests apply
to the feature being claimed. Keep security docs, limitations, CHANGELOG and
release notes with each pass. Every minor/patch/RC/tag needs an exact-source
pentest and tested remediation; NOT RUN never qualifies as PASS.
The maintainer performs that pentest. Completed candidate work may be committed
locally for their retest; a commit does not attest acceptance. The maintainer
pushes unless they explicitly delegate it. GitHub failures follow the
fix/report/retest loop in the runbook.

See [release runbook](docs/RELEASE_RUNBOOK.md), [threat model](docs/threat-model.md)
and [controls](docs/security-controls.md). GitHub uses CodeQL **Default setup**;
no advanced scanning workflow is added. Settings must be enabled externally.

Production runtime processes must never hold bootstrap root tokens or OpenBao
recovery shares. Secrets do not belong in URLs, logs, arguments, payload caches
or search indexes. Local .local/stacks custody shortcuts are only test fixtures
and have no production support claim.

All project-operated initialization, runtime, build and release secrets must
come through OpenBao; public Rust setup/build needs none. Vault startup trust
and independent recovery custody are the minimal explicit bootstrap boundary.
The v0.2 candidate issues service passwords in OpenBao before consumer startup;
persistent private delivery, build/release identity and production custody remain
separate qualification passes. Legacy v0.1 fixture data is preserved unchanged. See [secret lifecycle](docs/SECRETS_POLICY.md).
Search is optional infrastructure; current database permissions govern hits
and aggregates in both backends. See [search design](docs/SEARCH_DESIGN.md).

Apply the additive [verification gates](docs/VERIFICATION_GATES.md) and
[versioned gap owners](docs/gap-reconciliation-2026-10-03.md). Existing textual
workflow/portable-graph checks, fixture ownership and source/report metadata
validation have confirmed enforcement limits. Their hardening is planned;
metadata PASS cannot authenticate an assessor or distributed artifacts.
Public untrusted-job endpoints remain disabled until authority, admission,
kernel isolation, fencing, egress, TLS and recovery qualify together.
