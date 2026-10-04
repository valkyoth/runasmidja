# OpenBao on Wolfi — v0.2.3 development profile

OpenBao 2.7.1, Linux/amd64, local COPY-only packaging. The
[official image](https://openbao.org/docs/install/) supplies its reviewed static
executable. The [Chainguard catalogue](https://images.chainguard.dev/directory/image/openbao/overview)
requires organization access; the public registry denied access on 2026-10-04.
We do not introduce paid registry access or own a Go source build. Commercial
Chainguard OS is not assumed to be a public Wolfi starter.

`image.lock.json` binds the exact upstream signed index/platform leaf and signed
Wolfi base, publisher workflow identities/OIDC issuers, version and executable
SHA256. The freshness gate rejects disagreement with global monitored pins.
Material extraction uses a never-started, uniquely owned container; cleanup checks
its captured ID, label and actual image. Hash/ELF checks require x86_64 static
ELF64, without dynamic interpreter/linker headers. The assembled executable is
checked again before admission, and qualification checks the running image.

```sh
python3 scripts/build_openbao_image.py
python3 scripts/stack_qualification.py
```

The whitelist includes only the executable, Containerfile and upstream MPL-2.0
[license](OPENBAO-LICENSE). No network, RUN step, vault credentials, Go compiler
or plugin build is involved. The image uses UID/GID 65532; the fixture applies
its existing rootless keep-id mapping. Wolfi base shell/shared libraries remain
inventoried: audit qualification needs shell utilities. This is not shell-free.
The scanner inventories Go module versions but does not supply their complete
license/notice inventory. OS package license identifiers are retained where
reported; the upstream OpenBao MPL-2.0 license is copied explicitly. Complete
third-party redistribution notices must be qualified before distributing this
image. Project orchestration is EUPL-1.2 and does not relicense the executable.

Both inputs pass provenance and vulnerability admission before assembly. The
bounded exported candidate archive must bind image config/layers, then pass
exact-image scans and post-scan fingerprint/archive validation before its private
receipt is published. Failed publication cannot authorize an unreviewed image;
a missing receipt rebuilds, a mismatched existing receipt fails closed. Rebuild
explicitly after reviewed input changes. The timestamp stabilizes metadata only;
this is trusted local custody, not bit-for-bit reproducibility or a publisher
signature on the resulting image. No registry push is performed.

Observed candidate image:
`sha256:c110e5c1002a0f2cb09de178fc11378c05035d2de11daf1adaca177d2342b69e`.

Executable SHA256:
`535cf827b13753046757f5ec8b97ae0ef21f10a40ffe673f0d5e75616170f5ea`.

Archive SHA256:
`200ccae0f95cf8acf7c13579ba7ae601df9da961e956357b13ccb1d3167e03c6`.

Recipe fingerprint:
`c3936f183a854681209e080feac63692be6e38cab56b40b725fc3db4767dff0c`.

The 313-component scan retains GO-2026-5932 UNKNOWN. Its separately reviewed
exact-image not-affected evidence uses the byte-identical upstream executable
and existing complete affected-package absence inventory. It expires 2026-11-02;
it is neither an automatic transfer nor a removed finding. See
[advisory evidence](../../../security/advisories/README.md) and
[public inventories](../../../sbom/images/README.md). Every startup rescans.

The [local stack guide](../../../docs/local-stack.md#openbao-wolfi-profile-and-same-version-rollback-v023)
describes explicit official/Wolfi switching, failure checkpoints and retained
custody. This is same-version development rollback, not storage migration or
production recovery. KV v2, AppRole, HTTPS and PebbleDB are exercised; no external
plugin, HA, mlock, durable audit or production filesystem-hardening claim follows
from static linking or a green scan. Maintainer accepted the final v0.2.3 retest at `11f92bc`; GitHub and tag remain pending.


## Concurrent cache custody

All direct and automatic builders take one exclusive filesystem lock in
`.local/openbao-wolfi/artifact.lock` before touching context, candidate, archive
or receipt files. It is independent of stack ID. Receipt validation/selection
uses shared access, retained for the complete archive scan. Automatic callers
release shared access before requesting a build; the exclusive builder rechecks
whether another caller already published a valid artifact. There is no lock
upgrade or nested exclusive acquisition.

The directory and persistent lock must belong to the current user with no group/
other access. Symlink/nonregular lock files and multiply-linked locks are denied;
directory-relative opening and close-on-exec prevent accidental path/inheritance
misuse. Never remove/replace the lock to unblock a waiter. A terminated owner
releases its kernel lock automatically; an incomplete publication is rebuilt
under exclusive access. A normal failure releases the lock without authorizing
an unreviewed artifact. This serializes cooperating local tooling, not malicious
code with the same user's filesystem authority. Other artifact caches retain
their separate existing contracts.


Scan evidence now uses per-service transactions and immutable image/content-keyed
snapshots. Use the [exact-snapshot export procedure](../../../docs/IMAGE_EVIDENCE.md);
old fixed-name local reports are historical and are not updated or accepted
for current export. Probe annotations and qualification records use the same
publication contract.
