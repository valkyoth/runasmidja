# Container bases and Fluxheim qualification

Status: v0.2.1 probe and v0.2.2 Valkey packaging are signed/tagged. The current
bounded candidate is [v0.2.3 Wolfi OpenBao](releases/v0.2.3-scope.md), with
maintainer pentest PASS; GitHub and tag pending. Required Fluxheim coverage and all 386 minor
workstreams/source mappings remain unchanged.

## Decision and maintenance scope

Prefer a minimal Wolfi runtime where it preserves the current reviewed service
version, features and operational guarantees. Move one existing image at a time.
Keep orchestration, credentials and domain contracts independent of its base.
The portable Runasmidja crates remain no_std; only Linux hosting is containerized.
Wolfi is a packaging choice, not a CVE waiver or security guarantee.

Reuse maintained, accessible images or verified upstream artifacts before owning
another full source build. Our PostgreSQL 19beta4 build covers a concrete current
gap. A custom service build needs its own source/toolchain/dependency provenance,
ABI/TLS/plugin compatibility, license inventory and recurring rebuild owner.
Do not blindly copy musl-linked binaries into a glibc runtime. Runtime images
exclude build tools and unnecessary packages where practical. For v0.2.2, the
public maintained Valkey starter retains its upstream shell/shared libraries:
we accept and scan that inventory instead of maintaining a hand-stripped fork.
This is an explicit packaging tradeoff, not a claim that the fixture needs bash.

