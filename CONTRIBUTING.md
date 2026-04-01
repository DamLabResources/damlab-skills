# Contributing

Thanks for helping improve **damlab-skills**. This repo holds [AgentSkills](https://agentskills.io/)-compatible tool documentation under `skills/<name>/` plus [install.sh](install.sh) to create conda prefix envs and symlink skills into your agent’s skills directory.

## Before you open a PR

- **Install and smoke-test** locally: [INSTALL.md](INSTALL.md).
- **Follow skill conventions:** [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md) (required files, `SKILL.md` structure, `reference.md` format, allowlist patterns).
- **Keep `SKILL.md` under ~200 lines** — put exhaustive flags in `reference.md` and recipes in `patterns.md`.
- **Update the checklist** when adding a tool skill:
  - Add `<toolname>` to `TOOL_SKILLS` in [install.sh](install.sh).
  - Add a row to the skills table in [README.md](README.md).
  - Add an entry under **Unreleased** in [CHANGELOG.md](CHANGELOG.md) (and `skills/<tool>/CHANGELOG.md` if applicable).

## Semantic versioning (repo level)

Repo-level versioning is documented in [CHANGELOG.md](CHANGELOG.md): patch for doc-only fixes, minor for new skills or substantial README/layout updates, major for breaking install paths or skill layout changes.

## Adding a new tool skill

Use the `create-skill` meta-skill in your editor or follow the step-by-step checklist in [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md).

## Install script behavior

[install.sh](install.sh) supports linking skills to:

- **Cursor (default):** `~/.cursor/skills`
- **OpenClaw:** `bash install.sh --openclaw` → `~/.openclaw/skills`
- **Custom:** `bash install.sh --dest /path/to/skills` or `SKILLS_DST=...`

Contributors do not need to change install behavior unless adding a new top-level skill directory name (add to `TOOL_SKILLS` or `META_SKILLS`).

## Questions

Open an issue or PR on [DamLabResources/damlab-skills](https://github.com/DamLabResources/damlab-skills). Roadmap ideas: [WISHLIST.md](WISHLIST.md).
