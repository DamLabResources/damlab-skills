---
name: ncbi-edirect
description: Search NCBI databases and download papers, sequences, and records using
  NCBI EDirect CLI tools. Use when searching PubMed or PMC for literature, downloading
  abstracts or full-text papers, fetching GenBank/RefSeq sequences, linking records
  across NCBI databases, or parsing XML output from Entrez. Triggers on tasks involving
  PubMed, PMC, literature search, paper download, NCBI, esearch, efetch, elink,
  xtract, GenBank, SRA, gene, taxonomy, or Entrez.
---

# NCBI EDirect

## Environment

```bash
ESEARCH=~/.cursor/skills/ncbi-edirect/bin/esearch
EFETCH=~/.cursor/skills/ncbi-edirect/bin/efetch
EFILTER=~/.cursor/skills/ncbi-edirect/bin/efilter
ELINK=~/.cursor/skills/ncbi-edirect/bin/elink
XTRACT=~/.cursor/skills/ncbi-edirect/bin/xtract
EPOST=~/.cursor/skills/ncbi-edirect/bin/epost
EINFO=~/.cursor/skills/ncbi-edirect/bin/einfo
TRANSMUTE=~/.cursor/skills/ncbi-edirect/bin/transmute
NQUIRE=~/.cursor/skills/ncbi-edirect/bin/nquire

# nquire env vars (control the internal HTTP client used by all CLI tools)
export NQUIRE_HELPER=wget    # use wget instead of curl (fixes curl --http1.0 SSL failures)
export NQUIRE_TIMEOUT=10     # connection timeout in seconds (default 20)
```

## Subcommands

**Search & Filter**
- `esearch` — query any NCBI database (PubMed, PMC, nuccore, protein, gene, sra, …)
- `efilter` — refine a piped result set by date, publication type, organism, sequence properties, etc.
- `epost` — upload a list of UIDs/accessions to the Entrez history server

**Fetch**
- `efetch` — download records in any supported format (abstract, xml, fasta, gb, medline, …)

**Link**
- `elink` — follow cross-database links or find related records (e.g. pubmed → protein, cited-by, cites)

**Parse**
- `xtract` — extract fields from Entrez XML into tab-delimited tables
- `transmute` — convert or normalize XML, JSON, ASN.1, and other formats

**Utilities**
- `einfo` — list available databases, fields, and link names
- `nquire` — low-level HTTP fetch of any NCBI URL

## Common patterns

**Search PubMed and download abstracts:**
```bash
$ESEARCH -db pubmed -query "CRISPR base editing [Title] AND 2023 [PDAT]" |
$EFETCH -format abstract > abstracts.txt
```

**Download PubMed records as structured TSV (PMID, year, title, first author):**
```bash
$ESEARCH -db pubmed -query "prime editing [Title] AND review [PT]" |
$EFETCH -format xml |
$XTRACT -mixed -pattern PubmedArticle \
  -element MedlineCitation/PMID \
  -first PubDate/Year \
  -element ArticleTitle \
  -first Author/LastName > results.tsv
```

**Download full-text XML from PubMed Central:**
```bash
$ESEARCH -db pmc -query "ADAR base editing [Title]" |
$EFETCH -format xml > pmc_fulltext.xml
```

**Filter to free full-text articles from the last year:**
```bash
$ESEARCH -db pubmed -query "nanopore sequencing [Title]" |
$EFILTER -pub free -released last_year |
$EFETCH -format abstract
```

**Fetch a GenBank record by accession:**
```bash
$EFETCH -db nuccore -id NC_000913.3 -format gb > ecoli_k12.gb
```

**Fetch a FASTA sequence:**
```bash
$EFETCH -db nuccore -id NM_007294.4 -format fasta > brca1.fa
```

**Follow links: PubMed → citing articles (NIH Open Citation):**
```bash
$ESEARCH -db pubmed -query "Anzalone AV [AUTH] AND 2019 [PDAT]" |
$ELINK -cited |
$EFILTER -days 365 |
$EFETCH -format abstract
```

**Pipe xtract output to csvtk for further analysis:**
```bash
CSVTK=~/.cursor/skills/csvtk/bin/csvtk
$ESEARCH -db pubmed -query "CRISPR [MeSH] AND 2020:2024 [PDAT]" |
$EFETCH -format xml |
$XTRACT -mixed -pattern PubmedArticle \
  -element MedlineCitation/PMID PubDate/Year ArticleTitle |
$CSVTK -t -H freq -f 2 | sort -k2 -rn
```

## Troubleshooting

**esearch / efetch hang without output** — `nquire` (the internal HTTP client used by
all CLI tools) defaults to `curl --http1.0`. This can fail silently with an SSL
`bad extension` error on modern OpenSSL (3.x) + current NCBI servers. Fix:
```bash
export NQUIRE_HELPER=wget   # set before running any esearch/efetch/elink call
```
If wget is also unavailable, use the **curl + xtract fallback** in patterns.md instead.

**`-help` shows an FTP 403 error** — nquire checks for EDirect version updates over
`ftp://ftp.ncbi.nlm.nih.gov` only when `-help` is invoked. FTP may be blocked in
your environment; this does not affect real queries.

**PubMed XML contains `<i>`, `<b>`, `<sup>` tags** — always pass `-mixed` to `xtract`
when parsing `pubmed` or `pmc` format XML, or xtract will error and drop affected fields.

## Full flag reference

To look up all flags for a specific subcommand:
```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/ncbi-edirect/reference.md
```
Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
```bash
grep -A 20 "keyword" ~/.cursor/skills/ncbi-edirect/patterns.md
```
[patterns.md](patterns.md)
