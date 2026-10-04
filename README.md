<p align="center">
  <b>Runasmidja — Decode. Transform. Understand.</b><br>
  A security-first Rust data-transformation workbench with a portable no_std engine.
</p>

<div align="center">
  <a href="docs/IMPLEMENTATION_PLAN.md">Implementation Plan</a> |
  <a href="docs/RELEASE_PLAN.md">Release Plan</a> |
  <a href="docs/threat-model.md">Threat Model</a> |
  <a href="SECURITY.md">Security</a>
</div>

<br>

<p align="center">
  <img src=".github/images/runasmidja.webp" alt="Runasmidja — a Nordic workshop for decoding and transforming data">
</p>

# Runasmidja

Runasmidja is planned as a modern online CyberChef-style website and API.
The same Rust engine will execute in a browser worker and native hosts.
Browser processing is the default; saving, sharing, server execution and
external network operations are distinct explicit actions.

**Current status:** `v0.1.0`, `v0.2.0`, `v0.2.1` and `v0.2.2` are signed and
tagged with accepted pentests and green GitHub checks. The `0.2.3` candidate
packages the exact upstream OpenBao executable on a signed Wolfi base, with
vault data preserved across tested official/Wolfi image switches.
Maintainer pentest is **NOT RUN**; automated verification is separate.
No workbench, transformation, browser UI, production HTTP server or CyberChef
parity is implemented yet. See the [0.2.3 scope](docs/releases/v0.2.3-scope.md)
and [candidate assessment](security/pentest/v0.2.3.md).

GitHub checks code and dependencies; CodeQL uses Default setup. Container builds,
image scans and real service tests run locally before pushing. See the
[verification split](docs/RELEASE_RUNBOOK.md#local-pre-push-and-github-checks).

The [release plan](docs/RELEASE_PLAN.md) defines 386 small pre-1.0 passes,
through `0.386.0`, with further versions whenever needed. `1.0.0` is the first
serious production release with complete declared website/API functionality.
Desktop/mobile GUIs follow afterward.
The [gap reconciliation](docs/gap-reconciliation-2026-10-03.md) adds verified
prerequisite owners and stronger acceptance while preserving all 240 reference
workstreams. These are planned controls, not implemented remediation.

## Development

Rust **1.99.0**, edition 2024; EUPL-1.2. Weekly automation checks stable Rust,
crates, security tools, GitHub Actions and service upstream releases.

```sh
rustup target add --toolchain 1.99.0 thumbv7em-none-eabihf wasm32-unknown-unknown
scripts/checks.sh
cargo run -p runasmidja-server -- 18080
```

The development probe binds loopback and serves only `GET /healthz`.
It is disposable test infrastructure and will be replaced by a qualified HTTP
adapter. It is not the planned public API.

```sh
python3 scripts/install_image_tools.py
python3 scripts/stack.py up
python3 scripts/stack.py smoke
python3 scripts/stack.py stop
```

Dependencies run in rootless Podman: PostgreSQL **19 beta 4**, OpenBao **2.7.1**
and Valkey **9.1.2**. PostgreSQL is built automatically from pinned official source
on a verified Wolfi base. Private custody lives in ignored `.local/stacks/v023-wolfi-bao`;
earlier `.local/stacks/*` and `.local/stack` data remain separate and retained.
OpenBao is initialized over TLS with declarative audit, KV v2, scoped AppRole
and revoked bootstrap root token. Image provenance and exact-digest scans run
before startup. Untriaged UNKNOWN and all HIGH/CRITICAL findings block execution.
OpenBao retains one digest-specific, expiring not-affected review; no other
blocking findings were reported. See [local stack](docs/local-stack.md) and the
[PostgreSQL recipe](deploy/podman/postgres/README.md) and
[OpenBao recipe](deploy/podman/openbao/README.md).
The new fixture obtains database/cache passwords from OpenBao before dependent
startup, using separate scoped provisioning/runtime identities and version reuse.
Private password/ACL delivery copies remain until the v0.8 qualification. All project-operated secrets, including initialization/private
build/release credentials, must come through OpenBao; public Rust builds need
none. See [secret lifecycle](docs/SECRETS_POLICY.md) for bootstrap custody.

## Workspace

| Crate | Boundary | Current behavior |
| --- | --- | --- |
| `runasmidja` | Public no_std facade | Re-exports portable boundaries |
| `runasmidja-core` | Allocation-free portable domain | Reserved foundation |
| `runasmidja-ports` | Application-owned integration contracts | Reserved foundation |
| `runasmidja-html` | HTML/formatting extraction to future Vef | Reserved foundation |
| `runasmidja-crypto` | Crypto/TLS extraction to future Brynja | Reserved foundation |
| `runasmidja-server` | Linux process/I/O adapter | Loopback health probe |

Portable crates are always `no_std`, forbid unsafe code and have no external
runtime dependencies. Hosted adapters may use reviewed dependencies. The
website and service SDKs are not claimed to be allocation-free or no_std.
Every code file has a hard 500-line ceiling.

## Product and evidence

[Implementation plan](docs/IMPLEMENTATION_PLAN.md),
[version plan](docs/VERSION_PLAN.md),
[architecture](docs/ARCHITECTURE.md),
[testing](docs/testing.md),
[release runbook](docs/RELEASE_RUNBOOK.md),
[security controls](docs/security-controls.md),
[dependency policy](docs/supply-chain-security.md),
[candidate release notes](release-notes/v0.2.3.md),
[tagged foundation notes](release-notes/v0.1.0.md).

The [original idea](docs/IDEA.md) and [supplied planning bundle](docs/reference/workbench-plan/README.md)
are retained as design inputs. Their historical compiler/provider statements
are not current implementation evidence.

Operation search will work locally over descriptors. Saved-recipe metadata
search has an early portable SearchService contract and two planned backends:
repository search and optional Meilisearch. Both will be implemented/tested with
hosted persistence; operators may enable or disable Meilisearch without changing
the UI/API or recipe schema. Payloads/secrets are excluded and current database
permissions govern results. See [search design](docs/SEARCH_DESIGN.md).

## License

European Union Public Licence **1.2**: [LICENSE](LICENSE).
