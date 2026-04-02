---
name: jupyter-notebook
description: >
  Inspect, execute, convert, diff, and extract outputs from Jupyter notebooks (.ipynb)
  using the jupytext CLI and the nbformat Python API. Use when reading notebook source
  as plain text, running a notebook against a named kernel, comparing two notebook
  versions, piping cell code through a linter or formatter, extracting printed statistics
  or saved-figure paths from cell outputs, or syncing a paired .py representation.
  Pair with the eda skill for multi-turn exploratory analysis in notebooks. Triggers on:
  .ipynb, notebook, jupyter, jupytext, nbformat, execute notebook, notebook outputs,
  cell outputs, kernel, percent format, paired notebook.
---

# jupyter-notebook

Two surfaces for working with `.ipynb` without JupyterLab: **`jupytext`** (CLI) and **`nbformat`** (Python API, via this env’s `python`). The **`eda`** skill defines **what** to analyze in a collaborative notebook workflow; this skill covers **how** to sync text, execute, diff, and read outputs between turns.

## Environment

| Resource | Path |
|----------|------|
| CLI | `bin/jupytext` |
| Python | `bin/python` |

Resolve absolute paths (first token for allowlist-safe commands):

```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/bin/jupytext"
readlink -f "$(dirname <path-to-this-SKILL.md>)/bin/python"
```

In examples below, `$JUPYTEXT` and `$PYTHON` denote those resolved paths.

**Allowlist entries (optional):** add the same resolved paths to the terminal command allowlist if the agent invokes them from the integrated terminal.

---

## jupytext — grouped capabilities

**Conversion and inspection**

- `$JUPYTEXT notebook.ipynb --to md -o -` — Markdown to stdout
- `$JUPYTEXT notebook.ipynb --to py:percent -o -` — percent-format Python to stdout
- `$JUPYTEXT text.py --to ipynb` — text → notebook
- `--from <format>` — override format inference
- `--paired-paths` — list paired representations

**Execution**

- `$JUPYTEXT --execute notebook.ipynb` — run with notebook’s registered kernel
- `--execute --set-kernel damlab-eda` — use a named kernel (e.g. after `ipykernel install` from `eda`)
- `--run-path <dir>` — execution cwd (default: notebook parent)
- `--execute --warn-only` — continue on error

**Diff and lint**

- `$JUPYTEXT --diff nb1.ipynb nb2.ipynb`
- `--diff-format py:percent` — diff as percent script
- `--pipe black` — format code cells
- `--check flake8` — lint without writing

**Pairing and sync**

- `--set-formats ipynb,py:percent` — pair notebook with `.py`
- `--sync notebook.py` — sync from last modified paired file
- `--set-kernel <name>` — set metadata without executing

---

## Common patterns

1. **Readable source (no JSON):** `$JUPYTEXT nb.ipynb --to py:percent -o -`
2. **Execute with kernel:** `$JUPYTEXT --execute --set-kernel damlab-eda --run-path /path/to/project nb.ipynb`
3. **Execute to copy:** `$JUPYTEXT nb.ipynb --to ipynb -o nb_run.ipynb` then `$JUPYTEXT --execute --set-kernel damlab-eda nb_run.ipynb`
4. **Diff two versions:** `$JUPYTEXT --diff v1.ipynb v2.ipynb`
5. **Black cells:** `$JUPYTEXT nb.ipynb --pipe black`
6. **Pair and sync:** `$JUPYTEXT --set-formats ipynb,py:percent nb.ipynb` then `$JUPYTEXT --sync nb.py`
7. **nbconvert HTML (share):** `jupyter nbconvert nb.ipynb --to html --embed-images --output report.html` (use `bin/jupyter` from this env)
8. **nbconvert script:** `jupyter nbconvert nb.ipynb --to script --stdout > nb.py` — for agents, prefer jupytext `py:percent` for cleaner diffs

---

## Agent workflow: two-pass pattern

Often the agent **cannot** run kernels directly. Default loop:

1. Edit cells (`EditNotebook`) or sync from paired `.py`
2. **User runs** the notebook in Jupyter, **or** `$JUPYTEXT --execute ...` when allowed
3. Read outputs with **`nbformat`** (`$PYTHON -c ...`) — see [patterns.md](patterns.md)

**Output types:** `stream` (`out.text`), `execute_result` / `display_data` (`out.data["text/plain"]`, etc.), `error` (`ename`, `evalue`, `traceback`).

---

## Full flag reference

Verbatim `--help`: [reference.md](reference.md)

## Patterns

[patterns.md](patterns.md)
