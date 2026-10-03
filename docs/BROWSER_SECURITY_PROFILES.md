# Browser Security Profiles

Status: reviewed design remediation for the v0.1.0 pentest. Product browser
profiles and header enforcement are not implemented in this foundation.

## Trust boundary

A Dedicated Worker is an execution/responsiveness boundary, not protection from
a malicious owning page. Compromise of the website origin, CDN, deployment
account or served JavaScript can read input before the worker receives it,
change the worker and alter policies. Same-origin asset hashes checked by that
page do not make the page independently trustworthy. CSP and cross-origin
isolation provide defense in depth; they cannot repair a compromised origin.
This follows the browser's page/worker trust model in the
[HTML worker specification](https://html.spec.whatwg.org/multipage/workers.html).

Browser extensions and a compromised browser/OS are outside application defense.
No hosted website is represented as a safe place for classified data merely
because transforms run locally. The high-assurance profile below needs an
independently verified artifact and a separately enforced network-disabled host.
It cannot promise classification accreditation or protect a compromised host.

## Separate profiles

| Profile | Code custody and capabilities | Confidentiality limits |
| --- | --- | --- |
| Hosted local-only | Dedicated origin/application; local transforms only; no remote execution, network-capable transformations, accounts, sharing or payload telemetry | The origin and delivered code remain trusted. Static asset requests are permitted; payloads never enter them. This is not protection from origin compromise. |
| Verified offline/local-only | Signed, immutable bundle with reviewed UI/worker/Wasm/packs/models/fonts and manifest; independently verified before launch; local launcher/origin plus host network disabled | Verify signature and expected signer using an independently obtained trust anchor/tool, outside downloaded JavaScript. No online updates/service worker/CDN or fallback while processing. The trusted browser/OS/verifier and custody remain assumptions. |
| Explicit remote | Separate origin/application with its own UI, session and remote API capabilities | The user deliberately imports/discloses input there. Consent is specific to destination/effect; server processing has the server trust/retention boundary. |

Origins differ by host/scheme/port, not path prefixes. Local-only and remote
profiles share no cookies, storage, service worker, opener, ambient grants or
automatic payload postMessage bridge. Links to the remote application carry no
payload in URLs/referrers and open with no opener. Explicit file export/import
can cross the boundary only with deliberate user action. Missing local providers
or unsupported network operations report an error; they cannot switch profiles.

High-assurance use selects the independently verified offline distribution;
switching to remote processing ends that profile's confidentiality boundary.
Signature/manifest verification happens before any code executes. Update, import,
artifact substitution, stale service worker and untrusted signing key tests must
fail closed. Signing credentials follow the OpenBao release-secret policy.

## Local-only HTTP policy

The following is an enforced baseline contract, not a report-only policy.
Send the document CSP and appropriate isolation/resource headers on worker and
module responses too; the owning page's CSP alone does not qualify worker
execution. Frame restrictions must be HTTP headers, not only HTML meta tags.
Do not add reporting endpoints that could disclose URLs or user material.
Browser behavior is qualified against [CSP3](https://www.w3.org/TR/CSP3/).

Document CSP, as a single header value:

```text
default-src 'none'; script-src 'self' 'wasm-unsafe-eval'; worker-src 'self'; style-src 'self'; img-src 'self' blob:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'; require-trusted-types-for 'script'; trusted-types runasmidja-static
```

Worker CSP uses the same script/connect/default restrictions. Nested workers
are forbidden with `worker-src 'none'` unless a later bounded pass qualifies
an explicit same-origin worker topology; no blob/data worker or script URL is
admitted. Blob images are only inert bounded raster previews; active HTML/SVG
previews need the separately isolated preview contract. No inline script,
JavaScript eval, wildcard/third-party assets, remote fonts or external images.

| Header | Exact baseline value |
| --- | --- |
| Cross-Origin-Opener-Policy | `same-origin` |
| Cross-Origin-Embedder-Policy | `require-corp` |
| Cross-Origin-Resource-Policy | `same-origin` |
| X-Frame-Options | `DENY` |
| X-Content-Type-Options | `nosniff` |
| Referrer-Policy | `no-referrer` |
| Permissions-Policy | `camera=(), microphone=(), geolocation=(), display-capture=(), usb=(), serial=(), hid=(), bluetooth=(), payment=(), clipboard-read=(), clipboard-write=(self), web-share=()` |

Self-only clipboard writing still requires the explicit reviewed disclosure
grant/user action from 0.27.0; default processing never writes to the clipboard.
The network-disabled host may additionally forbid clipboard export. This header
permission is not application consent and does not authorize automatic copying.

Serve exactly one valid COOP/COEP value, including errors/redirects as applicable;
duplicated or malformed values can weaken the policy. See the
[HTML isolation policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-embedder-policy),
[Fetch CORP definition](https://fetch.spec.whatwg.org/#cross-origin-resource-policy-header)
and [Permissions Policy specification](https://www.w3.org/TR/permissions-policy/).
Platform support varies; record actual effective restrictions per browser.

The single named Trusted Types policy may create only static reviewed
same-origin script/worker URLs from the immutable asset manifest. No default
policy, user-controlled URLs, identity HTML conversion or arbitrary script
conversion. UI rendering uses inert DOM/text operations; framework admission
must prove compatibility. See [Trusted Types](https://www.w3.org/TR/trusted-types/).
Unsupported enforcement is a documented profile limitation; a browser lacking
required controls does not qualify for the high-assurance profile.

`connect-src 'none'` blocks Fetch/XHR/WebSocket/EventSource/beacon paths, including
ordinary Wasm/pack fetches. Load required verified Wasm bytes through reviewed
static modules/embedded bytes and offline bundled assets; measure their cost.
Do not weaken connect-src to accommodate a loader. No payload-bearing URLs,
navigation, forms, resource names or CSP reports are permitted. CSP alone does
not block every possible navigation or malicious same-origin script effect;
host network disablement is essential to the offline high-assurance boundary.

## Versioned implementation and verification owners

| Owner | Required implementation and runtime evidence |
| --- | --- |
| 0.14.0 executable seed | Local-only test origin; document/worker CSP and headers before entering seed input; real browser checks for worker startup/Wasm compatibility and absent payload network effects. No public/high-assurance claim. |
| 0.27.0 privacy | Separate capability/origin profiles, no automatic remote bridge/fallback, sensitivity and explicit export/import disclosure. Sentinel payloads never enter URLs/storage/telemetry or ambient cross-origin transfers. |
| 0.28.0 first browser workbench | Enforce document/worker CSP, named Trusted Types policy, COOP/COEP/CORP, framing and Permissions Policy. Actual Chromium/Firefox/WebKit negatives for Fetch/XHR/beacon/socket/EventSource, external workers/resources, injected HTML/script/URLs, frames/opener, permissions and remote bridging; test effective policy, not just response text. |
| 0.31.0 pack loader | Demonstrate worker/Wasm/lazy loading under connect-src none without widening policy or using payload resource paths; tampered/absent/offline packs fail safely. |
| 0.101.0 offline packaging | Implement signed immutable bundle and independent pre-launch verifier/launcher with correct HTTP policies; test clean network-disabled host, no update/service-worker/CDN requests, bad signature/key/manifest and substituted assets. No high-assurance support before this profile qualifies. |
| 0.133.0 server security | Qualify the separate remote origin/session/CORS/CSRF/opener/storage boundary with explicit disclosure and no local-origin authority bridge before exposing remote jobs. |
| 0.366.0–0.367.0 packaging/provenance | Bind exact offline/local/remote artifact identities and reviewed signer/verifier trust to assessment/SBOM/target evidence; recheck signature/substitution/rollback and network-disabled launch on release artifacts. |

Every owner retains original acceptance. Later plugin, pack, preview, cache and
UI changes rerun affected profile negatives. No mock or roadmap test can attest
browser enforcement, signature trust or offline network disablement.
