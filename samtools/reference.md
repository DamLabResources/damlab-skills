# samtools — Full Reference

Binary: `~/.cursor/skills/samtools/bin/samtools`

Each entry contains the verbatim `--help` / usage output. Grep for a subcommand:
```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/samtools/reference.md
```
Increase `-A` if output appears truncated.

---

## Indexing

### `dict`

```
About:   Create a sequence dictionary file from a fasta file
Usage:   samtools dict [options] <file.fa|file.fa.gz>

Options: -a, --assembly STR    assembly
         -A, --alias, --alternative-name
                               add AN tag by adding/removing 'chr'
         -H, --no-header       do not print @HD line
         -l, --alt FILE        add AH:* tag to alternate locus sequences
         -o, --output FILE     file to write out dict file [stdout]
         -s, --species STR     species
         -u, --uri STR         URI [file:///abs/path/to/file.fa]
```

### `faidx`

```
Usage: samtools faidx <file.fa|file.fa.gz> [<reg> [...]]
Option: 
  -o, --output FILE        Write FASTA to file.
  -n, --length INT         Length of FASTA sequence line. [60]
  -c, --continue           Continue after trying to retrieve missing region.
  -r, --region-file FILE   File of regions.  Format is chr:from-to. One per line.
  -i, --reverse-complement Reverse complement sequences.
      --mark-strand TYPE   Add strand indicator to sequence name
                           TYPE = rc   for /rc on negative strand (default)
                                  no   for no strand indicator
                                  sign for (+) / (-)
                                  custom,<pos>,<neg> for custom indicator
      --fai-idx      FILE  name of the index file (default file.fa.fai).
      --gzi-idx      FILE  name of compressed file index (default file.fa.gz.gzi).
  -f, --fastq              File and index in FASTQ format.
  -h, --help               This message.
      --output-fmt-option OPT[=VAL]
  -@, --threads INT        Number of additional threads to use [0]
      --write-index        Automatically index the output files [off]
```

### `fqidx`

```
Usage: samtools fqidx <file.fq|file.fq.gz> [<reg> [...]]
Option: 
  -o, --output FILE        Write FASTQ to file.
  -n, --length INT         Length of FASTQ sequence line. [60]
  -c, --continue           Continue after trying to retrieve missing region.
  -r, --region-file FILE   File of regions.  Format is chr:from-to. One per line.
  -i, --reverse-complement Reverse complement sequences.
      --mark-strand TYPE   Add strand indicator to sequence name
      --fai-idx      FILE  name of the index file (default file.fq.fai).
      --gzi-idx      FILE  name of compressed file index (default file.fq.gz.gzi).
  -h, --help               This message.
      --output-fmt-option OPT[=VAL]
  -@, --threads INT        Number of additional threads to use [0]
      --write-index        Automatically index the output files [off]
```

### `index`

```
Usage: samtools index -M [-bc] [-m INT] <in1.bam> <in2.bam>...
   or: samtools index [-bc] [-m INT] <in.bam> [out.index]
Options:
  -b, --bai            Generate BAI-format index for BAM files [default]
  -c, --csi            Generate CSI-format index for BAM files
  -m, --min-shift INT  Set minimum interval size for CSI indices to 2^INT [14]
  -M                   Interpret all filename arguments as files to be indexed
  -o, --output FILE    Write index to FILE [alternative to <out.index> in args]
  -@, --threads INT    Sets the number of additional threads [0]
```

---

## Editing

### `calmd`

```
Usage: samtools calmd [-eubrAESQ] <aln.bam> <ref.fasta>
Options:
  -e       change identical bases to '='
  -u       uncompressed BAM output (for piping)
  -b       compressed BAM output
  -S       ignored (input format is auto-detected)
  -A       modify the quality string
  -Q       use quiet mode to output less debug info to stdout
  -r       compute the BQ tag (without -A) or cap baseQ by BAQ (with -A)
  -E       extended BAQ for better sensitivity but lower specificity
  --no-PG  do not add a PG line
      --input-fmt-option OPT[=VAL]
      --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --verbosity INT
```

### `fixmate`

```
Usage: samtools fixmate <in.nameSrt.bam> <out.nameSrt.bam>
Options:
  -r           Remove unmapped reads and secondary alignments
  -p           Disable FR proper pair check
  -c           Add template cigar ct tag
  -m           Add mate score tag (required for markdup)
  -u           Uncompressed output
  -z, --sanitize FLAG[,FLAG]
               Sanitize alignment fields [defaults to all types]
  -M           Fix base modification tags (MM/ML/MN)
  --no-PG      do not add a PG line
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT

Input must be sorted by name. Run 'samtools sort -n' first.
```

### `reheader`

```
Usage: samtools reheader [-P] in.header.sam in.bam > out.bam
   or  samtools reheader [-P] -i in.header.sam file.cram
   or  samtools reheader -c CMD in.bam
   or  samtools reheader -c CMD in.cram

Options:
    -P, --no-PG         Do not generate a @PG header line.
    -i, --in-place      Modify the CRAM file directly, if possible.
    -c, --command CMD   Pass the header in SAM format to external program CMD.
```

