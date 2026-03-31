"""
damlab_plot — shared Altair setup for the plotting skill.

Import this module in chart scripts to enable vegafusion, the damlab theme,
and a small save() helper for PNG/SVG/HTML.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import altair as alt


@alt.theme.register("damlab", enable=True)
def damlab_theme() -> dict[str, Any]:
    """Minimal lab theme: white background, readable fonts, subtle grid."""

    return {
        "config": {
            "background": "white",
            "padding": 12,
            "title": {"fontSize": 16, "fontWeight": "normal"},
            "axis": {
                "labelFontSize": 11,
                "titleFontSize": 12,
                "grid": True,
                "gridOpacity": 0.2,
            },
            "legend": {"labelFontSize": 11, "titleFontSize": 12},
            "mark": {"tooltip": True},
        }
    }

# Server-side transforms for large datasets (avoids default 5000-row cap)
try:
    alt.data_transformers.enable("vegafusion")
except Exception:
    # If vegafusion is unavailable, fall back to default (may error on huge raw data)
    pass


def save(
    chart: alt.Chart | alt.LayerChart | alt.VConcatChart | alt.HConcatChart | alt.FacetChart,
    path: str | Path,
    *,
    scale: float = 2.0,
    embed_options: dict[str, Any] | None = None,
) -> None:
    """Save a chart to PNG, SVG, or self-contained HTML based on file extension.

    - ``.png`` / ``.svg``: static raster/vector via vl-convert.
    - ``.html``: interactive chart; default ``embed_options`` use SVG renderer for crisp text.
    """
    path = Path(path)
    suffix = path.suffix.lower()

    if suffix == ".html":
        opts = {"renderer": "svg"}
        if embed_options:
            opts = {**opts, **embed_options}
        chart.save(str(path), embed_options=opts)
        return

    if suffix in (".png", ".svg"):
        chart.save(str(path), scale_factor=scale)
        return

    raise ValueError(
        f"Unsupported extension {suffix!r}; use .png, .svg, or .html (got {path})"
    )


def save_from_spec(spec: dict[str, Any], path: str | Path, **kwargs: Any) -> None:
    """Build a chart from a Vega-Lite spec dict and save."""
    chart = alt.Chart.from_dict(spec)
    save(chart, path, **kwargs)
