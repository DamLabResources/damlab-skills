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

### CRISPRessoAggregate: sample order in quilts and tables

**Context:** Cross-sample summary plots (“quilts”) and tables from `CRISPRessoAggregate` appear in an order you may want to control (e.g. all control animals, then all CRISPR animals, each block alphabetical).

**Behavior (CRISPResso2):** There is **no** `--order` or similar flag. The tool collects matching run directories via `glob`, then sorts folder paths with Python’s `sorted()` before building plots and tables. The quantification summary DataFrame is also `sort_values(by=['Name'])`. So order is **lexicographic by path/folder name**, not by the sequence of `-p` arguments.

**Implications:**

- Passing many `-p /path/CRISPResso_on_AnimalA_...` vs `-p /path/CRISPResso_on_AnimalB_...` does **not** enforce “A then B” unless those paths sort that way alphabetically.
- Renaming original CRISPResso output folders is disruptive; **symlinks** in a scratch directory (e.g. under `/tmp`) are a practical workaround.

**Pattern: symlink staging with numeric prefixes**

1. Choose a scratch directory, e.g. `ORDER_TMP=/tmp/crispresso-agg-order/my_group`.
2. Decide your desired order (e.g. control IDs alphabetically, then treatment IDs alphabetically).
3. For each sample in that order, assign a two-digit prefix `01`, `02`, … and create symlinks:

   `ln -s /real/path/CRISPResso_on_SampleFoo_GAG "${ORDER_TMP}/01_CRISPResso_on_SampleFoo_GAG"`

   Use the **same** numeric prefix for all runs that should stay adjacent (e.g. `_GAG` and `_PSI` for one animal).

4. Run aggregate from the output directory as usual, pointing at the symlink tree:

   ```bash
   mkdir -p /path/to/groups/my_group && cd /path/to/groups/my_group
   $CRISPRESSO_AGGREGATE -n my_group -p "${ORDER_TMP}/"
   ```

   Prefix must end so that `glob` picks up children (e.g. `-p "${ORDER_TMP}/"` so `prefix + '*'` matches `01_...`, `02_...`).

5. Re-run aggregate after changing symlinks; remove the scratch dir when done if you like.

**Note:** Only include symlinks for runs that exist; skip animals with no data for that tissue so indices stay contiguous per present sample.
