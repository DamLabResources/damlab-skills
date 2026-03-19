# CRISPResso — Full Reference

Binaries: `~/.cursor/skills/crispresso/bin/CRISPResso`, `CRISPRessoBatch`, `CRISPRessoPooled`, `CRISPRessoCompare`, `CRISPRessoWGS`, `CRISPRessoAggregate`

Source: [docs.crispresso.com/latest/parameters.html](https://docs.crispresso.com/latest/parameters.html) (v2.3.3)

Grep for a tool's parameters:
```bash
grep -A 30 "^### \`CRISPResso\`" ~/.cursor/skills/crispresso/reference.md
grep -A 30 "^### \`CRISPRessoBatch\`" ~/.cursor/skills/crispresso/reference.md
```
Increase `-A` if output appears truncated.

---

## Tool entry points

### `CRISPResso`

Single amplicon analysis. Required: `--fastq_r1`, `--amplicon_seq`.

### `CRISPRessoBatch`

Batch analysis driven by a TSV batch settings file. Required: `--batch_settings`.

### `CRISPRessoPooled`

Multiple amplicons from one FASTQ. Required: `--fastq_r1`, `--amplicons_file`, `--bowtie2_index`.

### `CRISPRessoWGS`

Specific sites from whole-genome sequencing. Required: `--bam_file`, `--region_file`, `--reference_file`.

### `CRISPRessoCompare`

Compare two CRISPResso output folders. Required: two positional path arguments.

### `CRISPRessoAggregate`

Aggregate HTML reports from multiple CRISPResso runs.

---

## Input

#### `-r1, --fastq_r1`
First fastq file.
Tools: Core, Pooled

#### `-r2, --fastq_r2`
Second fastq file for paired-end reads.
Tools: Core, Pooled

#### `--bam_input`
Aligned reads for processing in BAM format (alternative to fastq input).
Tools: Core, Batch, Pooled

#### `--bam_chr_loc`
Chromosome location in BAM for reads to process. E.g. `chr1:50-100` or `chrX`.
Tools: Core, Batch, Pooled

#### `--split_interleaved_input, --split_paired_end`
Splits a single fastq containing interleaved paired-end reads into two files before processing.
Default: `False`
Tools: Core, Batch, Pooled

---

## Amplicon / Guide

#### `-a, --amplicon_seq`
Amplicon sequence. Comma-separated list for multiple alleles.
Tools: Core, Batch, Pooled

#### `-an, --amplicon_name`
Amplicon name(s), comma-separated, corresponding to `--amplicon_seq`.
Default: `Reference`
Tools: Core, Batch, Pooled

#### `-amas, --amplicon_min_alignment_score`
Minimum homology score (0–100) to align a read to each amplicon. Comma-separated list.
Tools: Core, Batch, Pooled, WGS

#### `--default_min_aln_score, --min_identity_score`
Default minimum homology score for a read to align to a reference amplicon.
Default: `60`
Tools: Core, Batch, Pooled, WGS

#### `--expand_ambiguous_alignments`
Reads aligning to multiple amplicons with equal score count equally toward each. Default: exclude ambiguous.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--assign_ambiguous_alignments_to_first_reference`
Ambiguous reads are assigned to the first amplicon instead of being excluded.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `-g, --guide_seq, --sgRNA`
sgRNA sequence(s), comma-separated. Enter without PAM. For SpCas9, PAM is on the 3' side of the guide.
Tools: Core, Batch, Pooled, WGS

#### `-gn, --guide_name`
sgRNA name(s), comma-separated, corresponding to `--guide_seq`.
Tools: Core, Batch, Pooled, WGS

#### `-fg, --flexiguide_seq`
Flexible sgRNA sequence(s). Aligned to amplicon with `--flexiguide_homology` threshold.
Default: `None`
Tools: Core, Batch, Pooled, WGS

#### `-fh, --flexiguide_homology`
Minimum homology (%) for a flexiguide to match an amplicon.
Default: `80`
Tools: Core, Batch, Pooled, WGS

#### `-fgn, --flexiguide_name`
Flexiguide name(s), comma-separated.
Tools: Core, Batch, Pooled, WGS

#### `--discard_guide_positions_overhanging_amplicon_edge`
Discard guide positions that would require plotting beyond amplicon ends.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `-e, --expected_hdr_amplicon_seq`
Expected amplicon sequence after HDR. Enables HDR quantification.
Tools: Core, Batch, Pooled, WGS

#### `-c, --coding_seq`
Subsequence(s) of the amplicon covering coding sequence(s) for frameshift analysis. Comma-separated.
Tools: Core, Batch, Pooled, WGS

#### `--config_file`
Path to JSON config file with parameter values.
Default: `None`
Tools: Core, Batch, Pooled, WGS

---

## Quality filtering

#### `-q, --min_average_read_quality`
Minimum average phred33 quality score to keep a read.
Tools: Core, Batch, Pooled, WGS

#### `-s, --min_single_bp_quality`
Minimum per-base phred33 quality score to keep a read.
Tools: Core, Batch, Pooled, WGS

#### `--min_bp_quality_or_N`
Bases below this phred33 score are replaced with 'N'.
Tools: Core, Batch, Pooled, WGS

---

## Read preprocessing / trimming

#### `--trim_sequences`
Enable adapter trimming with fastp.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--fastp_command`
Command to invoke fastp.
Default: `fastp`
Tools: Core, Batch, Pooled, WGS

#### `--fastp_options_string`
Override fastp options, e.g. `--length_required 70 --umi`.
Tools: Core, Batch, Pooled, WGS

#### `--crispresso_merge`
Merge paired-end reads using the CRISPResso aligner instead of fastp.
Default: `False`
Tools: Core only

#### `--min_paired_end_reads_overlap`
Minimum overlap length for fastp read merging.
Default: `10`
Tools: Core, Batch, Pooled, WGS

---

## Quantification

#### `-w, --quantification_window_size, --window_around_sgrna`
Radius (bp) of the quantification window around the cut site. 0 = entire amplicon. Default 1 = 2bp total window.
Default: `1`
Tools: Core, Batch, Pooled, WGS

#### `-wc, --quantification_window_center, --cleavage_offset`
Center of the quantification window relative to the 3' end of the guide. Default -3 (SpCas9). Use 1 for Cpf1.
Default: `-3`
Tools: Core, Batch, Pooled, WGS

#### `-qwc, --quantification_window_coordinates`
Explicit bp positions for the quantification window (0-based). Overrides `--quantification_window_center`. Ranges as `start-stop`; multiple ranges separated by `_`; comma-separated list per amplicon.
Tools: Core, Batch, Pooled, WGS

#### `--exclude_bp_from_left`
Exclude this many bp from the left edge of the amplicon from quantification.
Default: `15`
Tools: Core, Batch, Pooled, WGS

#### `--exclude_bp_from_right`
Exclude this many bp from the right edge of the amplicon from quantification.
Default: `15`
Tools: Core, Batch, Pooled, WGS

#### `--ignore_substitutions`
Exclude substitution events from quantification and visualization.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--ignore_insertions`
Exclude insertion events from quantification and visualization.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--ignore_deletions`
Exclude deletion events from quantification and visualization.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--discard_indel_reads`
Discard reads with indels in the quantification window entirely.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--use_legacy_insertion_quantification`
Use legacy quantification: with 1bp window, count insertions ±1bp from cut. Default: count only at cut.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--samtools_exclude_flags`
SAM flags to exclude reads (hex or decimal). Core default: 0 (no filtering). Pooled/WGS default: 4 (unmapped).
Tools: Core, Pooled, WGS

---

## Alignment algorithm

#### `--needleman_wunsch_gap_open`
Gap-open penalty for Needleman-Wunsch alignment.
Default: `-20`
Tools: Core, Batch, Pooled, WGS

#### `--needleman_wunsch_gap_extend`
Gap-extension penalty for Needleman-Wunsch alignment.
Default: `-2`
Tools: Core, Batch, Pooled, WGS

#### `--needleman_wunsch_gap_incentive`
Gap incentive at predicted cut sites to encourage biologically plausible indels.
Default: `1`
Tools: Core, Batch, Pooled, WGS

#### `--needleman_wunsch_aln_matrix_loc`
NCBI-format substitution matrix for alignment scoring.
Default: `EDNAFULL`
Tools: Core, Batch, Pooled, WGS

---

## Output / naming

#### `-n, --name`
Output name for the report (default: derived from fastq filename).
Tools: Core, Batch, Pooled, WGS, Compare

#### `--display_name`
Display name shown in HTML report (falls back to `--name`).
Tools: Core, Batch, Pooled, WGS, Compare

#### `-o, --output_folder`
Output directory (default: current directory).
Tools: Core, Batch, Pooled, WGS, Compare

#### `--file_prefix`
Prefix for output plot and table filenames.
Tools: Core, Batch, Pooled, WGS

#### `--suppress_amplicon_name_truncation`
Do not truncate amplicon names longer than 21 characters in output filenames.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--keep_intermediate`
Keep all intermediate files.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--write_detailed_allele_table`
Write a detailed allele table with per-read substitution, insertion, and deletion positions.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--fastq_output`
Write an annotated fastq file for each read.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--bam_output`
Write a BAM file with read alignments.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--zip_output`
Place output in a zip archive.
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--suppress_report`
Suppress the HTML output report.
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--place_report_in_output_folder`
Write the HTML report inside the output folder (default: one level up).
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--suppress_plots`
Suppress all output plots.
Default: `False`
Tools: Core, Batch, Pooled, WGS

---

## Visualization

#### `--plot_window_size, --offset_around_cut_to_plot`
Window radius around cut to display in plots.
Default: `20`
Tools: Core, Batch, Pooled, WGS

#### `--min_frequency_alleles_around_cut_to_plot`
Minimum read frequency (%) to show an allele in allele plots.
Default: `0.2`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--max_rows_alleles_around_cut_to_plot`
Maximum rows shown in the allele table plot.
Default: `50`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--expand_allele_plots_by_quantification`
Show alleles with identical sequence but different quantification-window modifications on separate rows.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--allele_plot_pcts_only_for_assigned_reference`
Allele plot percentages are per-reference instead of per-total reads.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--annotate_wildtype_allele`
Mark wildtype alleles in allele plots with this string (e.g. `**`).
Tools: Core, Batch, Pooled, WGS

#### `--plot_histogram_outliers`
Show all histogram values (default: clip at 99th percentile).
Default: `False`
Tools: Core, Batch, Pooled, WGS

---

## Base editor mode

#### `--base_editor_output`
Enable base editor analysis plots and tables.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--conversion_nuc_from`
Nucleotide targeted by the base editor (source).
Default: `C`
Tools: Core, Batch, Pooled, WGS

#### `--conversion_nuc_to`
Nucleotide produced by the base editor (product).
Default: `T`
Tools: Core, Batch, Pooled, WGS

---

## Prime editing mode

#### `--prime_editing_pegRNA_spacer_seq`
pegRNA spacer (sgRNA without PAM). 5'→3' RNA order.
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_pegRNA_extension_seq`
pegRNA extension: RT template (including edit) followed by PBS. 5'→3' RNA order.
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_pegRNA_extension_quantification_window_size`
Quantification window radius at the flap site for prime editing.
Default: `5`
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_pegRNA_scaffold_seq`
Scaffold sequence to identify scaffold-incorporated reads. Common: ends with `GGCACCGAGUCGGUGC`.
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_pegRNA_scaffold_min_match_length`
Minimum scaffold bases to classify a read as scaffold-incorporated.
Default: `1`
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_nicking_guide_seq`
Nicking sgRNA sequence (without PAM). 5'→3' RNA order.
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_override_prime_edited_ref_seq`
Override the inferred prime-edited reference sequence with this explicit sequence.
Tools: Core, Batch, Pooled, WGS

#### `--prime_editing_override_sequence_checks`
Skip orientation checks for pegRNA sequences.
Default: `False`
Tools: Core, Batch, Pooled, WGS

---

## Runtime / misc

#### `-p, --n_processes`
Number of parallel processes. Can be `max`.
Default: `1`
Tools: Core, Batch, Pooled, WGS

#### `-v, --verbosity`
Console verbosity level (1–4; 4 = most verbose).
Default: `3`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--no_rerun`
Skip analysis if a run with identical parameters already exists.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--auto`
Infer amplicon sequence from the most common reads.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--dsODN`
Label reads containing this dsODN sequence.
Tools: Core, Batch, Pooled, WGS

#### `--bowtie2_index`
Basename of Bowtie2 index for the reference genome.
Tools: Core, Batch, Pooled, WGS

#### `--dump`
Dump numpy arrays and pandas dataframes for debugging.
Default: `False`
Tools: Core, Batch, Pooled, WGS

#### `--debug`
Show debug messages.
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--disable_guardrails`
Disable guardrail warnings.
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--use_matplotlib`
Use matplotlib for plotting (instead of plotly/d3 when CRISPRessoPro is installed).
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

#### `--halt_on_plot_fail`
Halt if any plot fails to generate.
Default: `False`
Tools: Core, Batch, Pooled, WGS, Compare

---

## Batch-specific parameters

#### `-bs, --batch_settings`
Tab-separated batch file. Header row lists CRISPResso parameters; each subsequent row is one sample.
Required for CRISPRessoBatch.

#### `-bo, --batch_output_folder`
Directory for batch analysis output.
Tools: Batch

#### `--min_reads_for_inclusion`
Minimum reads required for a batch sample to appear in the summary.
Tools: Batch

#### `--skip_failed`
Continue batch even if individual samples fail.
Default: `False`
Tools: Batch, Pooled, WGS

#### `--suppress_batch_summary_plots`
Suppress cross-sample summary plots (useful for very large batches).
Default: `False`
Tools: Batch

#### `--crispresso_command`
CRISPResso command to invoke for each batch run.
Default: `CRISPResso`
Tools: Batch, Pooled, WGS

---

## Pooled-specific parameters

#### `-f, --amplicons_file`
Tab-delimited amplicons description file. Required columns: `amplicon_name`, `amplicon_seq`. Optional: `guide_seq`, `expected_hdr_amplicon_seq`, `coding_seq`, prime editing parameters, quantification window parameters.
Required for CRISPRessoPooled.

#### `--gene_annotations`
UCSC knownGene table (gzip compressed) for annotating cut sites.
Tools: Pooled, WGS

#### `--bowtie2_options_string`
Override Bowtie2 alignment options.
Tools: Pooled

#### `--min_reads_to_use_region`
Minimum reads aligning to a region to run CRISPResso analysis. Pooled default: `1000`.
Tools: Pooled

#### `--compile_postrun_references`
Write a file compiling reference sequences of frequent alleles.
Default: `False`
Tools: Pooled

#### `--alternate_alleles`
Path to TSV with alternate allele sequences for allele-specific analysis in pooled experiments.
Tools: Pooled

#### `--aligned_pooled_bam`
Pre-aligned BAM input instead of fastq; requires `--bowtie2_index` for reference extraction.
Tools: Pooled

#### `--demultiplex_genome_wide`
Demultiplex across the entire genome (exact coordinate matching to amplicons).
Default: `False`
Tools: Pooled

---

## WGS-specific parameters

#### `-b, --bam_file`
WGS aligned BAM file.
Required for CRISPRessoWGS.

#### `-f, --region_file`
BED file of regions to analyze. Required columns: `chr_id`, `bpstart`, `bpend`. Optional: `name`, `guide_seq`, `expected_hdr_amplicon_seq`, `coding_seq`.
Required for CRISPRessoWGS.

#### `-r, --reference_file`
Reference FASTA (e.g. hg38.fa).
Required for CRISPRessoWGS.

#### `--min_reads_to_use_region` (WGS)
Minimum reads per region to run CRISPResso analysis. WGS default: `10`.
Tools: WGS

---

## Compare-specific parameters

#### `crispresso_output_folder_1` (positional)
Path to first CRISPResso output folder.

#### `crispresso_output_folder_2` (positional)
Path to second CRISPResso output folder.

#### `-n1, --sample_1_name`
Label for sample 1 in comparison plots.
Tools: Compare

#### `-n2, --sample_2_name`
Label for sample 2 in comparison plots.
Tools: Compare

#### `--reported_qvalue_cutoff`
Q-value threshold for reporting significant differential editing at individual base positions (Fisher's exact test + Bonferroni).
Default: `0.05`
Tools: Compare