### `targetcut`

```
Usage: samtools targetcut [-Q minQ] [-i inPen] [-0 em0] [-1 em1] [-2 em2] <in.bam>
      --input-fmt-option OPT[=VAL]
  -f, --reference FILE
      --verbosity INT
```

### `addreplacerg`

```
Usage: samtools addreplacerg [options] [-r <@RG line> | -R <existing id>] [-m orphan_only|overwrite_all] [-o <output.bam>] <input.bam>

Options:
  -m MODE   Set the mode of operation from one of overwrite_all, orphan_only [overwrite_all]
  -o FILE   Where to write output to [stdout]
  -r STRING @RG line text
  -R STRING ID of @RG line in existing header to use
  -u        Output uncompressed data
  -w        Overwrite an existing @RG line
  --no-PG   Do not add a PG line
      --input-fmt FORMAT[,OPT[=VAL]]...
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
      --output-fmt-option OPT[=VAL]
      --reference FILE
  -@, --threads INT
      --write-index
      --verbosity INT
```

### `markdup`

```
Usage:  samtools markdup <input.bam> <output.bam>

Option: 
  -r                 Remove duplicate reads
  -l INT             Max read length (default 300 bases)
  -S                 Mark supplementary alignments of duplicates as duplicates (slower).
  -s                 Report stats.
  -f NAME            Write stats to named file.  Implies -s.
  --json             Output stats in JSON.  Also implies -s
  -T PREFIX          Write temporary files to PREFIX.samtools.nnnn.nnnn.tmp.
  -d INT             Optical distance (if set, marks with dt tag)
  -c                 Clear previous duplicate settings and tags.
  -m --mode TYPE     Duplicate decision method for paired reads.
                     TYPE = t measure positions based on template start/end (default).
                            s measure positions based on sequence start.
  -u                 Output uncompressed data
  --include-fails    Include quality check failed reads.
  --no-PG            Do not add a PG line
  --no-multi-dup     Reduced duplicates of duplicates checking.
  --read-coords STR  Regex for coords from read name.
  --coords-order STR Order of regex elements. txy (default).
  --barcode-tag STR  Use barcode a tag that duplicates must match.
  --barcode-name     Use the UMI/barcode in the read name.
  --barcode-rgx STR  Regex for barcode in the readname.
  --use-read-groups  Use the read group tags in duplicate matching.
  -t                 Mark primary duplicates with the name of the original in a 'do' tag.
  --duplicate-count  Record the original primary read duplication count in a 'dc' tag.
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --write-index
      --verbosity INT

Input must be coordinate sorted and must have gone through fixmate with -m flag.
```

### `ampliconclip`

```
Usage: samtools ampliconclip -b BED file <input.bam> -o <output.bam>

Option: 
 -b  FILE             BED file of regions (eg amplicon primers) to be removed.
 -o  FILE             output file name (default: stdout).
 -f  FILE             write stats to file name (default: stderr)
 -u                   Output uncompressed data
 --soft-clip          soft clip amplicon primers from reads (default)
 --hard-clip          hard clip amplicon primers from reads.
 --both-ends          clip on both 5' and 3' ends.
 --strand             use strand data from BED file to match read direction.
 --clipped            only output clipped reads.
 --fail               mark unclipped, mapped reads as QCFAIL.
 --filter-len INT     do not output reads INT size or shorter.
 --fail-len   INT     mark as QCFAIL reads INT size or shorter.
 --unmap-len  INT     unmap reads INT size or shorter, default 0.
 --no-excluded        do not write excluded reads (unmapped or QCFAIL).
 --rejects-file FILE  file to write filtered reads.
 --primer-counts FILE file to write read counts per bed entry (bedgraph format).
 --original           for clipped entries add an OA tag with original data.
 --keep-tag           for clipped entries keep the old NM and MD tags.
 --tolerance          match region within this number of bases, default 5.
 --no-PG              do not add an @PG line.
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --verbosity INT
```

---

## File Operations

### `collate`

```
Usage: samtools collate [options...] <in.bam> [<prefix>]

Options:
      -O       Output to stdout
      -o       Output file name (use prefix if not set)
      -u       Uncompressed BAM output
      -f       Fast (only primary alignments)
      -r       Working reads stored (with -f) [10000]
      -l INT   Compression level [1]
      -n INT   Number of temporary files [64]
      -T PREFIX
               Write temporary files to PREFIX.nnnn.bam
      --no-PG  do not add a PG line
      --input-fmt-option OPT[=VAL]
      --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --verbosity INT

<prefix> is required unless the -o or -O options are used.
```

### `cat`

