# Security Policy

Runasmidja is security-sensitive data-transformation software. Inputs, imported
recipes, crypto, rendering, secrets, caching, database access, HTTP/TLS, plugins,
workers and supply-chain changes require threat review and executable tests.
The current repository is an unpublished foundation, not a production service.

Report vulnerabilities privately through [GitHub private advisories](https://github.com/valkyoth/runasmidja/security/advisories/new).
Do not disclose exploitable details in public issues before remediation.

Run scripts/checks.sh, current freshness checks, cargo deny check and cargo audit
--deny warnings before releases; real service/browser/provider/fault tests apply
to the feature being claimed. Keep security docs, limitations, CHANGELOG and
release notes with each pass. Every minor/patch/RC/tag needs an exact-source
pentest and tested remediation; NOT RUN never qualifies as PASS.

See [release runbook](docs/RELEASE_RUNBOOK.md), [threat model](docs/threat-model.md)
and [controls](docs/security-controls.md). GitHub uses CodeQL **Default setup**;
no advanced scanning workflow is added. Settings must be enabled externally.

Production runtime processes must never hold bootstrap root tokens or OpenBao
recovery shares. Secrets do not belong in URLs, logs, arguments, payload caches
or search indexes. Local .local/stack custody shortcuts are only test fixtures
and have no production support claim.
