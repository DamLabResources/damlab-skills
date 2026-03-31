# Changelog — deep-research-query

## [Unreleased]

## [2026-03-30]
- Skill version: 1.2.0
- Changed: pandoc cross-reference in Phase 4 now uses the allowlist-safe `readlink -f` probe pattern pointing to the docx skill directory, instead of a hardcoded `~/.cursor/skills/docx/` path

## [2026-03-26] — Collaborative workflow
- Skill version: 1.1.0
- Changed: restructured into five explicit phases (clarifying questions, search planning, initial search + theme report, optional additional searches, drafting)
- Added: Phase 0 pre-search clarifying questions block
- Added: Phase 2 theme-report checkpoint with unexpected-territory surfacing and user direction prompt
- Added: Phase 3 optional additional searches loop
- Added: Phase 5 implied-concept gap check self-audit after drafting
- Added: explicit "never proceed silently through a phase gate" rule throughout

## [2026-03-26] — Initial skill
- Skill version: 1.0.0
- Added: initial SKILL.md with review-type selection, search planning workflow, screening and extraction workflow, and writing guidance
- Added: patterns.md stub
