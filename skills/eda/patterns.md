# eda — Patterns

Reusable notebook-oriented snippets. Search:

```bash
grep -n "Pattern" "$(dirname <path-to-this-SKILL.md>)/patterns.md"
```

---

## Pattern: encoding-safe CSV loader

Use in a **code cell** after imports and `DATA_PATH` is set.

```python
def _read_csv(path):
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return __import__("pandas").read_csv(path, encoding=enc)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("failed", b"", 0, 1, "no encoding worked")

raw = _read_csv(DATA_PATH)
raw.columns = [str(c).strip() for c in raw.columns]
raw = raw.loc[:, ~raw.columns.str.match(r"(?i)^Unnamed")]
raw = raw.dropna(how="all")
```

---

## Pattern: outputs tree + savefig / savetab

First code cell (or immediately after imports).

```python
from pathlib import Path

OUTDIR = Path("outputs")
FIG_DIR = OUTDIR / "figures"
TAB_DIR = OUTDIR / "tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TAB_DIR.mkdir(parents=True, exist_ok=True)

def savefig(name, **kw):
    import matplotlib.pyplot as plt
    plt.savefig(FIG_DIR / name, bbox_inches="tight", **kw)

def savetab(df, name, **kw):
    df.to_csv(TAB_DIR / name, **kw)
```

---

## Pattern: complete-case PCA pipeline (sketch)

After choosing `feature_cols` and a working `df_cc` (complete cases); print `len(df_cc)` first.

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Log1 transform right-skewed positive columns (add offset per column as needed)
X = df_cc[feature_cols].copy()
# ... apply log10(x + offset) to selected columns ...

scaler = StandardScaler()
Xz = scaler.fit_transform(X)
pca = PCA(n_components=min(10, Xz.shape[1]))
scores = pca.fit_transform(Xz)

fig, ax = plt.subplots()
ax.plot(np.cumsum(pca.explained_variance_ratio_))
ax.set_xlabel("PC"); ax.set_ylabel("Cumulative explained variance")
# savefig("fig5_pca_overview.png")  # combine with loadings + PC1 vs PC2 in same figure as your notebook design
```

Pair with the **PCA** module guidance in `SKILL.md` (loadings table, interpretation thresholds).

---

## Pattern: silhouette readout from a notebook cell (agent follow-up)

Use with **`jupyter-notebook`** to grep notebook JSON for cells containing `"silhouette"` and read `stdout` streams from those cells (see `skills/jupyter-notebook/patterns.md`).
