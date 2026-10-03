//! Fixed development probe responses; deliberately excludes product routes.
const OK: &[u8] = b"HTTP/1.1 200 OK\r\nContent-Length: 3\r\nContent-Type: text/plain\r\nX-Content-Type-Options: nosniff\r\nCache-Control: no-store\r\nConnection: close\r\n\r\nok\n";
const BAD: &[u8] = b"HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\nConnection: close\r\n\r\n";

pub(crate) fn response(request: &[u8]) -> &'static [u8] {
    if request.len() > 4096 || !request.ends_with(b"\r\n\r\n") {
        return BAD;
    }
    if request.starts_with(b"GET /healthz HTTP/1.1\r\n") {
        OK
    } else {
        BAD
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn health_is_fixed_and_has_no_cache() {
        assert_eq!(
            response(b"GET /healthz HTTP/1.1\r\nHost: localhost\r\n\r\n"),
            OK
        );
    }
    #[test]
    fn rejects_incomplete_other_routes_and_methods() {
        for input in [
            b"GET /healthz HTTP/1.1\r\n".as_slice(),
            b"POST /healthz HTTP/1.1\r\n\r\n",
            b"GET / HTTP/1.1\r\n\r\n",
            b"GET /healthz HTTP/1.0\r\n\r\n",
            b"",
        ] {
            assert_eq!(response(input), BAD);
        }
    }
    #[test]
    fn bounds_and_binary_input() {
        let oversized = [b'x'; 4097];
        assert_eq!(response(&oversized), BAD);
        assert_eq!(response(b"\xff\x00\r\n\r\n"), BAD);
    }
}
