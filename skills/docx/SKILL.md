---
name: docx
description: Read, write, and track-change Microsoft Word (.docx) files. Use when
  reading document content or paragraph structure, extracting reviewer comments,
  listing or accepting/rejecting tracked changes, making find-and-replace edits
  with or without tracked revision markup, inserting or deleting text with author
  attribution, or converting between .docx and Markdown. Triggers on tasks involving
  .docx, Word documents, manuscript editing, track changes, document revisions,
  reviewer comments, or find-and-replace in Word files.
---

# docx

## Environment

```bash
DOCX_TOOL="~/.cursor/skills/docx/bin/python ~/.cursor/skills/docx/docx_tool.py"
PANDOC=~/.cursor/skills/docx/bin/pandoc
STYLES_DIR=~/.cursor/skills/docx/styles
```

## Subcommands — docx_tool.py

**Reading**
- `read FILE` — print all paragraph text (accepted view; includes hyperlink text)
- `paragraphs FILE` — numbered paragraph list with style names
- `get-paragraph FILE N` — print exact text of paragraph N (zero-based); use `--json` for style too
- `list-styles FILE [--type paragraph|character|table|numbering] [--json]` — list all styles defined in the document; use `--type paragraph` to see valid `--style` values for `insert`
- `comments FILE [--json]` — extract all reviewer comments (author, date, text)

**Tracked changes**
- `revisions list FILE [--json]` — list all tracked changes (type, text, author, date)
- `revisions accept FILE [-o OUT]` — accept all tracked changes and save
- `revisions reject FILE [-o OUT]` — reject all tracked changes and save

**Editing**
- `replace FILE OLD NEW [-o OUT] [--track] [--author NAME] [--normalize-quotes] [--allow-no-match]` — find-and-replace; `--track` records a tracked revision; exits 1 on 0 matches (see notes below)
- `insert FILE ANCHOR TEXT [-o OUT] [--track] [--author NAME] [--style NAME]` — insert text as a new paragraph after anchor; `--style` sets the paragraph style (e.g. `Caption`, `Heading 1`); `--track` appends as tracked insertion within the anchor paragraph (style flag ignored in track mode)
- `insert-picture FILE IMAGE [-o OUT] (--after-paragraph N | --after-anchor TEXT) [--width INCHES] [--height INCHES] [--caption TEXT] [--caption-style STYLE]` — insert an inline image after a paragraph; width/height in inches (one scales proportionally if the other is omitted; native size if both omitted); optional caption paragraph added immediately after the image
- `delete FILE TEXT [-o OUT] [--track] [--author NAME]` — delete matched text; `--track` marks as tracked deletion

## Subcommands — pandoc

**Reading .docx**
- `-f docx -t markdown` — convert to Markdown (plain text, structure preserved)
- `--track-changes=all` — include insertions/deletions as annotated spans
- `--track-changes=accept` — show document with all changes accepted
- `--track-changes=reject` — show document with all changes rejected

**Writing .docx**
- `-o output.docx` — write Markdown/HTML/RST input to a new Word document
- `--reference-doc=TEMPLATE.docx` — apply fonts, margins, and paragraph styles from a template; pandoc maps Markdown structure to named Word styles in the template

## Common patterns

**Read a manuscript as plain text:**
```bash
$DOCX_TOOL read manuscript.docx
```

**Read as Markdown (preserves headings, bold, lists):**
```bash
$PANDOC manuscript.docx -t markdown
```

**Show document content with tracked changes visible as inline markup:**
```bash
$PANDOC manuscript.docx --track-changes=all -t markdown
```

**List all tracked changes with author and date:**
```bash
$DOCX_TOOL revisions list manuscript.docx
$DOCX_TOOL revisions list manuscript.docx --json   # machine-readable
```

**Accept all tracked changes:**
```bash
$DOCX_TOOL revisions accept manuscript.docx -o manuscript_clean.docx
# or via pandoc (bulk conversion only, no granular control):
$PANDOC manuscript.docx --track-changes=accept -o manuscript_clean.docx
```

