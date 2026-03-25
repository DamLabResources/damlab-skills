# damlab-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Curated [Cursor Agent Skills](https://docs.cursor.com/agent/skills) for command-line bioinformatics tools used in the Dampier lab. Each skill is an [AgentSkills](https://agentskills.io/)-compatible folder with a `SKILL.md` (YAML `name` and `description` plus usage notes) so coding agents learn how to invoke the tool, common patterns, and where to look up full `--help` text.

The same layout works in other agents that load skills from standard locations (for example OpenClaw, which uses AgentSkills-compatible directories under workspace `skills/` and `~/.openclaw/skills`; see [OpenClaw skills](https://docs.openclaw.ai/skills/) for `openclaw skills install`, updates, and [ClawHub](https://clawhub.com/). This repo is a **monorepo** of multiple skills: clone or copy the `skills/<name>/` directory you need, or point your agent’s extra skills path at this checkout’s `skills/` tree if your client supports it.

## Skills

| Skill | Tool | Description |
|---|---|---|
| `samtools` | [samtools](https://www.htslib.org/) | SAM/BAM/CRAM alignment file manipulation |
| `seqkit` | [seqkit](https://bioinf.shenwei.me/seqkit/) | FASTA/FASTQ sequence manipulation |
| `csvtk` | [csvtk](https://bioinf.shenwei.me/csvtk/) | CSV/TSV tabular data manipulation |
| `pod5` | [pod5](https://github.com/nanoporetech/pod5-file-format) | POD5 nanopore raw signal file inspection, merging, filtering, subsetting, and conversion |
| `crispresso` | [CRISPResso2](https://docs.crispresso.com/) | CRISPR genome editing outcome analysis from amplicon sequencing (indels, HDR, base editing, prime editing) |
| `rclone` | [rclone](https://rclone.org/) | Sync and transfer files with cloud storage and remote backends (S3, GCS, Drive, SFTP, etc.) |
| `create-skill` | — | Meta-skill: conventions for adding new skills to this repo |
| `bioinfo-best-practices` | — | Meta-skill: workflow conventions for reproducible bioinformatics analysis and debugging |
| `bioinformatics-methods-results-writer` | — | Meta-skill: draft Methods and Results manuscript sections from code, notebooks, logs, figures, and tables |

## Why conda environments instead of MCP servers?

These skills tell the agent to run **real CLI binaries** on your machine. We ship a conda `environment.yaml` per tool and [install.sh](install.sh) creates an isolated **prefix environment** under `venvs/<tool>/` (not a long-lived MCP server).

- **No extra daemon:** MCP servers are often separate processes with their own lifecycle, transport, and failure modes. Here the agent runs the tool in a normal shell when needed.
- **Reproducible stacks:** Bioconda / conda-forge pin the tool and its native dependencies in one place. MCP wrappers vary in how they bundle or call binaries.
- **Simpler operations:** After `install.sh`, you are not starting, updating, or authenticating a server socket—only refreshing envs when you choose.
- **Local trust boundary:** You still trust conda packages, but you are not adding a generic RPC layer in front of every command.

MCP remains a good fit when there is **no meaningful CLI** (hosted APIs, browsers, ticketing systems). For file-oriented bioinformatics CLIs, conda-isolated binaries plus skills are usually less moving parts.

## Compatibility and discovery (SEO)

- **Cursor:** Skills in `~/.cursor/skills/<name>/` or project `.cursor/skills/<name>/` are discovered automatically; relevance is driven by the `description` field in each `SKILL.md` frontmatter ([Cursor docs](https://docs.cursor.com/agent/skills)).
- **Keywords:** agent skills, Cursor, OpenClaw, ClawHub, bioinformatics, Bioconda, SAM, BAM, FASTQ, nanopore, CRISPR, cloud sync.
- **GitHub repository topics (set in repo settings):** e.g. `cursor`, `agent-skills`, `bioinformatics`, `conda`, `bioconda`, `openclaw`, `samtools`, `seqkit`.

## Installation

**Prerequisites:** `git`, and either [Mamba](https://mamba.readthedocs.io/) or [Conda](https://docs.conda.io/) on your `PATH` (install.sh prefers `mamba` when available).

```bash
git clone https://github.com/DamLabResources/damlab-skills ~/repos/damlab-skills
cd ~/repos/damlab-skills
bash install.sh
```

What [install.sh](install.sh) does:

1. For each tool skill, creates a conda environment **at a prefix path** `venvs/<tool>/` from `skills/<tool>/environment.yaml`, unless that directory already exists.
2. Symlinks `skills/<tool>/bin` → `../../venvs/<tool>/bin` so each `SKILL.md` can use stable paths like `~/.cursor/skills/samtools/bin/samtools` after linking.
3. Symlinks each skill directory into `~/.cursor/skills/`.

The `name:` field inside each `environment.yaml` (e.g. `damlab-skill-samtools`) is **documentation only**; install uses `--prefix` and does not register a conda **named** env. See [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md).

The `venvs/` directory is gitignored. Restart Cursor after install so skills reload.

Re-running `install.sh` is safe: existing prefix envs are skipped; symlinks are refreshed.

## Updating

```bash
cd ~/repos/damlab-skills
git pull
bash install.sh   # re-links any new skills; skips existing prefix envs
```

To **rebuild** a tool environment (e.g. pick up a newer Bioconda build):

```bash
cd ~/repos/damlab-skills
rm -rf venvs/samtools
bash install.sh
# or, equivalently:
# mamba env create --prefix venvs/samtools -f skills/samtools/environment.yaml
# then ensure install.sh has run once so skills/<tool>/bin symlinks exist
```

## Cursor setup (no MCP required)

Skills load automatically from `~/.cursor/skills/`. No `mcp.json` entry is required. For project-local sharing, symlink into `.cursor/skills/` in the repo root.

## Repo structure

```
damlab-skills/
├── CHANGELOG.md
├── LICENSE
├── README.md
├── WISHLIST.md
├── install.sh
├── venvs/                    # prefix conda envs (gitignored): venvs/<tool>/
└── skills/
    └── <tool>/
        ├── SKILL.md          # frontmatter + subcommands + patterns
        ├── reference.md      # captured --help output
        ├── patterns.md
        ├── environment.yaml  # conda spec; name: is docs-only for prefix installs
        ├── CHANGELOG.md
        └── bin/              # symlink -> ../../venvs/<tool>/bin (created by install.sh)
```

Tool names under `skills/` match rows in the table above plus meta-skills `create-skill`, `bioinfo-best-practices`, and `bioinformatics-methods-results-writer`.

## Adding a new skill

Use the `create-skill` skill in Cursor or follow the checklist in [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md).

**Contributing:** follow [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md) and open a pull request.

Roadmap ideas: [WISHLIST.md](WISHLIST.md). Release history: [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).
