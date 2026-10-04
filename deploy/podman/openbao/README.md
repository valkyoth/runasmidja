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
`sha256:9ffb8ed80617f40dfd6ade69797344d435dff809b69edf9e7e965743aae9983f`.

Executable SHA256:
`535cf827b13753046757f5ec8b97ae0ef21f10a40ffe673f0d5e75616170f5ea`.

Archive SHA256:
`c9551bb5e615d5128eb3b46a71fa91011ca19e18a5203862bbc93557f42f0f02`.

Recipe fingerprint:
`8e459a192b12b859d08481b89df302b4a79d5c62c264c6d81f8a74b667be216f`.

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
from static linking or a green scan. Maintainer pentest requires retest after SAST-001 remediation.


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