```
Usage: samtools cat [options] <in1.bam>  [... <inN.bam>]
       samtools cat [options] <in1.cram> [... <inN.cram>]

Concatenate BAM or CRAM files, first those in <bamlist.fofn>, then those on the command line.

Options: -b FILE  list of input BAM/CRAM file names, one per line
         -h FILE  copy the header from FILE [default is 1st input file]
         -o FILE  output BAM/CRAM
         --no-PG  do not add a PG line

CRAM only options for filtering:
         -r REG   filter to region REG.
         -p N/M   Specify part N of M (where N is 1 to M inclusive)
         -f       Fast mode: don't filter containers to exactly match region
         -q       Query the total number of indexed containers

Standard options:
      --output-fmt-option OPT[=VAL]
      --verbosity INT
```

### `consensus`

```
Usage: samtools consensus [options] <in.bam>

Options:
  -r, --region REG      Limit query to REG. Requires an index
  -f, --format FMT      Output in format FASTA, FASTQ or PILEUP [FASTA]
  -l, --line-len INT    Wrap FASTA/Q at line length INT [70]
  -o, --output FILE     Output consensus to FILE
  -m, --mode STR        Switch consensus mode to "simple"/"bayesian" [bayesian]
  -a                    Output all bases (start/end of reference)
  --rf, --incl-flags STR|INT
                        Only include reads with any flag bit set [0]
  --ff, --excl-flags STR|INT
                        Exclude reads with any flag bit set [UNMAP,SECONDARY,QCFAIL,DUP]
  --min-MQ INT          Exclude reads with mapping quality below INT [0]
  --min-BQ INT          Exclude reads with base quality below INT [0]
  --show-del yes/no     Whether to show deletion as "*" [no]
  --show-ins yes/no     Whether to show insertions [yes]
  --mark-ins            Add '+' before every inserted base/qual [off]
  -A, --ambig           Enable IUPAC ambiguity codes [off]
  -d, --min-depth INT   Minimum depth of INT [1]
  -Z, --block-size INT  Size of chromosome block (bp) when threading [100000]
      --ref-qual INT    QUAL to use for reference bases [0]

For simple consensus mode:
  -q, --(no-)use-qual   Use quality values in calculation [off]
  -c, --call-fract INT  At least INT portion of bases must agree [0.75]
  -H, --het-fract INT   Minimum fraction of 2nd-most to most common base [0.15]

For default "Bayesian" consensus mode:
  -C, --cutoff C        Consensus cutoff quality C [10]
      --(no-)adj-qual   Modify quality with local minima [on]
      --(no-)use-MQ     Use mapping quality in calculation [on]
      --(no-)adj-MQ     Modify mapping quality by local NM [on]
      --NM-halo INT     Size of window for NM count in --adj-MQ [50]
      --scale-MQ FLOAT  Scale mapping quality by FLOAT [1.00]
      --low-MQ  INT     Cap minimum mapping quality [1]
      --high-MQ INT     Cap maximum mapping quality [60]
      --P-het FLOAT     Probability of heterozygous site [1.0e-03]
      --P-indel FLOAT   Probability of indel sites [2.0e-04]
      --het-scale FLOAT Heterozygous SNP probability multiplier [1.0e+00]
  -p, --homopoly-fix    Spread low-qual bases to both ends of homopolymers
  -t, --qual-calibration FILE
                        Load quality calibration file
  -X, --config STR      Pre-defined config: hiseq, hifi, r10.4_sup, r10.4_dup, ultima

Global options:
      --input-fmt-option OPT[=VAL]
  -T, --reference FILE
  -@, --threads INT
      --verbosity INT
```

### `merge`

```
Usage: samtools merge [options] -o <out.bam> [options] <in1.bam> ... <inN.bam>
   or: samtools merge [options] <out.bam> <in1.bam> ... <inN.bam>

Options:
  -n         Input files are sorted by read name (natural)
  -N         Input files are sorted by read name (ASCII)
  -t TAG     Input files are sorted by TAG value
  -r         Attach RG tag (inferred from file names)
  -u         Uncompressed BAM output
  -f         Overwrite the output BAM if exist
  -o FILE    Specify output file via option instead of <out.bam> argument
  -1         Compress level 1
  -l INT     Compression level, from 0 to 9 [-1]
  -R STR     Merge file in the specified region STR [all]
  -h FILE    Copy the header in FILE to <out.bam> [in1.bam]
  -c         Combine @RG headers with colliding IDs [alter IDs to be distinct]
  -p         Combine @PG headers with colliding IDs [alter IDs to be distinct]
  -s VALUE   Override random seed
  -b FILE    List of input BAM filenames, one per line [null]
  -X         Use customized index files
  -L FILE    Specify a BED file for multiple region filtering [null]
  --no-PG    do not add a PG line
  --template-coordinate Input files are sorted by template-coordinate
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --write-index
      --verbosity INT
```

### `mpileup`

