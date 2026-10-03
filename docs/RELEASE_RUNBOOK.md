# Release Runbook

Every minor, patch, RC and production tag needs implementation scope, tests,
security review, release notes, SBOM and an exact-source pentest. This repository
setup creates a candidate; it does not tag, publish or attest that pentest passed.
The maintainer performs the pentest and decides when it is green. No external
assessor or additional approval service is required for this working loop.

1. Capture exact bounded scope, public behavior, numeric limits and test IDs.
2. Implement one pass and run common and release-specific gates, including real
   services/browsers/providers where claimed; refresh dependency/tool metadata.
3. Update threat controls, parity matrices, limitations, CHANGELOG and notes.
4. Stop implementation and say the candidate is ready for the maintainer's
   pentest. Leave new work uncommitted. Record the exact source digest and test
   results so the tested working tree can be matched to the later source commit.
5. If the pentest finds issues, read the maintainer's local PENTEST.md, fix them,
   run affected tests and document remediation. Hand the candidate back for
   retest; repeat until the maintainer confirms green. Never infer pentest PASS
   from automated tests or from fixes being complete.
6. After green, commit the tested source locally and preserve the maintainer's
   assessment in a permanent report with reviewed commit, unchanged source
   digest, commands, findings/resolutions, retest and limitations. The existing
   checker requires a report-only direct child commit; prepare both local
   commits as bookkeeping for one maintainer push, without another approval step.
   Remove private scratch only after its reviewed findings are preserved.
7. The maintainer pushes the commits. Wait for the required GitHub checks,
   including CodeQL Default. If GitHub fails, use the reported failure to fix
   the candidate, rerun local checks and update the pentest report honestly.
   Changes affecting tested behavior require maintainer retest before restoring
   PASS; unchanged coverage can retain its evidence. After green, commit locally
   again, let the maintainer push, and repeat until GitHub is green.
8. Stop and wait for the maintainer to explicitly request the version tag.
   Only then check readiness, create the signed tag and push that version tag.
   Tag authorization does not implicitly authorize publishing distributions.
   Keep hashes/notices/SBOM with separately approved distributions.

This loop starts at 0.1.0 and repeats for each bounded version. Do not start the
next version while the current candidate is awaiting pentest, GitHub results or
the maintainer's tag instruction. Planning updates follow the same commit timing.

`python3 scripts/check_release.py X.Y.Z` checks report shape/source lineage and
SBOM presence only; it does not authenticate the assessor or built artifacts.
Source changes after a green assessment need an updated source binding and
affected coverage reviewed again; report editing cannot make old evidence current.

Apply [G0–G7](VERIFICATION_GATES.md). The trust-contract and distribution-binding
passes in [gap reconciliation](gap-reconciliation-2026-10-03.md) qualify reviewed
assessment/reviewer identity and exact artifact/pack/model/SBOM/toolchain/target/
provenance/signing bindings. A formatted PASS cannot authorize publication.
Until enforcement exists, trusted review must reject missing evidence explicitly;
the source/report script's success alone is never the publishing decision.

A missing report, NOT RUN, unresolved critical/high finding, stale reviewed
commit, changed source or unverified target blocks readiness. Never fabricate
PASS to unblock a tag. Root PENTEST.md is private scratch: preserve reviewed
findings/resolutions in permanent reports, then remove scratch before release.

CI release workflow validates metadata only and has no publishing credentials.
Signed-tag trust and external release artifact signing receive explicit
qualification before publication; copied sibling signer files are not inherited
as Runasmidja authorization.
