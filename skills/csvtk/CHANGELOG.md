# Changelog — csvtk

## [Unreleased]

## [2026-03-30]
- Skill version: 1.1.0
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern instead of `$VAR` shell variable export
- Added: `## Allowlist entries` section with per-machine resolution instructions
- Changed: `## Full flag reference` and `## Patterns` grep paths updated to use skill-relative `$(dirname ...)` form

## [2026-03-17] — Initial skill
- Tool version: latest at install time — check with:
  `conda run -n damlab-skill-csvtk csvtk version`
- Skill version: 1.0.0
- Added: initial SKILL.md with dim/headers, cut, filter2, freq, summary, join, sort, csv2tab/tab2csv patterns
- Added: note on critical global flags (-t for TSV input, -T for TSV output)
- Added: reference.md covering inspection, column/row operations, aggregation, combining files, sorting, reshaping, format conversion, and utilities
- Added: environment.yaml (no version pin, resolves latest from bioconda)
