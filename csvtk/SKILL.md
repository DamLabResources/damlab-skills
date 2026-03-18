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
$CSVTK freq -f status -r input.csv  # sort by count desc
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

## Additional reference

Full subcommand reference: [reference.md](reference.md)
