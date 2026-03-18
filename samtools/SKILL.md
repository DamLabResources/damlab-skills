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
conda run -n damlab-skill-samtools samtools <subcommand> [options]
```

## Common patterns

**Sort + index (most common starting point):**
```bash
conda run -n damlab-skill-samtools samtools sort -@ 8 -o sorted.bam input.bam
conda run -n damlab-skill-samtools samtools index sorted.bam
```

**Quick alignment QC:**
```bash
conda run -n damlab-skill-samtools samtools flagstat input.bam
conda run -n damlab-skill-samtools samtools stats input.bam | grep ^SN | cut -f2-
```

**Filter reads (mapped only, min MAPQ 20):**
```bash
conda run -n damlab-skill-samtools samtools view -b -F 4 -q 20 -o filtered.bam input.bam
conda run -n damlab-skill-samtools samtools index filtered.bam
```

**Mark duplicates:**
```bash
conda run -n damlab-skill-samtools samtools sort -n -@ 8 -o namesorted.bam input.bam
conda run -n damlab-skill-samtools samtools fixmate -m namesorted.bam fixmate.bam
conda run -n damlab-skill-samtools samtools sort -@ 8 -o coordsorted.bam fixmate.bam
conda run -n damlab-skill-samtools samtools markdup coordsorted.bam markdup.bam
conda run -n damlab-skill-samtools samtools index markdup.bam
```

**Convert BAM to FASTQ (paired-end):**
```bash
conda run -n damlab-skill-samtools samtools collate -u -O input.bam \
  | conda run -n damlab-skill-samtools samtools fastq \
      -1 R1.fq.gz -2 R2.fq.gz -0 /dev/null -s /dev/null -n
```

**Index reference FASTA:**
```bash
conda run -n damlab-skill-samtools samtools faidx reference.fa
# Extract region:
conda run -n damlab-skill-samtools samtools faidx reference.fa chr1:1000-2000
```

**Coverage per position:**
```bash
conda run -n damlab-skill-samtools samtools depth -a input.bam > depth.tsv
conda run -n damlab-skill-samtools samtools coverage input.bam
```

## Piping with other tools

samtools works well in pipes. Use `bash -c` with `conda run`:
```bash
conda run -n damlab-skill-samtools bash -c \
  "samtools view -bS -@ 4 input.sam | samtools sort -@ 4 -o sorted.bam"
```

## Additional reference

Full subcommand reference with all flags: [reference.md](reference.md)
