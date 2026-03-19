---
name: csvtk
description: Manipulate CSV and TSV tabular data files using csvtk. Use when working
  with CSV or TSV files, inspecting table dimensions or column names, selecting or
  reordering columns, filtering rows by value, computing frequencies or summary statistics,
  joining tables, sorting, converting between CSV and TSV formats, or converting to
  Excel/JSON/Markdown. Triggers on tasks involving .csv, .tsv, tabular data, spreadsheet
  manipulation, groupby aggregation, or table joins.
---

# csvtk

## Environment

```bash
CSVTK=~/.cursor/skills/csvtk/bin/csvtk
```

## Critical global flags

| Flag | Meaning |
|---|---|
| `-t` | Input is **TSV** (tab-delimited) — omit for CSV |
| `-T` | Output as **TSV** |
| `-H` | Input has **no header row** |
| `-o FILE` | Output file (default stdout; `.gz` auto-compresses) |

**Always specify `-t` for TSV input. Forgetting this is the most common mistake.**

## Subcommands

**Information**
- `corr` — calculate Pearson correlation between two columns
- `dim` — print dimensions (rows × columns); aliases: size, stats, stat
- `headers` — print column names with index
- `ncol` — print number of columns
- `nrow` — print number of records
- `summary` — summary statistics (mean, sum, median, etc.) with optional groupby
- `watch` — live histogram of a field while streaming

**Format Conversion**
- `csv2json` — convert CSV to JSON
- `csv2md` — convert CSV to Markdown table
- `csv2rst` — convert CSV to reStructuredText table
- `csv2tab` — convert CSV to TSV
- `csv2xlsx` — convert CSV/TSV to Excel (.xlsx)
- `pretty` — render CSV as a human-readable aligned table (supports styles: grid, bold, double, etc.)
- `space2tab` — convert space-delimited input to TSV
- `splitxlsx` — split XLSX sheet into multiple sheets by column values
- `tab2csv` — convert TSV to CSV
- `xlsx2csv` — convert Excel to CSV

**Set Operations**
- `comb` — compute combinations of items per row
- `concat` — concatenate CSV/TSV files vertically (stack rows)
- `cut` — select and reorder columns; supports ranges and exclusion (`-f -col`)
- `filter` — filter rows by simple arithmetic on a single column
- `filter2` — filter rows by awk-like multi-column expressions (`$col > 10 && $status == "PASS"`)
- `freq` — frequency count of values in selected columns
- `grep` — filter rows by pattern or regex in selected fields
- `head` — print first N records
- `inter` — intersection: rows whose key appears in all files
- `join` — join files on a key column (inner, left, outer); alias: merge
- `sample` — sample rows by proportion
- `split` — split CSV into multiple files by column values
- `uniq` — deduplicate rows by key columns (no sort required)

**Editing**
- `add-header` — add a header row to a headerless file
- `del-header` — remove the header row
- `del-quotes` — remove extra double quotes added by `fix-quotes`
- `fix` — pad rows with too few columns to make column counts uniform
- `fix-quotes` — fix malformed CSV with bare or mismatched double-quotes
- `fmtdate` — reformat date columns (MS Excel format syntax)
- `mutate` — create new column using regex capture from existing column
- `mutate2` — create new column using awk-like arithmetic/string expressions
- `mutate3` — create new column using Go-like (Expr) expressions
- `rename` — rename columns by new names
- `rename2` — rename columns by regex with capture variables and key-value substitution
- `replace` — replace cell values by regex with capture variables and key-value substitution
- `round` — round numeric columns to N decimal places

**Data Transformation**
- `fold` — collapse multiple rows into a delimited cell per group (long → wide cell); alias: collapse
- `gather` — wide → long format (pivot_longer); alias: longer
- `sep` — split a column into multiple columns by a separator
- `spread` — long → wide format (pivot_wider); aliases: wider, scatter
- `transpose` — transpose rows and columns
- `unfold` — expand delimited cell values into multiple rows

**Ordering**
- `sort` — sort by one or more columns; supports numeric (`:n`), reverse (`:r`), natural (`:N`), user-defined (`:u`)

**Plotting**
- `plot box` — boxplot
- `plot hist` — histogram
- `plot line` — line or scatter plot

**Miscellaneous**
- `cat` — stream file to stdout with progress reporting on stderr

## Common patterns

**Inspect a table (dimensions + column names):**
```bash
$CSVTK dim input.csv
$CSVTK headers input.csv
# TSV:
$CSVTK dim -t input.tsv
$CSVTK headers -t input.tsv
```

**Select and reorder columns:**
```bash
$CSVTK cut -f sample,reads,coverage input.csv
$CSVTK cut -f 1,3,5 input.csv   # by index
```

**Filter rows by expression:**
```bash
# Numeric: keep rows where coverage > 10
$CSVTK filter2 -f '$coverage > 10' input.csv
# String match:
$CSVTK filter2 -f '$status == "PASS"' input.csv
# Combined:
$CSVTK filter2 -f '$coverage > 10 && $status == "PASS"' input.csv
```

**Frequency table for a column:**
```bash
$CSVTK freq -f sample input.csv
$CSVTK freq -f status -n input.csv  # sort by count desc
```

**Group-by summary statistics:**
```bash
# Mean and sum of coverage, grouped by sample
$CSVTK summary -f coverage:mean,reads:sum -g sample input.csv
```

**Join two tables on a shared key:**
```bash
# Inner join (default):
$CSVTK join -f sample table1.csv table2.csv -o joined.csv
# Left join:
$CSVTK join -f sample --left-join table1.csv table2.csv
```

**Sort by column:**
```bash
$CSVTK sort -k coverage:n input.csv   # numeric ascending
$CSVTK sort -k coverage:nr input.csv  # numeric descending
$CSVTK sort -k sample:r input.csv     # string descending
```

**Convert CSV ↔ TSV:**
```bash
$CSVTK csv2tab input.csv -o output.tsv
$CSVTK tab2csv input.tsv -o output.csv
```

**Pipe: filter then select columns, output TSV:**
```bash
$CSVTK filter2 -f '$coverage > 10' input.csv | $CSVTK cut -f sample,coverage -T
```

## Full flag reference

To look up all flags for a specific subcommand:
```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/csvtk/reference.md
```
Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
```bash
grep -A 20 "keyword" ~/.cursor/skills/csvtk/patterns.md
```
[patterns.md](patterns.md)
