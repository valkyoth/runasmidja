# Versioning Policy

0.1.0 and 0.2.0 are tagged foundation releases. Numbered minors are
small feature/contract passes; 0.N.P patches fix compatible defects and need a
patch rationale and the same pentest gate. Add arbitrarily many pre-1.0 minors
when required coverage remains incomplete. 1.0.0 is the first serious production
release after qualified RCs; desktop/mobile GUIs follow later.

Workspace crates initially share the candidate version and are publish=false.
Before public SDK distribution, admit package-specific compatibility, publish
ordering and independent downstream examples. No crates.io release cadence is
inferred from Eth's project-specific five-minor publication rule.

Application packages, HTTP API, recipe schema, operation semantic revisions,
provider/data revisions and plugin ABI are separate compatibility axes. Changing
defaults/encoding/errors can require recipe migration despite unchanged Rust
signatures. Preserve historical fixtures; never silently select a newer saved
operation revision. Exact signed tags and release notes accompany actual
releases, not unimplemented roadmap rows.
