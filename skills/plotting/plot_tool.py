#!/usr/bin/env python3
"""
plot_tool.py — CLI for running Altair chart scripts and rendering Vega-Lite JSON specs.

Run `plot_tool render SCRIPT.py --help` or `plot_tool spec SPEC.json --help` for usage.
"""

from __future__ import annotations

import argparse
import json
import runpy
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent


def _ensure_skill_path() -> None:
    s = str(SKILL_DIR)
    if s not in sys.path:
        sys.path.insert(0, s)


def cmd_render(args: argparse.Namespace) -> int:
    _ensure_skill_path()
    import damlab_plot  # noqa: F401 — theme + vegafusion side effects

    script = Path(args.script).resolve()
    if not script.is_file():
        print(f"error: script not found: {script}", file=sys.stderr)
        return 1

    globs = runpy.run_path(str(script), run_name="__main__")
    chart = globs.get("chart")

    if args.out or args.out_html:
        if chart is None:
            print(
                "error: --out / --out-html require a top-level variable `chart` "
                "in the script (an Altair chart object).",
                file=sys.stderr,
            )
            return 1
        if args.out:
            damlab_plot.save(chart, args.out, scale=args.scale)
        if args.out_html:
            damlab_plot.save(chart, args.out_html, scale=args.scale)

    return 0


def cmd_spec(args: argparse.Namespace) -> int:
    _ensure_skill_path()
    import altair as alt
    import damlab_plot  # noqa: F401

    spec_path = Path(args.spec_json).resolve()
    if not spec_path.is_file():
        print(f"error: spec file not found: {spec_path}", file=sys.stderr)
        return 1

    if not args.out and not args.out_html:
        print("error: specify at least one of --out and/or --out-html", file=sys.stderr)
        return 1

    with spec_path.open(encoding="utf-8") as f:
        spec = json.load(f)

    chart = alt.Chart.from_dict(spec)
    if args.out:
        damlab_plot.save(chart, args.out, scale=args.scale)
    if args.out_html:
        damlab_plot.save(chart, args.out_html, scale=args.scale)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="plot_tool",
        description="Render Altair charts from Python scripts or Vega-Lite JSON specs.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_render = sub.add_parser(
        "render",
        help="Run a Python script that builds an Altair chart (optional: assign to `chart`).",
    )
    p_render.add_argument(
        "script",
        help="Path to a .py file (import damlab_plot for theme + save helpers).",
    )
    p_render.add_argument(
        "--out",
        metavar="FILE",
        help="Write static PNG or SVG (extension .png or .svg); requires `chart` in script.",
    )
    p_render.add_argument(
        "--out-html",
        dest="out_html",
        metavar="FILE",
        help="Write self-contained interactive HTML; requires `chart` in script.",
    )
    p_render.add_argument(
        "--scale",
        type=float,
        default=2.0,
        help="Scale factor for raster PNG export (default: 2).",
    )
    p_render.set_defaults(func=cmd_render)

    p_spec = sub.add_parser(
        "spec",
        help="Load a Vega-Lite JSON spec and write PNG/SVG/HTML.",
    )
    p_spec.add_argument("spec_json", help="Path to a .json Vega-Lite specification.")
    p_spec.add_argument(
        "--out",
        metavar="FILE",
        help="Write static PNG or SVG.",
    )
    p_spec.add_argument(
        "--out-html",
        dest="out_html",
        metavar="FILE",
        help="Write self-contained interactive HTML.",
    )
    p_spec.add_argument(
        "--scale",
        type=float,
        default=2.0,
        help="Scale factor for raster PNG export (default: 2).",
    )
    p_spec.set_defaults(func=cmd_spec)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
