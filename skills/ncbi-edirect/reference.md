# NCBI EDirect — Full Reference

Binary directory: `~/.cursor/skills/ncbi-edirect/bin/`

Binaries: `esearch`, `efetch`, `efilter`, `elink`, `xtract`, `epost`, `einfo`, `transmute`, `nquire`

Each entry contains the verbatim `-help` output. Grep for a subcommand:
```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/ncbi-edirect/reference.md
```
Increase `-A` if output appears truncated.

---

## Search & Filter

### `esearch`

```
esearch 22.6

Query Specification

  -db            Database name
  -query         Query string

Spell Check

  -spell         Correct misspellings in query

Query Translation

  -translate     Show automatic term mapping
  -component     Individual term mapping items

Document Order

  -sort          Result presentation order

Sort Choices by Database

  gene           Chromosome, Gene Weight, Name, Relevance

  geoprofiles    Default Order, Deviation, Mean Value, Outliers, Subgroup Effect

  pubmed         First Author, Journal, Last Author, Pub Date, Recently Added,
                 Relevance, Title

  (sequences)    Accession, Date Modified, Date Released, Default Order,
                 Organism Name, Taxonomy ID

  snp            Chromosome Base Position, Default Order, Heterozygosity,
                 Organism, SNP_ID, Success Rate

Note

  All efilter shortcuts can also be used with esearch

Examples

  esearch -db pubmed -query "opsin gene conversion OR tetrachromacy"

  esearch -db pubmed -query "Garber ED [AUTH] AND PNAS [JOUR]"

  esearch -db nuccore -query "MatK [GENE] AND NC_0:NC_999999999 [PACC]"

  esearch -db protein -query "amyloid* [PROT]" |
  elink -target pubmed -label prot_cit |
  esearch -db gene -query "apo* [GENE]" |
  elink -target pubmed -label gene_cit |
  esearch -query "(#prot_cit) AND (#gene_cit)" |
  efetch -format docsum |
  xtract -pattern DocumentSummary -element Id Title
```

### `efilter`

```
efilter 22.6

Query Specification

  -query       Query string

Date Constraint

  -days        Number of days in the past
  -datetype    Date field abbreviation
  -mindate     Start of date range
  -maxdate     End of date range

Overview

  All efilter shortcuts can also be used with esearch

  Each shortcut is only legal for a specific database category

Publication Filters

  -pub         abstract, clinical, english, free, historical,
               journal, medline, preprint, published, retracted,
               retraction, review, structured
  -journal     pnas, "j bacteriol", ...
  -released    last_week, last_month, last_year, prev_years

Sequence Filters

  -country     usa:minnesota, united_kingdom, "pacific ocean", ...
  -feature     gene, mrna, cds, mat_peptide, ...
  -location    mitochondrion, chloroplast, plasmid, plastid
  -molecule    genomic, mrna, trna, rrna, ncrna
  -organism    animals, archaea, bacteria, eukaryotes, fungi,
               human, insects, mammals, plants, prokaryotes,
               protists, rodents, viruses
  -source      genbank, insd, pdb, pir, refseq, select, swissprot,
               tpa
  -division    bct, con, env, est, gss, htc, htg, inv, mam, pat,
               phg, pln, pri, rod, sts, syn, una, vrl, vrt
  -keyword     purpose
  -purpose     baseline, targeted

Gene Filters

  -status      alive
  -type        coding, pseudo

SNP Filters

  -class       acceptor, donor, coding, frameshift, indel,
               intron, missense, nonsense, synonymous

Assembly Filters

  -status      latest, replaced

Examples

  esearch -db pubmed -query "opsin gene conversion" |
  elink -related |
  efilter -query "tetrachromacy"

  esearch -db pubmed -query "opsin gene conversion" |
  efilter -mindate 2015
```

---

## Fetch

### `efetch`

