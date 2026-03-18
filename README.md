# damlab-skills

A collection of [Cursor AgentSkills](https://docs.cursor.com/agent/skills) for bioinformatics tools used in the DAM Lab. Each skill teaches the AI agent how to use a specific tool — its common patterns, invocation conventions, and full command reference.

## Skills

| Skill | Tool | Description |
|---|---|---|
| `samtools` | [samtools](https://www.htslib.org/) | SAM/BAM/CRAM alignment file manipulation |
| `seqkit` | [seqkit](https://bioinf.shenwei.me/seqkit/) | FASTA/FASTQ sequence manipulation |
| `csvtk` | [csvtk](https://bioinf.shenwei.me/csvtk/) | CSV/TSV tabular data manipulation |
| `create-skill` | — | Meta-skill: conventions for adding new skills to this repo |

## Installation

```bash
git clone https://github.com/damlab/damlab-skills ~/repos/damlab-skills
cd ~/repos/damlab-skills
bash install.sh
```

`install.sh` does two things:
1. Creates a dedicated conda environment for each tool (e.g. `damlab-skill-samtools`) from the tool's `environment.yaml`
2. Symlinks each skill directory into `~/.cursor/skills/`

Restart Cursor after running — skills are auto-discovered from `~/.cursor/skills/`.

Running `install.sh` again on a new machine is safe: existing envs are skipped, symlinks are refreshed.

## Updating

```bash
cd ~/repos/damlab-skills
git pull
bash install.sh   # re-links any new skills; skips existing conda envs
```

To update a conda env to the latest tool version:
```bash
conda env remove -n damlab-skill-samtools
conda env create -f samtools/environment.yaml
```

## Cursor Setup (`.cursor/mcp.json` not required)

Skills are loaded automatically by Cursor when placed in `~/.cursor/skills/`. No additional configuration is needed. The agent applies them based on the `description` field in each `SKILL.md`.

For project-level skills (shared via a repo), symlink into `.cursor/skills/` in the project root instead.

## Repo structure

```
damlab-skills/
├── README.md
├── install.sh
├── create-skill/       # Meta-skill for adding new tools to this repo
│   └── SKILL.md
├── samtools/
│   ├── SKILL.md
│   ├── reference.md
│   ├── environment.yaml
│   └── CHANGELOG.md
├── seqkit/
│   ├── SKILL.md
│   ├── reference.md
│   ├── environment.yaml
│   └── CHANGELOG.md
└── csvtk/
    ├── SKILL.md
    ├── reference.md
    ├── environment.yaml
    └── CHANGELOG.md
```

## Adding a new skill

Activate the `create-skill` skill in Cursor (it is symlinked alongside the tool skills) and ask the agent to add a new skill. The meta-skill contains all conventions for this repo.

Alternatively, follow the checklist in `create-skill/SKILL.md` manually.

## License

MIT
