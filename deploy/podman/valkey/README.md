# Wolfi Valkey development fixture

v0.2.2 selects the public Chainguard Valkey starter, without building our own
cache image or requiring paid registry credentials. The
[official catalogue](https://images.chainguard.dev/directory/image/valkey/overview)
describes access and packaging; admission uses actual pinned metadata, inventory
and runtime version rather than potentially stale catalogue examples.

- Version: Valkey 9.1.2, Wolfi package 9.1.2-r2; Linux/amd64 only.
- Signed index: `sha256:0d4a661641c6bffe0f2a95cd6adb5dff7b6884dbc3645f59d304961ad99bb021`.
- Platform leaf: `cgr.dev/chainguard/valkey@sha256:46daab244007fcd928009a4202f5ec090119441f90b350c3430c5d2982d59818`.
- Identity: `https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main`.
- Issuer: `https://token.actions.githubusercontent.com`.

The signed index must bind this platform leaf. Fresh exact-image scans and SBOMs
are required on each admission. `check_freshness.py` monitors both upstream
Valkey releases and the public Wolfi index weekly/manually. A changed index needs
review and qualification; no mutable tag is executed. Registry availability is
an external dependency; failure does not authorize another image or bypass.

The retained upstream inventory includes bash, glibc, OpenSSL and other shared
libraries. This is not a shell-free image. Package license identifiers and
upstream component information remain in [the SBOM](../../../sbom/images/valkey.cdx.json);
Runasmidja's EUPL-1.2 does not relicense those packages. No libraries or license
files are manually stripped. We do not publish this upstream image ourselves.

The entrypoint is `/usr/bin/valkey-server`, passed `/config/valkey.conf` directly.
The rootless fixture overrides its default UID with the host keep-id UID/GID to
read private configuration. Configuration uses OpenBao-issued scoped ACLs,
disables the default user and persistence, limits memory to 64 MiB with
allkeys-lru eviction, and publishes only loopback port 16379. Container limits
are 512 MiB, one CPU and 128 PIDs, read-only root, dropped capabilities and
no-new-privileges. Secret config is a private read-only mount, never argv.

The previous official digest and its narrowly reviewed unsigned-image exception
remain available only via `RUNASMIDJA_VALKEY_PROFILE=official`. It is rescanned,
not implicitly trusted because it was previously accepted. The new default
fixture has separate vault/database custody; no automatic data migration or
credential copying occurs. See [rollback commands](../../../docs/local-stack.md#valkey-profile-rollback-v022).
Actual runtime evidence is recorded in the [handoff](../../../docs/releases/v0.2.2-handoff.md).
