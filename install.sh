#!/usr/bin/env bash
# install.sh — set up damlab-skills on a new machine
#
# 1. Creates conda envs for each skill under venvs/<toolname>/ (skips if already exists)
# 2. Symlinks each skill directory into a configurable skills destination (default: ~/.cursor/skills/)
#
# Usage: bash install.sh [OPTIONS]
# Environment: SKILLS_DST overrides the destination (same as --dest).
# Re-running is safe: existing envs are skipped, symlinks are refreshed.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$REPO_DIR/skills"
# Default: Cursor global skills. Override with --dest, --openclaw, --cursor, or SKILLS_DST.
SKILLS_DST="${SKILLS_DST:-$HOME/.cursor/skills}"
VENVS_DIR="$REPO_DIR/venvs"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log()  { echo "[install] $*"; }
warn() { echo "[install] WARNING: $*" >&2; }

usage() {
    cat <<'EOF'
Usage: bash install.sh [OPTIONS]

Creates conda prefix envs under ./venvs/<tool>/ and symlinks each skill into the
chosen skills directory so agents (Cursor, OpenClaw, etc.) can discover them.

Options:
  --cursor              Link skills to ~/.cursor/skills (default if no SKILLS_DST)
  --openclaw            Link skills to ~/.openclaw/skills
  --dest DIR            Link skills to DIR (absolute path recommended)
  -h, --help            Show this help

Environment:
  SKILLS_DST            Same as --dest; if set, used unless overridden by flags

Examples:
  bash install.sh
  bash install.sh --openclaw
  bash install.sh --dest /opt/shared/damlab-skills-links
  SKILLS_DST=~/.openclaw/skills bash install.sh
EOF
}

expand_tilde() {
    # Expand leading ~ to $HOME (bash-only, no external realpath needed for ~)
    local p="$1"
    if [[ "$p" == ~ || "$p" == ~/* ]]; then
        p="${p/#\~/$HOME}"
    fi
    printf '%s' "$p"
}

# Parse args (last flag wins; SKILLS_DST env is default before parsing)
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        --cursor)
            SKILLS_DST="$HOME/.cursor/skills"
            shift
            ;;
        --openclaw)
            SKILLS_DST="$HOME/.openclaw/skills"
            shift
            ;;
        --dest)
            if [[ -z "${2:-}" ]]; then
                warn "--dest requires a directory argument"
                usage >&2
                exit 1
            fi
            SKILLS_DST="$(expand_tilde "$2")"
            shift 2
            ;;
        *)
            warn "Unknown option: $1"
            usage >&2
            exit 1
            ;;
    esac
done

SKILLS_DST="$(expand_tilde "$SKILLS_DST")"

venv_exists() {
    [[ -d "$VENVS_DIR/$1" ]]
}

# ---------------------------------------------------------------------------
# Skill directories — add new entries here when skills are added to the repo
# ---------------------------------------------------------------------------

TOOL_SKILLS=(samtools seqkit csvtk pod5 crispresso rclone docx ncbi-edirect plotting eda jupyter-notebook)
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
        # This lets SKILL.md reference <skills-dst>/<skill>/bin/<tool>
        # without hardcoding the repo location.
        ln -sfn "../../venvs/$skill/bin" "$SKILLS_DIR/$skill/bin"
    done
fi

# ---------------------------------------------------------------------------
# 2. Symlink skill directories into SKILLS_DST
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
log "Done. Skills linked under: $SKILLS_DST"
log "Restart your agent / IDE session if skills do not appear immediately."
log ""
log "To upgrade a tool's env to the latest version:"
log "  rm -rf $VENVS_DIR/<tool>"
log "  mamba env create --prefix $VENVS_DIR/<tool> -f skills/<tool>/environment.yaml"
