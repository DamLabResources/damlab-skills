# Installation

This guide is for **first-time setup** of [damlab-skills](README.md): clone the repo, create conda prefix environments, symlink skills into your agent’s skills directory, and verify a tool runs.

**Platforms:** Linux and macOS are supported. On **Windows**, use **WSL2** and follow the Linux steps inside the WSL distro.

## Prerequisites

| Requirement | Check |
|-------------|--------|
| `git` | `command -v git` |
| [Mamba](https://mamba.readthedocs.io/) or [Conda](https://docs.conda.io/) | `command -v mamba || command -v conda` |

`install.sh` prefers `mamba` when both are available.

## Clone and install

```bash
git clone https://github.com/DamLabResources/damlab-skills ~/repos/damlab-skills
cd ~/repos/damlab-skills
bash install.sh
```

By default, skills are linked into **`~/.cursor/skills/`** (Cursor global discovery).

### Choose where skills are linked (Cursor / OpenClaw / custom)

The conda environments always live under the repo at **`venvs/<tool>/`**. Only the **symlink destination** for skill folders changes.

| Goal | Command |
|------|---------|
| **Cursor** (default) | `bash install.sh` or `bash install.sh --cursor` |
| **OpenClaw** ([managed/local skills](https://docs.openclaw.ai/skills)) | `bash install.sh --openclaw` → `~/.openclaw/skills/` |
| **Custom directory** | `bash install.sh --dest /path/to/skills` |

You can also set **`SKILLS_DST`** (same meaning as `--dest`):

```bash
SKILLS_DST=~/.openclaw/skills bash install.sh
```

Run **`bash install.sh --help`** for the full option list.

### What `install.sh` does

1. For each **tool** skill, creates a conda environment at **`venvs/<tool>/`** from `skills/<tool>/environment.yaml`, unless that directory already exists.
2. Symlinks **`skills/<tool>/bin`** → **`../../venvs/<tool>/bin`** so each `SKILL.md` can use paths like `bin/<tool>` relative to the skill directory.
3. Symlinks each skill directory into **`$SKILLS_DST`** (default `~/.cursor/skills`).

The `name:` field in each `environment.yaml` is **documentation only**; install uses `--prefix` and does not create a conda **named** env. See [skills/create-skill/SKILL.md](skills/create-skill/SKILL.md).

The **`venvs/`** directory is gitignored. **Restart** Cursor or start a **new OpenClaw session** after install so skills reload.

Re-running `install.sh` is safe: existing prefix envs are skipped; symlinks are refreshed.

## Verify installation

1. **Skill symlink** (adjust path if you used `--openclaw` or `--dest`):

   ```bash
   ls -la ~/.cursor/skills/samtools
   ```

2. **Binary path** (use the path from the skill you care about; `plotting` uses `plot_tool` at the skill root—see its `SKILL.md`):

   ```bash
   readlink -f "$(dirname "$HOME/.cursor/skills/samtools/SKILL.md")/bin/samtools"
   ```

3. **Run the tool** (use the **literal** path from step 2 as the first token):

   ```bash
   /full/path/from/step/2 --version
   ```

## Terminal command allowlist (Cursor and similar)

Many agents evaluate an allowlist against the **literal first token** of each shell command—**before** `~` or variables expand. Skills in this repo assume you resolve paths with `readlink -f` and allowlist those paths.

**Checklist:**

1. Open the skill’s `SKILL.md` and find **`## Allowlist entries`**.
2. Run the `readlink -f "$(dirname <path-to-SKILL.md>)/bin/<tool>"` command (or the skill-specific variant for wrappers like `plot_tool`).
3. Add the printed path to your IDE’s command allowlist (**one entry per binary**).
4. Re-run the agent command.

**Pipelines:** both sides of a pipe must use **resolved literal** paths, e.g.  
`<resolved-samtools> view -b in.sam | <resolved-seqkit> stats`.

See [FAQ.md](FAQ.md) if commands still get blocked.

## Updating repo vs upgrading tool versions

**Update the repo and refresh links:**

```bash
cd ~/repos/damlab-skills
git pull
bash install.sh
# pass --openclaw or --dest if you use a non-default SKILLS_DST
```

**Rebuild one tool’s conda env** (e.g. newer Bioconda build):

```bash
cd ~/repos/damlab-skills
rm -rf venvs/samtools
bash install.sh
# or: mamba env create --prefix venvs/samtools -f skills/samtools/environment.yaml
# then run install.sh once so skills/<tool>/bin symlinks exist
```

## Uninstall

- **Remove skill symlinks** from your chosen destination only (does not delete the repo):

  ```bash
  rm -f ~/.cursor/skills/samtools   # repeat per skill, or remove the whole skills dir contents you linked
  ```

  For OpenClaw: `~/.openclaw/skills/<skill>`.

- **Remove conda envs** (frees disk space):

  ```bash
  rm -rf ~/repos/damlab-skills/venvs
  ```

- **Remove the git clone** if you no longer need the repo:

  ```bash
  rm -rf ~/repos/damlab-skills
  ```

## Claude Code

Claude Code does not use the same global “skills folder” as Cursor. Treat this repo as the **source of truth**: point the agent at `skills/<name>/SKILL.md` and follow the same **literal-path** convention for any bash allow/deny rules you configure. See [PHILOSOPHY.md](PHILOSOPHY.md).

## Further reading

- [PHILOSOPHY.md](PHILOSOPHY.md) — design goals and tradeoffs
- [FAQ.md](FAQ.md) — common failures
- [CONTRIBUTING.md](CONTRIBUTING.md) — adding or changing skills
