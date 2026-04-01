# Philosophy

This document explains **why** [damlab-skills](README.md) is structured the way it is, so other teams can adopt or adapt the pattern in their own repos.

## What a skill is (and is not)

A **skill** here is a folder with a `SKILL.md` (YAML frontmatter + operational notes) plus optional reference material. It teaches an agent **how** to run a tool: subcommands, common patterns, and where to look up full `--help` output—without loading huge text into every prompt.

A skill is **not** a long-lived service. It does not replace your own judgment, review of commands, or responsibility for data and compliance.

## Why conda prefix environments (`venvs/<tool>/`)

Each tool skill can ship an `environment.yaml`. [install.sh](install.sh) creates an isolated conda **prefix** under the repo at `venvs/<tool>/` (not necessarily a globally “named” conda env). That gives:

- **Reproducible stacks** — Bioconda / conda-forge bring in native dependencies in one place.
- **Debuggability** — You can run the same binary in a normal shell as the agent would.
- **No extra daemon** — Nothing to start, port-forward, or keep alive beyond conda itself.

## Why not MCP for these tools?

[MCP](https://modelcontextprotocol.io/) servers are a great fit when there is **no meaningful CLI** (hosted APIs, browsers, ticketing). For file-oriented bioinformatics CLIs, **conda-isolated binaries + skills** usually mean fewer moving parts: the agent runs a command in a shell when needed, with a clear local trust boundary (you trust the conda packages you installed).

## Why `bin/` symlinks under each skill directory

[install.sh](install.sh) links `skills/<tool>/bin` → `../../venvs/<tool>/bin`. Skills can document commands as `**bin/<tool>`** relative to the skill folder. After linking into `~/.cursor/skills/<tool>` or `~/.openclaw/skills/<tool>`, the same relative layout holds, so paths do not hardcode the repo clone location.

Some skills use a wrapper at the skill root (e.g. `plot_tool`); those skills document the exact path pattern in `SKILL.md`.

## Allowlist-first command design

Clients such as Cursor evaluate **terminal allowlists** against the **literal first token** of a command, **before** the shell expands `~` or variables. Skills therefore instruct agents to:

1. Resolve the real path (e.g. `readlink -f "$(dirname <path-to-SKILL.md>)/bin/<tool>"`).
2. Use that **literal** path as the first token in shell examples.

This keeps examples copy-pasteable into strict allowlist environments. **Pipelines** must resolve both sides if both binaries are allowlisted.

## Security and trust

- **You** control which conda environments exist and which paths are allowlisted.
- Third-party skill content should be treated like **code**: review before enabling, especially if it suggests downloads or privileged operations.
- Prefer **least privilege**: allowlist specific binaries under `.../bin/...` rather than broad patterns when your client supports it.

## Claude Code and other agents

Not every product loads “skills” from `~/.cursor/skills` or `~/.openclaw/skills`. For **Claude Code**, keep this repository (or a fork) as the reference tree and point the agent at `skills/<name>/SKILL.md`; configure permissions / allow rules in line with your org’s policy. The **literal-path** discipline still applies whenever bash execution is gated.

## Related

- [INSTALL.md](INSTALL.md) — step-by-step setup
- [FAQ.md](FAQ.md) — troubleshooting
- [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md) — conventions for new skills

