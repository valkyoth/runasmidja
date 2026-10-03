//! Portable facade for Runasmidja.
//!
//! Initial scaffold; product behavior is planned and has not shipped.
#![no_std]
#![forbid(unsafe_code)]

/// Portable domain foundations.
pub use runasmidja_core as core;
/// Replaceable cryptographic boundary.
pub use runasmidja_crypto as crypto;
/// Replaceable HTML boundary.
pub use runasmidja_html as html;
/// Host integration contracts.
pub use runasmidja_ports as ports;
