# Changelog

## Unreleased — 0.1.0 foundation candidate

Release review (2026-10-03): the maintainer accepted the green retest, resolving
all three submitted findings with no new actionable security issue. Full local
verification and version/documentation review pass; the monitored, unadmitted
OpenBao SDK was refreshed to 2.2.2. Pentest PASS covers the foundation only;
GitHub checks, tagging and publication remain pending.

The notes below preserve the earlier candidate's preparation history.

Pentest remediation (2026-10-03): addressed the browser origin threat-model gap,
assigned profile/header/independent offline verification owners, replaced
optimization-removable smoke assertions, and verified native probes using the
live child's announced ephemeral port. Added adversarial regressions and fixed
angle-bracket Markdown link checking. All 34 Python tests and optimized actual
native/container probes pass; maintainer retest is pending, not pentest PASS.

Foundation handoff (2026-10-03): reverified the v0.1.0 scope, common gates,
dependency/freshness checks, real native/container probes and service restart;
refreshed the SBOM and documented known limits for the maintainer's pentest.
The release loop now commits only after their green result, waits for GitHub,
and tags/pushes a version tag only on explicit instruction. Pentest is NOT RUN.

### Foundation scope

- Initialized EUPL-1.2/Rust 1.99.0 workspace with five no_std boundary crates
  and a Linux development health probe.
- Adapted Eth/Brynja repository files, dependency/CI/freshness controls and
  executable file-size/documentation/graph gates.
- Added automated PostgreSQL 19 beta 4, TLS OpenBao and ACL Valkey Podman tests.
- Preserved the idea/planning bundle and defined 386 pre-1.0 passes, including
  service lifecycle, provider feasibility, parity and operational qualification.
- Revised planned search to early portable contracts and mandatory qualification
  of repository/optional Meilisearch backends alongside hosted persistence.
- Required OpenBao as the source for initialization/runtime/private-build/release
  secrets; made local-password-first fixture remediation the next bounded pass.
- Reconciled the submitted gap analysis against source and official documentation;
  retained every original acceptance and added 240 reviewed verification gates.
- Added 15 bounded ownership/admission/seed/pack/privacy/performance/migration/
  isolation/egress/distribution prerequisites; actual artifacts now precede full
  seekable replay. Documented verified enforcement gaps without claiming fixes.
- Tightened unchanged 386-pass numbering: minimal SQL fencing at 0.107.0 precedes
  hosted publication at 0.112.0; local storage and early API test scopes are
  explicit, and actual continuation starts at 0.387.0. Generator rejects blank
  or nonstring verification gates before writing output.

No product parity or production readiness is claimed. Pentest is accepted;
GitHub checks, tagging and publication are pending. See release-notes/v0.1.0.md.
