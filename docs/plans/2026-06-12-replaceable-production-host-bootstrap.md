# Replaceable Production Host Bootstrap

Status: current

Approved: 2026-06-12

## Summary

Keep this repository limited to first-boot host preparation. Install rootless
Podman prerequisites and NetBird, then let the separate production-services
repository own applications, persistent state, backups, and restoration.

## Decisions

- Debian Trixie hosts are disposable and rebuilt through Ansible.
- Podman replaces Docker as the host application runtime.
- The bootstrap does not install PostgreSQL, identity services, or K3s.
- Future approved plans are saved and indexed under `docs/plans/`.

## Verification

- Validate Ansible syntax.
- Run the bootstrap twice and confirm idempotent host preparation.
- Confirm Podman can run rootless as the managed user.
- Confirm NetBird remains connected after reboot.
