# seqkit — Full Reference

Binary: `~/.cursor/skills/seqkit/bin/seqkit`

Each entry contains the verbatim `--help` output. Grep for a subcommand:
```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/seqkit/reference.md
```
Increase `-A` if output appears truncated.

**Global flags** (common to all subcommands):
```
    --alphabet-guess-seq-length int   length of sequence prefix for type-guessing (default 10000)
    --compress-level int              compression level for gzip/zstd/xz/bzip2 (default -1)
    --id-ncbi                         FASTA head is NCBI-style
    --id-regexp string                regular expression for parsing ID (default "^(\\S+)\\s?")
-X, --infile-list string              file of input files list (one per line)
-w, --line-width int                  line width when outputting FASTA format (0 for no wrap) (default 60)
-o, --out-file string                 out file ("-" for stdout, suffix .gz for gzipped out) (default "-")
    --quiet                           be quiet and do not show extra information
-t, --seq-type string                 sequence type (dna|rna|protein|unlimit|auto) (default "auto")
    --skip-file-check                 skip input file checking when given a file list
-j, --threads int                     number of CPUs (default 4)
```

---

## Basic Operation

### `seq`

```
transform sequences (extract ID, filter by length, remove gaps, reverse complement...)

Usage:
  seqkit seq [flags] 

Flags:
  -k, --color                    colorize sequences - to be piped into "less -R"
  -p, --complement               complement sequence, flag '-v' is recommended to switch on
      --dna2rna                  DNA to RNA
      --f-by-name                [target filter] match by full name instead of just ID
      --f-by-seq                 [target filter] search subseq on seq, both positive and negative strand
      --f-ignore-case            [target filter] ignore case
      --f-invert-match           [target filter] invert the sense of matching
      --f-only-positive-strand   [target filter] only search on positive strand
      --f-pattern strings        [target filter] search pattern (multiple values supported)
      --f-pattern-file string    [target filter] pattern file (one record per line)
      --f-use-regexp             [target filter] patterns are regular expression
  -G, --gap-letters string       gap letters to be removed with -g/--remove-gaps (default "- \t.")
  -h, --help                     help for seq
  -l, --lower-case               print sequences in lower case
  -M, --max-len int              only print sequences shorter than or equal to the maximum length (default -1)
  -R, --max-qual float           only print sequences with average quality less than this limit (default -1)
  -m, --min-len int              only print sequences longer than or equal to the minimum length (default -1)
  -Q, --min-qual float           only print sequences with average quality greater or equal than this limit (default -1)
  -n, --name                     only print names/sequence headers
  -i, --only-id                  print IDs instead of full headers
  -q, --qual                     only print qualities
  -b, --qual-ascii-base int      ASCII BASE, 33 for Phred+33 (default 33)
  -g, --remove-gaps              remove gap letters
  -r, --reverse                  reverse sequence
      --rna2dna                  RNA to DNA
  -s, --seq                      only print sequences
  -u, --upper-case               print sequences in upper case
  -v, --validate-seq             validate bases according to the alphabet
```

### `stats`

```
simple statistics of FASTA/Q files

Output columns (with -a/--all):
  file, format, type, num_seqs, sum_len, min_len, avg_len, max_len,
  Q1, Q2, Q3, sum_gap, N50, N50_num, Q20(%), Q30(%), AvgQual, GC(%), sum_n

Usage:
  seqkit stats [flags] 

Aliases:
  stats, stat

Flags:
  -N, --N strings            append other N50-like stats, e.g., -N 50,90
  -a, --all                  all statistics, including quartiles of seq length, sum_gap, N50
  -b, --basename             only output basename of files
  -E, --fq-encoding string   fastq quality encoding (default "sanger")
  -G, --gap-letters string   gap letters (default "- .")
  -h, --help                 help for stats
  -e, --skip-err             skip error, only show warning message
  -S, --skip-file-check      skip input file checking
  -i, --stdin-label string   label for replacing default "-" for stdin (default "-")
  -T, --tabular              output in machine-friendly tabular format
```

### `faidx`

