---
name: bioinfo-best-practices
description: >
  Workflow conventions and best practices for bioinformatics analysis and
  debugging sessions. Use whenever helping a user explore, analyze, or debug
  biological data — sequencing reads, alignments, variant calls, genome
  assemblies, or any multi-step bioinformatics pipeline. Triggers on:
  "analyze", "debug", "investigate", "explore data", "QC", "pipeline",
  "troubleshoot alignment", "check coverage", "figure out why", or any open-
  ended bioinformatics investigation.
---

# Bioinformatics Best Practices

A methodology for collaborative, reproducible bioinformatics analysis sessions
between the agent and the user.

---

## Core principles

1. **Explainability and reproducibility first.** Every session that goes beyond
   a single ad-hoc command should produce a living `{project}.md` document.
2. **Iterate with the user.** Propose, confirm, then act — never run off and do
   everything at once.
3. **Respect context-window limits.** Avoid commands that dump sequences or
   enormous text blobs. Summarize; grep counts; head small samples.
4. **Move from exploration → scripts.** Initial exploration uses quick CLI
   one-liners; once the approach is confirmed, encode it in a documented,
   parameterized script.
5. **Make debugging human-readable.** When diagnosing issues, produce small,
   inspectable files alongside any summary statistics.

---

## Session workflow

### Step 0 — Orient before acting

Before running any commands:
- Ask the user what the goal is if it is not clear.
- Ask where the relevant files live (project directory, sample sheet, reference).
- Confirm the expected outputs.

Do **not** start exploring the filesystem until the goal is clear.

---

### Step 1 — Create the project log

At the start of any non-trivial analysis, create a Markdown log file:

```
{project_name}.md
```

Seed it with:

```markdown
# {Project Name}

**Date:** YYYY-MM-DD  
**Goal:** <one-sentence statement of what we are trying to accomplish>  
**Data location:** <path>  
**Reference:** <path or accession>

## File inventory

| File | Description | Size |
|------|-------------|------|
| ...  | ...         | ...  |

## Log

### YYYY-MM-DD — Session start
- Goal confirmed with user: ...
```

Ask the user to confirm the goal and file inventory before proceeding.

---

### Step 2 — Exploration (interactive CLI)

Use quick, bounded CLI commands to understand the data. Rules:
- **Never** pipe raw sequences to stdout in a way that fills the context window.
  Count, summarize, or head instead.
- **Prefer summary statistics** over raw content:
  - Read counts: `seqkit stats`, `samtools flagstat`
  - Coverage depth: `samtools depth | awk` summaries, not raw per-base output
  - Variant counts: `bcftools stats | grep ^SN`
- If files are large (>1 GB, or >1 M reads), **downsample** before debugging:
  ```bash
  seqkit sample -p 0.01 input.fastq.gz -o debug_1pct.fastq.gz
  samtools view -s 0.01 -b input.bam -o debug_1pct.bam
  ```
- When uncertain about a file format or content, look at a small slice:
  ```bash
  seqkit head -n 5 file.fastq.gz          # first 5 reads
  samtools view input.bam | head -n 5     # first 5 alignments (no sequences)
  csvtk head -n 10 table.tsv              # first 10 rows of a table
  ```

After each exploration step, append findings to `{project}.md`:

```markdown
### YYYY-MM-DD — Exploration: <topic>
**Command:** `<exact command run>`  
**Finding:** <what was learned>  
**Next question:** <what to investigate next>
```

Then **pause and summarize to the user** before continuing. Ask if the findings
match expectations before moving forward.

---

### Step 3 — Propose and confirm the approach

Before running any multi-step analysis:
1. Write out the proposed steps in plain language.
2. Ask the user if the approach makes sense or if there are constraints to
   consider (e.g., reference genome version, aligner preference, memory limits).
3. Record the confirmed plan in `{project}.md` under a `## Plan` heading.

Do not proceed to Step 4 without explicit user confirmation.

---

### Step 4 — Implement as a parameterized script

Once the exploratory approach is validated, encode it in a script rather than
running ad-hoc commands:

- **Python** for data wrangling, parsing, or visualization.
- **Bash** for straightforward linear pipelines.
- **Snakemake** for multi-sample or multi-step pipelines with dependencies.

Script conventions:
- All input paths and key parameters go at the top as variables (bash) or
  `argparse` arguments (Python) — never hardcoded mid-script.
- Include a header docstring/comment block: purpose, author, date, usage.
- Log progress to stderr, not stdout (stdout is reserved for data).
- Test on the downsampled debug file before running on full data.

After creating the script, append to `{project}.md`:

```markdown
### YYYY-MM-DD — Script: `{script_name}`
**Purpose:** ...  
**Usage:** `python {script_name}.py --input ... --output ...`  
**Tested on:** debug_1pct sample  
**Full run:** pending user confirmation
```

Ask the user to review the script before running it on full data.

---

### Step 5 — Debugging protocol

When something is wrong (unexpected output, failing step, suspicious results):

1. **Narrow the scope first.** Downsample to a small file that reproduces the
   problem.
2. **Inspect intermediate files** at human-readable scale (10–100 records).
3. **Produce a small exemplar file** that clearly shows the bug — this can be
   shared, version-controlled, and used as a test case.
4. **Avoid** commands that print thousands of lines. Use `| head`, `| wc -l`,
   or aggregate with `awk`/`csvtk`.
5. State a hypothesis before running diagnostic commands. Record the hypothesis
   in `{project}.md`, then record whether it was confirmed or refuted.

Debugging log format:

```markdown
### YYYY-MM-DD — Debug: <symptom>
**Hypothesis:** ...  
**Test command:** `...`  
**Result:** ...  
**Conclusion:** confirmed / refuted  
**Next step:** ...
```

---

### Step 6 — Wrap up and document

At the end of a session:
- Summarize findings in `{project}.md` under a `## Summary` heading.
- List all scripts produced and their purpose.
- Note any caveats, open questions, or follow-up tasks.
- Ask the user if there is anything else to record before closing.

---

## Quick-reference checklist

| Stage | Action | Confirm with user? |
|-------|--------|--------------------|
| 0 | Clarify goal and file locations | Yes |
| 1 | Create `{project}.md`, seed file inventory | Yes — confirm goal |
| 2 | Explore with bounded CLI commands | Yes — share findings |
| 3 | Propose analysis approach | Yes — get sign-off |
| 4 | Write parameterized script, test on subsample | Yes — review script |
| 5 | Debug with small exemplar files | Yes — state hypothesis |
| 6 | Document summary, caveats, follow-ups | Yes |

---

## Anti-patterns (never do these)

- Running `cat large_file.fastq` or printing full sequences to the terminal.
- Executing a full multi-step pipeline without first confirming the plan.
- Hardcoding sample names or paths inside scripts.
- Reporting only counts — always interpret what the number means.
- Skipping the project log for "quick" tasks that turn out to be non-trivial.
- Using `samtools view` without `| head` when exploring BAM content.

---

## Patterns

Reusable real-world patterns accumulated over time. To search:

```bash
grep -A 20 "keyword" ~/.cursor/skills/bioinfo-best-practices/patterns.md
```

[patterns.md](patterns.md)
