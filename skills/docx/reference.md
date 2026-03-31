# docx — Full Reference

Binaries:
- `~/.cursor/skills/docx/bin/python ~/.cursor/skills/docx/docx_tool.py`
- `~/.cursor/skills/docx/bin/pandoc`

Each entry contains the `--help` output. Grep for a subcommand:
```bash
grep -A 40 "^### \`subcommand\`" ~/.cursor/skills/docx/reference.md
```
Increase `-A` if output appears truncated.

---

## docx_tool.py

### `read`

```
usage: docx_tool.py read [-h] file

Print all paragraph text (accepted view).

positional arguments:
  file        Input .docx file.

options:
  -h, --help  show this help message and exit
```

### `paragraphs`

```
usage: docx_tool.py paragraphs [-h] file

List paragraphs with index and style name.

positional arguments:
  file        Input .docx file.

options:
  -h, --help  show this help message and exit
```

### `comments`

```
usage: docx_tool.py comments [-h] [--json] file

Extract all reviewer comments.

positional arguments:
  file        Input .docx file.

options:
  -h, --help  show this help message and exit
  --json      Output as JSON array.
```

### `revisions list`

```
usage: docx_tool.py revisions list [-h] [--json] file

List all tracked changes.

positional arguments:
  file        Input .docx file.

options:
  -h, --help  show this help message and exit
  --json      Output as JSON array.
```

Output fields per change:
- `type` — `TrackedInsertion` or `TrackedDeletion`
- `text` — the changed text content
- `author` — revision author name
- `date` — ISO 8601 timestamp of the revision

### `revisions accept`

```
usage: docx_tool.py revisions accept [-h] [-o OUTPUT] file

Accept all tracked changes and save.

positional arguments:
  file                  Input .docx file.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path (default: <stem>_accepted.docx).
```

### `revisions reject`

```
usage: docx_tool.py revisions reject [-h] [-o OUTPUT] file

Reject all tracked changes and save.

positional arguments:
  file                  Input .docx file.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path (default: <stem>_rejected.docx).
```

### `replace`

```
usage: docx_tool.py replace [-h] [-o OUTPUT] [--track] [--author AUTHOR] file old new

Find and replace text.

positional arguments:
  file                  Input .docx file.
  old                   Text to find.
  new                   Replacement text.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path (default: overwrite input).
  --track               Record as tracked revision.
  --author AUTHOR       Author name for tracked revision.
```

Notes:
- Without `--track`: replaces within individual runs only. Text split across
  multiple runs (common in Word) may not be matched. Use `--track` for
  reliable cross-run replacement (handled by docx-revisions).
- With `--track`: uses `RevisionDocument.find_and_replace_tracked()`, which
  searches body paragraphs and table cells and creates proper `w:ins`/`w:del`
  markup visible in Word's Review pane.

### `insert`

```
usage: docx_tool.py insert [-h] [-o OUTPUT] [--track] [--author AUTHOR] file anchor text

Insert text at/after an anchor paragraph.

positional arguments:
  file                  Input .docx file.
  anchor                Substring that identifies the target paragraph.
  text                  Text to insert.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path (default: overwrite input).
  --track               Record as tracked insertion appended to anchor paragraph.
  --author AUTHOR       Author name for tracked revision.
```

Notes:
- Without `--track`: inserts a new plain paragraph immediately after the first
  paragraph containing `anchor`.
- With `--track`: appends `text` as a tracked insertion (`w:ins`) at the end of
  the anchor paragraph (same paragraph, not a new one).
- Exits with code 1 if anchor text is not found.

### `delete`

```
usage: docx_tool.py delete [-h] [-o OUTPUT] [--track] [--author AUTHOR] file text

Delete matched text.

positional arguments:
  file                  Input .docx file.
  text                  Text to delete.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path (default: overwrite input).
  --track               Record as tracked deletion.
  --author AUTHOR       Author name for tracked revision.
```

Notes:
- Without `--track`: plain deletion via run-level replacement (same run-split
  caveat as `replace` without `--track`).
- With `--track`: marks the first occurrence per paragraph as a `w:del` element
  using character positions from `para.text`. Works correctly when no other
  tracked changes are present in the same paragraph.
- Reports count of paragraphs affected (tracked mode) or runs affected (plain mode).

---

## pandoc (docx-relevant flags)

### `pandoc --help` (abridged)

```
pandoc [OPTIONS] [FILES]

Input/output formats relevant to .docx:
  -f FORMAT, --from=FORMAT     input format (use: docx)
  -t FORMAT, --to=FORMAT       output format (use: markdown, plain, html, rst, latex, ...)
  -o FILE,   --output=FILE     output file (use .docx extension to write Word document)
  -i,        --standalone      produce standalone document

DOCX-specific reader options:
  --track-changes=accept|reject|all
      How to handle track changes in a .docx input file.
        accept  (default) include insertions, remove deletions
        reject  keep deletions, remove insertions
        all     include both as annotated spans with classes
                ins/del/comment-start/comment-end

Common usage:
  pandoc input.docx -t markdown           convert to Markdown
  pandoc input.md   -o output.docx        write new Word document
  pandoc input.docx --track-changes=all -t markdown
                                           show all tracked changes inline
```

Full pandoc manual:
```bash
$PANDOC --help 2>&1 | less
man pandoc
```
