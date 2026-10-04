# Workflow reference admission

Version owner: v0.3.0; candidate, maintainer pentest RETEST REQUIRED.

## Checked references

The common repository gate parses `.github/workflows/*.yml` and `*.yaml` and
checks `jobs.<id>.uses`, `jobs.<id>.steps[*].uses`, job container images and
service images. Quoted/escaped keys, quoted values, flow collections and block
scalars are parsed before checking. Comments, names, inputs, environment values
and shell text are not misidentified as action references.

| Reference | Admitted profile |
| --- | --- |
| Remote action | `owner/repository[/path]@` followed by exactly 40 lowercase hexadecimal commit characters |
| Remote reusable workflow | `owner/repository/.github/workflows/file.yml@commit` (or `.yaml`), same commit rule |
| Container action | `docker://repository@sha256:` plus exactly 64 lowercase hexadecimal characters |
| Job/service container | `repository@sha256:digest`, same digest rule; no mutable tag |
| Local action | Canonical `./.github/actions/name[/subdirectory]`, explicitly reviewed in policy, exactly one regular `action.yml` or `action.yaml`, composite runtime only |
| Local workflow | Canonical `./.github/workflows/file.yml` (or `.yaml`), explicitly reviewed in policy, regular file |

Dynamic expressions and whitespace inside references reject. A block scalar's
terminal newlines are removed; other whitespace is not silently normalized.
Local path segments may not traverse, encode separators, contain Git refs or cross
symlinks. Referenced local files are parsed recursively, including currently unused
policy entries; cycles reject. The policy's empty local tables intentionally admit
no local action/workflow in the shipping configuration. To add one, review its
code, add its exact path and rationale in `.github/workflow-policy.toml`, and run
the gate. Review changes to that code on every commit; the allowlist is not a
signature or independent approval attestation.

The official `github/codeql-action` repository (case-insensitive) is rejected at
executable reference positions. CodeQL remains GitHub Default setup. A comment
mentioning CodeQL is harmless and does not block a workflow.

## Bounded YAML profile

The reviewed PyYAML parser is used through events and composed nodes, without
Python object construction from YAML tags. Scalars remain strings so the `on`
key cannot be interpreted as a YAML 1.1 boolean. Mapping duplicates are rejected
after string decoding. No aliases, anchors, merge keys, explicit tags, directives
or multiple documents are admitted. These are deliberate repository restrictions,
not claims that all these forms are invalid GitHub syntax.

Limits: 128 KiB UTF-8 per YAML/policy file; 40,000 YAML tokens; 20,000 YAML events; collection depth 40;
128 workflow directory entries and 128 admitted documents per run; 32 active local
reference levels. Unsupported/malformed inputs, read failures and parser-version
drift fail closed. No network calls or workflow execution occur during admission.

## Tooling and maintenance

PyYAML **6.0.3**, MIT license, is a development/checking dependency only. The separate `sbom/workflow-tooling.cdx.json` records its tooling scope. Rust and
production/container dependency graphs are unchanged. Its exact upstream wheel
hashes are retained in `scripts/python-tools.lock`; no source build or transitive
package is admitted by installation. `scripts/install_python_tools.sh` installs
into ignored `.local/check-tools` with pip's hash enforcement and an explicit PyPI
index. The interpreter/pip and local installation host remain trusted bootstrap
software. No project credential or OpenBao access is needed for this public setup.

Run the installer once on a new checkout, then `scripts/checks.sh`. The common
gate selects that environment automatically; direct Python commands may use
`.local/check-tools/bin/python3`. An existing system installation is accepted only
at the exact reviewed parser version. Updates require lock/version review, parser
regressions and fresh upstream/advisory checks. Weekly/manual freshness monitors
the current PyPI release and its published vulnerability inventory alongside
existing Rust/tools/services. Missing or nonempty advisory data rejects; an empty
feed is not proof of absence of undisclosed vulnerabilities.

Upstream references reviewed on 2026-10-04:

- [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) defines executable step/job reference positions and workflow file locations.
- [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation) describes event/node parsing APIs and loader behavior.
- [Official PyPI metadata](https://pypi.org/pypi/PyYAML/6.0.3/json) supplies the version, MIT metadata, wheel hashes and published vulnerability inventory.

## Trust limits and deferred owners

This gate is not a complete GitHub schema validator, shell analyzer, action
sandbox or proof of provenance. Full commits/digests prevent mutable references;
they do not prove the remote content safe, authentic or available. Remote reusable
workflow/action internals are not fetched or recursively inspected. Maintainers
must review those immutable inputs, including transitive references and CodeQL
behavior, before admission. Shell commands, checkout changes and deliberately
malicious edits to policy/checker/CI remain trusted-review boundaries. Local
reference validation assumes the checked repository content is what the runner
checks out and executes. Job permissions, event/OIDC trust, credentials and secret
delivery have later owners, notably v0.9.0. Feature/target graph hardening stays
v0.4.0. Local Docker/JavaScript actions and alternate local path syntaxes need a
separate reviewed extension; they are not silently admitted.

No service build/scan job is added to GitHub CI. Container reference tests are
small YAML fixtures; they never start containers. Release automation remains
read-only metadata checking, and all Rust packages remain publish=false.

## Platform bootstrap boundary — SAST-001 remediation

The repository check runs after checkout and parser installation. It is a
regression detector, not pre-execution enforcement for that bootstrap. On
2026-10-04 the live repository Actions API reported `sha_pinning_required: false`.
The setting was enabled and a fresh GET verified `true`, with Actions still enabled
and `allowed_actions: all` unchanged. GitHub's platform setting enforces full
commit pins for actions before they execute; it does not require full pins for
reusable workflows. See [GitHub settings guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)
and [REST policy API](https://docs.github.com/en/rest/actions/permissions).

Run `python3 scripts/check_github_policy.py` locally with the maintainer's existing
authenticated GitHub CLI before release and during security review. It only reads
this repository's settings; disabled/missing enforcement, malformed metadata,
auth/API errors and timeouts fail. No administrator credential is added to CI,
and no new credential is provisioned by this remediation. Settings can drift;
the recorded readback is point-in-time evidence, not a permanent attestation.

All three checked-in workflows currently have one job. Their first steps are the
pinned credential-free checkout, hash-pinned parser install, then the policy
checker using the installed venv interpreter. Workload steps follow. Regression
tests protect this narrow bootstrap and single-job shape. Future independent or
reusable-workflow jobs must depend on a minimal `reference-policy` job through
`needs`, without conditions that bypass success; each runner still needs its own
checkout/tool setup. Review this graph explicitly before relaxing the test.
This ordering does not make malicious repository changes safe or inspect remote
reusable-workflow internals. Maintainer review remains required for those cases.

No negative workflow was pushed to GitHub during this remediation. Live setting
readback and documented platform semantics are distinguished from local mocked
API/ordering tests. CodeQL remains Default and heavy qualification remains local.
