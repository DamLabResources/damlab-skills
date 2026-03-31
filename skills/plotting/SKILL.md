---
name: plotting
description: Build publication-style and interactive plots with Altair (Vega-Lite).
  Use when creating figures from tabular data, histograms, scatter plots, line or
  area charts, heatmaps, faceted small multiples, or exporting PNG/SVG/HTML from
  Python or Vega-Lite JSON. Triggers on tasks involving Altair, Vega-Lite,
  visualization, plotting, charts, figures, interactive HTML plots, or exporting
  plots from CSV/TSV/Parquet.
---

# plotting

## Environment

Resources relative to this skill directory:

| Resource | Path |
|----------|------|
| CLI wrapper | `plot_tool` (skill root — **not** under `bin/`) |
| Python CLI | `plot_tool.py` |
| Helper module | `damlab_plot.py` (import in chart scripts; enables vegafusion + theme) |
| Conda `python` / packages | `bin/python` (symlink to `venvs/plotting/` after `install.sh`) |

Before issuing any commands, resolve the full absolute path of the wrapper for this machine:

```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/plot_tool"
```

Substitute `<path-to-this-SKILL.md>` with the absolute path you used to read this file.
Use the printed output literally as the first token in every command.
In examples below, `$PLOT_TOOL` is a readable placeholder for that resolved path.

**Workflow:** write a small Python script that imports `damlab_plot`, builds an Altair `chart`, then either call `damlab_plot.save(chart, "out.png")` in the script or assign the chart to a top-level variable named `chart` and pass `--out` / `--out-html` to `render`.

## Subcommands — plot_tool.py

**`render`**
- `render SCRIPT.py` — execute a chart script (adds this skill directory to `PYTHONPATH` so `import damlab_plot` works from any working directory).
- `render SCRIPT.py --out FILE.png` — after the script runs, save top-level variable `chart` to PNG or SVG (by extension).
- `render SCRIPT.py --out-html FILE.html` — save `chart` to a self-contained interactive HTML file.
- `render SCRIPT.py --out FILE.png --out-html FILE.html` — both; requires `chart` in the script when any `--out*` flag is used.
- `render SCRIPT.py --scale 2.0` — PNG scale factor (default `2`).

**`spec`**
- `spec SPEC.json --out FILE.png` — load a Vega-Lite JSON spec and write static PNG/SVG.
- `spec SPEC.json --out-html FILE.html` — write interactive HTML.
- At least one of `--out` or `--out-html` is required for `spec`.

## Common patterns

**Minimal script (saves inside the file — no `chart` variable needed for CLI):**

```python
# my_plot.py
import pandas as pd
import altair as alt
import damlab_plot

df = pd.read_csv("data.csv")
chart = alt.Chart(df).mark_point().encode(x="x:Q", y="y:Q")
damlab_plot.save(chart, "scatter.png")
```

```bash
$PLOT_TOOL render my_plot.py
```

**Delegate saving to the CLI (script must define `chart`):**

```python
# my_plot.py
import pandas as pd
import altair as alt
import damlab_plot  # theme + vegafusion

df = pd.read_csv("data.csv")
chart = alt.Chart(df).mark_bar().encode(x=alt.X("value:Q", bin=True), y="count()")
```

```bash
$PLOT_TOOL render my_plot.py --out fig.png --out-html fig.html
```

**Render a Vega-Lite JSON file:**

```bash
$PLOT_TOOL spec chart.json --out fig.png --out-html fig.html
```

**Large datasets:** importing `damlab_plot` enables the **vegafusion** data transformer so server-side transforms (bin, aggregate, density, etc.) avoid Altair’s default row cap. Plots that encode every raw row (e.g. millions of points) may still need pre-aggregation in pandas/polars.

**`plot_tool` and `sys.argv`:** `runpy.run_path` sets `sys.argv[0]` to your script path but leaves `sys.argv[1:]` as the **plot_tool** process argv (e.g. `render`, `--out`, …). Do not assume `sys.argv[1]` is a user argument unless you validate it (e.g. `os.path.isdir(sys.argv[1])` for a data directory).

## Allowlist entries

Resolve and add to your terminal command allowlist (Cursor: Settings → Features → Terminal):

```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/plot_tool"
```

## Full flag reference

Altair/Vega-Lite concepts and API notes: [reference.md](reference.md)

To grep this file for a topic:

```bash
grep -A 30 "Type shorthand" "$(dirname <path-to-this-SKILL.md>)/reference.md"
```

## Patterns

Reusable bioinformatics-oriented chart recipes: [patterns.md](patterns.md)

```bash
grep -A 25 "Read length" "$(dirname <path-to-this-SKILL.md>)/patterns.md"
```