```
create the FASTA index file and extract subsequences

Similar to "samtools faidx" but with extra features:
  - Full header output with -f flag
  - Regex IDs with -r flag
  - Large ID lists via -l file

Region format: 1-based. 1:12 = first 12, -12:-1 = last 12, -1:-1 = last base.

Usage:
  seqkit faidx [flags] <fasta-file> [regions...]

Flags:
  -f, --full-head            print full header line instead of just ID
  -h, --help                 help for faidx
  -i, --ignore-case          ignore case
  -I, --immediate-output     print output immediately, do not use write buffer
  -l, --region-file string   file containing a list of regions
  -U, --update-faidx         update the fasta index file if it exists
  -r, --use-regexp           IDs are regular expression
```

### `scat`

```
real time recursive concatenation and streaming of fastx files

Usage:
  seqkit scat [flags] 

Flags:
  -A, --allow-gaps            allow gap character (-) in sequences
  -d, --delta int             minimum size increase in kilobytes to trigger parsing (default 5)
  -D, --drop-time string      Notification drop interval (default "500ms")
  -f, --find-only             concatenate existing files and quit
  -i, --format string         input and output format: fastq or fasta (default "fastq")
  -g, --gz-only               only look for gzipped files (.gz suffix)
  -h, --help                  help for scat
  -I, --in-format string      input format: fastq or fasta
  -O, --out-format string     output format: fastq or fasta
  -b, --qual-ascii-base int   ASCII BASE, 33 for Phred+33 (default 33)
  -r, --regexp string         regexp for watched files
  -T, --time-limit string     quit after inactive for this time period
  -p, --wait-pid int          after process with this PID exited (default -1)
```

### `sliding`

```
extract subsequences in sliding windows

Usage:
  seqkit sliding [flags] 

Flags:
  -c, --circular          circular genome
  -C, --circular-genome   circular genome (same to -c/--circular)
  -g, --greedy            greedy mode, i.e., also export last window even if shorter
  -h, --help              help for sliding
  -s, --step int          step size
  -S, --suffix string     suffix added to the sequence ID (default "_sliding")
  -W, --window int        window size
```

### `subseq`

```
get subsequences by region/gtf/bed, including flanking sequences.

Region format: 1-based. 1:12 = first 12, -12:-1 = last 12.

Usage:
  seqkit subseq [flags] 

Flags:
      --bed string        by tab-delimited BED file
      --chr strings       select limited sequence with sequence IDs when using --gtf or --bed
  -d, --down-stream int   down stream length
      --feature strings   select limited feature types (only works with GTF)
      --gtf string        by GTF (version 2.2) file
      --gtf-tag string    output this tag as sequence comment (default "gene_id")
  -h, --help              help for subseq
  -f, --only-flank        only return up/down stream sequence
  -r, --region string     by region. e.g 1:12 for first 12 bases, -12:-1 for last 12 bases
  -R, --region-coord      append coordinates to sequence ID for -r/--region
  -u, --up-stream int     up stream length
  -U, --update-faidx      update the fasta index file if it exists
```

### `translate`

```
translate DNA/RNA to protein sequence (supporting ambiguous bases)

Supports all NCBI translation tables (1-31). Ambiguous codons (e.g., ACN -> T) are supported.

Usage:
  seqkit translate [flags] 

Flags:
  -x, --allow-unknown-codon     translate unknown code to 'X'
  -F, --append-frame            append frame information to sequence ID
      --clean                   change all STOP codon positions from '*' to 'X'
  -f, --frame strings           frame(s) to translate: 1, 2, 3, -1, -2, -3, 6 for all (default [1])
  -h, --help                    help for translate
  -M, --init-codon-as-M         translate initial codon at beginning to 'M'
  -l, --list-transl-table int   show details of translate table N, 0 for all (default -1)
  -m, --min-len int             the minimum length of amino acid sequence
  -s, --out-subseqs             output individual amino acid subsequences separated by stop symbol "*"
  -e, --skip-translate-errors   skip errors during translate and output blank sequence
  -T, --transl-table int        translate table/genetic code (default 1)
      --trim                    remove all 'X' and '*' characters from the right end
```

### `watch`

