# Changelog — plotting

## [Unreleased]


## [2026-03-31]
- Skill version: 1.1.0

### Added

- `test/iris_equivalent.csv` (canonical Fisher iris, seaborn-data mirror) and `test/plot_iris_test.py` for smoke-testing `plot_tool render` / `damlab_plot`.

### Fixed

- `damlab_plot.py`: register the lab theme with Altair 6’s `@alt.theme.register(..., enable=True)` decorator (the old positional `alt.theme.register("name", fn)` API was removed in Altair 6).
- `environment.yaml`: add `pyarrow` (required by vegafusion + pandas when saving PNG with the vegafusion transformer); pin `altair >=6.0` to match the theme API.
- `SKILL.md`: note that `plot_tool` / `runpy.run_path` leaves `sys.argv[1:]` as the wrapper’s args.
- `environment.yaml`: removed `vegafusion-python` — that name exists on PyPI, not as a separate conda-forge package. The `vegafusion` conda package supplies the Python bindings used by `alt.data_transformers.enable("vegafusion")`.

## [2026-03-30] — Initial skill

- Tool stack: Altair (Vega-Lite), vl-convert-python, vegafusion, pandas, polars (versions: latest at install time)
- Skill version: 1.0.0
- Added: `SKILL.md`, `reference.md`, `patterns.md`, `environment.yaml`, `plot_tool` wrapper, `plot_tool.py`, `damlab_plot.py`
