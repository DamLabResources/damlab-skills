# Changelog — ncbi-edirect

## [Unreleased]

## [2026-03-30] — v1.2.0
- Skill version: 1.2.0
- Changed: Environment section now uses allowlist-safe `readlink -f` probe pattern instead of `$VAR` shell variable export (all 9 binaries)
- Added: `## Allowlist entries` section listing probe commands for all 9 EDirect binaries
- Changed: `## Full flag reference` and `## Patterns` grep paths updated to use skill-relative `$(dirname ...)` form
- Changed: cross-skill `CSVTK=~/.cursor/...` reference in Common patterns replaced with a note to resolve via the csvtk skill

## [2026-03-26] — v1.1.0
- Skill version: 1.1.0
- Added: `NQUIRE_HELPER` and `NQUIRE_TIMEOUT` env vars to Environment section
- Added: Troubleshooting section covering HTTP/1.0 SSL hang, FTP 403 on -help, and -mixed requirement
- Fixed: added `-mixed` flag to all `xtract` invocations that parse PubMed/PMC XML in SKILL.md and patterns.md
- Added: curl + xtract fallback pattern for environments where the CLI tools hang

## [2026-03-26] — Initial skill
- Tool version: 22.6 (run `readlink -f "$(dirname <SKILL.md path>)/bin/esearch"` then `<path> -version` to check current)
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, patterns.md, environment.yaml
- Covers: esearch, efetch, efilter, elink, xtract, epost, einfo, transmute, nquire