```
monitoring and online histograms of sequence features

Usage:
  seqkit watch [flags] 

Flags:
  -B, --bins int              number of histogram bins (default -1)
  -W, --delay int             sleep this many seconds after online plotting (default 1)
  -y, --dump                  print histogram data to stderr instead of plotting
  -f, --fields string         target fields: ReadLen, MeanQual, GC, GCSkew (default "ReadLen")
  -h, --help                  help for watch
  -O, --img string            save histogram to this PDF/image file
  -H, --list-fields           print out a list of available fields
  -L, --log                   log10(x+1) transform numeric values
  -x, --pass                  pass through mode (write input to stdout)
  -p, --print-freq int        print/report after this many records (-1 for print after EOF) (default -1)
  -b, --qual-ascii-base int   ASCII BASE, 33 for Phred+33 (default 33)
  -Q, --quiet-mode            supress all plotting to stderr
  -R, --reset                 reset histogram after every report
  -v, --validate-seq          validate bases according to the alphabet
```

---

## Format Conversion

### `convert`

```
convert FASTQ quality encoding between Sanger, Solexa and Illumina

Usage:
  seqkit convert [flags] 

Flags:
  -d, --dry-run                         dry run
  -f, --force                           for Illumina-1.8+ -> Sanger, truncate scores > 40 to 40
      --from string                     source quality encoding (if not given, we'll guess it)
  -h, --help                            help for convert
  -n, --nrecords int                    number of records for guessing quality encoding (default 1000)
  -N, --thresh-B-in-n-most-common int   threshold of 'B' in top N most common quality for guessing Illumina 1.5 (default 2)
  -F, --thresh-illumina1.5-frac float   threshold of faction of Illumina 1.5 in the leading N records (default 0.1)
      --to string                       target quality encoding (default "Sanger")
```

### `fa2fq`

```
retrieve corresponding FASTQ records by a FASTA file

Attention:
  1. We assume the FASTA file comes from the FASTQ file, so they share sequence IDs.

Usage:
  seqkit fa2fq [flags] 

Flags:
  -f, --fasta-file string      FASTA file
  -h, --help                   help for fa2fq
  -P, --only-positive-strand   only search on positive strand
```

### `fq2fa`

```
convert FASTQ to FASTA

Usage:
  seqkit fq2fa [flags] 

Flags:
  -h, --help   help for fq2fa
```

### `fx2tab`

```
convert FASTA/Q to tabular format, and provide various information,
like sequence length, GC content/GC skew.

Output: 3 fixed columns (ID, sequence, quality) for FASTA or FASTQ, plus optional extras.

Usage:
  seqkit fx2tab [flags] 

Flags:
  -a, --alphabet               print alphabet letters
  -q, --avg-qual               print average quality of a read
  -B, --base-content strings   print base content (case ignored, e.g., -B AT -B N)
  -C, --base-count strings     print base count (case ignored, e.g., -C AT -C N)
  -I, --case-sensitive         calculate case sensitive base content/sequence hash
  -g, --gc                     print GC content, i.e., (G+C)/(G+C+A+T)
  -G, --gc-skew                print GC-Skew
  -H, --header-line            print header line
  -h, --help                   help for fx2tab
  -l, --length                 print sequence length
  -n, --name                   only print names (no sequences and qualities)
  -Q, --no-qual                only output two column even for FASTQ file
  -i, --only-id                print ID instead of full head
  -b, --qual-ascii-base int    ASCII BASE, 33 for Phred+33 (default 33)
  -s, --seq-hash               print hash (MD5) of sequence
```

### `tab2fx`

```
convert tabular format (first two/three columns) to FASTA/Q format

Usage:
  seqkit tab2fx [flags] 

Flags:
  -b, --buffer-size string            size of buffer (default "1G")
  -p, --comment-line-prefix strings   comment line prefix (default [#,//])
  -h, --help                          help for tab2fx
```

---

## Searching

### `amplicon`

```
extract amplicon (or specific region around it) via primer(s).

Attention:
  1. Only one (the longest) matching location is returned for every primer pair.
  2. Mismatch is allowed.
  3. Degenerate bases are supported.

Region format: inner region or flanking region (-f flag). e.g., 1:-1 for full amplicon.

Usage:
  seqkit amplicon [flags] 

Flags:
      --bed                    output in BED6+1 format
  -f, --flanking-region        region is flanking region
  -F, --forward string         forward primer (5'-primer-3'), degenerate bases allowed
  -h, --help                   help for amplicon
  -I, --immediate-output       print output immediately
  -m, --max-mismatch int       max mismatch when matching primers
  -P, --only-positive-strand   only search on positive strand
  -M, --output-mismatches      append the total mismatches and mismatches of 5' end and 3' end
  -p, --primer-file string     3- or 2-column tabular primer file, with first column as primer name
  -r, --region string          specify region to return
  -R, --reverse string         reverse primer (5'-primer-3'), degenerate bases allowed
  -u, --save-unmatched         also save records that do not match any primer
  -s, --strict-mode            strict mode, discarding seqs not fully matching given region range
```

