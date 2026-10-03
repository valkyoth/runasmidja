# Rust Data-Transformation Workbench — Planning Bundle

Prepared **2 October 2026** for a Rust 1.99.0, security-first, local-first CyberChef-style web application. Project naming is deliberately left open; `workbench-*` identifiers are architectural placeholders.

## Contents

- **ARCHITECTURE.md** — Detailed architecture, Gemini-draft corrections, execution model, UI/API design, no_std/dependency policy, database portability, Vef/Brynja adapter boundaries, security and 1.0 acceptance.
- **ROADMAP.md** — 240 individually numbered and testable minor releases, 0.1.0 through 0.240.0, followed by candidate/1.0 gates and post-1.0 desktop/mobile milestones.
- **PARITY_AND_RISK_REGISTER.md** — Compatibility inventory process, source-review limits, high-risk implementation areas, evidence requirements and 20 tracked planning risks.
- **roadmap.json** — Machine-readable release objectives, acceptance checks, default dependencies and phase metadata.

## Essential boundaries

The browser defaults to local processing without an account or database. Remote execution and saved server workspaces are optional. The same operation engine serves browser and native hosts. PostgreSQL begins as the production backend; an actual MySQL proof adapter and migration drill test independence before 1.0. Vef is the future native HTTP/web adapter and Brynja the future native TLS provider, including database TLS where supported. Browser-controlled HTTPS remains browser-controlled.

The reviewed reference tag is CyberChef v11.5.0. Exact commit capture, complete operation/argument enumeration and reconciliation of adopted current-source deltas are first-stage implementation tasks. Known certificate-bundle parsing in current source is not silently omitted. No complete operation count, immutable commit, compiled provider stack, speed multiplier or audited implementation is invented.

The release numbers are a baseline work breakdown, not a fixed deadline. Add as many 0.x releases as needed. 1.0.0 requires complete declared functionality and qualification; desktop/mobile application delivery begins afterward. Security tests and conformance run throughout, not only in the last phase.

## Starting point

Read Architecture sections 1–6, then Roadmap phase A. Implement the smallest working browser/native slice at 0.1.0, perform scope reconciliation at 0.2.0, and run hard-feature feasibility at 0.12.0. Do not start by generating hundreds of empty crates or speculative APIs for unavailable sibling repositories.

These documents are proposed engineering plans. Their internal version/phase consistency was checked; no application code has been implemented or tested by creating this bundle. External sources are listed in Architecture section 20, and references to the supplied Gemini material identify its original line ranges.
