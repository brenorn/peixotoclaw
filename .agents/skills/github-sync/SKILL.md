---
name: github-sync
description: Automate safe, industrial synchronization of the PeixotoClaw workspace to GitHub. This skill implements the "Nuclear Reset" pattern with safety branching to prevent data loss and ensure privacy. Use this skill when the user wants to "subir para o git", "sincronizar workspace", or needs a clean "re-upload" that strictly respects .gitignore and privacy rules.
---

# GitHub Sync (Safety-First)

This skill automates the process of synchronizing the PeixotoClaw workspace to a remote repository (GitHub) while ensuring that personal project data and archival bloat are never uploaded.

## Workflow

1. **Safety Branching**: The skill ALWAYS creates a new branch named `sync/YYYY-MM-DD-HHmm` before performing any synchronization.
2. **Index Purge (Nuclear Reset)**: It clears the Git index (`git rm -r --cached .`) to ensure that previously tracked but now ignored folders (like `projects/`) are properly removed.
3. **Core Mapping**: It adds only the essential core folders and files:
    - `.agents/`, `.rulebook/`, `.claude/`, `.cursor/`, `.github/`
    - `scripts/`, `src/`, `templates/`, `dashboard/`
    - Root configuration files (`package.json`, `README.md`, `.gitignore`, etc.)
4. **Privacy Audit**: A script-based validation ensures no forbidden paths (e.g., `projects/`) are staged.
5. **Push to Branch**: The changes are committed with a Conventional Commit message in English and pushed to the new branch on `origin`.

## Usage

Run the sync script located at `scripts/sync.py`:

```bash
python .agents/skills/github-sync/scripts/sync.py
```

## Security Rules

- **NEVER** push directly to `main` if the environment is in a "Nuclear Reset" state.
- **NEVER** force-add the `projects/` directory.
- **ALWAYS** check the output of the privacy auditor.

---
**Signed**: @Maestro (Orquestrador PeixotoClaw)