### `fish`

```
look for short sequences in larger sequences using local alignment

Attention:
  1. output coordinates are BED-like 0-based, left-close and right-open.
  2. alignment information are printed to STDERR.

Usage:
  seqkit fish [flags] 

Flags:
  -a, --all                      search all
  -p, --aln-params string        alignment parameters "<match>,<mismatch>,<gap_open>,<gap_extend>" (default "4,-4,-2,-1")
  -h, --help                     help for fish
  -i, --invert                   print out references not matching with any query
  -q, --min-qual float           minimum mapping quality (default 5)
  -b, --out-bam string           save alignments to this BAM file (memory intensive)
  -x, --pass                     pass through mode (write input to stdout)
  -g, --print-aln                print sequence alignments
  -D, --print-desc               print full sequence header
  -f, --query-fastx string       query fasta
  -F, --query-sequences string   query sequences
  -r, --ranges string            target ranges, for example: ":10,30:40,-20:"
  -s, --stranded                 search + strand only
  -v, --validate-seq             validate bases according to the alphabet
```

### `grep`

```
search sequences by ID/name/sequence/sequence motifs, mismatch allowed

Attention:
  0. By default, match sequence ID with patterns; use "-n/--by-name" for full name matching.
  1. We compare the pattern to the whole target (ID/full header) by default.
     Use "-r/--use-regexp" for partial matching.
  2. When searching by sequences, both positive and negative strands are searched.
  3. Degenerate bases/residues are supported with flag -d.
  4. Use double quotation marks for patterns containing comma: -p '"A{2,}"'
  5. Order of sequences in result is consistent with that in original file.

Usage:
  seqkit grep [flags] 

Flags:
  -D, --allow-duplicated-patterns   output records multiple times when duplicated patterns are given
  -n, --by-name                     match by full name instead of just ID
  -s, --by-seq                      search subseq on seq (both strands by default)
  -c, --circular                    circular genome
  -C, --count                       just print a count of matching records
  -d, --degenerate                  pattern/motif contains degenerate base
      --delete-matched              delete a pattern right after being matched
  -h, --help                        help for grep
  -i, --ignore-case                 ignore case
  -I, --immediate-output            print output immediately
  -v, --invert-match                invert the sense of matching
  -m, --max-mismatch int            max mismatch when matching by seq
  -P, --only-positive-strand        only search on the positive strand
  -p, --pattern strings             search pattern (multiple values supported)
  -f, --pattern-file string         pattern file (one record per line)
  -R, --region string               specify sequence region for searching, e.g 1:12
  -r, --use-regexp                  patterns are regular expression
```

### `locate`

```
locate subsequences/motifs, mismatch allowed

Attention:
  1. Motifs can be plain sequence OR regular expression.
  2. Degenerate bases/residues like "RYMM.." are supported with flag -d.
  3. Use double quotation marks for patterns containing comma: -p '"A{2,}"'
  4. Mismatch is allowed using flag "-m/--max-mismatch".

Usage:
  seqkit locate [flags] 

Flags:
      --bed                    output in BED6 format
  -c, --circular               circular genome
  -d, --degenerate             pattern/motif contains degenerate base
      --gtf                    output in GTF format
  -h, --help                   help for locate
  -M, --hide-matched           do not show matched sequences
  -i, --ignore-case            ignore case
  -I, --immediate-output       print output immediately
  -s, --max-len-to-show int    show at most X characters for the search pattern or matched sequences
  -m, --max-mismatch int       max mismatch when matching by seq
  -G, --non-greedy             non-greedy mode, faster but may miss overlapping motifs
  -P, --only-positive-strand   only search on positive strand
  -p, --pattern strings        pattern/motif (multiple values supported)
  -f, --pattern-file string    pattern/motif file (FASTA format)
  -F, --use-fmi                use FM-index for much faster search of lots of sequence patterns
  -r, --use-regexp             patterns/motifs are regular expression
```

---

## Set Operations

### `common`

