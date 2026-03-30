---
name: deep-research-query
description: >
  Plan and execute rigorous literature searches and evidence syntheses for
  biomedical, computational biology, and general scientific topics. Use when an
  agent must build a search strategy, search multiple databases, screen and
  document records, write review methods or review-style summaries, or prepare a
  reproducible evidence map or review. Triggers on: "literature search",
  "systematic review", "scoping review", "evidence synthesis", "search
  strategy", "PubMed search", "review methods", "PICO", "narrative review",
  "grey literature", "citation screening", "evidence map", "deep research".
---

# Deep Research Query

Use this skill to plan and execute a rigorous literature search, then turn the findings into a review-ready evidence base. Prefer reproducibility, transparency, and explicit scope control over speed.

**This is a collaborative, multi-turn skill.** Do not execute silently. Narrate each phase, surface surprises and judgment calls, ask clarifying questions before proceeding, and invite the user to redirect at every major checkpoint.

## When to use

Use this skill when the task involves any of the following:

* building a systematic, scoping, or narrative literature search
* finding primary studies, review articles, methodological guidance, or consensus statements
* drafting a review methods section or a review outline
* comparing evidence across papers, databases, or search strategies
* documenting query logic, screening decisions, and synthesis choices

## Core principles

1. Start with a precise question.
2. Match the review type to the question.
3. Search more than one source.
4. Record the exact search strings and dates.
5. Prefer controlled vocabulary plus free-text synonyms.
6. Use grey literature when completeness matters.
7. Screen in duplicate when the task is systematic.
8. Separate search methods from synthesis methods.
9. Distinguish evidence summary from interpretation.
10. Do not claim completeness unless the search design supports it.

---

## Phase 0 — Clarifying questions (ALWAYS run first)

Before doing anything else, ask the user the following questions. Present them together in a single, clearly formatted block so the user can answer them all at once. Adapt or skip questions that the user has already answered in their initial prompt.

**Questions to ask:**

1. **Review type** — Is this intended as a systematic review (exhaustive and reproducible), a scoping review (broad mapping), or a narrative/rapid review (framing and synthesis)? Or are you unsure and want a recommendation?
2. **Question framing** — What is the core question? If you can, state the population or domain, the phenomenon or intervention, and the outcome or goal. (PICO, SPIDER, or plain language are all fine.)
3. **Scope limits** — Are there date ranges, languages, study designs, or species/model systems to include or exclude?
4. **Known anchors** — Are there 2–5 papers, authors, or keywords you already know are relevant? These serve as sentinel records to calibrate the search.
5. **Intended use** — Will this feed a manuscript, a grant, an internal report, or something else? This shapes how much depth and documentation is needed.
6. **Depth vs. speed tradeoff** — Do you need a thorough search across multiple databases, or is a targeted rapid search acceptable?
7. **Project directory** — Where should I save the project files (PMID list, downloaded records, review draft, bibliography)? If you have no preference, I will propose a path based on the review topic (e.g. `~/research/<topic-slug>/`).

Do not proceed to Phase 1 until the user has responded. Summarize the answers back in one or two sentences to confirm understanding before continuing.

### Project directory setup (run immediately after Phase 0 answers)

Once the user confirms or provides a project directory, create it and confirm the path before continuing:

```
<project_dir>/
  data/
    pmids.txt          # one PMID per line — written after Phase 2 search
    records.xml        # full PubMed XML for all retrieved records
    records.tsv        # PMID / year / journal / title / authors / abstract
    search_log.md      # exact query string, database, date, result count
  refs.bib             # generated in Phase 4 before rendering
  review.md            # Markdown draft — generated in Phase 4
  review.docx          # final rendered output — generated in Phase 4
```

If the user has not specified a path, propose `~/research/<slug>/` where `<slug>` is a short lowercase hyphenated version of the review topic (e.g. `~/research/crispr-hiv-cure/`), state the proposed path explicitly, and wait for confirmation before creating it.

---

## Phase 1 — Search planning (narrate before executing)

After receiving clarifying answers:

1. Propose the review type and question framing. State the PICO/SPIDER/concept-block structure explicitly.
2. List the concept blocks and show the synonym expansion for each (synonyms, acronyms, spelling variants, MeSH or Emtree terms where applicable).
3. Propose the database list and explain why each is included or excluded.
4. Show a draft search string for the primary database.
5. **Pause and ask:** "Does this search strategy look right? Are there synonyms, terms, or databases I should add or remove before I run it?"

Do not run the search until the user approves the strategy.

### Review-type reference

* **Systematic review**: focused question, explicit eligibility criteria, reproducible search, dual screening.
* **Scoping review**: broad area mapping, concept clarification, gap identification.
* **Narrative review**: topic overview, synthesis and framing, not exhaustive.
* **Methodological review**: literature about how to search, screen, appraise, or report reviews.

If the question is too broad for a systematic review, narrow it or switch to scoping review logic.

### Source selection reference

* biomedical core: PubMed/MEDLINE, Embase, CENTRAL
* broader coverage: Scopus or Web of Science
* qualitative or interdisciplinary work: add subject-specific databases
* grey literature: dissertations, theses, conference abstracts, preprints, trial registries, reports
* citation chasing: forward and backward reference tracking

Do not rely on a single database. Use Google Scholar only as a supplementary source.

### Search construction rules

* Combine synonyms with OR inside a concept block.
* Combine concept blocks with AND.
* Include both free text and subject headings where supported.
* Use truncation and wildcards carefully; do not over-truncate into noise.
* Apply filters only when justified.
* Keep a copy of the exact final search string for each source.

---

## Phase 2 — Initial search and theme report (present before synthesizing)

Run the approved search. Then immediately save all artifacts to the project directory:

```bash
# Save PMID list
<one PMID per line> > <project_dir>/data/pmids.txt

# Save full XML (used for .bib generation in Phase 4)
<fetched PubMed XML> > <project_dir>/data/records.xml

# Save structured TSV (PMID / year / journal / title / authors / abstract)
<parsed TSV> > <project_dir>/data/records.tsv

# Write search log
cat > <project_dir>/data/search_log.md << EOF
# Search Log
- Database: PubMed/MEDLINE
- Date: <YYYY-MM-DD>
- Query: <exact query string>
- Total retrieved: <N>
- After eligibility filtering: <N>
EOF
```

Then, before drafting any synthesis:

1. Report the raw result counts per database and the de-duplicated total.
2. Present the **major themes** found — 4–8 high-level clusters that emerge from the titles/abstracts screened. For each theme, give:
   * a one-line label
   * 2–3 representative citations
   * an estimated share of the retrieved literature
3. Flag any **unexpected territory** — topics, populations, or study types that appeared but were not part of the original query.
4. **Ask the user:**
   * "Do these themes match what you were expecting?"
   * "Are there themes here you want to deprioritize or exclude?"
   * "I also found evidence touching on [unexpected topic A] and [unexpected topic B] — would either of these be worth folding into the review?"
   * "Should I run any additional searches before drafting (e.g., a targeted search on [gap area], a citation-chasing pass on [key paper], or a grey literature sweep)?"

Do not begin drafting the synthesis until the user confirms the thematic scope.

---

## Phase 3 — Optional additional searches

If the user requests additional searches based on Phase 2 feedback:

1. State the new search rationale (what gap it fills).
2. Show the new search string.
3. Run it, report the new record count, and note how many records were already retrieved.
4. Update the theme map with any new themes or additional coverage.
5. Briefly confirm with the user before moving to drafting: "The updated evidence base now covers [summary]. Ready to proceed to drafting?"

---

## Phase 4 — Drafting

Draft the requested output (synthesis, methods section, results section, or review outline). During drafting:

* Follow the writing rules below.
* Cite sources explicitly; do not paraphrase without attribution.
* Mark uncertainty and evidence gaps inline.
* Where the evidence is genuinely thin or conflicting, say so rather than smoothing it over.

### Citation markers (REQUIRED)

Every in-text citation **must** use a pandoc-citeproc marker: `[@PMID_XXXXXXXX]`, where `XXXXXXXX` is the PubMed ID of the cited paper. Do **not** write free-text citations like "Author et al. (Year)" — always use the marker so that cross-references and the bibliography are generated automatically.

