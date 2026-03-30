# Changelog — rclone

## [Unreleased]

## [2026-03-30]
- Skill version: 1.1.0
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern instead of `$VAR` shell variable export
- Added: `## Allowlist entries` section with per-machine resolution instructions
- Changed: `## Full flag reference` and `## Patterns` grep paths updated to use skill-relative `$(dirname ...)` form

## [2026-03-20] — Initial skill
- Tool version: latest at install time (run `readlink -f "$(dirname <SKILL.md path>)/bin/rclone"` then `<path> version` to check)
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, patterns.md, environment.yaml