```
find common/shared sequences of multiple files by id/name/sequence

Usage:
  seqkit common [flags] 

Flags:
  -n, --by-name                match by full name instead of just id
  -s, --by-seq                 match by sequence (both strands compared by default)
  -e, --check-embedded-seqs    check embedded sequences
  -h, --help                   help for common
  -i, --ignore-case            ignore case
  -P, --only-positive-strand   only considering the positive strand when comparing by sequence
```

### `duplicate`

```
duplicate sequences N times

Usage:
  seqkit duplicate [flags] 

Aliases:
  duplicate, dup

Flags:
  -h, --help        help for duplicate
  -n, --times int   duplication number (default 1)
```

### `head`

```
print the first N FASTA/Q records, or leading records whose total length >= L

For last N records: seqkit range -r -N:-1 seqs.fasta

Usage:
  seqkit head [flags] 

Flags:
  -h, --help            help for head
  -l, --length string   print leading records whose total sequence length >= L (supports K/M/G suffix)
  -n, --number int      print the first N FASTA/Q records (default 10)
```

### `head-genome`

```
print sequences of the first genome with common prefixes in name

Useful for FASTA files with multiple strains where descriptions share a common prefix.

Usage:
  seqkit head-genome [flags] 

Flags:
  -h, --help                    help for head-genome
  -m, --mini-common-words int   minimal shared prefix words (default 1)
```

### `pair`

```
match up paired-end reads from two fastq files

Attention:
1. Orders of headers in the two files should be the same (not shuffled).
2. Unpaired reads are optional outputted with -u/--save-unpaired.
3. If -O/--out-dir is not given, output saved in same directory as input with "paired" suffix.

Usage:
  seqkit pair [flags] 

Flags:
  -f, --force            overwrite output directory
  -h, --help             help for pair
  -O, --out-dir string   output directory
  -1, --read1 string     (gzipped) read1 file
  -2, --read2 string     (gzipped) read2 file
  -u, --save-unpaired    save unpaired reads if there are
```

### `range`

```
print FASTA/Q records in a range (start:end)

Examples:
  1:100   = first 100 (head -n 100)
  -100:-1 = last 100 (tail -n 100)
  101:-1  = remove first 100 (tail -n +101)

Usage:
  seqkit range [flags] 

Flags:
  -h, --help           help for range
  -r, --range string   range. e.g., 1:100 (head -n 100), -100:-1 (tail -n 100)
```

### `rmdup`

```
remove duplicated sequences by ID/name/sequence

Attention:
  1. When comparing by sequences, both positive and negative strands are compared.
  2. Only the first record is saved for duplicates.

Usage:
  seqkit rmdup [flags] 

Flags:
  -n, --by-name                by full name instead of just id
  -s, --by-seq                 by seq
  -D, --dup-num-file string    file to save numbers and ID lists of duplicated seqs
  -d, --dup-seqs-file string   file to save duplicated seqs
  -h, --help                   help for rmdup
  -i, --ignore-case            ignore case
  -P, --only-positive-strand   only considering positive strand when comparing by sequence
```

### `sample`

```
sample sequences by number or proportion.

Attention:
1. Do not use '-n' on large FASTQ files, it loads all seqs into memory!
   Use 'seqkit sample -p 0.1 seqs.fq.gz | seqkit head -n N' instead!
2. See also 'seqkit sample2' for more accurate and memory efficient sampling.

Usage:
  seqkit sample [flags] 

Flags:
  -h, --help                help for sample
  -r, --non-deterministic   use a time-based seed for truly random results
  -n, --number int          sample by number (result may not exactly match). DO NOT use on large FASTQ.
  -p, --proportion float    sample by proportion
  -s, --rand-seed int       random seed (default 11)
  -2, --two-pass            2-pass mode read files twice to lower memory usage
```

### `sample2`

```
sample sequences by number or proportion (version 2).

Provides unbiased, fixed-size sampling with controlled memory usage.
Guarantees exact target count. More memory efficient than 'seqkit sample'.

Attention:
1. '-n' SHOULD BE coupled with 2-pass mode (-2) when large FASTQ files.

Usage:
  seqkit sample2 [flags] 

Flags:
  -h, --help                help for sample2
  -r, --non-deterministic   use a time-based seed for truly random results
  -n, --number int          sample by number. SHOULD BE coupled with -2 flag for large files.
  -p, --proportion float    sample by proportion
  -s, --rand-seed int       random seed (default 11)
  -2, --two-pass            2-pass mode read files twice to lower memory usage
```