```
Usage: samtools mpileup [options] in1.bam [in2.bam [...]]

Input options:
  -6, --illumina1.3+      quality is in the Illumina-1.3+ encoding
  -A, --count-orphans     do not discard anomalous read pairs
  -b, --bam-list FILE     list of input BAM filenames, one per line
  -B, --no-BAQ            disable BAQ (per-Base Alignment Quality)
  -C, --adjust-MQ INT     adjust mapping quality; recommended:50, disable:0 [0]
  -d, --max-depth INT     max per-file depth; avoids excessive memory usage [8000]
  -E, --redo-BAQ          recalculate BAQ on the fly, ignore existing BQs
  -f, --fasta-ref FILE    faidx indexed reference sequence file
  -G, --exclude-RG FILE   exclude read groups listed in FILE
  -l, --positions FILE    skip unlisted positions (chr pos) or regions (BED)
  -q, --min-MQ INT        skip alignments with mapQ smaller than INT [0]
  -Q, --min-BQ INT        skip bases with baseQ/BAQ smaller than INT [13]
  -r, --region REG        region in which pileup is generated
  -R, --ignore-RG         ignore RG tags (one BAM = one sample)
  --rf, --incl-flags STR|INT  required flags
  --ff, --excl-flags STR|INT  filter flags [UNMAP,SECONDARY,QCFAIL,DUP]
  -x, --ignore-overlaps-removal  disable read-pair overlap detection
  -X, --customized-index  use customized index files

Output options:
  -o, --output FILE        write output to FILE [standard output]
  -O, --output-BP          output base positions on reads
  -s, --output-MQ          output mapping quality
      --output-QNAME       output read names
      --output-extra STR   output extra read fields and read tag values
  -a                       output all positions (including zero depth)
  -a -a (or -aa)           output absolutely all positions

Generic options:
      --input-fmt-option OPT[=VAL]
      --reference FILE
      --verbosity INT

Note: Use 'bcftools mpileup' for BCF/VCF output (no longer supported here).
```

### `sort`

```
Usage: samtools sort [options...] [in.bam]
Options:
  -l INT     Set compression level, from 0 (uncompressed) to 9 (best)
  -u         Output uncompressed data (equivalent to -l 0)
  -m INT     Set maximum memory per thread; suffix K/M/G recognized [768M]
  -M         Use minimiser for clustering unaligned/unplaced reads
  -n         Sort by read name (natural): cannot be used with samtools index
  -N         Sort by read name (ASCII): cannot be used with samtools index
  -t TAG     Sort by value of TAG
  -o FILE    Write final output to FILE rather than standard output
  -T PREFIX  Write temporary files to PREFIX.nnnn.bam
      --no-PG
      --template-coordinate  Sort by template-coordinate
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --write-index
      --verbosity INT
```

### `split`

```
Usage: samtools split [-u <unaccounted.bam>] [-h <unaccounted_header.sam>]
                      [-f <format_string>] [-v] <merged.bam>
Options:
  -f STRING           output filename format string ["%*_%#.%."]
  -u FILE1            put left-over reads in FILE1
  -h FILE2            ... and override the header with FILE2 (-u file only)
  -d TAG              split by TAG value. TAG value must be a string.
  -p NUMBER           zero-pad numbers in filenames to NUMBER digits
  -M,--max-split NUM  limit number of output files from -d to NUM [100]
  -v                  verbose output
  --no-PG             do not add a PG line
      --input-fmt-option OPT[=VAL]
      --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
  -@, --threads INT
      --write-index
      --verbosity INT

Format string expansions: %% = %, %* = basename, %# = index, %! = @RG ID or TAG value, %. = extension
```

### `quickcheck`

```
Usage: samtools quickcheck [options] <input> [...]
Options:
  -v              verbose output (repeat for more verbosity)
  -q              suppress warning messages
  -u              unmapped input (do not require targets in header)

Exits non-zero if any file fails checks. Silent on success by default.
```

### `fastq`

```
Usage: samtools fastq [options...] <in.bam>

Description: Converts a SAM, BAM or CRAM to FASTQ format.

Options:
  -0 FILE      write reads designated READ_OTHER to FILE
  -1 FILE      write reads designated READ1 to FILE
  -2 FILE      write reads designated READ2 to FILE
  -o FILE      write reads designated READ1 or READ2 to FILE
  -d, --tag TAG[:VAL]  only include reads containing TAG, optionally with value VAL
  -D, --tag-file STR:FILE  only include reads containing TAG with value listed in FILE
  -f, --require-flags INT  only include reads with all FLAGs present [0]
  -F, --excl-flags INT     only include reads with none of FLAGs present [0x900]
      --rf, --incl-flags INT  only include reads with any of FLAGs present [0]
  -G INT       only EXCLUDE reads with all of the FLAGs in INT present [0]
  -n           don't append /1 and /2 to the read name
  -N           always append /1 and /2 to the read name
  --no-sc      Remove soft-clips from output
  -O           output quality in the OQ tag if present
  -s FILE      write singleton reads to FILE
  -t           copy RG, BC and QT tags to the FASTQ header line
  -T TAGLIST   copy arbitrary tags to the FASTQ header line, '*' for all
  -v INT       default quality score if not given in file [1]
  -i           add Illumina Casava 1.8 format entry to header
  -U, --UMI    add UMI to read name
  -c INT       compression level [0..9] to use when writing bgzf files [1]
  --i1 FILE    write first index reads to FILE
  --i2 FILE    write second index reads to FILE
  --barcode-tag TAG   Barcode tag [BC]
  --quality-tag TAG   Quality tag [QT]
  --index-format STR  How to parse barcode and quality tags
      --input-fmt-option OPT[=VAL]
      --reference FILE
  -@, --threads INT
      --verbosity INT

Input must be collated by name. Run 'samtools collate' or 'samtools sort -n' first.
```

