# damlab-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Curated [Cursor Agent Skills](https://docs.cursor.com/agent/skills) for command-line bioinformatics tools used in the Dampier lab. Each skill is an [AgentSkills](https://agentskills.io/)-compatible folder with a `SKILL.md` (YAML `name` and `description` plus usage notes) so coding agents learn how to invoke the tool, common patterns, and where to look up full `--help` text.

**New here?** Read [INSTALL.md](INSTALL.md) (setup), [PHILOSOPHY.md](PHILOSOPHY.md) (why this layout), and [FAQ.md](FAQ.md) (troubleshooting). **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md).

## Quickstart

```bash
git clone https://github.com/DamLabResources/damlab-skills ~/repos/damlab-skills
cd ~/repos/damlab-skills
bash install.sh
```

- Default: links skills into **`~/.cursor/skills/`**. Use **`bash install.sh --openclaw`** for **`~/.openclaw/skills/`**, or **`bash install.sh --dest /path/to/skills`**. See [INSTALL.md](INSTALL.md).
- Restart Cursor (or start a new OpenClaw session) after install.
- **Versioning:** repo-level history and SemVer policy are in [CHANGELOG.md](CHANGELOG.md).

## Skills

| Skill | Tool | Description |
|---|---|---|
| `samtools` | [samtools](https://www.htslib.org/) | SAM/BAM/CRAM alignment file manipulation |
| `seqkit` | [seqkit](https://bioinf.shenwei.me/seqkit/) | FASTA/FASTQ sequence manipulation |
| `csvtk` | [csvtk](https://bioinf.shenwei.me/csvtk/) | CSV/TSV tabular data manipulation |
| `pod5` | [pod5](https://github.com/nanoporetech/pod5-file-format) | POD5 nanopore raw signal file inspection, merging, filtering, subsetting, and conversion |
| `crispresso` | [CRISPResso2](https://docs.crispresso.com/) | CRISPR genome editing outcome analysis from amplicon sequencing (indels, HDR, base editing, prime editing) |
| `rclone` | [rclone](https://rclone.org/) | Sync and transfer files with cloud storage and remote backends (S3, GCS, Drive, SFTP, etc.) |
| `docx` | [python-docx](https://python-docx.readthedocs.io/) + [pandoc](https://pandoc.org/) | Read, write, and track-change Microsoft Word .docx files |
| `ncbi-edirect` | [NCBI EDirect](https://www.ncbi.nlm.nih.gov/books/NBK179288/) | Search NCBI databases and download papers, sequences, and records (esearch, efetch, elink, xtract) |
| `plotting` | [Altair](https://altair-viz.github.io/) + [vl-convert](https://github.com/vega/vl-convert) | Declarative charts (Vega-Lite): PNG/SVG and interactive HTML from Python or JSON specs |
| `eda` | Python (numpy, pandas, matplotlib, seaborn, pingouin, statsmodels, scikit-learn, Jupyter kernel tooling) | Notebook-first collaborative exploratory data analysis workflow for tabular biological data |
| `jupyter-notebook` | [Jupytext](https://jupytext.readthedocs.io/) + [nbformat](https://nbformat.readthedocs.io/) + [nbconvert](https://nbconvert.readthedocs.io/) | Convert, execute, diff, sync, and read outputs from `.ipynb` notebooks |
| `create-skill` | — | Meta-skill: conventions for adding new skills to this repo |
| `bioinfo-best-practices` | — | Meta-skill: workflow conventions for reproducible bioinformatics analysis and debugging |
| `bioinformatics-methods-results-writer` | — | Meta-skill: draft Methods and Results manuscript sections from code, notebooks, logs, figures, and tables |
| `deep-research-query` | — | Meta-skill: plan and execute rigorous literature searches, evidence syntheses, and review-style summaries for biomedical and computational biology topics |

## Documentation map

| Doc | Purpose |
|-----|---------|
| [INSTALL.md](INSTALL.md) | Prerequisites, `install.sh` options (Cursor / OpenClaw / custom), verification, allowlist, update, uninstall |
| [PHILOSOPHY.md](PHILOSOPHY.md) | Design goals: conda vs MCP, allowlist-first paths, security |
| [FAQ.md](FAQ.md) | Common failures (conda missing, allowlist, macOS `readlink`, OpenClaw discovery) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose changes and add skills |
| [CHANGELOG.md](CHANGELOG.md) | Repo-level release notes and SemVer |
| [WISHLIST.md](WISHLIST.md) | Roadmap ideas |

## Other agents (OpenClaw, project-local, Claude Code)

- **OpenClaw:** Uses AgentSkills-compatible directories; install with `bash install.sh --openclaw` or see [OpenClaw skills](https://docs.openclaw.ai/skills/). You can also copy or point `skills.load.extraDirs` at this repo’s `skills/` tree if your config supports it.
- **Project-local sharing:** Symlink into `.cursor/skills/` in a repo root, or use OpenClaw’s workspace `/skills` / `.agents/skills` per their docs.
- **Claude Code:** No universal skills folder like Cursor; use this repo as the reference tree and point the agent at `skills/<name>/SKILL.md`. See [INSTALL.md](INSTALL.md#claude-code) and [PHILOSOPHY.md](PHILOSOPHY.md#claude-code-and-other-agents).

## Why conda environments instead of MCP servers?

Briefly: these skills run **real CLI binaries** via conda prefix envs under `venvs/<tool>/`, not a long-lived MCP server—fewer moving parts for file-oriented tools. Full rationale: [PHILOSOPHY.md](PHILOSOPHY.md).

## Repo structure

```
damlab-skills/
  CHANGELOG.md
  CONTRIBUTING.md
  FAQ.md
  INSTALL.md
  LICENSE
  PHILOSOPHY.md
  README.md
  WISHLIST.md
  install.sh
  venvs/                    # prefix conda envs (gitignored): venvs/<tool>/
  skills/<tool>/
    SKILL.md                 # frontmatter + subcommands + patterns
    reference.md             # captured --help output
    patterns.md
    environment.yaml         # conda spec; name: is docs-only for prefix installs
    CHANGELOG.md
    bin/                     # symlink -> ../../venvs/<tool>/bin (created by install.sh)
```

## License

MIT. See [LICENSE](LICENSE).
