---
name: seqkit
description: Manipulate FASTA and FASTQ files using seqkit. Use when working with
  sequence files, getting sequence statistics, filtering by length or quality, searching
  by ID or motif, converting between FASTA and FASTQ, subsampling reads, extracting
  subsequences, splitting files, or reverse complementing sequences. Triggers on tasks
  involving .fa, .fasta, .fq, .fastq files, sequence QC, read filtering, or FASTA/FASTQ
  format conversion.
---

# seqkit

## Environment

```bash
SEQKIT=~/.cursor/skills/seqkit/bin/seqkit
```

Supports gzip (.gz), xz (.xz), zstd (.zst), and bzip2 (.bz2) input/output natively.

## Common patterns

**File statistics (read count, length distribution, GC content):**
```bash
$SEQKIT stats -a input.fq.gz
# -a includes N50, Q20/Q30% for FASTQ; use for multiple files:
$SEQKIT stats -a *.fq.gz
```

**Filter reads by length:**
```bash
# Keep reads >= 1000 bp
$SEQKIT seq -m 1000 input.fq.gz -o filtered.fq.gz
# Keep reads between 500 and 5000 bp
$SEQKIT seq -m 500 -M 5000 input.fq.gz -o filtered.fq.gz
```

**Convert FASTQ to FASTA:**
```bash
$SEQKIT fq2fa input.fq.gz -o output.fa.gz
```

**Grep sequences by ID list:**
```bash
# ids.txt: one ID per line
$SEQKIT grep -f ids.txt input.fa.gz -o subset.fa.gz
# By pattern (regex):
$SEQKIT grep -r -p "^contig_[0-9]+" input.fa -o contigs.fa
```

**Random subsample:**
```bash
# By count:
$SEQKIT sample -n 10000 -s 42 input.fq.gz -o sampled.fq.gz
# By proportion:
$SEQKIT sample -p 0.1 -s 42 input.fq.gz -o sampled.fq.gz
```

**Extract subsequences by region:**
```bash
# BED-based:
$SEQKIT subseq --bed regions.bed genome.fa -o regions.fa
# By coordinate (1-based):
$SEQKIT subseq -r 100:200 input.fa
```

**Reverse complement:**
```bash
$SEQKIT seq -r -p input.fa -o revcomp.fa
# -r: reverse complement; -p alone: complement only; -r alone: reverse only
```

**Split paired-end FASTQ into per-file chunks:**
```bash
$SEQKIT split2 -1 R1.fq.gz -2 R2.fq.gz -s 1000000 -O split_out/
```

**Remove duplicate sequences:**
```bash
$SEQKIT rmdup -s input.fa -o deduped.fa
# -s: by sequence; default is by ID
```

## Piping

seqkit reads/writes stdin/stdout cleanly:
```bash
$SEQKIT seq -m 1000 input.fq.gz | $SEQKIT sample -n 5000 -s 1 > sampled_long.fq
```

## Additional reference

Full subcommand reference: [reference.md](reference.md)