### `split`

```
split sequences into files by name ID, subsequence of given region, part size or number of parts.

For splitting by parts or sizes only, use 'seqkit split2' (also supports paired FASTQ).

Usage:
  seqkit split [flags] 

Flags:
  -i, --by-id                     split sequences according to sequence ID
      --by-id-prefix string       file prefix for --by-id
  -p, --by-part int               split sequences into N parts
      --by-part-prefix string     file prefix for --by-part
  -r, --by-region string          split sequences according to subsequence of given region
      --by-region-prefix string   file prefix for --by-region
  -s, --by-size int               split sequences into multi parts with N sequences
      --by-size-prefix string     file prefix for --by-size
  -d, --dry-run                   dry run, just print message and no files will be created
  -e, --extension string          set output file extension, e.g., ".gz", ".xz", or ".zst"
  -f, --force                     overwrite output directory
  -h, --help                      help for split
  -I, --ignore-case               ignore case when using -i/--by-id
  -k, --keep-temp                 keep temporary FASTA and .fai file when using 2-pass mode
  -O, --out-dir string            output directory (default value is $infile.split)
  -P, --out-prefix string         file prefix (overrides --by-*-prefix)
  -2, --two-pass                  two-pass mode (only for FASTA format)
  -U, --update-faidx              update the fasta index file if it exists
```

### `split2`

```
split sequences into files by part size or number of parts

Supports FASTA and paired- or single-end FASTQ with low memory usage.

Usage:
  seqkit split2 [flags] 

Flags:
  -l, --by-length string          split sequences into chunks of >=N bases (supports K/M/G suffix)
      --by-length-prefix string   file prefix for --by-length
  -p, --by-part int               split sequences into N parts (round robin distribution)
      --by-part-prefix string     file prefix for --by-part
  -s, --by-size int               split sequences into multi parts with N sequences
      --by-size-prefix string     file prefix for --by-size
  -e, --extension string          set output file extension, e.g., ".gz", ".xz", or ".zst"
  -f, --force                     overwrite output directory
  -h, --help                      help for split2
  -O, --out-dir string            output directory (default value is $infile.split)
  -P, --out-prefix string         file prefix (overrides --by-*-prefix)
  -1, --read1 string              (gzipped) read1 file
  -2, --read2 string              (gzipped) read2 file
  -N, --seqid-as-filename         use the first sequence ID as the file name
```

---

## Edit

### `concat`

```
concatenate sequences with same ID from multiple files

Attention:
  1. By default, only sequences with IDs in all files are outputted.
     Use -f/--full to output all sequences.
  2. If there are multiple sequences of the same ID, we output the Cartesian product.
  3. Descriptions are also concatenated with a separator (-s/--separator).

Usage:
  seqkit concat [flags] 

Aliases:
  concat, concate

Flags:
  -F, --fill string        fill with N bases/residues for IDs missing in some files when using -f/--full
  -f, --full               keep all sequences, like full/outer join
  -h, --help               help for concat
  -s, --separator string   separator for descriptions of records with the same ID (default "|")
```

### `mutate`

```
edit sequence (point mutation, insertion, deletion)

Attention:
  1. Multiple point mutations (-p/--point) are allowed, but only single insertion OR deletion.
  2. Point mutation takes place before insertion/deletion.

Position is 1-based. 1:2 = first 2, -3:-1 = last 3.

Usage:
  seqkit mutate [flags] 

Flags:
  -n, --by-name               [match seqs to mutate] match by full name instead of just id
  -d, --deletion string       deletion: deleting subsequence in a range. e.g., -d 1:2 for leading two bases
  -h, --help                  help for mutate
  -I, --ignore-case           [match seqs to mutate] ignore case of search pattern
  -i, --insertion string      insertion: inserting bases behind of given position, e.g., -i 0:ACGT for inserting at the beginning
  -v, --invert-match          [match seqs to mutate] invert the sense of matching
  -s, --pattern strings       [match seqs to mutate] search pattern (multiple values supported)
  -f, --pattern-file string   [match seqs to mutate] pattern file (one record per line)
  -p, --point strings         point mutation: changing base at given position. e.g., -p 2:C
  -r, --use-regexp            [match seqs to mutate] search patterns are regular expression
```

### `rename`

