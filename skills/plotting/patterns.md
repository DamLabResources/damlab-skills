# plotting — Patterns

Reusable patterns for bioinformatics-style charts with Altair. Each assumes `import damlab_plot` (theme + vegafusion). Replace file paths and column names to match your tables.

<!-- Add patterns below as they arise -->

### Read length histogram

**Context:** Nanopore or Illumina read lengths from a TSV with a `length` column.

```python
import pandas as pd
import altair as alt
import damlab_plot

df = pd.read_csv("reads.tsv", sep="\t")
chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("length:Q", bin=alt.Bin(maxbins=50), title="Read length (bp)"),
        y=alt.Y("count():Q", title="Reads"),
        tooltip=[alt.Tooltip("length:Q", bin=True), "count():Q"],
    )
    .properties(title="Read length distribution", width=500, height=300)
)
damlab_plot.save(chart, "read_length_hist.png")
```

### Coverage depth along a contig (faceted by sample)

**Context:** Per-window coverage TSV with columns `sample`, `position`, `depth`.

```python
import pandas as pd
import altair as alt
import damlab_plot

df = pd.read_csv("coverage.tsv", sep="\t")
chart = (
    alt.Chart(df)
    .mark_area(opacity=0.7)
    .encode(
        x=alt.X("position:Q", title="Position (bp)"),
        y=alt.Y("depth:Q", title="Depth"),
        color="sample:N",
        tooltip=["sample:N", "position:Q", "depth:Q"],
    )
    .facet(row=alt.Row("sample:N", title=None))
    .properties(width=600, height=120)
)
damlab_plot.save(chart, "coverage_faceted.png")
damlab_plot.save(chart, "coverage_faceted.html")
```

### Edit efficiency by guide (grouped bar)

**Context:** Aggregated editing outcomes: `guide`, `condition`, `efficiency` (0–1 or percent).

```python
import pandas as pd
import altair as alt
import damlab_plot

df = pd.read_csv("editing_summary.tsv", sep="\t")
chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("guide:N", title="Guide", sort="-y"),
        y=alt.Y("efficiency:Q", title="Editing efficiency", axis=alt.Axis(format="%")),
        color="condition:N",
        xOffset="condition:N",
        tooltip=["guide:N", "condition:N", "efficiency:Q"],
    )
    .properties(width=500, height=350, title="Editing efficiency by guide")
)
damlab_plot.save(chart, "edit_efficiency.png")
```

### Identity vs. read length (scatter with tooltip)

**Context:** Alignment QC table with `read_id`, `length`, `identity` (or `pident`).

```python
import pandas as pd
import altair as alt
import damlab_plot

df = pd.read_csv("alignments.tsv", sep="\t")
# Downsample if needed for raw per-read scatter: df = df.sample(5000, random_state=1)
chart = (
    alt.Chart(df)
    .mark_point(filled=True, size=12, opacity=0.5)
    .encode(
        x=alt.X("length:Q", title="Read length (bp)"),
        y=alt.Y("identity:Q", title="Identity (%)", scale=alt.Scale(domain=[80, 100])),
        color="sample:N",
        tooltip=["read_id:N", "length:Q", "identity:Q", "sample:N"],
    )
    .properties(width=500, height=400, title="Identity vs. length")
    .interactive()
)
damlab_plot.save(chart, "identity_vs_length.html")
```
