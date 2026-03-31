"""Scatter plot of iris-equivalent test data (uses plotting skill: damlab_plot + plot_tool render)."""
from pathlib import Path

import altair as alt
import pandas as pd

import damlab_plot  # noqa: F401 — theme + vegafusion

_HERE = Path(__file__).resolve().parent
_CSV = _HERE / "iris_equivalent.csv"


def _chart() -> alt.Chart:
    df = pd.read_csv(_CSV)
    return (
        alt.Chart(df)
        .mark_point(size=60, filled=True, opacity=0.7)
        .encode(
            x=alt.X("petal_length:Q", title="Petal length (cm)"),
            y=alt.Y("petal_width:Q", title="Petal width (cm)"),
            color=alt.Color("species:N", title="Species"),
            tooltip=[
                alt.Tooltip("species:N", title="Species"),
                alt.Tooltip("sepal_length:Q", title="Sepal length", format=".1f"),
                alt.Tooltip("sepal_width:Q", title="Sepal width", format=".1f"),
                alt.Tooltip("petal_length:Q", title="Petal length", format=".1f"),
                alt.Tooltip("petal_width:Q", title="Petal width", format=".1f"),
            ],
        )
        .properties(
            width=400,
            height=300,
            title="Iris-equivalent data: petal length vs width",
        )
    )


if __name__ == "__main__":
    chart = _chart()
