# Dependency-free probe scaffold; production server packaging is a later milestone.
FROM scratch
COPY target/x86_64-unknown-linux-musl/release/runasmidja-server /runasmidja-server
USER 65532:65532
ENTRYPOINT ["/runasmidja-server"]
CMD ["18080", "--container"]
