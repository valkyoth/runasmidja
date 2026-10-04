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
   pentest. Commit completed candidate work locally as needed, without implying
   pentest acceptance. Record the exact source digest, candidate commit and test
   results so the tested source can be matched to the accepted assessment.
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
   For v0.3.0 onward, run `python3 scripts/check_github_policy.py` locally before
   release to verify live platform SHA enforcement; do not put administrator
   credentials in CI. See [workflow bootstrap boundary](WORKFLOW_POLICY.md#platform-bootstrap-boundary--sast-001-remediation).
8. Stop and wait for the maintainer to explicitly request the version tag.
   Only then check readiness, create the signed tag and push that version tag.
   Tag authorization does not implicitly authorize publishing distributions.
   Keep hashes/notices/SBOM with separately approved distributions.

This loop starts at 0.1.0 and repeats for each bounded version. Do not start the
next version while the current candidate is awaiting pentest, GitHub results or
the maintainer's tag instruction. Local commits do not authorize pushing or tagging.

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

## Local pre-push and GitHub checks

Heavy qualification runs locally before pushing an implementation candidate:
container builds, exact-image provenance/scans/SBOMs, real external services,
resource/fault tests, and applicable browser/provider/fuzz/performance suites.
Use the actual candidate and record results and limitations in its assessment;
GitHub green alone cannot replace this evidence. Reuse unchanged evidence for
CI/documentation-only changes; rerun affected qualification after behavior,
image, build recipe, policy or relevant environment changes.

For the current v0.2 fixture, run these local commands as applicable (install
reviewed image tools first if absent):

```sh
python3 scripts/smoke_probe.py --container
python3 scripts/qualify_probe_wolfi.py
python3 scripts/build_sandbox.py --qualify
python3 scripts/stack_qualification.py
python3 scripts/qualification_bounds.py
```

Stack qualification admits exact images and builds PostgreSQL when no committed
receipt exists. Rebuild explicitly with `python3 scripts/build_postgres_image.py`
when qualifying changed build inputs; retained fixtures must not be silently
reset or reused across an image mismatch. Preserve their data and select a
separate profile as described in [local stack](local-stack.md).

For v0.2.3 OpenBao packaging, also run `python3 scripts/build_openbao_image.py`
when its recipe changes, and qualify a fresh default vault followed by the
[official/Wolfi retained-data switch round trip](local-stack.md#openbao-wolfi-profile-and-same-version-rollback-v023).
Full service qualification includes actual vault audit exhaustion/recovery.
Keep previous fixture custody; never reset secrets/data to make a check pass.
An interrupted switch retains a target-bound checkpoint; retry the same target.
Any new exact image requires fresh scans and explicit advisory evidence review.

Push/PR CI runs repository/whitespace checks, Rust formatting/Clippy/tests/docs,
no_std target checks, Python unit/regression tests, the small native smoke probe,
and dependency/license/advisory checks with a Cargo SBOM. Its job ceiling is
15 minutes, not a runtime promise. Do not add container builds, image scans or
service/browser/fuzz/performance qualification to the automatic push path.
The weekly/manual freshness workflow only queries upstream metadata; the manual
release workflow only validates source/report metadata. Neither runs services.

CodeQL stays on GitHub Default setup, independently of Rust CI, using the default
query suite. Its runtime is GitHub-managed and may grow with the codebase; no
one-hour runtime guarantee or custom timeout is claimed. Do not introduce
advanced workflows or container builds into scanning. Review future expensive
checks for the same local/hosted split before enabling them.
