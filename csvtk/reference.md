# csvtk — Full Reference

Binary: `~/.cursor/skills/csvtk/bin/csvtk`

Each entry contains the verbatim `--help` output. Grep for a subcommand:
```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/csvtk/reference.md
```
Increase `-A` if output appears truncated.

---

## Information

### `corr`

```
calculate Pearson correlation between two columns

Usage:
  csvtk corr [flags] 

Flags:
  -f, --fields string   comma separated fields
  -h, --help            help for corr
  -i, --ignore_nan      Ignore non-numeric fields to avoid returning NaN
  -L, --log             Calcute correlations on Log10 transformed data
  -x, --pass            passthrough mode (forward input to output)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `dim`

```
dimensions of CSV file

Usage:
  csvtk dim [flags] 

Aliases:
  dim, size, stats, stat

Flags:
      --cols       only print number of columns (or using "csvtk ncol"
  -h, --help       help for dim
  -n, --no-files   do not print file names (only affect --cols and --rows)
      --rows       only print number of rows (or using "csvtk nrow")
      --tabular    output in machine-friendly tabular format

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `headers`

```
print headers

Usage:
  csvtk headers [flags] 

Flags:
  -h, --help      help for headers
  -v, --verbose   print verbose information

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `ncol`

```
print number of columns

Usage:
  csvtk ncol [flags] 

Aliases:
  ncol, ncols

Flags:
  -n, --file-name   print file names
  -h, --help        help for ncol

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `nrow`

```
print number of records

Usage:
  csvtk nrow [flags] 

Aliases:
  nrow, nrows

Flags:
  -n, --file-name   print file names
  -h, --help        help for nrow

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `summary`

```
summary statistics of selected numeric or text fields (groupby group fields)

Attention:

  1. Do not mix use field (column) numbers and names.

Available operations:
 
  # numeric/statistical operations
  # provided by github.com/gonum/stat and github.com/gonum/floats
  countn (count numeric values), min, max, sum, argmin, argmax,
  mean, stdev, variance, median, q1, q2, q3,
  entropy (Shannon entropy), 
  prod (product of the elements)

  # textual/numeric operations
  count, first, last, rand, unique/uniq, collapse, countunique

Usage:
  csvtk summary [flags] 

Flags:
  -w, --decimal-width int    limit floats to N decimal points (default 2)
  -f, --fields strings       operations on these fields. e.g -f 1:count,1:sum or -f colA:mean. available
                             operations: argmax, argmin, collapse, count, countn, countuniq,
                             countunique, entropy, first, last, max, mean, median, min, prod, q1, q2,
                             q3, rand, stdev, sum, uniq, unique, variance
  -g, --groups string        group via fields. e.g -f 1,2 or -f columnA,columnB
  -h, --help                 help for summary
  -i, --ignore-non-numbers   ignore non-numeric values like "NA" or "N/A"
  -S, --rand-seed int        rand seed for operation "rand" (default 11)
  -s, --separater string     separater for collapsed data (default "; ")

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `watch`

```
monitor the specified fields

Usage:
  csvtk watch [flags] 

Flags:
  -B, --bins int         number of histogram bins (default -1)
  -W, --delay int        sleep this many seconds after plotting (default 1)
  -y, --dump             print histogram data to stderr instead of plotting
  -f, --field string     field to watch
  -h, --help             help for watch
  -O, --image string     save histogram to this PDF/image file
  -L, --log              log10(x+1) transform numeric values
  -x, --pass             passthrough mode (forward input to output)
  -p, --print-freq int   print/report after this many records (-1 for print after EOF) (default -1)
  -Q, --quiet            supress all plotting to stderr
  -R, --reset            reset histogram after every report

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

---

## Format Conversion

### `csv2json`

```
convert CSV to JSON format

Usage:
  csvtk csv2json [flags] 

Flags:
  -b, --blanks              do not convert "", "na", "n/a", "none", "null", "." to null
  -h, --help                help for csv2json
  -i, --indent string       indent. if given blank, output json in one line. (default "  ")
  -k, --key string          output json as an array of objects keyed by a given field rather than as a
                            list. e.g -k 1 or -k columnA
  -n, --parse-num strings   parse numeric values for nth column, multiple values are supported and
                            "a"/"all" for all columns

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `csv2md`

```
convert CSV to markdown format

Attention:

  csv2md treats the first row as header line and requires them to be unique

Usage:
  csvtk csv2md [flags] 

Flags:
  -a, --alignments string   comma separated alignments. e.g. -a l,c,c,c or -a c (default "l")
  -h, --help                help for csv2md
  -w, --min-width int       min width (at least 3) (default 3)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `csv2rst`

```
convert CSV to readable aligned table

Attention:

  1. row span is not supported.

Usage:
  csvtk csv2rst [flags] 

Flags:
  -k, --cross string               charactor of cross (default "+")
  -s, --header string              charactor of separator between header row and data rowws (default "=")
  -h, --help                       help for csv2rst
  -b, --horizontal-border string   charactor of horizontal border (default "-")
  -p, --padding string             charactor of padding (default " ")
  -B, --vertical-border string     charactor of vertical border (default "|")

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `csv2tab`

```
convert CSV to tabular format

Usage:
  csvtk csv2tab [flags] 

Flags:
  -h, --help   help for csv2tab

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `csv2xlsx`

```
convert CSV/TSV files to XLSX file

Attention:

  1. Multiple CSV/TSV files are saved as separated sheets in .xlsx file.
  2. All input files should all be CSV or TSV.
  3. First rows are freezed unless given '-H/--no-header-row'.

Usage:
  csvtk csv2xlsx [flags] 

Flags:
  -f, --format-numbers   save numbers in number format, instead of text
  -h, --help             help for csv2xlsx

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `pretty`

```
convert CSV to a readable aligned table

How to:
  1. First -n/--buf-rows rows are read to check the minimum and maximum widths
     of each columns. You can also set the global thresholds -w/--min-width and
     -W/--max-width.
     1a. Cells longer than the maximum width will be wrapped (default) or
         clipped (--clip).
     1b. Texts are aligned left (default), center (-m/--align-center)
         or right (-r/--align-right). Users can specify columns with column names,
         field indexes or ranges.

Styles: default, plain, simple, 3line, grid, light, bold, double
  Use -S/--style to select.

Usage:
  csvtk pretty [flags] 

Flags:
  -m, --align-center strings    align center for selected columns
  -r, --align-right strings     align right for selected columns
  -n, --buf-rows int            the number of rows to determine the min and max widths (0 for all rows)
                                (default 1024)
      --clip                    clip longer cell instead of wrapping
      --clip-mark string        clip mark (default "...")
  -h, --help                    help for pretty
  -W, --max-width int           max width
  -w, --min-width int           min width
  -s, --separator string        fields/columns separator (default "   ")
  -S, --style string            output style: default, plain, simple, 3line, grid, light, bold, double
  -x, --wrap-delimiter string   delimiter for wrapping cells (default " ")

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `space2tab`

```
convert space delimited format to TSV

Usage:
  csvtk space2tab [flags] 

Flags:
  -b, --buffer-size string   size of buffer, supported unit: K, M, G (default "1G")
  -h, --help                 help for space2tab

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `splitxlsx`

```
split XLSX sheet into multiple sheets according to column values

Usage:
  csvtk splitxlsx [flags] 

Flags:
  -f, --fields string       comma separated key fields, column name or index (default "1")
  -F, --fuzzy-fields        using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                help for splitxlsx
  -i, --ignore-case         ignore case (cell value)
  -a, --list-sheets         list all sheets
  -N, --sheet-index int     Nth sheet to retrieve (default 1)
  -n, --sheet-name string   sheet to retrieve

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `tab2csv`

```
convert tabular format to CSV

Usage:
  csvtk tab2csv [flags] 

Flags:
  -h, --help   help for tab2csv

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `xlsx2csv`

```
convert XLSX to CSV format

Usage:
  csvtk xlsx2csv [flags] 

Flags:
  -h, --help                help for xlsx2csv
  -a, --list-sheets         list all sheets
  -i, --sheet-index int     Nth sheet to retrieve (default 1)
  -n, --sheet-name string   sheet to retrieve

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

---

## Set Operations

### `comb`

```
compute combinations of items at every row

Usage:
  csvtk comb [flags] 

Aliases:
  comb, combination

Flags:
  -h, --help          help for comb
  -i, --ignore-case   ignore-case
  -S, --nat-sort      sort items in natural order
  -n, --number int    number of items in a combination, 0 for no limit (default 2)
  -s, --sort          sort items in a combination

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `concat`

```
concatenate CSV/TSV files by rows

Note that the second and later files are concatenated to the first one,
so only columns match that of the first files kept.

Usage:
  csvtk concat [flags] 

Flags:
  -h, --help                    help for concat
  -i, --ignore-case             ignore case (column name)
  -k, --keep-unmatched          keep blanks even if no any data of a file matches
  -u, --unmatched-repl string   replacement for unmatched data

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `cut`

```
select and arrange fields

Examples:

  1. Single column
     csvtk cut -f 1
     csvtk cut -f colA
  2. Multiple columns (replicates allowed)
     csvtk cut -f 1,3,2,1
     csvtk cut -f colA,colB,colA
  3. Column ranges
     csvtk cut -f 1,3-5       # 1, 3, 4, 5
     csvtk cut -f 3,5-        # 3rd col, and 5th col to the end
     csvtk cut -f 1-          # for all
     csvtk cut -f 2-,1        # move 1th col to the end
  4. Unselect
     csvtk cut -f -1,-3       # discard 1st and 3rd column
     csvtk cut -f -1--3       # discard 1st to 3rd column
     csvtk cut -f -2-         # discard 2nd and all columns on the right.
     csvtk cut -f -colA,-colB # discard colA and colB

Usage:
  csvtk cut [flags] 

Flags:
  -m, --allow-missing-col   allow missing column
  -b, --blank-missing-col   blank missing column, only for using column fields
  -f, --fields string       select only these fields. type "csvtk cut -h" for examples
  -F, --fuzzy-fields        using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                help for cut
  -i, --ignore-case         ignore case (column name)
  -u, --uniq-column         deduplicate columns matched by multiple fuzzy column names

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `filter`

```
filter rows by values of selected fields with arithmetic expression

Usage:
  csvtk filter [flags] 

Flags:
      --any             print record if any of the field satisfy the condition
  -f, --filter string   filter condition. e.g. -f "age>12" or -f "1,3<=2" or -F -f "c*!=0"
  -F, --fuzzy-fields    using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help            help for filter
  -n, --line-number     print line number as the first column ("n")

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `filter2`

```
filter rows by awk-like arithmetic/string expressions

Variables formats:
  $1 or ${1}                        The first field/column
  $a or ${a}                        Column "a"
  ${a,b} or ${a b} or ${a (b)}      Column name with special characters

Supported operators: + - / * & | ^ ** % >> << > >= < <= == != =~ !~ in || &&
Ternary conditional: ? :   Null coalescence: ??

Custom functions:
  - len(), ulen() for string/unicode length

Usage:
  csvtk filter2 [flags] 

Flags:
  -f, --filter string       awk-like filter condition. e.g. '$age>12' or '$1 > $3' or '$name=="abc"'
  -h, --help                help for filter2
  -n, --line-number         print line number as the first column ("n")
  -s, --numeric-as-string   treat even numeric fields as strings to avoid converting big numbers into
                            scientific notation

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `freq`

```
frequencies of selected fields

Usage:
  csvtk freq [flags] 

Flags:
  -f, --fields string   select these fields as the key. e.g -f 1,2 or -f columnA,columnB (default "1")
  -F, --fuzzy-fields    using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help            help for freq
  -i, --ignore-case     ignore case
  -r, --reverse         reverse order while sorting
  -n, --sort-by-freq    sort by frequency
  -k, --sort-by-key     sort by key

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `grep`

```
grep data by selected fields with patterns/regular expressions

Attentions:

  1. By default, we directly compare the column value with patterns,
     use "-r/--use-regexp" for partly matching.
  2. Multiple patterns can be given by setting '-p/--pattern' more than once,
     or giving comma separated values (CSV formats).

Usage:
  csvtk grep [flags] 

Flags:
      --delete-matched        delete a pattern right after being matched
  -f, --fields string         comma separated key fields (default "1")
  -F, --fuzzy-fields          using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                  help for grep
  -i, --ignore-case           ignore case
      --immediate-output      print output immediately, do not use write buffer
  -v, --invert                invert match
  -n, --line-number           print line number as the first column ("n")
  -N, --no-highlight          no highlight
  -p, --pattern strings       query pattern (multiple values supported)
  -P, --pattern-file string   pattern files (one pattern per line)
  -r, --use-regexp            patterns are regular expression
      --verbose               verbose output

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `head`

```
print first N records

Usage:
  csvtk head [flags] 

Flags:
  -h, --help         help for head
  -n, --number int   print first N records (default 10)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `inter`

```
intersection of multiple files

Attention:

  1. fields in all files should be the same, 
     if not, extracting to another file using "csvtk cut".

Usage:
  csvtk inter [flags] 

Flags:
  -f, --fields string   select these fields as the key. e.g -f 1,2 or -f columnA,columnB (default "1")
  -F, --fuzzy-fields    using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help            help for inter
  -i, --ignore-case     ignore case

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `join`

```
join files by selected fields (inner, left and outer join).

Attention:

  1. Multiple keys supported
  2. Default operation is inner join, use --left-join for left join 
     and --outer-join for outer join.

Usage:
  csvtk join [flags] 

Aliases:
  join, merge

Flags:
  -f, --fields string     Semicolon separated key fields of all files. Fields of different files should
                          be separated by ";", e.g -f "1;2" or -f "A,B;C,D" or -f id (default "1")
  -F, --fuzzy-fields      using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help              help for join
  -i, --ignore-case       ignore case
  -n, --ignore-null       do not match NULL values
  -k, --keep-unmatched    keep unmatched data of the first file (left join)
  -L, --left-join         left join, equals to -k/--keep-unmatched, exclusive with --outer-join
      --na string         content for filling NA data
  -P, --only-duplicates   add filenames as colname prefixes or add custom suffixes only for duplicated
                          colnames
  -O, --outer-join        outer join, exclusive with --left-join
  -p, --prefix-filename   add each filename as a prefix to each colname
  -e, --prefix-trim-ext   trim extension when adding filename as colname prefix
  -s, --suffix strings    add suffixes to colnames from each file

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `sample`

```
sampling by proportion

Usage:
  csvtk sample [flags] 

Flags:
  -h, --help               help for sample
  -n, --line-number        print line number as the first column ("row")
  -p, --proportion float   sample by proportion
  -s, --rand-seed int      rand seed (default 11)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `split`

```
split CSV/TSV into multiple files according to column values

Notes:

  1. flag -o/--out-file can specify out directory for split files.
  2. flag -s/--prefix-as-subdir can create subdirectories with prefixes of
     keys of length X, to avoid writing too many files in the output directory.

Usage:
  csvtk split [flags] 

Flags:
  -g, --buf-groups int         buffering N groups before writing to file (default 100)
  -b, --buf-rows int           buffering N rows for every group before writing to file (default 100000)
  -f, --fields string          comma separated key fields (default "1")
      --force                  overwrite existing output directory (given by -o)
  -F, --fuzzy-fields           using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                   help for split
  -i, --ignore-case            ignore case
  -G, --out-gzip               force output gzipped file
  -p, --out-prefix string      output file prefix, the default value is the input file
  -s, --prefix-as-subdir int   create subdirectories with prefixes of keys of length X

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `uniq`

```
unique data without sorting

Usage:
  csvtk uniq [flags] 

Flags:
  -f, --fields string   select these fields as keys. e.g -f 1,2 or -f columnA,columnB (default "1")
  -F, --fuzzy-fields    using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help            help for uniq
  -i, --ignore-case     ignore case
  -n, --keep-n int      keep at most N records for a key (default 1)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

---

## Editing

### `add-header`

```
add column names

Usage:
  csvtk add-header [flags] 

Flags:
  -h, --help            help for add-header
  -n, --names strings   column names to add, in CSV format

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `del-header`

```
delete column names

Attention:
  1. It deletes the first line of all input files.

Usage:
  csvtk del-header [flags] 

Flags:
  -h, --help   help for del-header

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `del-quotes`

```
remove extra double quotes added by 'fix-quotes'

Limitation:
  1. Values containing line breaks are not supported.

Usage:
  csvtk del-quotes [flags] 

Flags:
  -h, --help   help for del-quotes

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `fix`

```
fix CSV/TSV with different numbers of columns in rows

How to:
  1. First -n/--buf-rows rows are read to check the maximum number of columns.
     The default value 0 means all rows will be read.
  2. Buffered and remaining rows with fewer columns are appended with empty
     cells before output.

Usage:
  csvtk fix [flags] 

Flags:
  -n, --buf-rows int   the number of rows to determine the maximum number of columns. 0 for all rows.
  -h, --help           help for fix

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `fix-quotes`

```
fix malformed CSV/TSV caused by double-quotes

This command fixes fields not appropriately enclosed by double-quotes
to meet the RFC4180 specification.

Limitation:
  1. Values containing line breaks are not supported.

Usage:
  csvtk fix-quotes [flags] 

Flags:
  -b, --buffer-size string   size of buffer, supported unit: K, M, G (default "1G")
  -h, --help                 help for fix-quotes

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `fmtdate`

```
format date of selected fields

Date parsing: https://github.com/araddon/dateparse
Date formatting: https://github.com/metakeule/fmtdate (MS Excel syntax)

Placeholders: M MM MMM MMMM D DD DDD DDDD YY YYYY hh mm ss hpm h:mmpm h:mm:sspm
Time zones: ZZZZ ZZZ ZZ (e.g., hh:mm:ss ZZZZ -> 16:05:06 +0100)

Usage:
  csvtk fmtdate [flags] 

Flags:
  -f, --fields string      select only these fields. e.g -f 1,2 or -f columnA,columnB (default "1")
      --format string      output date format in MS Excel syntax (default "YYYY-MM-DD hh:mm:ss")
  -F, --fuzzy-fields       using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help               help for fmtdate
  -k, --keep-unparsed      keep the key as value when no value found for the key
  -z, --time-zone string   timezone aka "Asia/Shanghai" or "America/Los_Angeles"

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `mutate`

```
create new column from selected fields by regular expression

Usage:
  csvtk mutate [flags] 

Flags:
      --after string     insert the new column right after the given column name
      --at int           where the new column should appear, 1 for the 1st column, 0 for the last column
      --before string    insert the new column right before the given column name
  -f, --fields string    select only these fields. e.g -f 1,2 or -f columnA,columnB (default "1")
  -h, --help             help for mutate
  -i, --ignore-case      ignore case
      --na               for unmatched data, use blank instead of original data
  -n, --name string      new column name
  -p, --pattern string   search regular expression with capture bracket (default "^(.+)$")
  -R, --remove           remove input column

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `mutate2`

```
create a new column from selected fields by awk-like arithmetic/string expressions

Variables: $1 or ${1} (by index), $a or ${a} (by name), ${a,b} (special chars in name)
Operators: + - / * & | ^ ** % >> << > >= < <= == != =~ !~ in || &&
Ternary: ? :   Null coalescence: ??
Custom functions: len(), ulen()

Usage:
  csvtk mutate2 [flags] 

Flags:
      --after string        insert the new column right after the given column name
      --at int              where the new column should appear, 1 for the 1st column, 0 for the last column
      --before string       insert the new column right before the given column name
  -w, --decimal-width int   limit floats to N decimal points (default 2)
  -e, --expression string   arithmetic/string expressions. e.g. '$a + "-" + $b', '$1 + $2', '$a / $b'
  -h, --help                help for mutate2
  -n, --name string         new column name
  -s, --numeric-as-string   treat even numeric fields as strings to avoid converting big numbers into
                            scientific notation

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `mutate3`

```
create a new column from selected fields with Go-like expressions (Expr language)

Variables: $1 or ${1} (by index), $a or ${a} (by name), ${a,b} (special chars in name)
Operators: + - / * ^ ** % > >= < <= == != not ! and && or || contains startsWith endsWith matches
Ternary: ? :   Null coalescence: ??
See https://expr-lang.org/docs/language-definition for built-in functions.
Custom functions: ulen()

Usage:
  csvtk mutate3 [flags] 

Flags:
      --after string        insert the new column right after the given column name
      --at int              where the new column should appear, 1 for the 1st column, 0 for the last column
      --before string       insert the new column right before the given column name
  -w, --decimal-width int   limit floats to N decimal points (default 2)
  -e, --expression string   Go-like expressions. e.g. '$a + "-" + $b', '$1 > 100 ? "big" : "small"'
  -h, --help                help for mutate3
  -n, --name string         new column name
  -s, --numeric-as-string   treat even numeric fields as strings to avoid converting big numbers into
                            scientific notation

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `rename`

```
rename column names with new names

Usage:
  csvtk rename [flags] 

Flags:
  -f, --fields string   select only these fields. e.g -f 1,2 or -f columnA,columnB
  -F, --fuzzy-fields    using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help            help for rename
  -n, --names string    comma separated new names

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `rename2`

```
rename column names by regular expression

Special replacement symbols:
  {nr}  ascending number, starting from --start-num
  {kv}  value from key-value file (captured variable $n)

Usage:
  csvtk rename2 [flags] 

Flags:
  -f, --fields string                       select only these fields. e.g -f 1,2 or -f columnA,columnB
  -F, --fuzzy-fields                        using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                                help for rename2
  -i, --ignore-case                         ignore case
  -K, --keep-key                            keep the key as value when no value found for the key
      --key-capt-idx int                    capture variable index of key (1-based) (default 1)
      --key-miss-repl string                replacement for key with no corresponding value
  -k, --kv-file string                      tab-delimited key-value file for replacing key with value
  -A, --kv-file-all-left-columns-as-value   treat all columns except 1th one as value for kv-file with
                                            more than 2 columns
      --nr-width int                        minimum width for {nr} (default 1)
  -p, --pattern string                      search regular expression
  -r, --replacement string                  replacement supporting capture variables (use SINGLE quotes)
  -n, --start-num int                       starting number when using {nr} in replacement (default 1)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `replace`

```
replace data of selected fields by regular expression

Note that the replacement supports capture variables.
ATTENTION: use SINGLE quote NOT double quotes in *nix OS.

Special replacement symbols:
  {nr}    Record number, starting from 1
  {kv}    Value from key-value file (captured variable $n)

Usage:
  csvtk replace [flags] 

Flags:
  -f, --fields string                       select only these fields (default "1")
  -F, --fuzzy-fields                        using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                                help for replace
  -i, --ignore-case                         ignore case
  -K, --keep-key                            keep the key as value when no value found for the key
      --key-capt-idx int                    capture variable index of key (1-based) (default 1)
      --key-miss-repl string                replacement for key with no corresponding value
  -k, --kv-file string                      tab-delimited key-value file for replacing key with value
  -A, --kv-file-all-left-columns-as-value   treat all columns except 1th one as value for kv-file
      --nr-width int                        minimum width for {nr} (default 1)
  -p, --pattern string                      search regular expression
  -r, --replacement string                  replacement supporting capture variables (use SINGLE quotes)
  -n, --start-num int                       starting number when using {nr} in replacement (default 1)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `round`

```
round float to n decimal places

Usage:
  csvtk round [flags] 

Flags:
  -a, --all-fields          all fields, overides -f/--fields
  -n, --decimal-width int   limit floats to N decimal points (default 2)
  -f, --fields string       select only these fields. e.g -f 1,2 or -f columnA,columnB (default "1")
  -F, --fuzzy-fields        using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help                help for round

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

---

## Data Transformation

### `fold`

```
fold multiple values of a field into cells of groups

Attention: Only grouping fields and value field are outputted.

Usage:
  csvtk fold [flags] 

Aliases:
  fold, collapse

Flags:
  -f, --fields string      key fields for grouping. e.g -f 1,2 or -f columnA,columnB (default "1")
  -F, --fuzzy-fields       using fuzzy fields (only for key fields)
  -h, --help               help for fold
  -i, --ignore-case        ignore case
  -s, --separater string   separater for folded values (default "; ")
  -v, --vfield string      value field for folding

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `gather`

```
gather columns into key-value pairs, like tidyr::gather/pivot_longer

Usage:
  csvtk gather [flags] 

Aliases:
  gather, longer

Flags:
  -f, --fields string   fields for gathering (e.g -f 1,2 or -f columnA,columnB, or -f -columnA to exclude)
  -F, --fuzzy-fields    using fuzzy fields, e.g., -F -f "*name" or -F -f "id123*"
  -h, --help            help for gather
  -k, --key string      name of key column to create in output
  -v, --value string    name of value column to create in output

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `sep`

```
separate column into multiple columns

Usage:
  csvtk sep [flags] 

Aliases:
  sep, separate

Flags:
      --drop            drop extra data, exclusive with --merge
  -f, --fields string   select only these fields (default "1")
  -h, --help            help for sep
  -i, --ignore-case     ignore case
      --merge           only splits at most N times, exclusive with --drop
      --na string       content for filling NA data
  -n, --names strings   new column names
  -N, --num-cols int    preset number of new created columns
  -R, --remove          remove input column
  -s, --sep string      separator
  -r, --use-regexp      separator is a regular expression

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `spread`

```
spread a key-value pair across multiple columns, like tidyr::spread/pivot_wider

Usage:
  csvtk spread [flags] 

Aliases:
  spread, wider, scatter

Flags:
  -h, --help               help for spread
  -k, --key string         field of the key. e.g -k 1 or -k columnA
      --na string          content for filling NA data
  -s, --separater string   separater for values that share the same key (default "; ")
  -v, --value string       field of the value. e.g -v 1 or -v columnA

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `transpose`

```
transpose CSV data

Usage:
  csvtk transpose [flags] 

Flags:
  -h, --help   help for transpose

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

### `unfold`

```
unfold multiple values in cells of a field

Usage:
  csvtk unfold [flags] 

Flags:
  -f, --fields string      field to expand, only one field is allowed
  -h, --help               help for unfold
  -s, --separater string   separater for folded values (default "; ")

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

---

## Ordering

### `sort`

```
sort by selected fields

Usage:
  csvtk sort [flags] 

Flags:
  -h, --help             help for sort
  -i, --ignore-case      ignore-case
  -k, --keys strings     keys (multiple values supported). sort type: "N" natural, "n" numeric,
                         "u" user-defined, "r" reverse. e.g., "-k 1" or "-k A:r" or "-k 1:nr -k 2"
                         (default [1])
  -L, --levels strings   user-defined level file (one level per line, multiple values supported).
                         format: <field>:<level-file>. e.g., "-k name:u -L name:level.txt"

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```

---

## Plotting

### `plot`

```
plot common figures

Subcommands: box, hist, line

Flags:
      --axis-width float      axis width (default 1.5)
  -f, --data-field string     column index or column name of data (default "1")
      --format string         image format for stdout: eps, jpg, pdf, png, svg, tif (default "png")
  -g, --group-field string    column index or column name of group
      --height float          figure height (default 4.5)
  -h, --help                  help for plot
      --label-size int        label font size (default 14)
      --na-values strings     NA values, case ignored (default [,NA,N/A])
      --scale float           scale image width/height/tick/axes/font proportionally (default 1)
      --skip-na               skip NA values
      --tick-label-size int   tick label font size (default 12)
      --tick-width float      axis tick width (default 1.5)
      --title string          figure title
      --title-size int        title font size (default 16)
      --width float           figure width (default 6)
      --x-max string          maximum value of X axis
      --x-min string          minimum value of X axis
      --xlab string           x label text
      --y-max string          maximum value of Y axis
      --y-min string          minimum value of Y axis
      --ylab string           y label text
```

### `plot box`

```
plot boxplot

Usage:
  csvtk plot box [flags] 

Flags:
      --box-width float    box width
      --color-index int    color index, 1-7 (default 1)
  -h, --help               help for box
      --horiz              horizontal box plot
      --line-width float   line width (default 1.5)
      --point-size float   point size (default 3)

(Inherits all global plot flags: --data-field, --group-field, --title, --width, --height, etc.)
```

### `plot hist`

```
plot histogram

Usage:
  csvtk plot hist [flags] 

Flags:
      --bins int           number of bins (default 50)
      --color-index int    color index, 1-7 (default 1)
  -h, --help               help for hist
      --line-width float   line width (default 1)
      --percentiles        calculate percentiles

(Inherits all global plot flags: --data-field, --group-field, --title, --width, --height, etc.)
```

### `plot line`

```
line plot and scatter plot

Usage:
  csvtk plot line [flags] 

Flags:
      --color-index int       color index, 1-7 (default 1)
  -x, --data-field-x string   column index or column name of X
  -y, --data-field-y string   column index or column name of Y
  -h, --help                  help for line
      --legend-left           locate legend along the left edge of the plot
      --legend-top            locate legend along the top edge of the plot
      --line-width float      line width (default 1.5)
      --point-size float      point size (default 3)
      --scatter               only plot points (scatter plot)

(Inherits all global plot flags: --group-field, --title, --width, --height, etc.)
```

---

## Miscellaneous

### `cat`

```
stream file to stdout and report progress on stderr

Usage:
  csvtk cat [flags] 

Flags:
  -b, --buffsize int     buffer size (default 8192)
  -h, --help             help for cat
  -L, --lines            count lines instead of bytes
  -p, --print-freq int   print frequency (-1 for print after parsing) (default 1)
  -s, --total int        expected total bytes/lines (default -1)

Global Flags:
  -C, --comment-char string    lines starting with commment-character will be ignored. if your header
                               row starts with '#', please assign "-C" another rare symbol, e.g. '$'
                               (default "#")
  -U, --delete-header          do not output header row
  -d, --delimiter string       delimiting character of the input CSV file (default ",")
  -E, --ignore-empty-row       ignore empty rows
  -I, --ignore-illegal-row     ignore illegal rows. You can also use 'csvtk fix' to fix files with
                               different numbers of columns in rows
  -X, --infile-list string     file of input files list (one file per line), if given, they are appended
                               to files from cli arguments
  -l, --lazy-quotes            if given, a quote may appear in an unquoted field and a non-doubled quote
                               may appear in a quoted field
  -H, --no-header-row          specifies that the input CSV file does not have header row
  -j, --num-cpus int           number of CPUs to use (default 4)
  -D, --out-delimiter string   delimiting character of the output CSV file, e.g., -D $'\t' for tab
                               (default ",")
  -o, --out-file string        out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
  -T, --out-tabs               specifies that the output is delimited with tabs. Overrides "-D"
      --quiet                  be quiet and do not show extra information and warnings
  -Z, --show-row-number        show row number as the first column, with header row skipped
  -t, --tabs                   specifies that the input CSV file is delimited with tabs. Overrides "-d"
```