```
efetch 22.6

Format Selection

  -format        Format of record or report
  -mode          text, xml, asn.1, json
  -style         master, conwithfeat

Direct Record Selection

  -db            Database name
  -id            Unique identifier or accession number
  -input         Read identifier(s) from file instead of stdin

Sequence Range

  -seq_start     First sequence position to retrieve
  -seq_stop      Last sequence position to retrieve
  -strand        1 = forward DNA strand, 2 = reverse complement
  -forward       Force strand 1
  -revcomp       Force strand 2

Gene Range

  -chr_start     Sequence range from 0-based coordinates
  -chr_stop        in gene docsum GenomicInfoType object

Sequence Flags

  -complexity    0 = default, 1 = bioseq, 3 = nuc-prot set
  -extend        Extend sequence retrieval in both directions
  -extrafeat     Bit flag specifying extra features
  -showgaps      Propagate component gaps

Subset Retrieval

  -start         First record to fetch
  -stop          Last record to fetch

Miscellaneous

  -raw           Skip database-specific XML modifications
  -express       Direct sequence retrieval in groups of 5
  -immediate     Express mode on a single record at a time

Format Examples

  -db            -format            -mode    Report Type
  ___            _______            _____    ___________

  (all)
                 docsum                      DocumentSummarySet XML
                 docsum             json     DocumentSummarySet JSON
                 full                        Same as native except for mesh
                 uid                         Unique Identifier List
                 url                         Entrez URL
                 xml                         Same as -format full -mode xml

  pmc
                 bioc                        PubTator Central BioC XML
                 medline                     MEDLINE
                 native             xml      pmc-articleset XML

  pubmed
                 abstract                    Abstract
                 apa                         PMID plus APA citation
                 bioc                        PubTator Central BioC XML
                 medline                     MEDLINE
                 native             asn.1    Pubmed-entry ASN.1
                 native             xml      PubmedArticleSet XML

  (sequences)
                 acc                         Accession Number
                 fasta                       FASTA
                 fasta              xml      TinySeq XML
                 fasta_cds_aa                FASTA of CDS Products
                 fasta_cds_na                FASTA of Coding Regions
                 gb                          GenBank Flatfile
                 gb                 xml      GBSet XML
                 gp                          GenPept Flatfile

  gene
                 full_report                 Detailed Report
                 gene_table                  Gene Table
                 native                      Gene Report
                 native             xml      Entrezgene-Set XML
                 tabular                     Tabular Report

  sra
                 native             xml      EXPERIMENT_PACKAGE_SET XML
                 runinfo            xml      SraRunInfo XML

  taxonomy
                 native                      Taxonomy List
                 native             xml      TaxaSet XML

Examples

  efetch -db pubmed -id 6271474,5685784 -format xml |
  xtract -pattern PubmedArticle -element MedlineCitation/PMID "#Author" \
    -block Author -position first -sep " " -element Initials,LastName \
    -block Article -element ArticleTitle

  efetch -db nuccore -id CM000177.6 -format gb -style conwithfeat -showgaps

  efetch -db protein -id 3OQZ_a -format fasta

  esearch -db protein -query "conotoxin AND mat_peptide [FKEY]" |
  efetch -format fasta -start 1 -stop 5
```

---

## Link

### `elink`

```
elink 22.6

Destination Database

  -related    Neighbors in same database
  -target     Links in different database

Direct Record Selection

  -db         Database name
  -id         Unique identifier(s)
  -input      Read identifier(s) from file instead of stdin

PubMed Citation Lookup*

  -cited      References to this paper
  -cites      Publication reference list

Command Mode

  -cmd        Command type

-cmd Options

  edirect     Instantiate results in ENTREZ_DIRECT message
  history     Save results in Entrez history server
  neighbor    Neighbors or links
  score       Neighbors with computed similarity scores
  acheck      All links available
  ncheck      Existence of neighbors
  lcheck      Existence of external links (LinkOuts)
  llinks      Non-library LinkOut providers
  llibs       All LinkOut providers
  prlinks     Primary LinkOut provider

Restrict Neighbor Links

  -name       Link name (e.g., pubmed_protein_refseq, pubmed_pubmed_citedin)

Note

  * -cited and -cites use the NIH Open Citation Collection
    dataset (see PMID 31600197) to follow reference lists

Examples

  esearch -db pubmed -query "lycopene cyclase" |
  elink -related |
  elink -target protein |
  efilter -organism rodents -source refseq |
  efetch -format docsum |
  xtract -pattern DocumentSummary -element AccessionVersion Title |
  grep -i carotene

  esearch -db pubmed -query "Beadle GW [AUTH] AND Tatum EL [AUTH]" |
  elink -cited |
  efilter -days 365 |
  efetch -format abstract

  elink -db pubmed -id 19880848 -cmd prlinks |
  xtract -pattern LinkSet -first Id -element ObjUrl/Url
```

---

## Post

### `epost`

