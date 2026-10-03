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

**Current status:** repository foundation, development health probe and
service-test tooling. No workbench, transformation operation, browser UI,
production HTTP server or CyberChef parity is implemented yet. `0.1.0` is an
unpublished foundation candidate, with pentest pending.

The [release plan](docs/RELEASE_PLAN.md) defines 363 small pre-1.0 passes,
through `0.363.0`, with further versions whenever needed. `1.0.0` is the first
serious production release with complete declared website/API functionality.
Desktop/mobile GUIs follow afterward.

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
python3 scripts/stack.py up
python3 scripts/stack.py smoke
python3 scripts/stack.py stop
```

Dependencies run in rootless Podman: PostgreSQL **19 beta 4**, OpenBao **2.7.1**
and Valkey **9.1.2**. State and credentials stay in ignored `.local/stack`.
OpenBao is initialized over TLS with declarative audit, KV v2, scoped AppRole
and revoked bootstrap root token. See [local stack](docs/local-stack.md).

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
[release notes](release-notes/v0.1.0.md).

The [original idea](docs/IDEA.md) and [supplied planning bundle](docs/reference/workbench-plan/README.md)
are retained as design inputs. Their historical compiler/provider statements
are not current implementation evidence.

Operation search will work locally over descriptors. Saved-recipe metadata
search starts behind a portable repository boundary. Meilisearch is optional
if measured requirements justify it; payloads and secrets are excluded.

## License

European Union Public Licence **1.2**: [LICENSE](LICENSE).
