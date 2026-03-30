# Changelog — samtools

## [Unreleased]

## [2026-03-30]
- Skill version: 1.1.0
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern instead of `$VAR` shell variable export
- Added: `## Allowlist entries` section with per-machine resolution instructions
- Changed: `## Full flag reference` and `## Patterns` grep paths updated to use skill-relative `$(dirname ...)` form

## [2026-03-17] — Initial skill
- Tool version: latest at install time — check with:
  `conda run -n damlab-skill-samtools samtools --version`
- Skill version: 1.0.0
- Added: initial SKILL.md with sort/index, view, flagstat, markdup, fastq, faidx, depth patterns
- Added: reference.md covering indexing, file operations, editing, statistics, and pileup subcommands
- Added: environment.yaml (no version pin, resolves latest from bioconda)
