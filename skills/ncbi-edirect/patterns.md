# NCBI EDirect — Patterns

Reusable patterns collected from real tasks. Each entry has a title, context, and runnable example.

<!-- Add patterns below as they arise -->

### Extract full citation fields from PubMed XML for .bib generation

**Context:** After fetching `records.xml`, pull every field needed for a BibTeX entry in a single `xtract` pass. Output is a TSV suitable for review or for feeding the `xml_to_bib.py` script in the deep-research-query patterns.

```bash
XTRACT=~/.cursor/skills/ncbi-edirect/bin/xtract

$XTRACT -mixed -input records.xml \
  -pattern PubmedArticle \
  -element MedlineCitation/PMID \
  -first PubDate/Year \
  -element ISOAbbreviation \
  -element ArticleTitle \
  -block AuthorList -sep " and " -tab "|" -element "Author/LastName ForeName" \
  -element JournalIssue/Volume \
  -element JournalIssue/Issue \
  -element MedlinePgn \
  -element "ELocationID[@EIdType='doi']" \
> citation_fields.tsv
```

Columns (tab-separated): `pmid | year | journal_iso | title | authors | volume | issue | pages | doi`

The same data is also fully accessible via Python from the raw XML — see the `xml_to_bib.py` script in `deep-research-query/patterns.md` for a complete BibTeX converter that reads `records.xml` directly.

---

### curl + xtract fallback when CLI tools hang (HTTP/1.0 SSL issue)

**Context:** `esearch` and `efetch` use `nquire` internally, which forces `curl --http1.0`.
This causes an SSL `bad extension` failure on modern OpenSSL + current NCBI servers.
Use raw `curl` GET requests (HTTP/1.1 by default) + `xtract` as a drop-in replacement.
Set `XTRACT=~/.cursor/skills/ncbi-edirect/bin/xtract` before running.

```bash
# Step 1 — search: get all PMIDs via Entrez history server
SEARCH=$(curl -s --max-time 15 \
  "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=YOUR+QUERY+HERE&retmax=200&usehistory=y&retmode=xml")
WEBENV=$(echo "$SEARCH" | grep -o '<WebEnv>[^<]*</WebEnv>' | sed 's/<[^>]*>//g')
QKEY=$(echo "$SEARCH"  | grep -o '<QueryKey>[^<]*</QueryKey>' | sed 's/<[^>]*>//g')
COUNT=$(echo "$SEARCH"  | grep -o '<Count>[^<]*</Count>' | head -1 | sed 's/<[^>]*>//g')
echo "Found $COUNT records"

# Step 2 — fetch all records as XML using the history server (no URL length limit)
curl -s --max-time 60 \
  "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key=${QKEY}&WebEnv=${WEBENV}&rettype=xml&retmode=xml&retmax=200" \
  -o records.xml

# Step 3 — extract fields with xtract (-mixed handles HTML tags in PubMed abstracts)
$XTRACT -mixed -input records.xml \
  -pattern PubmedArticle \
  -element MedlineCitation/PMID \
  -first PubDate/Year \
  -element ISOAbbreviation \
  -element ArticleTitle \
  -block AuthorList -sep ", " -tab " | " -element LastName \
> papers.tsv
```

URL-encode the query term: spaces → `+`, `[` → `%5B`, `]` → `%5D`.
Example: `"Dampier W [AUTH] AND HIV"` → `Dampier+W+%5BAUTH%5D+AND+HIV`

### Search PubMed by author and date, download abstracts

**Context:** Retrieve all abstracts from a specific author in a date range.

```bash
$ESEARCH -db pubmed -query "Dampier W [AUTH] AND 2020:2024 [PDAT]" |
$EFETCH -format abstract > dampier_abstracts.txt
```

### Build a TSV of PMID / year / journal / title from a keyword search

**Context:** Get a quick spreadsheet of papers matching a topic for literature review.

```bash
$ESEARCH -db pubmed -query "CRISPR base editing [Title] AND human [ORGN]" |
$EFETCH -format xml |
$XTRACT -mixed -pattern PubmedArticle \
  -element MedlineCitation/PMID \
  -first PubDate/Year \
  -element ISOAbbreviation \
  -element ArticleTitle \
> papers.tsv
```

### Download free full-text XML from PMC for a topic

**Context:** Bulk-download structured full-text articles from PubMed Central (open access only).

```bash
$ESEARCH -db pmc -query "prime editing [Title] AND free full text [FILTER]" |
$EFETCH -format xml > pmc_articles.xml
```

### Get all papers that cite a known PMID (NIH Open Citation)

**Context:** Find downstream work that cites a landmark paper.

```bash
$ELINK -db pubmed -id 31634902 -cited |
$EFETCH -format abstract > citing_papers.txt
```

### Get reference list of a paper (what it cites)

**Context:** Pull the bibliography of a paper to identify primary sources.

```bash
$ELINK -db pubmed -id 31634902 -cites |
$EFETCH -format abstract > references.txt
```

### Filter to reviews published in the last year

**Context:** Quickly narrow a large result set to recent review articles.

```bash
$ESEARCH -db pubmed -query "nanopore sequencing [MeSH]" |
$EFILTER -pub review -released last_year |
$EFETCH -format abstract
```

### Fetch a GenBank record by accession

**Context:** Download a nucleotide record in GenBank flat-file format for inspection or annotation.

```bash
$EFETCH -db nuccore -id NC_000913.3 -format gb > ecoli_k12.gb
```

### Fetch a protein FASTA by accession

**Context:** Get a protein sequence for downstream alignment or structure work.

```bash
$EFETCH -db protein -id NP_001123887.1 -format fasta > protein.fa
```

### Fetch SRA run info for a BioProject

**Context:** Get run accessions and metadata before downloading raw sequencing data.

```bash
$ESEARCH -db sra -query "PRJNA257197 [BioProject]" |
$EFETCH -format runinfo -mode xml |
$XTRACT -mixed -pattern Row -element Run Spots Bases LibraryLayout SampleName > runinfo.tsv
```

### List all NCBI databases

**Context:** Explore what databases are searchable with EDirect.

```bash
$EINFO -dbs
```

### List searchable fields for a database

**Context:** Find valid field tags (e.g. [AUTH], [JOUR], [MeSH]) for query construction.

```bash
$EINFO -db pubmed -fields
```

### Post a list of PMIDs from a file and fetch abstracts

**Context:** Fetch records for a pre-assembled list of IDs (e.g. from a previous analysis).

```bash
$EPOST -db pubmed -input pmid_list.txt |
$EFETCH -format abstract > batch_abstracts.txt
```

### Cross-database link: PubMed → RefSeq proteins

**Context:** From a set of papers, find the associated RefSeq protein sequences.

```bash
$ESEARCH -db pubmed -query "conotoxin [MeSH] AND review [PT]" |
$ELINK -target protein |
$EFILTER -source refseq |
$EFETCH -format fasta > conotoxin_refseq.fa
```
