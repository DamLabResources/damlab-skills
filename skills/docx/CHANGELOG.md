# Changelog — docx

## [Unreleased]

## [2026-03-30]
- Skill version: 1.1.0
- Added: `docx_tool` self-locating wrapper script (bash, `chmod +x`) so agents can call `docx_tool` directly without a `python` prefix
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern; `DOCX_TOOL` now resolves to `docx_tool` wrapper, `PANDOC` resolves to `bin/pandoc`
- Added: `## Allowlist entries` section with probe commands for `docx_tool` and `bin/pandoc`
- Changed: `## Full flag reference`, `## Patterns`, and style template paths updated to use skill-relative `$(dirname ...)` form
- Changed: removed hardcoded `~/.cursor/skills/docx/styles/` in favour of `styles/` relative reference

## [2026-03-25] — Initial skill
- Tool versions: python-docx latest, pandoc latest, docx-revisions latest at install time
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, patterns.md, environment.yaml, docx_tool.py