```
epost 22.6

  -db        Database name
  -id        Unique identifier(s) or accession number(s)
  -format    uid or acc
  -input     Read identifier(s) from file instead of stdin

Examples

  echo 3OQZ_a | epost -db protein | efetch -format fasta

  epost -db protein -id 3OQZ_a | efetch -format fasta

  echo GCF_000001405.38 | epost -db assembly | efetch -format docsum

  echo PRJNA257197 | epost -db bioproject | efetch -format docsum
```

---

## Info

### `einfo`

```
einfo 22.6

Database Selection

  -dbs       Print all database names
  -db        Database name (or "all")

Data Summaries

  -fields    Print field names
  -links     Print link names

Field Example

  <Field>
    <Name>ALL</Name>
    <FullName>All Fields</FullName>
    <Description>All terms from all searchable fields</Description>
    <IsDate>N</IsDate>
    <IsNumerical>N</IsNumerical>
    <SingleToken>N</SingleToken>
    <Hierarchy>N</Hierarchy>
    <IsHidden>N</IsHidden>
    <IsTruncatable>Y</IsTruncatable>
    <IsRangable>N</IsRangable>
  </Field>
```

---

## Parse

### `xtract`

```
xtract 22.6

Overview

  Xtract uses command-line arguments to convert XML data into a tab-delimited table.

  -pattern places the data from individual records into separate rows.

  -element extracts values from specified fields into separate columns.

  -group, -block, and -subset limit element exploration to selected XML subregions.

Exploration Argument Hierarchy

  -pattern         Name of record within set
  -group             Use of different argument
  -block               names allows command-line
  -subset                control of nested looping

Path Navigation

  -path            Explore by list of adjacent object names

Element Selection

  -element         Print all items that match tag name
  -first           Only print value of first item
  -last            Only print value of last item
  -even            Only print value of even items
  -odd             Only print value of odd items
  -backward        Print values in reverse order

Conditional Execution

  -if              Element [@attribute] required
  -unless          Skip if element matches
  -and             All tests must pass
  -or              Any passing test suffices
  -else            Execute if conditional test failed
  -position        [first|last|outer|inner|even|odd|all]

String Constraints

  -equals          String must match exactly
  -contains        Substring must be present
  -excludes        Substring must be absent
  -starts-with     Substring must be at beginning
  -ends-with       Substring must be at end

Numeric Constraints

  -gt -ge -lt -le -eq -ne

Format Customization

  -ret             Override line break between patterns
  -tab             Replace tab character between fields
  -sep             Separator between group members
  -pfx             Prefix before group
  -sfx             Suffix after group
  -def             Default placeholder for missing fields
  -lbl             Insert arbitrary text

-element Constructs

  Tag              Caption
  Group            Initials,LastName
  Parent/Child     MedlineCitation/PMID
  Attribute        DescriptorName@MajorTopicYN
  Range            MedlineDate[1:4]
  Object Count     "#Author"
  Item Length      "%Title"
  Variable         "&NAME"

Numeric Processing

  -num -len -sum -min -max -inc -dec -sub -avg -dev -med -mul -div -mod

Character Processing

  -upper -lower -chain -title -encode -decode

Citation Functions

  -year            Extract first 4-digit year from string
  -month           Match first month name, return as integer
  -date            YYYY/MM/DD from -unit "PubDate" -date "*"
  -page            Get digits of first page number
  -auth            Convert GenBank authors to Medline form

Sequence Commands

  -insd            Generate INSDSeq extraction commands

Examples

  -pattern DocumentSummary -element Id -first Name Title

  -pattern PubmedArticle -block Author -sep " " -element Initials,LastName

  -pattern PubmedArticle -block MeshHeading \
    -if "@MajorTopicYN" -equals Y -sep " / " -element DescriptorName,QualifierName

  -pattern GenomicInfoType -element ChrAccVer ChrStart ChrStop
```

---

## Convert

### `transmute`

```
transmute 22.6

  transmute -j2x -set - -rec GeneRec       JSON to XML
  transmute -t2x -set Set -rec Rec -skip 1 TSV to XML
  transmute -filter ExpXml decode content   Decode base64 content
  transmute -normalize pubmed               Normalize PubMed XML
  transmute -head "<PubmedArticleSet>" -tail "</PubmedArticleSet>" \
    -pattern "PubmedArticleSet/*" -format   Reformat XML
```
