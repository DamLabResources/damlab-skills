# jupyter-notebook — Patterns

```bash
grep -n "Pattern" "$(dirname <path-to-this-SKILL.md>)/patterns.md"
```

---

## Pattern: read stdout from cell N (nbformat)

Replace `notebook.ipynb` and `N` with your paths.

```python
import nbformat

nb = nbformat.read("notebook.ipynb", as_version=4)
for out in nb.cells[N].outputs:
    if out.output_type == "stream" and out.name == "stdout":
        print("".join(out.text))
```

---

## Pattern: find cell by keyword and print outputs

Example: cells mentioning `silhouette`.

```python
import nbformat

nb = nbformat.read("notebook.ipynb", as_version=4)
for i, c in enumerate(nb.cells):
    if c.cell_type != "code":
        continue
    if "silhouette" not in "".join(c.source):
        continue
    for out in c.get("outputs", []):
        if out.output_type == "stream" and out.name == "stdout":
            print(f"cell {i}:", "".join(out.text)[:800])
```

---

## Pattern: execute with a named project kernel

After registering a kernel (e.g. `damlab-eda` from the `eda` skill), run from the **project root** so imports resolve:

```bash
$JUPYTEXT --execute --set-kernel damlab-eda --run-path /path/to/project /path/to/project/analysis.ipynb
```

Use the resolved `jupytext` path as `$JUPYTEXT`.

---

## Pattern: stale execution counts (sanity check)

```python
import nbformat

nb = nbformat.read("notebook.ipynb", as_version=4)
for i, c in enumerate(nb.cells):
    if c.cell_type != "code":
        continue
    print(i, c.execution_count, len(c.get("outputs", [])))
```

If a cell’s `execution_count` is `None`, it was not run after last edit.