### `fasta`

```
Usage: samtools fasta [options...] <in.bam>

Description: Converts a SAM, BAM or CRAM to FASTA format.

Options:
  -0 FILE      write reads designated READ_OTHER to FILE
  -1 FILE      write reads designated READ1 to FILE
  -2 FILE      write reads designated READ2 to FILE
  -o FILE      write reads designated READ1 or READ2 to FILE
  -d, --tag TAG[:VAL]  only include reads containing TAG
  -D, --tag-file STR:FILE  only include reads with TAG listed in FILE
  -f, --require-flags INT  only include reads with all FLAGs present [0]
  -F, --excl-flags INT     only include reads with none of FLAGs present [0x900]
      --rf, --incl-flags INT  only include reads with any of FLAGs present [0]
  -G INT       only EXCLUDE reads with all of the FLAGs in INT present [0]
  -n           don't append /1 and /2 to the read name
  -N           always append /1 and /2 to the read name
  --no-sc      Remove soft-clips from output
  -s FILE      write singleton reads to FILE
  -t           copy RG, BC and QT tags to the FASTA header line
  -T TAGLIST   copy arbitrary tags to the FASTA header line, '*' for all
  -i           add Illumina Casava 1.8 format entry to header
  -U, --UMI    add UMI to read name
  -c INT       compression level [0..9]
  --i1 FILE    write first index reads to FILE
  --i2 FILE    write second index reads to FILE
  --barcode-tag TAG
  --index-format STR
      --input-fmt-option OPT[=VAL]
      --reference FILE
  -@, --threads INT
      --verbosity INT

Input must be collated by name. Run 'samtools collate' or 'samtools sort -n' first.
```

### `import`

```
Usage: samtools import [options] [file.fastq ...]

Options:
  -s FILE      Read paired-ended data from single FILE
  -0 FILE      Read single-ended data from FILE
  -1 FILE      Read-1 from FILE
  -2 FILE      Read-2 from FILE
  --i1 FILE    Index-1 from FILE
  --i2 FILE    Index-2 from FILE
  -i           Parse CASAVA identifier
  -U, --UMI    Parse UMI from read name
  --UMI-tag TAG       Tag to use for UMI sequences [RX]
  --barcode-tag TAG   Tag to use with barcode sequences [BC]
  --quality-tag TAG   Tag to use with barcode qualities [QT]
  -N, --name2  Use 2nd field as read name (SRA format)
  -r STRING    Build up a complete @RG line
  -R STRING    Add a simple RG line of "@RG\tID:STRING"
  -T TAGLIST   Parse tags in SAM format; list of '*' for all
  -o FILE      Output to FILE instead of stdout
  -u           Uncompressed output
  --order TAG  Store Nth record count in TAG
      --no-PG
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
  -@, --threads INT
```

### `reference`

```
Usage: samtools reference [-@ N] [-r region] [-e] [-q] [-o out.fa] [in.cram]

Generates a reference FASTA from aligned CRAM data.
```

### `reset`

```
Usage: samtools reset [options]
  -o FILE      Output file
  -x, --remove-tag STR    Aux tags to be removed
      --keep-tag STR       Aux tags to be retained (equivalent to -x ^STR)
      --reject-PG ID       Removes PG line with ID matching to input and succeeding PG lines
      --no-RG              Remove RG lines
      --no-PG              Remove PG entry for reset operation
      --dupflag            Keeps the duplicate flag as it is
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
  -@, --threads INT

Reverts aligner changes in reads (strips alignment information).
```

---

## Statistics

### `bedcov`

```
Usage: samtools bedcov [options] <in.bed> <in1.bam> [...]

Options:
      -Q, --min-MQ <int>  mapping quality threshold [0]
      -X                  use customized index files
      -g <flags>          remove the specified flags from the filter-out set
      -G <flags>          add the specified flags to the filter-out set
                          Default filter set: UNMAP,SECONDARY,QCFAIL,DUP or 0x704
      -j                  do not include deletions (D) and ref skips (N) in bedcov
      --max-depth <int>   sets the maximum depth used in the mpileup algorithm
      -d <int>            depth threshold for separate coverage column
      -c                  add an additional column showing read count
      -H                  print a comment/header line with column information
      --input-fmt-option OPT[=VAL]
      --reference FILE
      --verbosity INT
```