Multiple citations at one location: `[@PMID_25049410; @PMID_27974196]`.

Do not hand-write citation numbers. Pandoc-citeproc assigns and reconciles them. Multiple uses of the same PMID in the text resolve to the same bibliography entry.

### After the Markdown draft is complete

Run the following steps before presenting the final document to the user:

**Step 1 — Generate `refs.bib` from `<project_dir>/data/records.xml`:**

See the "Generate .bib from PubMed XML" pattern in `patterns.md` for the full Python script. Each cited PMID must appear in `refs.bib` with cite key `PMID_{pmid}`.

**Step 2 — Save the Markdown draft:**

```bash
<draft text> > <project_dir>/review.md
```

**Step 3 — Render to `.docx` with bibliography:**

Use the pandoc binary from the docx skill. Resolve its path with:
```bash
readlink -f "$(dirname <path-to-docx-SKILL.md>)/bin/pandoc"
```
where `<path-to-docx-SKILL.md>` is the absolute path you used to read the docx SKILL.md.
`$PANDOC` and `$STYLES` below are placeholders for those resolved paths.

```bash
$PANDOC <project_dir>/review.md \
  --citeproc \
  --bibliography=<project_dir>/refs.bib \
  --reference-doc=$STYLES/nih-proposal-template.docx \
  -o <project_dir>/review.docx
```

Pandoc-citeproc resolves all `[@PMID_...]` markers, inserts numbered in-text citations (Vancouver style by default), and appends a formatted bibliography section at the end of the document.

**Do not produce a `.docx` without a bibliography.** If `records.xml` is missing or a cited PMID is not in the XML, report the missing IDs and fetch them before rendering.

### Writing order for a full review

1. State the question and review type.
2. Explain search sources and date range.
3. Describe search terms and strategy development.
4. Explain screening and eligibility criteria.
5. Describe extraction and appraisal.
6. Summarize the evidence base.
7. Report major findings and limitations.
8. Note gaps, uncertainty, and future directions.

### Methods section rules

* Name the databases and other sources searched.
* Provide the search date.
* Include the core concept blocks or an appendix search string.
* State inclusion and exclusion criteria.
* Describe screening and conflict resolution.
* Name risk-of-bias or quality appraisal tools.
* State how data were extracted and synthesized.
* Describe any protocol registration.
* Mention deviations from the protocol.

### Results section rules

* Report counts at each stage.
* Report what types of studies were found.
* Summarize the dominant findings by theme or outcome.
* Describe heterogeneity, inconsistencies, or null findings.
* Reference tables and figures explicitly.
* Avoid methodological detail that belongs in Methods.
* Avoid interpretation that belongs in Discussion.

---

## Phase 5 — Implied-concept gap check (ALWAYS run after drafting)

After producing a draft, perform a self-audit before presenting it to the user. Ask yourself:

> "What concepts, populations, comparators, or mechanisms are *implied* by what I wrote but were never explicitly searched or cited?"

Make a short list of these implied-but-unsearched concepts. Then ask the user:

"I noticed the draft implies the following concepts that we didn't explicitly search:

* [implied concept A] — e.g., the draft assumes [mechanism/population/method] but we didn't retrieve literature on it directly
* [implied concept B] — ...

Would you like me to run targeted searches on any of these before finalizing? Or should I flag them as limitations instead?"

If the user wants them searched, return to Phase 3 for each one, then revise the draft accordingly before finalizing.

---

## Operational defaults

* Use concise, exact language.
* Prefer names, versions, accessions, and dates over vague descriptions.
* Mark uncertainty explicitly.
* Keep auditability over elegance when those conflict.
* When evidence is weak or incomplete, say so directly.
* **Never proceed silently through a phase gate.** Always surface your reasoning and invite redirection.

## Refusal boundary

Do not pretend a search is exhaustive if the scope, sources, or limits do not justify that claim. Do not fabricate citations, screening outcomes, or study counts. When the search is incomplete, label it as partial and explain what is missing.
