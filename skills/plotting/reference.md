# plotting — Altair / Vega-Lite reference

Helper CLI: `plot_tool` (see [SKILL.md](SKILL.md)). Grep sections below, e.g.:

```bash
grep -A 40 "## Type shorthand" "$(dirname <path-to-this-SKILL.md>)/reference.md"
```

---

## Type shorthand

Altair encodings often append a **type letter** to the field name inside quotes:

| Shorthand | Vega-Lite type | Use for |
|-----------|----------------|---------|
| `:Q` | quantitative | Numbers, continuous measures |
| `:N` | nominal | Categories with no order (colors, labels) |
| `:O` | ordinal | Ordered categories (sorted levels) |
| `:T` | temporal | Dates/times (parsed as time) |
| `:G` | geojson | Geographic shapes |

Example: `x="coverage:Q", color="sample:N"`.

You can also use explicit objects: `alt.X("length", type="quantitative")`.

---

## Mark types

| Mark | Typical use |
|------|-------------|
| `mark_point()` | Scatter, dot plots |
| `mark_circle()` | Scatter with uniform point size |
| `mark_square()` | Scatter with square glyphs |
| `mark_line()` | Time series, connected trends |
| `mark_area()` | Stacked or single-series area |
| `mark_bar()` | Bar charts (use `x` or `y` as categorical) |
| `mark_rect()` | Heatmaps (matrix cells) |
| `mark_boxplot()` | Tukey box plots |
| `mark_rule()` | Vertical/horizontal reference lines |
| `mark_tick()` | 1D distributions |
| `mark_errorbar()` / `mark_errorband()` | Uncertainty intervals |

Combine marks with `alt.layer()` for points + lines + rules.

---

## Encoding channels

Common channels inside `.encode(...)`:

| Channel | Role |
|---------|------|
| `x`, `y` | Position |
| `x2`, `y2` | Span endpoints (rules, rects) |
| `color`, `fill`, `stroke` | Color aesthetics |
| `opacity`, `size`, `strokeWidth` | Magnitude / emphasis |
| `shape` | Point shapes |
| `detail` | Group without visual channel (line grouping) |
| `order` | Sort order for lines / stacking |
| `tooltip` | List of fields for hover (HTML output) |
| `href` | Clickable URLs |
| `text` | Labels (`mark_text`) |

Faceting (small multiples):

- `facet = "field:N"` or `.facet("field:N", columns=2)`
- `row="field:N"`, `column="field:N"` on `Chart` for wrapped facets

---

## Transforms

Chained as methods on `Chart` before or after `encode` (order matters for some pipelines):

| Method | Purpose |
|--------|---------|
| `transform_filter(...)` | Subset rows (predicate string or `datum`) |
| `transform_bin(...)` | Histogram bins |
| `transform_aggregate(...)` | groupby summaries |
| `transform_timeunit(...)` | Bin dates (yearmonth, hours, etc.) |
| `transform_calculate(...)` | Derived fields (`as` + `calculate` expr) |
| `transform_fold(...)` | Wide → long (measure names in one column) |
| `transform_pivot(...)` | Long → wide |
| `transform_density(...)` | KDE curves |
| `transform_regression(...)` | Linear/polynomial trend lines |
| `transform_loess(...)` | Smoothed trend |
| `transform_window(...)` | Ranking, rolling stats |
| `transform_joinaggregate(...)` | Global aggregates per group |

**Counting:** use `y="count():Q"` or `alt.Y(aggregate="count")` after binning/grouping.

---

## Composition

| Pattern | Syntax |
|---------|--------|
| Overlay layers | `alt.layer(chart_a, chart_b)` |
| Horizontal concat | `chart_a \| chart_b` |
| Vertical concat | `chart_a & chart_b` |
| Facet | `chart.facet(row="r:N", column="c:N")` or `alt.facet(...)` |
| Repeat small multiples | `alt.repeat(...).mark_point().encode(...)` |

Shared scales across concatenated charts: use `alt.resolve_scale(...)` on the composed chart.

---

## Interactivity

| Feature | Pattern |
|---------|---------|
| Pan/zoom | `.interactive()` on the chart |
| Interval brush | `brush = alt.selection_interval(...); chart.add_params(brush).encode(opacity=...)` |
| Single/multi click | `alt.selection_point(...)` |
| Bind UI control | `param = alt.param(..., bind=alt.binding_select(options=[...]))` |
| Filter by selection | `transform_filter(brush)` on a second chart |

Tooltips: pass `tooltip=["field:Q", "label:N"]` in `encode()` (HTML output).

---

## Saving and data transformers

- **PNG/SVG:** `chart.save("out.png")` or `damlab_plot.save(chart, "out.png")` (uses vl-convert).
- **HTML:** `damlab_plot.save(chart, "out.html")` embeds Vega-Lite + renderer (SVG default for crisp text).
- **Large data:** `import damlab_plot` enables **vegafusion** so transforms run server-side; avoid plotting one mark per row for millions of points—aggregate first.

---

## Python and CLI entry points

- Run a script: `$PLOT_TOOL render script.py [--out …] [--out-html …]`
- JSON spec: `$PLOT_TOOL spec spec.json --out …` / `--out-html …`
- Helper module: `import damlab_plot` then `damlab_plot.save(chart, path)`.
