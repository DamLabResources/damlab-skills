# Changelog — seqkit

## [Unreleased]

## [2026-03-30]
- Skill version: 1.1.0
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern instead of `$VAR` shell variable export
- Added: `## Allowlist entries` section with per-machine resolution instructions
- Changed: `## Full flag reference` and `## Patterns` grep paths updated to use skill-relative `$(dirname ...)` form

## [2026-03-17] — Initial skill
- Tool version: latest at install time — check with:
  `conda run -n damlab-skill-seqkit seqkit version`
- Skill version: 1.0.0
- Added: initial SKILL.md with stats, seq filtering, fq2fa, grep, sample, subseq, revcomp, split2 patterns
- Added: reference.md covering statistics, transformation, search, format conversion, sampling, splitting, and utilities
- Added: environment.yaml (no version pin, resolves latest from bioconda)
