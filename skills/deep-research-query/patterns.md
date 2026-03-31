# Deep Research Query — Patterns

Reusable patterns collected from real tasks. Each entry has a title, context, and runnable example.

---

### Scaffold project directory and write search log

**Context:** Create the standard project directory layout at the start of a search session (Phase 0), then write `search_log.md` immediately after the Phase 2 search completes.

```bash
PROJECT_DIR="$HOME/research/crispr-hiv-cure"   # set from user input or Phase 0 default
mkdir -p "$PROJECT_DIR/data"

# --- write after Phase 2 search completes ---
SEARCH_DATE=$(date +%Y-%m-%d)
QUERY='(CRISPR[TIAB] OR ...) AND (HIV[TIAB] OR ...) AND (cure[TIAB] OR ...)'
TOTAL_RETRIEVED=455
AFTER_FILTERING=262

cat > "$PROJECT_DIR/data/search_log.md" << EOF
# Search Log

- **Database:** PubMed/MEDLINE
- **Date:** $SEARCH_DATE
- **Query:**

\`\`\`
$QUERY
\`\`\`

- **Total retrieved:** $TOTAL_RETRIEVED
- **After eligibility filtering:** $AFTER_FILTERING
EOF

echo "Project directory ready: $PROJECT_DIR"
```

Expected layout after Phase 2 + Phase 4 complete:

```
<project_dir>/
  data/
    pmids.txt        # one PMID per line
    records.xml      # full PubMed XML
    records.tsv      # PMID / year / journal / title / authors / abstract
    search_log.md    # query, date, counts
  refs.bib           # BibTeX bibliography (generated in Phase 4)
  review.md          # Markdown draft
  review.docx        # Final rendered output
```

---

### Generate .bib from PubMed XML and render .docx with bibliography

**Context:** After a Phase 4 draft is written using `[@PMID_XXXXXXXX]` cite markers, convert `data/records.xml` to `refs.bib`, then render `review.docx` with pandoc-citeproc so that numbered in-text citations and a bibliography section are produced automatically.

**Step 1 — Generate `refs.bib`:**

```python
#!/usr/bin/env python3
"""
xml_to_bib.py  —  convert PubMed XML to BibTeX
Usage: python3 xml_to_bib.py data/records.xml refs.bib
"""
import sys, re, xml.etree.ElementTree as ET

def itertext(el):
    return "".join(el.itertext()) if el is not None else ""

def make_bib_entry(article):
    mc = article.find("MedlineCitation")
    if mc is None:
        return None

    pmid   = itertext(mc.find("PMID"))
    art    = mc.find("Article") or mc

    # Title
    title  = itertext(art.find("ArticleTitle")).strip().rstrip(".")

    # Authors  → "Last, F and Last, F and ..."
    authors = []
    for auth in art.findall(".//Author"):
        ln = itertext(auth.find("LastName"))
        fn = itertext(auth.find("ForeName"))
        if ln:
            authors.append(f"{ln}, {fn}".strip(", "))
    author_str = " and ".join(authors) if authors else "Unknown"

    # Journal / year / volume / issue / pages
    journal  = itertext(art.find(".//ISOAbbreviation") or art.find(".//Title"))
    ji       = art.find(".//JournalIssue")
    year     = itertext((ji.find(".//Year") if ji is not None else None)
                        or mc.find(".//PubDate/Year"))[:4] if ji is not None else ""
    volume   = itertext(ji.find("Volume") if ji is not None else None)
    issue    = itertext(ji.find("Issue")  if ji is not None else None)
    pages    = itertext(art.find(".//MedlinePgn"))

    # DOI
    doi = ""
    for eid in art.findall(".//ELocationID"):
        if eid.get("EIdType") == "doi":
            doi = eid.text or ""
            break

    key = f"PMID_{pmid}"
    lines = [
        f"@article{{{key},",
        f"  author  = {{{author_str}}},",
        f"  title   = {{{title}}},",
        f"  journal = {{{journal}}},",
        f"  year    = {{{year}}},",
    ]
    if volume: lines.append(f"  volume  = {{{volume}}},")
    if issue:  lines.append(f"  number  = {{{issue}}},")
    if pages:  lines.append(f"  pages   = {{{pages}}},")
    if doi:    lines.append(f"  doi     = {{{doi}}},")
    lines.append(f"  pmid    = {{{pmid}}},")
    lines.append("}")
    return "\n".join(lines)

xml_path, bib_path = sys.argv[1], sys.argv[2]
tree = ET.parse(xml_path)
root = tree.getroot()

entries = []
for article in root.findall(".//PubmedArticle"):
    entry = make_bib_entry(article)
    if entry:
        entries.append(entry)

with open(bib_path, "w") as f:
    f.write("\n\n".join(entries) + "\n")

print(f"Wrote {len(entries)} BibTeX entries to {bib_path}")
```

Run:

```bash
python3 xml_to_bib.py <project_dir>/data/records.xml <project_dir>/refs.bib
```

**Step 2 — Render `.docx` with pandoc-citeproc:**

```bash
PANDOC=~/.cursor/skills/docx/bin/pandoc
STYLES=~/.cursor/skills/docx/styles

$PANDOC <project_dir>/review.md \
  --citeproc \
  --bibliography=<project_dir>/refs.bib \
  --reference-doc=$STYLES/nih-proposal-template.docx \
  -o <project_dir>/review.docx
```

Pandoc resolves every `[@PMID_XXXXXXXX]` marker to a numbered citation `[N]` (Vancouver style), deduplicates repeated citations, and appends a numbered **References** section at the end of the document. The bibliography section title and formatting inherit from the NIH template styles.
