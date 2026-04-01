# FAQ / Troubleshooting

Common issues when installing or using [damlab-skills](README.md). For full install steps see [INSTALL.md](INSTALL.md).

## `install.sh` skipped creating environments

**Symptom:** Log says neither `mamba` nor `conda` was found.

**Fix:** Install [Mamba](https://mamba.readthedocs.io/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), ensure it is on your `PATH`, then re-run:

```bash
bash install.sh
```

Or create envs manually (example):

```bash
mamba env create --prefix venvs/samtools -f skills/samtools/environment.yaml
```

Then run `bash install.sh` once so `skills/<tool>/bin` symlinks exist.

## Allowlist still blocks commands

**Symptom:** Agent runs a command but the IDE blocks it.

**Causes:**

1. First token is **`~`**, a **variable**, or a **relative** path — allowlists often see the command **before** shell expansion.
2. Wrong binary — you allowlisted `samtools` but the skill uses a different path after symlink.
3. **Pipeline** — both commands need allowed first tokens if both are restricted.

**Fix:** Use the exact path from the skill’s `## Allowlist entries` section:

```bash
readlink -f "$(dirname /absolute/path/to/SKILL.md)/bin/samtools"
```

Add **that** output to the allowlist. For wrappers (e.g. `plot_tool`), use the path printed by the skill’s documented `readlink` command.

## `bin/<tool>` missing or broken symlink

**Symptom:** `skills/<tool>/bin` does not exist or points nowhere.

**Fix:**

1. Ensure `venvs/<tool>/` was created (conda succeeded).
2. Re-run **`bash install.sh`** from the repo root (refreshes `skills/<tool>/bin` → `../../venvs/<tool>/bin`).

If `venvs/<tool>` is missing, create it with `mamba env create --prefix venvs/<tool> -f skills/<tool>/environment.yaml`, then run `install.sh` again.

## macOS: `readlink -f` not found or wrong behavior

GNU `readlink -f` is common on Linux. On **macOS**, the stock `readlink` may not support `-f`.

**Alternatives:**

```bash
# BSD realpath (macOS)
realpath "$(dirname /path/to/SKILL.md)/bin/samtools"
```

Or Python:

```bash
python3 -c 'import os; print(os.path.realpath("/path/to/skills/samtools/bin/samtools"))'
```

Use whatever produces a **single absolute path** for the allowlist.

## Conda solve failures or wrong package versions

**Symptom:** `mamba env create` fails or pulls unexpected builds.

**Fixes:**

- Ensure [Bioconda](https://bioconda.github.io/) channel order matches your policy (`bioconda`, `conda-forge`, `defaults` as in each `environment.yaml`).
- Remove the broken prefix and retry: `rm -rf venvs/<tool>` then `bash install.sh`.
- For reproducibility in production, consider pinning versions in a fork (this repo often uses “latest compatible” from conda).

## OpenClaw does not see skills

**Symptom:** Skills linked but agent does not list them.

**Fixes:**

- Confirm you linked into a [documented OpenClaw location](https://docs.openclaw.ai/skills) (e.g. `~/.openclaw/skills` via `bash install.sh --openclaw`).
- Start a **new session** after install; some clients snapshot skills at session start.
- Check for **name conflicts** — workspace or higher-precedence skill folders can override the same skill name.

## Skills linked to the wrong place

**Symptom:** You used `--openclaw` but wanted Cursor, or vice versa.

**Fix:** Re-run with the intended flag:

```bash
bash install.sh --cursor
# or
bash install.sh --openclaw
```

Symlinks in the previous destination are not removed automatically; remove old links manually if needed (see [INSTALL.md](INSTALL.md) uninstall section).
