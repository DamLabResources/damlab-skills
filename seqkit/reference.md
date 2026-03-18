# seqkit — Full Reference

Invoke all commands as: `conda run -n damlab-skill-seqkit seqkit <subcommand>`

## Global flags (apply to most subcommands)

| Flag | Description |
|---|---|
| `-j INT` | Threads (default 4; or set `SEQKIT_THREADS`) |
| `-o FILE` | Output file (default stdout; `.gz` suffix auto-compresses) |
| `--quiet` | Suppress progress/info messages |
| `-t TYPE` | Sequence type: `dna`, `rna`, `protein`, `auto` (default auto) |
| `-w INT` | Line width for FASTA output (0 = no wrap, default 60) |

---

## Statistics & QC

### `stats`
Summary statistics for one or more FASTA/FASTQ files.
```bash
seqkit stats [-a] [-T] [-G CHAR] file(s)
```
| Flag | Description |
|---|---|
| `-a` | All stats: N50, Q20/Q30, GC%, min/max/mean length |
| `-T` | Tabular (TSV) output |
| `-G CHAR` | Gap character for gap counting (default `-`) |

### `watch`
Online histogram of sequence features while streaming.
```bash
seqkit watch -f ReadLen input.fq
```

---

## Sequence transformation

### `seq`
Transform sequences: filter length, reverse complement, mask, extract IDs.
```bash
seqkit seq [options] input
```
| Flag | Description |
|---|---|
| `-m INT` | Min sequence length |
| `-M INT` | Max sequence length |
| `-r` | Reverse complement |
| `-p` | Complement only |
| `-R` | Reverse only |
| `-l` | Lowercase sequences |
| `-u` | Uppercase sequences |
| `-g` | Remove gaps |
| `-n` | Only print sequence names/IDs |
| `-s` | Only print sequences |
| `-q` | Only print quality scores |
| `--min-qual FLOAT` | Min average quality (FASTQ) |
| `--max-qual FLOAT` | Max average quality (FASTQ) |
| `--qual-encoding STR` | `sanger`, `solexa`, `illumina-1.3+`, `illumina-1.5+` |

### `translate`
Translate DNA/RNA to protein.
```bash
seqkit translate [-f INT] input.fa
```
`-f`: frame (1, 2, 3, -1, -2, -3, or 6 for all frames).

### `mutate`
Point mutations, insertions, deletions.
```bash
seqkit mutate --point-mutation 10:A>T input.fa
seqkit mutate --insertion 10:ATG input.fa
seqkit mutate --deletion 10:3 input.fa
```

---

## Searching & filtering

### `grep`
Search by ID, name, or sequence motif.
```bash
seqkit grep [-n] [-s] [-r] [-p PATTERN] [-f FILE] input
```
| Flag | Description |
|---|---|
| `-p STR` | Pattern (can repeat) |
| `-f FILE` | File of patterns (one per line) |
| `-r` | Use regex patterns |
| `-n` | Match by full name (not just ID) |
| `-s` | Search in sequence (not ID) |
| `-m INT` | Mismatches allowed (sequence search) |
| `-v` | Invert match |
| `-i` | Case-insensitive |

### `locate`
Find subsequence/motif positions.
```bash
seqkit locate -p ATCG [-r] [-m INT] input.fa
```

### `fish`
Short sequence lookup using local alignment.
```bash
seqkit fish -p query.fa input.fa
```

### `common`
Find sequences common to multiple files (by ID or sequence).
```bash
seqkit common file1.fa file2.fa -o common.fa
seqkit common -s file1.fa file2.fa    # by sequence
```

---

## Format conversion

### `fq2fa`
FASTQ → FASTA (drops quality scores).
```bash
seqkit fq2fa input.fq.gz -o output.fa.gz
```

### `fa2fq`
Retrieve FASTQ records matching a FASTA file (by ID).
```bash
seqkit fa2fq input.fa reads.fq.gz -o matched.fq.gz
```

