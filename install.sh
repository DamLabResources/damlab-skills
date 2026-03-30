#!/usr/bin/env bash
# install.sh — set up damlab-skills on a new machine
#
# 1. Creates conda envs for each skill under venvs/<toolname>/ (skips if already exists)
# 2. Symlinks each skill directory into ~/.cursor/skills/
#
# Usage: bash install.sh
# Re-running is safe: existing envs are skipped, symlinks are refreshed.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$REPO_DIR/skills"
SKILLS_DST="$HOME/.cursor/skills"
VENVS_DIR="$REPO_DIR/venvs"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log()  { echo "[install] $*"; }
warn() { echo "[install] WARNING: $*" >&2; }

venv_exists() {
    [[ -d "$VENVS_DIR/$1" ]]
}

# ---------------------------------------------------------------------------
# Skill directories — add new entries here when skills are added to the repo
# ---------------------------------------------------------------------------

TOOL_SKILLS=(samtools seqkit csvtk pod5 crispresso rclone docx ncbi-edirect)
META_SKILLS=(create-skill bioinfo-best-practices bioinformatics-methods-results-writer deep-research-query)

# ---------------------------------------------------------------------------
# 1. Create conda environments under venvs/
# ---------------------------------------------------------------------------

log "Creating conda environments in $VENVS_DIR ..."
mkdir -p "$VENVS_DIR"

# Prefer mamba for faster solves, fall back to conda
if command -v mamba &>/dev/null; then
    CONDA_CMD=mamba
elif command -v conda &>/dev/null; then
    CONDA_CMD=conda
else
    warn "Neither mamba nor conda found in PATH. Skipping env creation."
    warn "Install mamba or conda and re-run, or create envs manually:"
    for skill in "${TOOL_SKILLS[@]}"; do
        warn "  mamba env create --prefix $VENVS_DIR/$skill -f $SKILLS_DIR/$skill/environment.yaml"
    done
    CONDA_CMD=""
fi

if [[ -n "$CONDA_CMD" ]]; then
    log "Using $CONDA_CMD to create environments."
    for skill in "${TOOL_SKILLS[@]}"; do
        env_file="$SKILLS_DIR/$skill/environment.yaml"
        if [[ ! -f "$env_file" ]]; then
            warn "No environment.yaml found for $skill — skipping"
            continue
        fi

        if venv_exists "$skill"; then
            log "  $VENVS_DIR/$skill already exists — skipping (remove and re-run to upgrade)"
        else
            log "  Creating $VENVS_DIR/$skill from skills/$skill/environment.yaml ..."
            "$CONDA_CMD" env create --prefix "$VENVS_DIR/$skill" -f "$env_file"
            log "  $VENVS_DIR/$skill created."
        fi

        # Create a bin/ symlink inside the skill dir -> ../../venvs/<skill>/bin
        # This lets SKILL.md reference ~/.cursor/skills/<skill>/bin/<tool>
        # without hardcoding the repo location.
        ln -sfn "../../venvs/$skill/bin" "$SKILLS_DIR/$skill/bin"
    done
fi

# ---------------------------------------------------------------------------
# 2. Symlink skill directories into ~/.cursor/skills/
# ---------------------------------------------------------------------------

log "Linking skills into $SKILLS_DST ..."
mkdir -p "$SKILLS_DST"

for skill in "${TOOL_SKILLS[@]}" "${META_SKILLS[@]}"; do
    src="$SKILLS_DIR/$skill"
    dst="$SKILLS_DST/$skill"
    if [[ ! -d "$src" ]]; then
        warn "Skill directory not found: $src — skipping"
        continue
    fi
    ln -sfn "$src" "$dst"
    log "  Linked: $skill -> $dst"
done

# ---------------------------------------------------------------------------

log ""
log "Done. Restart Cursor to pick up new skills."
log ""
log "To upgrade a tool's env to the latest version:"
log "  rm -rf $VENVS_DIR/<tool>"
log "  mamba env create --prefix $VENVS_DIR/<tool> -f skills/<tool>/environment.yaml"