The current [Valkey catalogue](https://images.chainguard.dev/directory/image/valkey/overview)
offers a free starter image, with access restrictions for specific version tags.
[OpenBao](https://images.chainguard.dev/directory/image/openbao/overview) and
[Meilisearch](https://images.chainguard.dev/directory/image/meilisearch/overview)
describe organization-access images. These pages were reviewed on 2026-10-03;
OpenBao access was rechecked on 2026-10-04 (public registry denied access);
they are not proof that a freely accessible, current-version Wolfi image exists.
Commercial Chainguard OS images are distinct from Wolfi starter images. Verify
actual base/package/version/signature/access metadata before admission. Do not
add a paid registry dependency or accept an older service merely to match bases.

## Compatible patch sequence

v0.2.3 is the authorized current patch; v0.2.1 and v0.2.2 are released.
They harden packaging of existing foundation behavior. If an image requires new
application features or changes secret/storage/auth contracts, split that work
into a bounded minor instead of hiding it in a patch. v0.3/v0.4 workflow/graph
hardening and all existing later security owners remain required.

Shared setup: finish v0.2.0 first; freeze exact image/source/tool/base identities,
Linux/amd64 profile, existing behavior and numeric resource limits. Public builds
need no secrets; private access/signing/publishing uses OpenBao under its existing
qualification owners. Preserve earlier fixture data and define an executable
rollback before changing an owned container. No production/external exposure.

| Proposed version | Goal and deliverables | Verification and exit criteria |
| --- | --- | --- |
| v0.2.1 | Add a minimal Wolfi runtime for the existing Runasmidja health probe, using the reviewed Rust version and exact built executable. Retain native/scratch qualification as regression profiles; no website/API feature is added. | Native, scratch and Wolfi responses/rejections agree; nonroot/read-only/capability/resource limits, artifact binding, current scans/SBOM/notices and common gates pass. Complete the exact-source maintainer pentest and release loop. |
| v0.2.2 | Admit one current Wolfi Valkey image or verified minimal build, preserving OpenBao-issued ACL delivery, key-prefix isolation, memory limits and existing cache fixture behavior. Record provenance/access/build obligations. | Real auth/ACL/prefix denials, existing set/get/delete, restart, outage and disclosure/resource checks pass; scans and inventory bind the image that runs. Actual TTL qualification remains v0.7, not claimed by the patch. Complete the exact-source maintainer pentest and release loop. |
| v0.2.3 | Admit one current Wolfi OpenBao image/build after ABI/TLS/storage/plugin compatibility review. Preserve bootstrap trust, KV versions, AppRoles, root revocation, audit bounds and recovery custody. Do not rewrite vault initialization or reset state. | Fresh and retained vault/consumer runs, seal/outage/bad-CA/identity denials, version reuse, audit-full behavior and interrupted/root-revoked restart pass. A same-version image switch preserves data/custody and has tested rollback; unsupported migration gets its own pass. Current image/source inventory and scans pass. Complete the exact-source maintainer pentest and release loop. |

Meilisearch starts with the preferred reviewed minimal base at **v0.115.0**;
building it now would maintain an unused service. Both enabled and disabled
search profiles remain mandatory before 1.0. No search provider is introduced
into portable defaults or exposed directly to a browser.

## Fluxheim owners and concrete test scope

Fluxheim is a required reverse-proxy qualification target in addition to direct
execution. Its sibling repository contains `containers/Containerfile.wolfi` and
documents a focused `proxy-wolfi` image at GHCR/Quay. Use only Fluxheim's official
published Wolfi proxy image, pinned by immutable digest after current-version,
publisher/issuer/platform, inventory and scan review. Runasmidja does not build or
repackage Fluxheim. The sibling path and its present README version are not
required build dependencies. Do not change the sibling project as part of
Runasmidja work.

**v0.11.0 — service lifecycle harness:** introduce the first real rootless
Fluxheim Wolfi proxy fixture against the bounded health probe. Automate private
network/config/readiness/owned cleanup, constrain proxy/backend publications to
the local test profile, and keep admin services inaccessible through proxy
routes. Test native backend and container backend through the actual proxy,
upstream outage/restart, rejected routes/methods, bounded timeouts and spoofed
forwarding headers. Freeze the exact trust/HTTP/TLS subset in that pass's scope;
health-only evidence does not attest sessions, uploads, browsers or production.

**v0.12.0 — freshness/supply chain:** monitor Fluxheim release, admitted image,
base and package/source materials with the existing product freshness gate.
Pin exact publisher/issuer/architecture and retain per-image scans/SBOMs. Local
Tumbleweed/Podman package drift remains outside this gate.

**v0.129.0 — server deployment:** qualify the actual website/API both directly and
behind Fluxheim's focused Wolfi image. Only explicit trusted proxy peers may
supply forwarding metadata; reject/ignore client-forged Forwarded/X-Forwarded
and PROXY-protocol claims. Verify external scheme/host/origin handling, redirects,
secure-cookie/session behavior, streaming/cancellation, body/header/time limits,
cache exclusions, response headers and any admitted WebSocket/SSE behavior.
Private backend bypass cannot become a public alternative to proxy admission.

**v0.130.0 — TLS policy:** test actual Fluxheim client TLS and upstream TLS/mTLS
when admitted, wrong names/roots/expiry, spoofed termination metadata and direct
TLS parity. Proxy termination does not replace private PostgreSQL/Valkey/OpenBao
transport qualification. Private keys/certificate credentials follow OpenBao
policy; the enumerated initial vault trust anchor retains its separate custody.

**v0.133.0 — server security gate:** assess the combined proxy/application
deployment for auth/object/origin/cache/rate-limit bypass, backend exposure,
request framing/smuggling, forwarded identity and denied admin routes, alongside
the existing worker/egress/fencing/recovery gates. A green Fluxheim assessment
alone cannot attest the Runasmidja integration. Run the maintainer's exact-source
pentest and retest loop for each numbered implementation pass.

**v0.366.0 and RC/1.0:** rerun both direct and Fluxheim deployment suites on exact
release artifacts, record compatible proxy/config versions, manifests/notices,
backup/restore/rollback and upgrade evidence. Meilisearch on/off remains covered.
Every service image still requires its own scan and runtime qualification, even
when all images share a Wolfi base.
