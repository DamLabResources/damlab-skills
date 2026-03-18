# samtools — Full Reference

Invoke all commands as: `conda run -n damlab-skill-samtools samtools <subcommand>`

---

## Indexing

### `index`
Index a coordinate-sorted BAM/CRAM/SAM.
```bash
samtools index [-b|-c] [-m INT] [-@ INT] <in.bam>
```
| Flag | Description |
|---|---|
| `-b` | Force BAI index |
| `-c` | Force CSI index (required for contigs >512 Mbp) |
| `-m INT` | Minimum interval size for CSI (default 14) |
| `-@ INT` | Threads |

### `faidx`
Index FASTA or extract subsequences.
```bash
samtools faidx <ref.fa> [region ...]
```
Regions format: `chr:start-end` (1-based, inclusive). Creates `<ref.fa>.fai`.

### `fqidx`
Index FASTQ (for random access).
```bash
samtools fqidx <in.fq>
```

### `dict`
Create a sequence dictionary (`.dict`) from a FASTA.
```bash
samtools dict <ref.fa> -o ref.dict
```

---

## File operations

### `sort`
Sort alignments.
```bash
samtools sort [-n] [-t TAG] [-l INT] [-m MEM] [-@ INT] -o <out.bam> <in.bam>
```
| Flag | Description |
|---|---|
| `-n` | Sort by read name (required before `fixmate`) |
| `-t TAG` | Sort by auxiliary tag |
| `-l INT` | Compression level 0–9 |
| `-m MEM` | Memory per thread (e.g. `2G`) |
| `-@ INT` | Threads |

### `view`
Filter, convert, and subset alignments.
```bash
samtools view [options] <in.bam> [region ...]
```
| Flag | Description |
|---|---|
| `-b` | Output BAM |
| `-C` | Output CRAM |
| `-h` | Include header |
| `-H` | Print header only |
| `-F INT` | Skip reads with any flag bit set (e.g. `-F 4` mapped only) |
| `-f INT` | Keep reads with all flag bits set |
| `-q INT` | Minimum MAPQ |
| `-o FILE` | Output file |
| `-@ INT` | Threads |
| `-c` | Count reads instead of printing |
| `--subsample FLOAT` | Subsample fraction (0.0–1.0) |

Common flag values: `4`=unmapped, `8`=mate unmapped, `16`=reverse strand, `256`=secondary, `512`=QC fail, `1024`=duplicate, `2048`=supplementary.

### `merge`
Merge sorted BAMs.
```bash
samtools merge [-n] [-@ INT] -o out.bam in1.bam in2.bam [...]
```

### `cat`
Concatenate BAMs (no re-sorting, headers must be compatible).
```bash
samtools cat -o out.bam in1.bam in2.bam
```

### `split`
Split by read group.
```bash
samtools split -f '%*_%!.bam' input.bam
```

### `collate`
Shuffle so read pairs are adjacent (required before `fastq` for paired-end).
```bash
samtools collate -u -O input.bam
```

### `import`
Convert FASTA/FASTQ to BAM.
```bash
samtools import -1 R1.fq -2 R2.fq -o out.bam
```

### `fastq` / `fasta`
Convert BAM to FASTQ or FASTA.
```bash
samtools fastq [-1 R1.fq] [-2 R2.fq] [-0 other.fq] [-s singleton.fq] [-n] <in.bam>
samtools fasta <in.bam> > out.fa
```
`-n` preserves read names without `/1` `/2` suffixes.

---

## Editing

### `fixmate`
Fill in mate information (run after `sort -n`).
```bash
samtools fixmate -m <namesorted.bam> <out.bam>
```
`-m` adds ms (mate score) tag required by `markdup`.

### `markdup`
Mark or remove duplicate reads (run after coordinate sort + fixmate).
```bash
samtools markdup [-r] [-@ INT] <in.bam> <out.bam>
```
| Flag | Description |
|---|---|
| `-r` | Remove duplicates instead of marking |
| `-s` | Print statistics |
| `-f FILE` | Write stats to file |

### `calmd`
Recalculate MD/NM tags.
```bash
samtools calmd -b input.bam ref.fa > output.bam
```

### `addreplacerg`
Add or replace `@RG` header lines and RG tags.
```bash
samtools addreplacerg -r 'ID:sample1\tSM:sample1\tPL:ILLUMINA' -o out.bam in.bam
```

### `reheader`
Replace BAM header.
```bash
samtools reheader new_header.sam input.bam > output.bam
```

### `ampliconclip`
Soft-clip primer sequences from amplicon data.
```bash
samtools ampliconclip -b primers.bed -o clipped.bam input.bam
```

---

## Statistics & QC

### `flagstat`
Summary alignment statistics.
```bash
samtools flagstat [-@ INT] <in.bam>
```

### `stats`
Detailed statistics (use with `plot-bamstats`).
```bash
samtools stats [-r ref.fa] <in.bam> > stats.txt
grep ^SN stats.txt | cut -f2-    # summary numbers
grep ^IS stats.txt | cut -f2-    # insert sizes
```

### `depth`
Per-position read depth.
```bash
samtools depth [-a] [-q INT] [-Q INT] [-r region] <in.bam> > depth.tsv
```
`-a` outputs all positions including zero-coverage.

### `coverage`
Per-chromosome coverage summary.
```bash
samtools coverage <in.bam>
```

### `idxstats`
Per-reference read counts (requires index).
```bash
samtools idxstats <in.bam>
```

### `quickcheck`
Verify BAM is not truncated.
```bash
samtools quickcheck <in.bam> && echo "OK"
```

---

## Variant / pileup

### `mpileup`
Multi-way pileup (used upstream of bcftools call).
```bash
samtools mpileup -f ref.fa -o pileup.txt input.bam
samtools mpileup -f ref.fa -g -o raw.bcf input.bam   # for bcftools
```

### `consensus`
Generate consensus sequence from aligned reads.
```bash
samtools consensus -f fasta -o consensus.fa input.bam
```