### `coverage`

```
Usage: samtools coverage [options] in1.bam [in2.bam [...]]

Input options:
  -b, --bam-list FILE     list of input BAM filenames, one per line
  -l, --min-read-len INT  ignore reads shorter than INT bp [0]
  -q, --min-MQ INT        mapping quality threshold [0]
  -Q, --min-BQ INT        base quality threshold [0]
  --rf <int|str>          required flags: skip reads with mask bits unset []
  --ff <int|str>          filter flags: skip reads with mask bits set [UNMAP,SECONDARY,QCFAIL,DUP]
  -d, --depth INT         maximum allowed coverage depth [1000000]
      --min-depth INT     minimum coverage depth below which a position is ignored [1]

Output options:
  -m, --histogram         show histogram instead of tabular output
  -D, --plot-depth        plot depth instead of tabular output
  -A, --ascii             show only ASCII characters in histogram
  -o, --output FILE       write output to FILE [stdout]
  -H, --no-header         don't print a header in tabular mode
  -w, --n-bins INT        number of bins in histogram [terminal width - 40]
  -r, --region REG        show specified region. Format: chr:start-end.
  -h, --help              help

Generic options:
      --input-fmt-option OPT[=VAL]
      --reference FILE
      --verbosity INT

Output columns: rname, startpos, endpos, numreads, covbases, coverage, meandepth, meanbaseq, meanmapq
```

### `depth`

```
Usage: samtools depth [options] in.bam [in.bam ...]

Options:
  -a           Output all positions (including zero depth)
  -a -a, -aa   Output absolutely all positions, including unused ref seqs
  -r REG       Specify a region in chr or chr:from-to syntax
  -b FILE      Use bed FILE for list of regions
  -f FILE      Specify list of input BAM/SAM/CRAM filenames
  -X           Use custom index files
  -g INT       Remove specified flags from default filter-out flag list
  -G, --excl-flags FLAGS  Add flags to the default filter-out list [UNMAP,SECONDARY,QCFAIL,DUP]
      --incl-flags FLAGS  Only include records with at least one FLAG present [0]
      --require-flags FLAGS  Only include records with all FLAGs present [0]
  -H           Print a file header line
  -l INT       Minimum read length [0]
  -o FILE      Write output to FILE [stdout]
  -q, --min-BQ INT  Filter bases with base quality smaller than INT [0]
  -Q, --min-MQ INT  Filter alignments with mapping quality smaller than INT [0]
  -J           Include reads with deletions in depth computation
  -s           Do not count overlapping reads within a template
      --input-fmt-option OPT[=VAL]
      --reference FILE
  -@, --threads INT
      --verbosity INT
```

### `flagstat`

```
Usage: samtools flagstat [options] <in.bam>
      --input-fmt-option OPT[=VAL]
  -@, --threads INT
      --verbosity INT
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
               Specify output format (json, tsv)
```

### `idxstats`

```
Usage: samtools idxstats [options] <in.bam>
  -X           Include customized index file
      --input-fmt-option OPT[=VAL]
  -@, --threads INT
      --verbosity INT

Output: reference name, sequence length, mapped reads, unmapped reads
```

### `cram-size`

```
Usage: samtools cram_size [-ve] [-o out.size] [in.cram]

Lists CRAM Content-ID and Data-Series sizes.
```

### `phase`

```
Usage:   samtools phase [options] <in.bam>

Options: -k INT    block length [13]
         -b STR    prefix of BAMs to output [null]
         -q INT    min het phred-LOD [37]
         -Q, --min-BQ INT  min base quality in het calling [13]
         -D INT    max read depth [256]
         -F        do not attempt to fix chimeras
         -A        drop reads with ambiguous phase
         --no-PG   do not add a PG line
      --input-fmt-option OPT[=VAL]
      --output-fmt FORMAT[,OPT[=VAL]]...
      --reference FILE
      --verbosity INT
```

### `stats`

```
About: The program collects statistics from BAM files. The output can be visualized using plot-bamstats.
Usage: samtools stats [OPTIONS] file.bam
       samtools stats [OPTIONS] file.bam chr:from-to
Options:
    -c, --coverage <int>,<int>,<int>    Coverage distribution min,max,step [1,1000,1]
    -d, --remove-dups                   Exclude from statistics reads marked as duplicates
    -X, --customized-index-file         Use a customized index file
    -f, --required-flag  <str|int>      Required flag, 0 for unset [0]
    -F, --filtering-flag <str|int>      Filtering flag, 0 for unset [0]
        --GC-depth <float>              the size of GC-depth bins [2e4]
    -h, --help                          This help message
    -i, --insert-size <int>             Maximum insert size [8000]
    -I, --id <string>                   Include only listed read group or sample name
    -l, --read-length <int>             Include only reads with given read length [-1]
    -m, --most-inserts <float>          Report only the main part of inserts [0.99]
    -P, --split-prefix <str>            Path or string prefix for filepaths output by -S
    -q, --trim-quality <int>            The BWA trimming parameter [0]
    -r, --ref-seq <file>                Reference sequence (for GC-depth and mismatches-per-cycle)
    -s, --sam                           Ignored (input format is auto-detected)
    -S, --split <tag>                   Also write statistics to separate files split by tagged field
    -t, --target-regions <file>         Do stats in these regions only (chr,from,to TSV file)
    -x, --sparse                        Suppress outputting IS rows where there are no insertions
    -p, --remove-overlaps               Remove overlaps of paired-end reads from coverage computation
    -g, --cov-threshold <int>           Only bases with coverage above this value in target % [0]
        --ref-stats                     Create statistics on reference data
      --input-fmt-option OPT[=VAL]
      --reference FILE
  -@, --threads INT
      --verbosity INT
```

