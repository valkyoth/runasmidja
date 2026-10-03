# Planning Revision: Optional Search and OpenBao Secret Origin

Status: planning change only, after foundation commit `586fdd2`; no release is
published and no search/secret-provisioning runtime change is claimed.

The revised roadmap has 371 bounded pre-1.0 passes through 0.371.0. Every one
of the 240 original source workstreams still has a mapped owner. Unpublished
Runasmidja versions were reassigned to put prerequisites before consumers.
All handoffs retain setup, goal, deliverables, verification and exact-source
pentest exit criteria. The supplied reference bundle remains unchanged.

## Moved and new owners

| Workstream | Previous Runasmidja assignment | Revised assignment |
| --- | --- | --- |
| Foundation | 0.1.0 | 0.1.0 |
| Vault bootstrap/source remediation | OpenBao fixture at 0.3.0 | 0.2.0 OpenBao-first secret provisioning |
| PostgreSQL fixture | 0.2.0 | 0.3.0, after vault credential issuance |
| Valkey fixture | 0.4.0 | 0.4.0, after vault credential issuance |
| Initialization delivery | No separate owner | 0.5.0 |
| Private build/release delivery | No separate owner | 0.6.0 |
| SDK / secret references / rotation | 0.94.0 / 0.95.0 / 0.96.0 | 0.12.0 / 0.13.0 / 0.14.0 |
| Search contracts | Late search boundary at 0.332.0 | 0.15.0, after application contracts |
| Hosted search implementations | Conditional qualification at 0.333.0 | 0.103.0–0.108.0, after database/authorization |
| Shared-collection search | Implicit in late search work | 0.341.0 integration of qualified backends |

The six hosted search passes separately own repository search, projection/outbox,
Meilisearch Podman provisioning, its adapter, current authorization, and backend
switching/recovery. Both implementations are required before 1.0. Deployment
may disable Meilisearch; operation and local-recipe search remain browser-local.
See [search design](SEARCH_DESIGN.md) and [implementation order](IMPLEMENTATION_PLAN.md).

OpenBao is now explicitly the source for all project-operated initialization,
runtime, private Rust/build, CI, signing, publishing and deployment credentials.
Minimal vault startup trust and independent recovery custody are enumerated
outside-vault responsibilities. Public Rust initialization/builds need no
credentials. See [secret lifecycle](SECRETS_POLICY.md).

## Current limitation and next pass

The existing harness generates PostgreSQL/Valkey passwords locally before
seeding OpenBao and retains private password/config files. It therefore fails
the new secret-origin/delivery target. The next bounded pass is 0.2.0: vault-first
credential provisioning, including partial failure, sealed/unavailable vault,
least privilege, version reuse and root-revoked restart. Preserve existing
state/custody through a tested migration; never silently reset it. The separate
0.5.0 delivery pass removes persistent plaintext delivery copies.

The original [foundation evidence](verification-2026-10-03.md) records the earlier
363-pass plan and actual runtime tests at that point. It is historical evidence,
not an assertion that this new policy or planned search is implemented.

## Verification of this planning revision

Executed `scripts/checks.sh`: repository/link/500-line gates, Rust formatting,
strict clippy, debug/release/all-feature tests, rustdoc, bare-metal/Wasm portable
checks and 16 Python tests passed. Added roadmap prerequisite tests protect
vault-first ordering and early search contracts/implementation ordering.
Regeneration preserves every original source owner and linear handoffs.
No runtime code, dependency pin or reference-source bytes changed; service tests
from the foundation are not reused as proof of the new planned capabilities.
Pentest remains NOT RUN; no tag or publication is authorized by these tests.
