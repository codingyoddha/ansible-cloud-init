# Same-Disk Encrypted Application Data

Use an unencrypted root filesystem and a same-disk LUKS2 partition mounted at
`/secure`. Store LLDAP and Authelia persistent data there, recover disposable
hosts from encrypted off-server restic backups, and defer paid Hetzner Volumes
and full-root encryption.