### `ampliconstats`

```
Usage: samtools ampliconstats [options] primers.bed *.bam > astats.txt

Options:
  -f, --required-flag STR|INT  Only include reads with all FLAGs present [0x0]
  -F, --filter-flag STR|INT    Only include reads with none FLAGs present [0xB04]
  -a, --max-amplicons INT      Change the maximum number of amplicons permitted [1000]
  -l, --max-amplicon-length INT  Change the maximum length of an individual amplicon [1000]
  -d, --min-depth INT[,INT]... Minimum base depth(s) to consider position covered [1]
  -m, --pos-margin INT         Margin of error for matching primer positions [30]
  -o, --output FILE            Specify output file [stdout if unset]
  -s, --use-sample-name        Use the sample name from the first @RG header line
  -t, --tlen-adjust INT        Add/subtract from TLEN; use when clipping but no fixmate step
  -b, --tcoord-bin INT         Bin template start,end positions into multiples of INT [1]
  -c, --tcoord-min-count INT   Minimum template start,end frequency for recording [10]
  -D, --depth-bin FRACTION     Merge FDP values within +/- FRACTION together
  -S, --single-ref             Force single-ref (<=1.12) output format
  -I, --input-fmt FORMAT[,OPT[=VAL]]...
      --input-fmt-option OPT[=VAL]
      --reference FILE
  -@, --threads INT
```

### `checksum`

```
Usage: samtools checksum [options] [file.bam ...]
or     samtools checksum [options] -m [file.chk ...]

Options:
  -F, --exclude-flags FLAG    Filter if any FLAGs are present [0x900]
  -f, --require-flags FLAG    Filter unless all FLAGs are present [0]
  -b, --flag-mask FLAG        BAM FLAGs to use in checksums [0x0c1]
  -c, --no-rev-comp           Do not reverse-complement sequences [off]
  -t, --tags STR[,STR]        Select tags to checksum [BC,FI,QT,RT,TC]
  -O, --in-order              Use order-specific checksumming [off]
  -P, --check-pos             Also checksum CHR / POS [off]
  -C, --check-cigar           Also checksum MAPQ / CIGAR [off]
  -M, --check_mate            Also checksum PNEXT / RNEXT / TLEN [off]
  -z, --sanitize FLAGS        Perform sanity checks and fix records [off]
  -N, --count INT             Stop after INT number of records [0]
  -o, --output FILE           Write report to FILE [stdout]
  -q, --show-qc               Also show QC pass/fail lines
  -v, --verbose               Increase verbosity: show lines with 0 counts
  -a, --all                   Check all: -PCMOc -b 0xfff -f0 -F0 -z all,cigarx
  -T, --tabs                  Format output as tab delimited text
  -m, --merge FILE            Merge checksum output files
  -B, --bamseqchksum          Report in bamseqchksum format
      --input-fmt-option OPT[=VAL]
  -@, --threads INT
```

---

## Viewing

### `flags`

```
About: Convert between textual and numeric flag representation
Usage: samtools flags FLAGS...

Flag values:
   0x1     1  PAIRED         paired-end / multiple-segment sequencing technology
   0x2     2  PROPER_PAIR    each segment properly aligned according to aligner
   0x4     4  UNMAP          segment unmapped
   0x8     8  MUNMAP         next segment in the template unmapped
  0x10    16  REVERSE        SEQ is reverse complemented
  0x20    32  MREVERSE       SEQ of next segment in template is rev.complemented
  0x40    64  READ1          the first segment in the template
  0x80   128  READ2          the last segment in the template
 0x100   256  SECONDARY      secondary alignment
 0x200   512  QCFAIL         not passing quality controls or other filters
 0x400  1024  DUP            PCR or optical duplicate
 0x800  2048  SUPPLEMENTARY  supplementary alignment
```

### `head`

```
Usage: samtools head [OPTION]... [FILE]
Options:
  -h, --headers INT   Display INT header lines [all]
  -n, --records INT   Display INT alignment record lines [none]
      --input-fmt-option OPT[=VAL]
  -T, --reference FILE
  -@, --threads INT
      --verbosity INT
```

### `tview`

