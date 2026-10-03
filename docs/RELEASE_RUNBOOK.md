# Release Runbook

Every minor, patch, RC and production tag needs implementation scope, tests,
security review, release notes, SBOM and an exact-source pentest. This repository
setup creates a candidate; it does not tag, publish or attest that pentest passed.

1. Capture exact bounded scope, public behavior, numeric limits and test IDs.
2. Implement one pass and run common and release-specific gates, including real
   services/browsers/providers where claimed; refresh dependency/tool metadata.
3. Update threat controls, parity matrices, limitations, CHANGELOG and notes.
4. Commit the implementation source for review. Stop implementation and pentest
   this exact commit; record findings, fixes and independent limits.
5. Remediate; commit fixes and repeat affected tests and pentest on changed source.
6. Preserve a permanent report with reviewed commit, source digest, commands,
   findings/resolutions and Status: PASS only after the assessment completes.
7. Make a report-only direct child commit; keep reviewed source unchanged.
   `python3 scripts/check_release.py X.Y.Z` verifies evidence and lineage.
8. Review GitHub CI and CodeQL Default results, then create a signed tag and
   separately publish approved distributions. Keep hashes/notices/SBOM with them.

A missing report, NOT RUN, unresolved critical/high finding, stale reviewed
commit, changed source or unverified target blocks readiness. Never fabricate
PASS to unblock a tag. Root PENTEST.md is private scratch: preserve reviewed
findings/resolutions in permanent reports, then remove scratch before release.

CI release workflow validates metadata only and has no publishing credentials.
Signed-tag trust and external release artifact signing receive explicit
qualification before publication; copied sibling signer files are not inherited
as Runasmidja authorization.
