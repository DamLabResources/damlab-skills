# csvtk — Full Reference

Invoke all commands as: `conda run -n damlab-skill-csvtk csvtk <subcommand>`

## Global flags

| Flag | Description |
|---|---|
| `-t, --tabs` | Input is tab-delimited (TSV). Also set via `CSVTK_T=1` |
| `-T, --out-tabs` | Output as TSV |
| `-d CHAR` | Input delimiter (default `,`) |
| `-D CHAR` | Output delimiter |
| `-H, --no-header-row` | Input has no header |
| `-o FILE` | Output file (stdout default; `.gz` suffix compresses) |
| `-j INT` | CPU threads (default all) |
| `-C CHAR` | Comment character (default `#`) |
| `-l, --lazy-quotes` | Allow non-standard quoting |
| `-I, --ignore-illegal-row` | Skip rows with wrong column count |
| `-E, --ignore-empty-row` | Skip empty rows |

---

## Inspection

### `dim`
Print dimensions (rows × columns).
```bash
csvtk dim input.csv
csvtk dim -t input.tsv
```

### `headers`
Print column names with index.
```bash
csvtk headers input.csv
```

### `head`
Print first N rows.
```bash
csvtk head -n 5 input.csv
```

### `cat`
Stream file to stdout (with progress on stderr).
```bash
csvtk cat input.csv
```

---

## Column operations

### `cut`
Select and reorder columns.
```bash
csvtk cut -f col1,col2,col3 input.csv
csvtk cut -f 1,3,5 input.csv            # by index
csvtk cut -f -col1 input.csv            # exclude col1
```

### `rename`
Rename column headers.
```bash
csvtk rename -f old_name -n new_name input.csv
csvtk rename -f 1,2 -n id,value input.csv
```

### `add-header`
Add a header row to a file that lacks one.
```bash
csvtk add-header -n id,value,score input.csv
```

### `del-header`
Remove the header row.
```bash
csvtk del-header input.csv
```

### `transpose`
Transpose rows and columns.
```bash
csvtk transpose input.csv
```

---

## Row operations

### `filter`
Filter rows using simple arithmetic on a single column.
```bash
csvtk filter -f 'coverage>10' input.csv
```

### `filter2`
Filter rows using awk-like arithmetic/string expressions across multiple columns.
```bash
csvtk filter2 -f '$coverage > 10 && $status == "PASS"' input.csv
csvtk filter2 -f '$name =~ "sample[0-9]+"' input.csv   # regex match
```
Column names are prefixed with `$`. Use `=~` for regex, `!~` for negated regex.

### `grep`
Filter rows by pattern in selected fields.
```bash
csvtk grep -f sample -p "ctrl" input.csv          # exact match
csvtk grep -f sample -r -p "^ctrl_" input.csv     # regex
csvtk grep -f sample -v -p "ctrl" input.csv       # invert (exclude)
csvtk grep -f sample -f status -p "ctrl,PASS" input.csv  # multiple fields
```

### `uniq`
Remove rows with duplicate values in selected columns.
```bash
csvtk uniq -f sample input.csv
```

---

## Aggregation

### `freq`
Frequency count of values in a column.
```bash
csvtk freq -f status input.csv
csvtk freq -f status -r input.csv    # sort by count descending
csvtk freq -f status -n input.csv    # sort by name
```

### `summary`
Aggregate statistics, with optional groupby.
```bash
# Summary of all numeric columns:
csvtk summary input.csv

# Specific stats grouped by a column:
csvtk summary -f reads:sum,coverage:mean,coverage:stdev -g sample input.csv
```

Available functions: `sum`, `mean`, `median`, `stdev`, `variance`, `min`, `max`, `q1`, `q3`, `iqr`, `count`, `countn`, `first`, `last`, `uniq`, `collapse`, `countuniq`.

### `corr`
Pearson correlation between two columns.
```bash
csvtk corr -f col1,col2 input.csv
```

---

## Combining files

### `concat`
Concatenate CSV/TSV files vertically (stacks rows).
```bash
csvtk concat file1.csv file2.csv -o merged.csv
```
Headers must match. Use `-u` to allow missing columns (fills with empty).

### `join`
Join files on a shared key column (SQL-style).
```bash
csvtk join -f key_col file1.csv file2.csv          # inner join
csvtk join -f key_col --left-join file1.csv file2.csv
csvtk join -f key_col --outer-join file1.csv file2.csv
csvtk join -f "col1;col2" file1.csv file2.csv       # multi-column key
```

### `inter`
Intersection: rows whose key appears in all files.
```bash
csvtk inter -f sample file1.csv file2.csv file3.csv
```

---

## Sorting & reshaping

### `sort`
Sort by one or more columns.
```bash
csvtk sort -k col:n input.csv      # numeric ascending
csvtk sort -k col:nr input.csv     # numeric descending
csvtk sort -k col:r input.csv      # string descending
csvtk sort -k col1:n -k col2:r input.csv   # multi-column
```
Sort keys: `:n` numeric, `:nr` numeric reverse, `:r` string reverse (default string ascending).

### `gather`
Wide → long format (melt columns into key-value rows).
```bash
csvtk gather -k variable -v value -f col1,col2,col3 input.csv
```

### `fold`
Long → wide format (collapse multiple rows into cell lists).
```bash
csvtk fold -f group -v value -s ";" input.csv
```

### `unfold`
Expand delimited cell values into multiple rows.
```bash
csvtk unfold -f value -s ";" input.csv
```

### `split`
Split a CSV into multiple files based on values in a column.
```bash
csvtk split -f sample input.csv -o outdir/
```

---

## Format conversion

### `csv2tab`
CSV → TSV.
```bash
csvtk csv2tab input.csv -o output.tsv
```

### `tab2csv`
TSV → CSV.
```bash
csvtk tab2csv -t input.tsv -o output.csv
```

### `csv2xlsx`
CSV/TSV → Excel.
```bash
csvtk csv2xlsx file1.csv file2.csv -o output.xlsx
```

### `xlsx2csv`
Excel → CSV (one sheet at a time).
```bash
csvtk xlsx2csv input.xlsx                    # first sheet
csvtk xlsx2csv input.xlsx --sheet-name Sheet2
```

### `csv2json`
CSV → JSON.
```bash
csvtk csv2json input.csv
```

### `csv2md`
CSV → Markdown table.
```bash
csvtk csv2md input.csv
```

### `csv2rst`
CSV → reStructuredText table.
```bash
csvtk csv2rst input.csv
```

---

## Utilities

### `fix`
Fix rows with inconsistent column counts.
```bash
csvtk fix input.csv -o fixed.csv
```

### `fmtdate`
Format date columns.
```bash
csvtk fmtdate -f date_col --from-format "2006-01-02" --to-format "01/02/2006" input.csv
```

### `comb`
Compute all combinations of values in a column per row.
```bash
csvtk comb -n 2 -f items input.csv
```

### `space2tab`
Convert space-delimited input to TSV.
```bash
csvtk space2tab input.txt
```

### `watch`
Live histogram of column values while streaming.
```bash
csvtk watch -f coverage input.csv
```
