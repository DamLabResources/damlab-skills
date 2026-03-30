---
name: samtools
description: Manipulate SAM/BAM/CRAM alignment files using samtools. Use when working
  with alignment files, sorting or indexing BAMs, filtering reads, computing alignment
  statistics, marking duplicates, converting BAM to FASTQ/FASTA, or indexing reference
  FASTA files. Triggers on tasks involving .bam, .sam, .cram, flagstat, pileup, coverage,
  read depth, or alignment QC.
---

# samtools

## Environment

Binary: `bin/samtools` — relative to this skill directory.

Before issuing any commands, resolve the full absolute path for this machine:
```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/bin/samtools"
```
Substitute `<path-to-this-SKILL.md>` with the absolute path you used to read this file.
Use the printed output literally as the first token in every command.
In examples below, `$SAMTOOLS` is a readable placeholder for that resolved path.

## Subcommands

**Indexing**
- `dict` — create a sequence dictionary (.dict) from a FASTA
- `faidx` — index FASTA (creates .fai) and/or extract subsequences by region
- `fqidx` — index FASTQ for random access
- `index` — index a coordinate-sorted BAM/CRAM (BAI or CSI format)

**Editing**
- `calmd` — recalculate MD/NM tags and optionally '=' bases
- `fixmate` — fill in mate information (run after `sort -n`; use `-m` for markdup compatibility)
- `reheader` — replace BAM/CRAM header in-place or via external command
- `targetcut` — cut fosmid regions (fosmid pool only)
- `addreplacerg` — add or replace `@RG` header lines and RG tags on reads
- `markdup` — mark or remove PCR/optical duplicate reads (requires fixmate -m + coord sort)
- `ampliconclip` — soft- or hard-clip amplicon primer sequences from reads

**File Operations**
- `collate` — shuffle alignments so read pairs are adjacent (required before `fastq` for PE)
- `cat` — concatenate BAMs/CRAMs without re-sorting (headers must be compatible)
- `consensus` — generate consensus FASTA/FASTQ/pileup from aligned reads (simple or Bayesian)
- `merge` — merge multiple sorted BAMs/CRAMs into one
- `mpileup` — multi-way pileup for variant calling (use bcftools for BCF/VCF output)
- `sort` — sort alignments by coordinate, name, or TAG
- `split` — split BAM by read group or TAG value
- `quickcheck` — verify BAM/CRAM is not truncated or corrupt
- `fastq` — convert BAM to FASTQ (supports paired-end splitting)
- `fasta` — convert BAM to FASTA
- `import` — convert FASTA/FASTQ to SAM/BAM/CRAM
- `reference` — generate a reference FASTA from aligned CRAM data
- `reset` — revert aligner changes in reads (strips alignment information)

**Statistics**
- `bedcov` — total read depth per BED region
- `coverage` — per-reference coverage summary table or histogram
- `depth` — per-position read depth (one line per position)
- `flagstat` — summary alignment statistics (mapped, paired, duplicates, etc.)
- `idxstats` — per-reference mapped/unmapped read counts (requires index)
- `cram-size` — list CRAM Content-ID and Data-Series sizes
- `phase` — phase heterozygous SNPs
- `stats` — detailed statistics for plot-bamstats visualization
- `ampliconstats` — generate amplicon-specific stats from a primers BED file
- `checksum` — produce order-agnostic checksums of sequence content

**Viewing**
- `flags` — convert between numeric and textual BAM flag representations
- `head` — display SAM header and/or first N alignment records
- `tview` — interactive text alignment viewer in terminal
- `view` — filter, convert, and subset SAM/BAM/CRAM; supports all flag, region, tag, and expression filters
- `depad` — convert padded BAM to unpadded BAM
- `samples` — list the samples present in a set of SAM/BAM/CRAM files

## Common patterns

**Sort + index (most common starting point):**
```bash
$SAMTOOLS sort -@ 8 -o sorted.bam input.bam
$SAMTOOLS index sorted.bam
```

**Quick alignment QC:**
```bash
$SAMTOOLS flagstat input.bam
$SAMTOOLS stats input.bam | grep ^SN | cut -f2-
```

**Filter reads (mapped only, min MAPQ 20):**
```bash
$SAMTOOLS view -b -F 4 -q 20 -o filtered.bam input.bam
$SAMTOOLS index filtered.bam
```

**Mark duplicates:**
```bash
$SAMTOOLS sort -n -@ 8 -o namesorted.bam input.bam
$SAMTOOLS fixmate -m namesorted.bam fixmate.bam
$SAMTOOLS sort -@ 8 -o coordsorted.bam fixmate.bam
$SAMTOOLS markdup coordsorted.bam markdup.bam
$SAMTOOLS index markdup.bam
```

**Convert BAM to FASTQ (paired-end):**
```bash
$SAMTOOLS collate -u -O input.bam \
  | $SAMTOOLS fastq -1 R1.fq.gz -2 R2.fq.gz -0 /dev/null -s /dev/null -n
```

**Index reference FASTA:**
```bash
$SAMTOOLS faidx reference.fa
# Extract region:
$SAMTOOLS faidx reference.fa chr1:1000-2000
```

**Coverage per position:**
```bash
$SAMTOOLS depth -a input.bam > depth.tsv
$SAMTOOLS coverage input.bam
```

## Piping with other tools

samtools reads/writes stdin/stdout and pipes cleanly with other tools:
```bash
$SAMTOOLS view -bS -@ 4 input.sam | $SAMTOOLS sort -@ 4 -o sorted.bam
```

## Allowlist entries

Resolve and add to your terminal command allowlist (Cursor: Settings → Features → Terminal):
```bash
readlink -f "$(dirname <path-to-this-SKILL.md>)/bin/samtools"
```

## Full flag reference

To look up all flags for a specific subcommand:
```bash
grep -A 80 "^### \`subcommand\`" "$(dirname <path-to-this-SKILL.md>)/reference.md"
```
Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
```bash
grep -A 20 "keyword" "$(dirname <path-to-this-SKILL.md>)/patterns.md"
```
[patterns.md](patterns.md)
