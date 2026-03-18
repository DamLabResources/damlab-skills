#!/usr/bin/env bash
# install.sh — set up damlab-skills on a new machine
#
# 1. Creates a conda env for each skill from its environment.yaml (skips if already exists)
# 2. Symlinks each skill directory into ~/.cursor/skills/
#
# Usage: bash install.sh
# Re-running is safe: existing envs are skipped, symlinks are refreshed.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DST="$HOME/.cursor/skills"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log()  { echo "[install] $*"; }
warn() { echo "[install] WARNING: $*" >&2; }

conda_env_exists() {
    conda env list 2>/dev/null | awk '{print $1}' | grep -qx "$1"
}

# ---------------------------------------------------------------------------
# Skill directories — add new entries here when skills are added to the repo
# ---------------------------------------------------------------------------

TOOL_SKILLS=(samtools seqkit csvtk)
META_SKILLS=(create-skill)

# ---------------------------------------------------------------------------
# 1. Create conda environments
# ---------------------------------------------------------------------------

log "Creating conda environments..."

# Ensure conda is available
if ! command -v conda &>/dev/null; then
    warn "conda not found in PATH. Skipping env creation."
    warn "Install conda/mamba and re-run, or create envs manually:"
    for skill in "${TOOL_SKILLS[@]}"; do
        warn "  conda env create -f $REPO_DIR/$skill/environment.yaml"
    done
else
    for skill in "${TOOL_SKILLS[@]}"; do
        env_file="$REPO_DIR/$skill/environment.yaml"
        if [[ ! -f "$env_file" ]]; then
            warn "No environment.yaml found for $skill — skipping"
            continue
        fi

        env_name="damlab-skill-$skill"
        if conda_env_exists "$env_name"; then
            log "  $env_name already exists — skipping (remove and re-run to upgrade)"
        else
            log "  Creating $env_name from $skill/environment.yaml ..."
            conda env create -f "$env_file"
            log "  $env_name created."
        fi
    done
fi

# ---------------------------------------------------------------------------
# 2. Symlink skill directories into ~/.cursor/skills/
# ---------------------------------------------------------------------------

log "Linking skills into $SKILLS_DST ..."
mkdir -p "$SKILLS_DST"

for skill in "${TOOL_SKILLS[@]}" "${META_SKILLS[@]}"; do
    src="$REPO_DIR/$skill"
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
log "To upgrade a tool's conda env to the latest version:"
log "  conda env remove -n damlab-skill-<tool>"
log "  conda env create -f <tool>/environment.yaml"
