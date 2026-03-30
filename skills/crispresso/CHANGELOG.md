# Changelog — crispresso

## [Unreleased]

## [2026-03-30]
- Skill version: 1.1.0
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern instead of `$VAR` shell variable export (all 6 binaries)
- Added: `## Allowlist entries` section listing probe commands for all 6 CRISPResso binaries
- Changed: `## Full flag reference` and `## Patterns` grep paths updated to use skill-relative `$(dirname ...)` form

## [2026-03-19] — Initial skill
- Documented `CRISPRessoAggregate` sample ordering (alphabetical by path; no CLI order flag) in SKILL.md, with symlink-prefix workaround in patterns.md.
- Tool version: latest at install time (run `readlink -f "$(dirname <SKILL.md path>)/bin/CRISPResso"` then `<path> --version` to check)
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, patterns.md, environment.yaml
- Reference source: docs.crispresso.com v2.3.3
