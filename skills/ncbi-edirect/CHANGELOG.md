# Changelog — ncbi-edirect

## [Unreleased]

## [2026-03-26] — v1.1.0
- Skill version: 1.1.0
- Added: `NQUIRE_HELPER` and `NQUIRE_TIMEOUT` env vars to Environment section
- Added: Troubleshooting section covering HTTP/1.0 SSL hang, FTP 403 on -help, and -mixed requirement
- Fixed: added `-mixed` flag to all `xtract` invocations that parse PubMed/PMC XML in SKILL.md and patterns.md
- Added: curl + xtract fallback pattern for environments where the CLI tools hang

## [2026-03-26] — Initial skill
- Tool version: 22.6 (run `~/.cursor/skills/ncbi-edirect/bin/esearch -version` to check current)
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, patterns.md, environment.yaml
- Covers: esearch, efetch, efilter, elink, xtract, epost, einfo, transmute, nquire
