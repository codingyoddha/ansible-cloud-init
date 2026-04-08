# Repo Instructions

This repository is for the first machine-side `ansible-pull` bootstrap only.

## Scope

- Keep changes minimal and focused on the file or role the user asked for.
- Do not add extra services, examples, or scaffolding unless the user explicitly requests them.
- Do not introduce unrelated playbooks, handlers, defaults, task splits, or repo structure changes unless asked.
- If the user says to focus on Docker, stay on Docker only.

## Target Environment

- Target OS is Debian Trixie.
- Target CPU may be Intel/AMD64 or ARM.
- Do not add Ubuntu branches, distro assertions, or environment checks unless explicitly requested.

## User and Privilege Model

- The managed user is `ansible`.
- Privileged operations must run through `ansible` using `sudo` for audit purposes.
- Prefer `remote_user: ansible`, `become: true`, and `become_method: sudo` when working in playbook-style files.
- Do not switch task execution to some other user unless the user explicitly asks for that.

## Editing Style

- Prefer the smallest correct change over proactive restructuring.
- Preserve the existing file layout unless the user asks for a refactor.
- Avoid adding defensive logic, validations, or assertions when the user has already provided the required environment assumptions.
- Do not broaden the problem statement on your own.