### `convert`
Convert FASTQ quality encoding.
```bash
seqkit convert --from sanger --to illumina-1.8 input.fq -o converted.fq
```

### `fx2tab`
FASTA/FASTQ → tabular (useful for awk/csvtk post-processing).
```bash
seqkit fx2tab [-n] [-l] [-g] [-q] [-Q] input
```
| Flag | Description |
|---|---|
| `-n` | Print name only (no sequence) |
| `-l` | Append sequence length column |
| `-g` | Append GC content column |
| `-q` | Append mean quality column |
| `-Q` | Append base qualities |

### `tab2fx`
Tabular format → FASTA/FASTQ.
```bash
seqkit tab2fx input.tsv -o output.fa
```

---

## Sampling & splitting

### `sample`
Randomly subsample sequences.
```bash
seqkit sample -n INT -s INT input    # by count
seqkit sample -p FLOAT -s INT input  # by proportion
```
`-s`: random seed (for reproducibility).

### `head`
Print first N records.
```bash
seqkit head -n 100 input.fa
```

### `sort`
Sort by ID, name, sequence, or length.
```bash
seqkit sort [-n] [-l] [-s] [-r] input.fa
```
`-l`: by length; `-s`: by sequence; `-n`: by ID; `-r`: reverse.

### `shuffle`
Shuffle sequences randomly.
```bash
seqkit shuffle -s 42 input.fa -o shuffled.fa
```

### `split`
Split FASTA by ID, size, or parts (FASTA only).
```bash
seqkit split -i input.fa            # by ID (one file per sequence)
seqkit split -s 1000 input.fa       # 1000 seqs per file
seqkit split -p 4 input.fa          # 4 equal parts
```

### `split2`
Split FASTA/FASTQ (including paired-end) by size or parts.
```bash
seqkit split2 -s 1000000 input.fq.gz -O outdir/
seqkit split2 -1 R1.fq.gz -2 R2.fq.gz -s 1000000 -O outdir/
```

---

## Subsequence extraction

### `subseq`
Extract by region, GTF, or BED.
```bash
seqkit subseq -r 1:100 input.fa              # 1-based, inclusive
seqkit subseq --bed regions.bed genome.fa
seqkit subseq --gtf annotation.gtf --feature gene genome.fa
seqkit subseq -r 1:100 --up-stream 50 input.fa
```

### `sliding`
Extract overlapping sliding windows.
```bash
seqkit sliding -s 100 -W 200 input.fa    # step 100, window 200
```

### `amplicon`
Extract amplicon regions flanked by primers.
```bash
seqkit amplicon -F PRIMER_FWD -R PRIMER_REV input.fa
```

---

## Deduplication

### `rmdup`
Remove duplicate sequences.
```bash
seqkit rmdup [-s] [-n] input.fa -o deduped.fa
```
`-s`: by sequence; `-n`: by name; default by ID.

### `uniq`
Remove consecutive duplicates (requires sorted input).
```bash
seqkit sort -s input.fa | seqkit uniq -s -o deduped.fa
```

---

## Utilities

### `concat`
Concatenate sequences with the same ID from multiple files.
```bash
seqkit concat file1.fa file2.fa -o merged.fa
```

### `pair`
Match up paired-end reads from two FASTQ files.
```bash
seqkit pair -1 R1.fq.gz -2 R2.fq.gz -O paired_out/
```

### `sum`
Compute checksum of all sequences (for reproducibility verification).
```bash
seqkit sum input.fa
```

### `restart`
Reset start position for circular sequences.
```bash
seqkit restart -i 100 input.fa
```

### `sana`
Sanitize broken single-line FASTQ files.
```bash
seqkit sana input.fq -o fixed.fq
```

### `faidx`
Create FASTA index and extract subsequences (like samtools faidx).
```bash
seqkit faidx input.fa
seqkit faidx input.fa chr1:1-1000
```