**Find-and-replace leaving a tracked revision (shows in Word's review pane):**
```bash
$DOCX_TOOL replace manuscript.docx "samtools v1.17" "samtools v1.21" \
    --track --author "Agent" -o manuscript_revised.docx
```

**`replace` exits 1 when nothing matched — this is intentional.** If you want to suppress the failure:
```bash
$DOCX_TOOL replace doc.docx "old" "new" --allow-no-match
```

**Smart-quote / curly-quote mismatch (most common failure mode):**
Word documents often contain typographic quotes (`'` `'` `"` `"`) and dashes (`–` `—`) instead of
ASCII equivalents.  When an exact match returns 0, the tool checks for near-matches and prints a hint:
```
hint: 1 near-match(es) found that differ only in quote/dash style. Re-run with --normalize-quotes to match.
```
Fix by adding `--normalize-quotes`:
```bash
$DOCX_TOOL replace doc.docx "agent's" "the agent's" --normalize-quotes --track --author "Me"
```

**Get the exact paragraph text to use as a replace argument (avoids quote issues):**
```bash
# Find the paragraph index first
$DOCX_TOOL paragraphs doc.docx | grep -i "keyword"
# Then fetch its exact text
$DOCX_TOOL get-paragraph doc.docx 3
# Pipe directly into a shell variable for use in replace
OLD=$($DOCX_TOOL get-paragraph doc.docx 3)
$DOCX_TOOL replace doc.docx "$OLD" "new text" --track --author "Me"
```

**Extract all reviewer comments:**
```bash
$DOCX_TOOL comments manuscript.docx
$DOCX_TOOL comments manuscript.docx --json
```

**List paragraph styles available in a document (use before inserting with --style):**
```bash
$DOCX_TOOL list-styles manuscript.docx --type paragraph
```

**Insert a caption paragraph after a figure anchor:**
```bash
$DOCX_TOOL insert manuscript.docx "Figure 1" "Figure 1. Sample overview." \
    --style "Caption" -o manuscript_captioned.docx
```

**Insert an image after paragraph index 3 at max 7.5-inch width (NIH page width):**
```bash
$DOCX_TOOL insert-picture manuscript.docx figures/fig1.png \
    --after-paragraph 3 --width 7.5 -o manuscript_with_fig.docx
```

**Insert an image after an anchor paragraph, with a caption:**
```bash
$DOCX_TOOL insert-picture manuscript.docx figures/fig1.png \
    --after-anchor "workflow overview" \
    --width 6.5 \
    --caption "Figure 1. Analysis workflow overview." \
    --caption-style "Caption" \
    -o manuscript_with_fig.docx
```

**Convert Markdown to a new .docx:**
```bash
$PANDOC methods.md -o methods.docx
```

**Convert Markdown to .docx using a style template:**
```bash
$PANDOC methods.md --reference-doc=$STYLES_DIR/nih-proposal-template.docx -o methods.docx
```

**Pipe: convert .docx to markdown and search for a string:**
```bash
$PANDOC manuscript.docx -t markdown | grep -i "sample size"
```

## Style templates

Reusable Word templates live in `~/.cursor/skills/docx/styles/`. Pass any of them to pandoc via `--reference-doc` to control fonts, margins, and paragraph formatting. Pandoc maps Markdown structural elements to named Word styles in the template (e.g. `#` → **Heading 1**, body text → **Body Text**).

| File | Description |
|---|---|
| `nih-proposal-template.docx` | NIH grant proposal: Arial 11 pt, 0.5″ margins, tight line spacing |

**Inspect what paragraph styles a template exposes** (use these names with `insert --style`):
```bash
$DOCX_TOOL list-styles $STYLES_DIR/nih-proposal-template.docx --type paragraph
```

**Add your own template:** place any `.docx` whose paragraph styles are correctly configured into `~/.cursor/skills/docx/styles/`. To bootstrap a new template from pandoc's default:
```bash
$PANDOC --print-default-data-file reference.docx > $STYLES_DIR/my-template.docx
# then open my-template.docx in Word, adjust styles and margins, save
```

## Full flag reference

To look up all flags for a specific subcommand:
```bash
grep -A 40 "^### \`subcommand\`" ~/.cursor/skills/docx/reference.md
```
Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
```bash
grep -A 20 "keyword" ~/.cursor/skills/docx/patterns.md
```
[patterns.md](patterns.md)
