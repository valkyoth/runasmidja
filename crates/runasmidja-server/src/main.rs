//! Loopback-only development health probe. Not a product HTTP server.
#![forbid(unsafe_code)]
mod probe;

use std::io::{Read, Write};
use std::net::{Ipv4Addr, TcpListener};
use std::time::Duration;

fn main() -> std::io::Result<()> {
    let port = match std::env::args().nth(1) {
        Some(value) => value.parse::<u16>().map_err(|_| {
            std::io::Error::new(std::io::ErrorKind::InvalidInput, "invalid probe port")
        })?,
        None => 18080,
    };
    let address = match std::env::args().nth(2).as_deref() {
        None => Ipv4Addr::LOCALHOST,
        Some("--container") => Ipv4Addr::UNSPECIFIED,
        Some(_) => {
            return Err(std::io::Error::new(
                std::io::ErrorKind::InvalidInput,
                "invalid probe mode",
            ));
        }
    };
    let listener = TcpListener::bind((address, port))?;
    println!("Runasmidja development probe on {}", listener.local_addr()?);
    for connection in listener.incoming() {
        let Ok(mut stream) = connection else { continue };
        stream.set_read_timeout(Some(Duration::from_secs(2)))?;
        stream.set_write_timeout(Some(Duration::from_secs(2)))?;
        let mut buffer = [0_u8; 4096];
        let mut used = 0;
        while used < buffer.len() {
            match stream.read(&mut buffer[used..]) {
                Ok(0) | Err(_) => break,
                Ok(count) => used += count,
            }
            if buffer[..used].windows(4).any(|part| part == b"\r\n\r\n") {
                break;
            }
        }
        let _ = stream.write_all(probe::response(&buffer[..used]));
    }
    Ok(())
}
