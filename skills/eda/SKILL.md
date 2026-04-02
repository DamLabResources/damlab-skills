---
name: eda
description: >
  Collaborative, multi-turn exploratory data analysis (EDA) for tabular biological
  datasets in Jupyter notebooks (conda env: pandas, seaborn, sklearn, etc.). Use when
  exploring CSV/TSV, auditing quality before hypothesis tests, distributions, PCA or
  clustering overviews, or building outputs/ figures and tables with stable names. Prefer
  .ipynb with the user running cells between turns; pair with jupyter-notebook for
  execute/diff/outputs. Triggers on: explore, EDA, exploratory, notebook EDA, data quality,
  missingness, distributions, PCA overview, clustering overview, understand the data,
  collaborative analysis, follow-up questions, change of scope.
---

# eda

**Primary artifact:** Jupyter notebooks (`.ipynb`). Do EDA in one notebook per dataset or analysis thread; map **modules** below to **notebook sections or cell groups**. Do not dump an entire analysis in one shot unless the user asks—this is a **collaborative, multi-turn** skill (same spirit as `deep-research-query`).

**Opening stance:** Say clearly that you will work in a notebook (kernel `damlab-eda` after registration), propose cells **across turns**, and interpret results with the user. **Do not execute silently:** narrate phases, surface surprises, ask before irreversible or heavy steps, invite redirect at checkpoints.

## Phase 0 — Clarifying questions (always first)

Before loading data, ask in **one formatted block** (skip items already answered): data path(s) and format; **column schema** (identifiers, outcomes, covariates); **the main question or deliverable** (what they need to learn or produce); **where the `.ipynb` lives**; whether to use **paired** `py:percent` via `jupyter-notebook`; **breadth** (targeted pass vs full exploratory audit). **Wait for answers** and **echo back** in one or two sentences.

**Ongoing:** When the user sends **follow-up questions** or changes direction (“ignore these columns”, “only compare groups A/B”, “add PCA”), **treat that as a new scoping turn**: restate the updated goal briefly, then add, remove, or rewrite notebook sections—do not assume the original plan still applies.

**Checkpoints:** After each **major module** you add (e.g. schema, univariate block, multivariate block), **pause**: summarize findings, flag oddities, and ask what they want next—especially before expensive steps (wide correlation matrices, PCA, clustering). Extra checkpoints whenever a follow-up narrows or widens scope.

**Division of labor:** You **edit cells** (`EditNotebook`); the **user runs** the kernel in Jupyter (or approves `jupytext --execute` if policy allows). On the next turn, read outputs with **`jupyter-notebook`** (nbformat / jupytext)—two-pass workflow.

## Core principles

- Canonical `outputs/figures/` and `outputs/tables/` from the first code cell; stable names (`fig1_distributions.png`, `table_S1_missingness.csv`, …) for downstream skills—renumber or add suffixes if the user asks for alternate runs (e.g. `fig1b_…`).
- Log₁₀-transform skewed positive features before multivariate steps; use complete-case subsets; **print n** before each analysis.
- Prefer non-parametric comparisons when n per group &lt; 30.
- End each **session or agreed milestone** with a short plain-language summary, list of saved outputs, and suggested next steps—not only at the end of a maximal audit.

## Environment

Interpreter: **`bin/python`** (conda env under this skill; created by repo `install.sh`).

**Kernel (recommended):** register once so Jupyter and `jupytext --set-kernel` can use this stack:

```bash
<resolved-python> -m ipykernel install --user --name damlab-eda --display-name "Python (damlab-eda)"
```

Resolve `<resolved-python>`:

```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/bin/python"
```

Use that literal path as the first token; placeholders like `$EDA_PYTHON` are documentation only.

---

## Allowlist and trust

**Allowlist entries (optional):** if the agent runs this env’s interpreter from the integrated terminal, add the resolved path from:

```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/bin/python"
```

Resolving `bin/python` satisfies Cursor’s **first-token** / expansion rules; it does **not** make Python a narrow CLI. Allowlisting that path means trusting **general-purpose execution** in this conda env (same as trusting `environment.yaml` from this repo). **Optional:** omit `python` from the allowlist and rely on the user running cells; the collaboration model and patterns still apply. `jupytext` execution (see `jupyter-notebook`) also runs notebook code—use only when policy allows.

---

## Staging the notebook (query-driven modules)

**Not a fixed pipeline.** The rows below are **optional modules**—pick and order them from the **user’s question and follow-ups**, not from a default 0→9 march. If they only want missingness and one figure, do that. If they later ask for PCA, add a section then. If they pivot (“compare these two batches only”), subset the data and **repeat or replace** earlier modules as needed.

**Planning:** After Phase 0, state a **short plan** (“I’ll start with load + schema + univariates; we can add bivariate or PCA next based on what we see”). Revise the plan aloud when follow-ups change scope.

Use `df`, `numeric_cols`, `OUTDIR`, etc. as generic names. **Example artifact names** below are conventions when you produce that kind of output; renumber if the user already has figures or wants a minimal pass.

| Module | Typical use when the user cares about… | Example outputs |
|--------|----------------------------------------|-----------------|
| **Setup** | Reproducibility, paths | `outputs/` tree, `savefig` / `savetab`, library versions |
| **Load & clean** | Getting a trustworthy table | Encoding-safe read, stripped names, types, shapes printed |
| **Schema & quality** | Missingness, ranges, categories | `table_S1_missingness.csv`, `table_S2_numeric_summary.csv`, `value_counts` |
| **Univariates** | Distributions, skew | `fig1_distributions.png` (split if many panels) |
| **Bivariate** | Pairs of continuous variables | `fig2_bivariate.png` (exploratory; Spearman as note, not inference) |
| **Correlation overview** | Many numeric columns at once | `table_S3_spearman_corr.csv`, `fig3_correlation_heatmap.png` |
| **Group comparisons** | Categories × outcomes | `fig4_group_comparisons.png` |
| **PCA** | Low-dimensional structure | `table_S4_pca_loadings.csv`, `fig5_pca_overview.png` |
| **Clustering** | Sample groupings (exploratory) | `table_S5_cluster_assignments.csv`, `fig6_clustering_overview.png` |
| **Wrap-up** | Handoff, documentation | Short summary, list of paths, next steps (`bioinformatics-methods-results-writer`, `rclone`, deeper modeling) |

**Responsive moves:** If the user asks a **narrow** question (“which column has most NAs?”), answer with the **smallest** module set (often schema only). If they ask **“what else should we check?”**, suggest 1–2 modules from the menu with rationale. If they **contradict** an earlier choice, delete or supersede cells and say so.

**Details and copy-paste snippets:** [patterns.md](patterns.md). **CLI help / versions:** [reference.md](reference.md).

## Related skills

| Skill | When |
|-------|------|
| `csvtk` | Quick CLI table peek before Python |
| `plotting` | Publication Altair beyond seaborn defaults |
| `jupyter-notebook` | Execute, diff, paired text, read cell outputs between turns |
| `bioinformatics-methods-results-writer` | Methods + Results from artifacts |
| `rclone` | Ship `outputs/` |

## Full reference

- **Patterns:** [patterns.md](patterns.md)
- **CLI / versions:** [reference.md](reference.md)
