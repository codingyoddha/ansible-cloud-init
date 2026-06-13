# Ansible pull for cloud-init

First-boot bootstrap for a replaceable Debian Trixie production host. It installs
rootless Podman prerequisites and enrolls the host in NetBird. Application
services and persistent state are managed by the separate production-services
repository.

`docker.yml` remains available as a standalone optional runtime playbook for
other servers. It is intentionally not imported by `bootstrap.yml`; choose one
runtime owner per server.

`secure-data.yml` configures and validates the prepared same-disk LUKS2
application-data partition. Supply `luks_passphrase` through Ansible Vault and
set `wipe_luks_device=true` only for the first format. The key is never stored
on the host; `/secure` requires manual unlock after reboot.

Persistent LLDAP and Authelia data must use `/secure/lldap` and
`/secure/authelia`. Back these paths up to encrypted off-server restic storage
and test full restoration onto a disposable host.

Approved implementation plans are stored under `docs/plans/`.

## License

GPL-3.0-or-later. See `LICENSE`.