```
rename duplicated IDs

Attention:
  1. This command only appends "_N" to duplicated sequence IDs to make them unique.
  2. Use "seqkit replace" for editing sequence IDs/headers using regular expression.

Usage:
  seqkit rename [flags] 

Flags:
  -n, --by-name             check duplication by full name instead of just id
  -f, --force               overwrite output directory
  -h, --help                help for rename
  -m, --multiple-outfiles   write results into separated files for multiple input files
  -O, --out-dir string      output directory (default "renamed")
  -1, --rename-1st-rec      rename the first record as well
  -s, --separator string    separator between original ID/name and the counter (default "_")
  -N, --start-num int       starting count number for *duplicated* IDs/names (default 2)
```

### `replace`

```
replace name/sequence by regular expression.

Note that the replacement supports capture variables.
ATTENTION: use SINGLE quote NOT double quotes in *nix OS.

Special replacement symbols (for name, not sequence):
  {nr}    Record number, starting from 1
  {uuid}  Random 16-character UUID
  {fn}    File name
  {fbn}   File base name
  {fbne}  File base name without any extension
  {kv}    Value from key-value file (captured variable $n)

Usage:
  seqkit replace [flags] 

Flags:
  -s, --by-seq                   replace seq (only FASTA)
      --f-by-name                [target filter] match by full name instead of just ID
      --f-by-seq                 [target filter] search subseq on seq
      --f-ignore-case            [target filter] ignore case
      --f-invert-match           [target filter] invert the sense of matching
      --f-only-positive-strand   [target filter] only search on positive strand
      --f-pattern strings        [target filter] search pattern
      --f-pattern-file string    [target filter] pattern file
      --f-use-regexp             [target filter] patterns are regular expression
  -h, --help                     help for replace
  -i, --ignore-case              ignore case
  -K, --keep-key                 keep the key as value when no value found for the key
  -U, --keep-untouch             do not change anything when no value found for the key
  -I, --key-capt-idx int         capture variable index of key (1-based) (default 1)
  -m, --key-miss-repl string     replacement for key with no corresponding value
  -k, --kv-file string           tab-delimited key-value file for replacing key with value when using "{kv}"
      --nr-width int             minimum width for {nr} (default 1)
  -p, --pattern string           search regular expression
  -r, --replacement string       replacement (supports capture variables, {nr}, {fn})
```

### `restart`

```
reset start position (rotate) for circular genomes

Usage:
  seqkit restart [flags] 

Aliases:
  restart, rotate

Flags:
  -h, --help                help for restart
  -I, --ignore-case         ignore case when searching the custom starting subsequence
  -m, --max-mismatch int    max mismatch when searching the custom starting subsequence
  -i, --new-start int       new start position (1-based, negative counts from end) (default 1)
  -s, --start-with string   rotate the genome to make it starting with the given subsequence
```

### `sana`

```
sanitize broken single line FASTQ files

Sana is a resilient FASTQ/FASTA parser that skips malformed records and continues.
Supports only single-line per sequence/quality FASTQ dialect.

Usage:
  seqkit sana [flags] 

Flags:
  -A, --allow-gaps            allow gap character (-) in sequences
  -i, --format string         input and output format: fastq or fasta (default "fastq")
  -h, --help                  help for sana
  -I, --in-format string      input format: fastq or fasta
  -O, --out-format string     output format: fastq or fasta
  -b, --qual-ascii-base int   ASCII BASE, 33 for Phred+33 (default 33)
```

---

## Ordering

### `shuffle`

```
shuffle sequences.

By default, all records will be read into memory.
For FASTA format, use flag -2 (--two-pass) to reduce memory usage. FASTQ not supported in 2-pass mode.

Usage:
  seqkit shuffle [flags] 

Flags:
  -h, --help                help for shuffle
  -k, --keep-temp           keep temporary FASTA and .fai file when using 2-pass mode
  -r, --non-deterministic   use a time-based seed for truly random results
  -s, --rand-seed int       rand seed for shuffle (default 23)
      --tmp-dir string      tmp directory for saving temporary FASTA and .fai file (default "./")
  -2, --two-pass            two-pass mode read files twice to lower memory usage (only for FASTA format)
  -U, --update-faidx        update the fasta index file if it exists
```

### `sort`

