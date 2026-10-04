# Exact-image advisory reviews

Image admission fails on untriaged UNKNOWN and all HIGH/CRITICAL advisories,
including unfixed findings. A reviewed UNKNOWN may pass only for the exact
image digest, affected module/version and retained evidence SHA-256 in
[advisory-reviews.json](../../deploy/podman/advisory-reviews.json). Review windows
are at most 30 days; the expiry date is exclusive at 00:00 UTC. Missing, changed,
expired or positive affected-symbol evidence blocks admission. A new digest,
module version or advisory needs a new review. No HIGH/CRITICAL waiver exists.
The scanner finding remains in the public CycloneDX report with a review count.

## OpenBao GO-2026-5932

The [official Go advisory](https://pkg.go.dev/vuln/GO-2026-5932) affects the seven
legacy golang.org/x/crypto/openpgp packages, without a fixed version. Module
presence alone does not establish affected-package inclusion. The exact pinned
OpenBao 2.7.1 image contains x/crypto v0.56.0 but its bundled `/usr/bin/bao`
has zero affected-package symbols in a populated 153,297-entry inventory.
It contains 538 symbols from the maintained ProtonMail OpenPGP fork; the
[pinned OpenBao source](https://github.com/openbao/openbao/blob/v2.7.1/internal/helper/pgpkeys/encrypt_decrypt.go)
also imports that fork. The
[public evidence](openbao-GO-2026-5932.json) binds binary/tool/image hashes,
versions, package inventory hash and limitations. This review expires on
2026-11-02; admission rejects it starting that date unless reviewed again.

Analysis used govulncheck v1.8.0 built by Go 1.27.1, downloaded through the official
Go module proxy/checksum database. It is a local review tool, not a product or
CI runtime dependency. Reproduce by verifying the pinned image's publisher,
copying `/usr/bin/bao` from an owned non-running container (do not execute it),
checking its recorded hash, then running `govulncheck -mode=extract bao`.
Read the extraction record's pkgSymbols inventory; count every package equal
to or below each affected package prefix. Compare inventory/module/hash results
and the current official advisory before updating the review and evidence hash.
Review again before expiry and after image/advisory changes; never extend the
date without repeating analysis. Normal `image_gate.py` and startup retain the
advisory and enforce the current UTC expiry.

The symbol-absence finding covers this immutable bundled binary only, not
external plugins, runtime call graphs, all OpenPGP implementations or future
images. Incomplete/unpopulated inventories cannot establish absence. Raw binary
and extraction records stay in ignored private local state; no workstation path
is embedded in published evidence. This is a scoped not-affected determination,
not a blanket dependency ignore or pentest PASS.
