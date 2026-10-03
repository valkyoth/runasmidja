# Contributing To Runasmidja

Use pinned Rust 1.99.0 and run scripts/checks.sh plus applicable real-service,
browser and security tests. Contributions are EUPL-1.2 as described in LICENSE.

Keep portable code no_std, first-party unsafe forbidden and every code file at
or below 500 lines. Use focused crates and keep host/provider types outside
application contracts. Check current stable dependency/tool versions, license,
features and advisories before admission. New behavior requires positive,
negative/resource tests and documentation/release notes.

Treat payloads/recipes/rendering, crypto, permissions, secret lifecycle,
HTTP/TLS, plugins, caching and release workflows as security-sensitive. Report
vulnerabilities privately according to [SECURITY.md](../SECURITY.md).