```
sort sequences by id/name/sequence/length.

By default, all records will be read into memory.
For FASTA format, use flag -2 (--two-pass) to reduce memory usage. FASTQ not supported.

Usage:
  seqkit sort [flags] 

Flags:
  -b, --by-bases                by non-gap bases
  -l, --by-length               by sequence length
  -n, --by-name                 by full name instead of just id
  -s, --by-seq                  by sequence
  -G, --gap-letters string      gap letters (default "- \t.")
  -h, --help                    help for sort
  -i, --ignore-case             ignore case
  -k, --keep-temp               keep temporary FASTA and .fai file when using 2-pass mode
  -N, --natural-order           sort in natural order, when sorting by IDs/full name
  -r, --reverse                 reverse the result
  -L, --seq-prefix-length int   length of sequence prefix on which seqkit sorts by sequences (default 10000)
  -2, --two-pass                two-pass mode (only for FASTA format)
  -U, --update-faidx            update the fasta index file if it exists
```

---

## BAM Processing

### `bam`

```
monitoring and online histograms of BAM record features

Usage:
  seqkit bam [flags] 

Flags:
  -B, --bins int             number of histogram bins (default -1)
  -N, --bundle int           partition BAM file into loci (-1) or bundles with this minimum size
  -c, --count string         count reads per reference and save to this file
  -W, --delay int            sleep this many seconds after plotting (default 1)
  -y, --dump                 print histogram data to stderr instead of plotting
  -G, --exclude-ids string   exclude records with IDs contained in this file
  -e, --exec-after string    execute command after reporting
  -E, --exec-before string   execute command before reporting
  -f, --field string         target fields
  -g, --grep-ids string      only keep records with IDs contained in this file
  -h, --help                 help for bam
  -C, --idx-count            fast read per reference counting based on the BAM index
  -i, --idx-stat             fast statistics based on the BAM index
  -O, --img string           save histogram to this PDF/image file
  -H, --list-fields          list all available BAM record features
  -L, --log                  log10(x+1) transform numeric values
  -q, --map-qual int         minimum mapping quality
  -x, --pass                 passthrough mode (forward filtered BAM to output)
  -k, --pretty               pretty print certain TSV outputs
  -F, --prim-only            filter out non-primary alignment records
  -p, --print-freq int       print/report after this many records (default -1)
  -Q, --quiet-mode           supress all plotting to stderr
  -M, --range-max float      discard record with field (-f) value greater than this flag (default NaN)
  -m, --range-min float      discard record with field (-f) value less than this flag (default NaN)
  -R, --reset                reset histogram after every report
  -Z, --silent-mode          supress TSV output to stderr
  -s, --stat                 print BAM statistics of the input files
  -T, --tool string          invoke toolbox in YAML format
```

---

## Miscellaneous

### `merge-slides`

```
merge sliding windows generated from seqkit sliding

Merges overlapping/adjacent windows from seqkit sliding output into BED3 format.

Usage:
  seqkit merge-slides [flags] 

Flags:
  -b, --buffer-size string            size of buffer (default "1G")
  -p, --comment-line-prefix strings   comment line prefix (default [#,//])
  -h, --help                          help for merge-slides
  -g, --max-gap int                   maximum distance of starting positions of two adjacent regions (0 for no limit)
  -l, --min-overlap int               minimum overlap of two adjacent regions (default 1)
  -r, --regexp string                 regular expression for extract the reference name and window position
                                      (default "^(.+)_sliding:(\\d+)\\-(\\d+)")
```

### `sum`

```
compute message digest for all sequences in FASTA/Q files

Attention:
  1. Sequence headers and qualities are skipped, only sequences matter.
  2. The order of sequences records does not matter.
  3. Circular complete genomes are supported with -c/--circular.

Method: xxhash of sequences/k-mers -> sorted -> MD5 digest.
Format: seqkit.<version>_<seq type><seq structure><strand>_<kmer size>_<seq digest>

Usage:
  seqkit sum [flags] 

Flags:
  -a, --all                  show all information, including sequences length and number
  -b, --basename             only output basename of files
  -c, --circular             the file contains a single circular genome sequence
  -G, --gap-letters string   gap letters to delete with -g/--remove-gaps (default "- \t.*")
  -h, --help                 help for sum
  -k, --kmer-size int        k-mer size for processing circular genomes (default 1000)
  -g, --remove-gaps          remove gap characters set in -G/gap-letters
      --rna2dna              convert RNA to DNA
  -s, --single-strand        only consider the positive strand of a circular genome
```
