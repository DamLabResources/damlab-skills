# Changelog — csvtk

## [Unreleased]

## [2026-03-17] — Initial skill
- Tool version: latest at install time — check with:
  `conda run -n damlab-skill-csvtk csvtk version`
- Skill version: 1.0.0
- Added: initial SKILL.md with dim/headers, cut, filter2, freq, summary, join, sort, csv2tab/tab2csv patterns
- Added: note on critical global flags (-t for TSV input, -T for TSV output)
- Added: reference.md covering inspection, column/row operations, aggregation, combining files, sorting, reshaping, format conversion, and utilities
- Added: environment.yaml (no version pin, resolves latest from bioconda)
