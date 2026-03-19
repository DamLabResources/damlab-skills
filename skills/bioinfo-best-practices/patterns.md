# Bioinformatics Best Practices — Patterns

Reusable patterns collected from real analysis and debugging sessions.
Each entry has a title, context, and runnable example.

<!-- Add patterns below as they arise -->

### Downsample a FASTQ for rapid debugging

**Context:** Input FASTQ is too large to iterate on quickly; reproduce the
problem with a 1% subsample before running the full pipeline.

```bash
seqkit sample -p 0.01 -s 42 input.fastq.gz -o debug_1pct.fastq.gz
```

---

### Downsample a BAM for rapid debugging

**Context:** Alignment file is large; test a pipeline change on a small slice.

```bash
samtools view -s 42.01 -b input.bam -o debug_1pct.bam && samtools index debug_1pct.bam
```

(`42.01` = random seed 42, fraction 0.01)

---

### Quick read-count and length stats without printing sequences

**Context:** First look at a FASTQ file — how many reads, what length distribution?

```bash
seqkit stats -a input.fastq.gz
```

---

### Check alignment quality at a glance

**Context:** Just received a BAM; want a one-line QC summary before diving deeper.

```bash
samtools flagstat input.bam
```

---

### Inspect first N alignments without printing sequences

**Context:** Want to see CIGAR strings, flags, or tags but not the read sequence
(which can flood the context window).

```bash
samtools view input.bam | head -n 10 | cut -f1-12
```

---

### Seed a project log

**Context:** Starting a new analysis session — create the tracking document.

```bash
cat > project_name.md << 'EOF'
# Project Name

**Date:** $(date +%Y-%m-%d)
**Goal:** <one-sentence goal>
**Data:** <path>
**Reference:** <path or accession>

## File inventory

| File | Description | Size |
|------|-------------|------|

## Log

### $(date +%Y-%m-%d) — Session start
- Goal confirmed with user:
EOF
```

---

### Count variant types without printing all records

**Context:** VCF has been produced; want a summary of SNP/indel counts before
any downstream analysis.

```bash
bcftools stats input.vcf.gz | grep "^SN"
```

---

### Extract a small genomic region for debugging

**Context:** A problem appears genome-wide but can be reproduced in one region;
create a small BAM for human review.

```bash
samtools view -b input.bam chr1:1000000-1100000 -o debug_region.bam
samtools index debug_region.bam
```
