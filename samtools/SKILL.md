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

```bash
SAMTOOLS=~/.cursor/skills/samtools/bin/samtools
```

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

## Additional reference

Full subcommand reference with all flags: [reference.md](reference.md)