```
Usage: samtools tview [options] <aln.bam> [ref.fasta]
Options:
   -d display      output as (H)tml or (C)urses or (T)ext 
   -X              include customized index file
   -p chr:pos      go directly to this position
   -s STR          display only reads from this sample or group
   -w INT          display width (with -d T only)
   -i              hide inserts
      --input-fmt-option OPT[=VAL]
      --reference FILE
      --verbosity INT
```

### `view`

```
Usage: samtools view [options] <in.bam>|<in.sam>|<in.cram> [region ...]

Output options:
  -b, --bam                  Output BAM
  -C, --cram                 Output CRAM (requires -T)
  -1, --fast                 Use fast BAM compression
  -u, --uncompressed         Uncompressed BAM output
  -h, --with-header          Include header in SAM output
  -H, --header-only          Print SAM header only (no alignments)
      --no-header            Print SAM alignment records only [default]
  -c, --count                Print only the count of matching records
      --save-counts FILE     Write counts of passed/failed records to FILE
  -o, --output FILE          Write output to FILE [standard output]
  -U, --output-unselected FILE  Output reads not selected by filters to FILE
  -p, --unmap                Set flag to UNMAP on reads not selected
  -P, --fetch-pairs          Retrieve complete pairs even when outside of region

Input options:
  -t, --fai-reference FILE   FILE listing reference names and lengths
  -M, --use-index            Use index and multi-region iterator for regions
      --region[s]-file FILE  Use index to include only reads overlapping FILE
  -X, --customized-index     Expect extra index file argument after <in.bam>

Filtering options (Only include in output reads that...):
  -L, --targets-file FILE    ...overlap (BED) regions in FILE
  -N, --qname-file [^]FILE   ...whose read name is listed in FILE ("^" negates)
  -r, --read-group STR       ...are in read group STR or in no read group
  -R, --read-group-file [^]FILE  ...are in a read group listed in FILE
  -n, --exclude-no-read_group  ...have a read group
  -d, --tag STR1[:STR2]      ...have a tag STR1 (with associated value STR2)
  -D, --tag-file STR:FILE    ...have a tag STR whose value is listed in FILE
  -q, --min-MQ INT           ...have mapping quality >= INT
  -l, --library STR          ...are in library STR
  -m, --min-qlen INT         ...cover >= INT query bases (via CIGAR)
  -e, --expr STR             ...match the filter expression STR
  -f, --require-flags FLAG   ...have all of the FLAGs present
  -F, --excl-flags FLAG      ...have none of the FLAGs present
      --rf, --incl-flags FLAG  ...have some of the FLAGs present
  -G FLAG                    EXCLUDE reads with all of the FLAGs present
      --subsample FLOAT      Keep only FLOAT fraction of templates/read pairs
      --subsample-seed INT   Influence WHICH reads are kept in subsampling [0]
  -s INT.FRAC                Same as --subsample 0.FRAC --subsample-seed INT

Processing options:
      --add-flags FLAG       Add FLAGs to reads
      --remove-flags FLAG    Remove FLAGs from reads
  -x, --remove-tag STR       Comma-separated read tags to strip
      --keep-tag STR         Comma-separated read tags to preserve
  -B, --remove-B             Collapse the backward CIGAR operation
  -z, --sanitize FLAGS       Perform sanity checking and fixing on records

General options:
  -?, --help   Print long help
  -S           Ignored (input format is auto-detected)
      --no-PG  Do not add a PG line
      --input-fmt-option OPT[=VAL]
  -O, --output-fmt FORMAT[,OPT[=VAL]]...
  -T, --reference FILE
  -@, --threads INT
      --write-index
      --verbosity INT

Common flag values: 4=unmapped, 8=mate unmapped, 16=reverse, 256=secondary, 512=QC fail, 1024=dup, 2048=supplementary
```

### `depad`

```
Usage:   samtools depad <in.bam>

Options:
  -s           Output is SAM (default is BAM)
  -S           Input is SAM (default is BAM)
  -u           Uncompressed BAM output (can't use with -s)
  -1           Fast compression BAM output (can't use with -s)
  -T, --reference FILE  Padded reference sequence file [null]
  -o FILE      Output file name [stdout]
  --no-PG      do not add a PG line
      --input-fmt-option OPT[=VAL]
      --output-fmt FORMAT[,OPT[=VAL]]...
      --write-index
      --verbosity INT

Convert padded BAM to unpadded BAM.
```

### `samples`

```
Usage: samtools samples [options] <input> [...]
       samtools samples [options] -X f1.bam f2.bam f1.bam.bai f2.bai 

Options:
  -?              print help and exit
  -h              add the columns header before printing the results
  -i              test if the file is indexed.
  -T <tag>        provide the sample tag name from the @RG line [SM].
  -o <file>       output file [stdout].
  -f <file.fa>    load an indexed fasta file in the collection of references.
  -F <file.txt>   read a file containing the paths to indexed fasta files.
  -X              use a custom index file.

Lists the samples in a set of SAM/BAM/CRAM files.
```
