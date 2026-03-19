# CRISPResso — Patterns

Reusable patterns collected from real tasks. Each entry has a title, context, and runnable example.

<!-- Add patterns below as they arise -->

### Run CRISPResso on all samples in a directory

**Context:** When you have many per-sample fastq files in one directory and want to run CRISPResso on each with the same amplicon and guide.

```bash
AMPLICON="AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT"
GUIDE="ATCACCTTGTCCCTGTGAGT"

for fq in samples/*.fastq.gz; do
    sample=$(basename "$fq" .fastq.gz)
    $CRISPRESSO \
        --fastq_r1 "$fq" \
        --amplicon_seq "$AMPLICON" \
        --guide_seq "$GUIDE" \
        --name "$sample" \
        --output_folder "results/$sample/" \
        --suppress_plots \
        --suppress_report
done
```

### Extract editing efficiency from CRISPResso output

**Context:** After running CRISPResso, parse the quantification summary to get NHEJ/HDR percentages.

```bash
# CRISPResso_on_<name>/CRISPResso_quantification_of_editing_frequency.txt
cat results/CRISPResso_on_my_sample/CRISPResso_quantification_of_editing_frequency.txt
```

### Build a batch TSV for CRISPRessoBatch

**Context:** When running many samples with the same amplicon/guide but different fastq files.

```bash
# batch.tsv format (tab-separated):
# fastq_r1    name
# sample1.fastq.gz    ctrl
# sample2.fastq.gz    treated

printf 'fastq_r1\tname\n' > batch.tsv
for fq in samples/*.fastq.gz; do
    name=$(basename "$fq" .fastq.gz)
    printf '%s\t%s\n' "$fq" "$name"
done >> batch.tsv

$CRISPRESSO_BATCH \
    --batch_settings batch.tsv \
    --amplicon_seq "AATGTCCCCCAATGGGAGTTTCAAAGTGCATCACCTTGTCCCTGTGAGTCTGT" \
    --guide_seq "ATCACCTTGTCCCTGTGAGT" \
    --batch_output_folder results/batch/ \
    --n_processes 4
```
