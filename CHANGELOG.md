# Changelog

All notable changes to this repository are documented here. Per-tool history (version bumps, reference refreshes) remains in `skills/<tool>/CHANGELOG.md`.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) at the repo level: patch for documentation-only fixes, minor for new skills or substantial README/layout updates, major for breaking changes to install paths or skill layout.

## [Unreleased]

### Added

- Documentation: [INSTALL.md](INSTALL.md), [PHILOSOPHY.md](PHILOSOPHY.md), [FAQ.md](FAQ.md), [CONTRIBUTING.md](CONTRIBUTING.md); README refactored as a landing page with links to those docs.
- `install.sh`: configurable skill link destination via `--cursor`, `--openclaw`, `--dest <dir>`, or `SKILLS_DST`; `bash install.sh --help`.
- Tool skill `plotting`: Altair (Vega-Lite) charts with `plot_tool` CLI, `damlab_plot` helpers, PNG/SVG/HTML export (vl-convert, vegafusion).
- Meta-skill `bioinformatics-methods-results-writer`: draft Methods and Results manuscript sections from code, notebooks, logs, figures, and tables.

## [0.0.1] - 2026-03-23

### Added

- Initial tagged release of the damlab-skills collection.
- Tool skills: `samtools`, `seqkit`, `csvtk`, `pod5`, `crispresso`, `rclone`.
- Meta-skills: `create-skill`, `bioinfo-best-practices`.
- Root `LICENSE` (MIT) and this changelog.
- README aligned with prefix-based conda environments under `venvs/<tool>/`.

[0.0.1]: https://github.com/DamLabResources/damlab-skills/releases/tag/v0.0.1
