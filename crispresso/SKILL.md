---
name: crispresso
description: Analyze CRISPR genome editing outcomes from amplicon sequencing using
  the CRISPResso2 suite. Use when quantifying indels, substitutions, HDR, base editing
  conversions, or prime editing from FASTQ or BAM input. Covers CRISPResso (single
  amplicon), CRISPRessoBatch (multiple conditions via TSV), CRISPRessoPooled (multiple
  amplicons), CRISPRessoWGS (whole-genome sites), CRISPRessoCompare (treated vs
  control), and CRISPRessoAggregate (aggregating results). Triggers on: CRISPR
  editing analysis, indel quantification, HDR efficiency, base editor, prime editing,
  sgRNA, amplicon sequencing, NHEJ, genome editing outcomes.
---

# CRISPResso

## Environment

```bash
CRISPRESSO=~/.cursor/skills/crispresso/bin/CRISPResso
CRISPRESSO_BATCH=~/.cursor/skills/crispresso/bin/CRISPRessoBatch
CRISPRESSO_POOLED=~/.cursor/skills/crispresso/bin/CRISPRessoPooled
CRISPRESSO_COMPARE=~/.cursor/skills/crispresso/bin/CRISPRessoCompare
CRISPRESSO_WGS=~/.cursor/skills/crispresso/bin/CRISPRessoWGS
CRISPRESSO_AGGREGATE=~/.cursor/skills/crispresso/bin/CRISPRessoAggregate
```

## Tools

**Single-sample**
- `CRISPResso` — align reads to one amplicon; quantify indels, substitutions, HDR, base edits, prime edits

**Multi-sample**
- `CRISPRessoBatch` — run CRISPResso on many samples defined in a TSV batch file; generates cross-sample summary plots
- `CRISPRessoPooled` — process multiple amplicons from a single FASTQ (uses Bowtie2 to assign reads to amplicons)
- `CRISPRessoWGS` — analyze specific genomic sites from whole-genome sequencing BAM/FASTQ
- `CRISPRessoCompare` — compare editing outcomes between two CRISPResso runs (e.g. treated vs control)
- `CRISPRessoAggregate` — aggregate HTML reports from previously-run CRISPResso analyses into a single summary

## Common patterns

**Basic single-end run (amplicon + guide):**
```bash
$CRISPRESSO \
  --fastq_r1 reads.fastq.gz \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --guide_seq ATCACCTTGTCCCTGTGAGT \
  --name my_sample \
  --output_folder results/
```

**Paired-end run with read merging:**
```bash
$CRISPRESSO \
  --fastq_r1 R1.fastq.gz \
  --fastq_r2 R2.fastq.gz \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --guide_seq ATCACCTTGTCCCTGTGAGT \
  --name paired_sample \
  --output_folder results/
```

**Base editor analysis (C→T CBE):**
```bash
$CRISPRESSO \
  --fastq_r1 reads.fastq.gz \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --guide_seq ATCACCTTGTCCCTGTGAGT \
  --base_editor_output \
  --conversion_nuc_from C \
  --conversion_nuc_to T \
  --output_folder results/base_editor/
```

**Prime editing analysis:**
```bash
$CRISPRESSO \
  --fastq_r1 reads.fastq.gz \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --prime_editing_pegRNA_spacer_seq ATCACCTTGTCCCTGTGAGT \
  --prime_editing_pegRNA_extension_seq GCACCGAGUCGGUGCAAACAAAGCCACGAGTGG \
  --prime_editing_nicking_guide_seq GTTTCAAAGTGCATCACCTT \
  --output_folder results/prime_editing/
```

**HDR quantification:**
```bash
$CRISPRESSO \
  --fastq_r1 reads.fastq.gz \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --guide_seq ATCACCTTGTCCCTGTGAGT \
  --expected_hdr_amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTTTGAGTCTGT \
  --output_folder results/hdr/
```

**Batch run from a TSV file:**
```bash
# batch.tsv columns: fastq_r1 [fastq_r2] amplicon_seq [guide_seq] [name] [...]
$CRISPRESSO_BATCH \
  --batch_settings batch.tsv \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --guide_seq ATCACCTTGTCCCTGTGAGT \
  --batch_output_folder results/batch/ \
  --n_processes 8
```

**Suppress plots and report for headless/HPC use:**
```bash
$CRISPRESSO \
  --fastq_r1 reads.fastq.gz \
  --amplicon_seq AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT \
  --guide_seq ATCACCTTGTCCCTGTGAGT \
  --suppress_plots \
  --suppress_report \
  --output_folder results/
```

**Pooled amplicon sequencing:**
```bash
# amplicons.tsv: tab-delimited with columns amplicon_name, amplicon_seq, [guide_seq, ...]
$CRISPRESSO_POOLED \
  --fastq_r1 reads.fastq.gz \
  --amplicons_file amplicons.tsv \
  --bowtie2_index /path/to/genome \
  --output_folder results/pooled/ \
  --n_processes 4
```

## Full flag reference

To look up all flags for a specific tool:
```bash
grep -A 30 "^### \`CRISPResso\`" ~/.cursor/skills/crispresso/reference.md
grep -A 30 "^### \`CRISPRessoBatch\`" ~/.cursor/skills/crispresso/reference.md
```
Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
```bash
grep -A 20 "keyword" ~/.cursor/skills/crispresso/patterns.md
```
[patterns.md](patterns.md)
