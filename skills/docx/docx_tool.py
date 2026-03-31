#!/usr/bin/env python3
"""
docx_tool.py — CLI for reading, writing, and track-changing Word (.docx) files.

All functions are importable for direct Python use.
Run `python docx_tool.py <subcommand> --help` for usage.
"""

import argparse
import json
import sys
import zipfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Unicode / normalization helpers
# ---------------------------------------------------------------------------

# 1-to-1 mapping: typographic quotes and dashes → ASCII equivalents.
# All substitutions are single-character so character offsets are preserved
# after translation, making it safe to use positions from normalized text
# as positions into the original text for splice operations.
_QUOTE_NORM_TABLE = str.maketrans({
    '\u2018': "'",   # left single quotation mark  '
    '\u2019': "'",   # right single quotation mark '
    '\u201c': '"',   # left double quotation mark  "
    '\u201d': '"',   # right double quotation mark "
    '\u2013': '-',   # en dash                     –
    '\u2014': '-',   # em dash                     —
})


def _normalize_quotes(text: str) -> str:
    """Fold typographic quotes and dashes to ASCII equivalents for fuzzy matching."""
    return text.translate(_QUOTE_NORM_TABLE)


def _count_near_matches(path, old_text: str) -> int:
    """Count paragraphs that contain old_text after quote normalization.

    Used to produce a helpful hint when an exact match returns 0 results.
    """
    from docx import Document
    norm_old = _normalize_quotes(old_text)
    doc = Document(str(path))
    count = 0
    for para in doc.paragraphs:
        count += _normalize_quotes(para.text).count(norm_old)
    return count


# ---------------------------------------------------------------------------
# Read operations
# ---------------------------------------------------------------------------

def read_text(path):
    """Return all paragraph text joined by newlines (accepted view of tracked changes).

    Uses para.text (which includes hyperlink runs) for paragraphs without tracked
    changes, and accepted_text for paragraphs that contain track-change markup.
    """
    from docx_revisions import RevisionDocument
    rdoc = RevisionDocument(str(path))
    lines = []
    for para in rdoc.paragraphs:
        if para.has_track_changes:
            lines.append(para.accepted_text)
        else:
            # para.text traverses hyperlink child runs; accepted_text does not.
            lines.append(para.text)
    return "\n".join(lines)


def read_paragraphs(path):
    """Return list of dicts with keys: index, style, text."""
    from docx import Document
    doc = Document(str(path))
    return [
        {"index": i, "style": para.style.name, "text": para.text}
        for i, para in enumerate(doc.paragraphs)
    ]


def get_paragraph(path, index: int) -> dict:
    """Return the paragraph at *index* as a dict with keys: index, style, text.

    Raises IndexError if index is out of range.
    """
    paragraphs = read_paragraphs(path)
    if index < 0 or index >= len(paragraphs):
        raise IndexError(
            f"Paragraph index {index} out of range (document has {len(paragraphs)} paragraphs)."
        )
    return paragraphs[index]


def list_styles(path, style_type=None):
    """Return list of dicts with keys: name, type for styles defined in the document.

    Args:
        style_type: Optional filter — 'paragraph', 'character', 'table', or 'numbering'.
            If None, all styles are returned.
    """
    from docx import Document
    doc = Document(str(path))
    type_filter = style_type.lower() if style_type else None
    return [
        {"name": s.name, "type": s.type.name.lower()}
        for s in doc.styles
        if type_filter is None or s.type.name.lower() == type_filter
    ]


def read_comments(path):
    """Return list of dicts with keys: id, author, date, text."""
    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    comments = []
    with zipfile.ZipFile(str(path)) as zf:
        if "word/comments.xml" not in zf.namelist():
            return comments
        from lxml import etree
        root = etree.fromstring(zf.read("word/comments.xml"))
    for el in root.findall(f"{{{W}}}comment"):
        texts = [t.text or "" for t in el.iter(f"{{{W}}}t")]
        comments.append({
            "id": el.get(f"{{{W}}}id", ""),
            "author": el.get(f"{{{W}}}author", ""),
            "date": el.get(f"{{{W}}}date", ""),
            "text": "".join(texts),
        })
    return comments


# ---------------------------------------------------------------------------
# Revision operations
# ---------------------------------------------------------------------------

def list_revisions(path):
    """Return list of dicts with keys: type, text, author, date."""
    from docx_revisions import RevisionDocument
    rdoc = RevisionDocument(str(path))
    return [
        {
            "type": type(change).__name__,
            "text": change.text,
            "author": change.author,
            "date": change.date,
        }
        for change in rdoc.track_changes
    ]


def accept_all(path, output):
    """Accept all tracked changes and save to output path."""
    from docx_revisions import RevisionDocument
    rdoc = RevisionDocument(str(path))
    rdoc.accept_all()
    rdoc.save(str(output))


def reject_all(path, output):
    """Reject all tracked changes and save to output path."""
    from docx_revisions import RevisionDocument
    rdoc = RevisionDocument(str(path))
    rdoc.reject_all()
    rdoc.save(str(output))


# ---------------------------------------------------------------------------
# Edit operations
# ---------------------------------------------------------------------------

def tracked_replace(path, old_text, new_text, output, author="", normalize=False):
    """Find-and-replace creating tracked change markup. Returns replacement count.

    Args:
        normalize: If True, fold typographic quotes/dashes to ASCII before
            matching (positions are preserved because the mapping is 1-to-1).
    """
    from docx_revisions import RevisionDocument
    rdoc = RevisionDocument(str(path))

    if normalize:
        norm_old = _normalize_quotes(old_text)
        search_len = len(norm_old)
        count = 0
        for para in rdoc.paragraphs:
            norm_text = _normalize_quotes(para.text)
            positions: list[int] = []
            start = 0
            while True:
                idx = norm_text.find(norm_old, start)
                if idx == -1:
                    break
                positions.append(idx)
                start = idx + search_len
            for pos in reversed(positions):
                para.replace_tracked_at(pos, pos + search_len, new_text, author=author)
                count += 1
    else:
        count = rdoc.find_and_replace_tracked(old_text, new_text, author=author)

    rdoc.save(str(output))
    return count


def plain_replace(path, old_text, new_text, output, normalize=False):
    """Plain find-and-replace with no tracking. Returns replacement count.

    Note: replaces within individual runs; text split across multiple runs is
    not matched. For cross-run replacement use --track which uses the
    docx-revisions implementation.

    Args:
        normalize: If True, fold typographic quotes/dashes to ASCII before
            matching (operates on the normalized run text).
    """
    from docx import Document
    doc = Document(str(path))
    count = 0
    for para in doc.paragraphs:
        for run in para.runs:
            search_in = _normalize_quotes(run.text) if normalize else run.text
            search_for = _normalize_quotes(old_text) if normalize else old_text
            if search_for in search_in:
                run.text = search_in.replace(search_for, new_text)
                count += 1
    doc.save(str(output))
    return count


def tracked_insert(path, anchor_text, insert_text, output, author=""):
    """Append insert_text as a tracked insertion at the end of the first paragraph
    containing anchor_text. Returns True if anchor was found."""
    from docx import Document
    from docx_revisions import RevisionParagraph
    doc = Document(str(path))
    for para in doc.paragraphs:
        if anchor_text in para.text:
            rp = RevisionParagraph.from_paragraph(para)
            rp.add_tracked_insertion(insert_text, author=author)
            doc.save(str(output))
            return True
    return False


def plain_insert(path, anchor_text, insert_text, output, style=None):
    """Insert insert_text as a new paragraph immediately after the first paragraph
    containing anchor_text. Returns True if anchor was found.

    Args:
        style: Word paragraph style name (e.g. 'Caption', 'Heading 1'). If None,
            uses the document default ('Normal'). Raises KeyError if the style
            does not exist in the document.
    """
    from docx import Document
    doc = Document(str(path))
    if style is not None and style not in [s.name for s in doc.styles]:
        raise KeyError(
            f"Style {style!r} not found in document. "
            f"Available styles: {[s.name for s in doc.styles if s.type.name == 'PARAGRAPH']}"
        )
    body = doc.element.body
    for para in doc.paragraphs:
        if anchor_text in para.text:
            new_para = doc.add_paragraph(insert_text, style=style)
            new_el = new_para._element
            body.remove(new_el)
            para._element.addnext(new_el)
            doc.save(str(output))
            return True
    return False


def insert_picture(path, image_path, output, after_index=None, after_anchor=None,
                   width_inches=None, height_inches=None,
                   caption=None, caption_style="Caption"):
    """Insert an inline picture into the document.

    The insertion point is identified by either *after_index* (zero-based paragraph
    index) or *after_anchor* (substring of the target paragraph's text). Exactly one
    must be provided.

    Args:
        after_index:   Insert the picture paragraph after this paragraph index.
        after_anchor:  Insert after the first paragraph whose text contains this string.
        width_inches:  Desired width in inches. If only width is given, height scales
                       proportionally. If neither is given, the image is inserted at its
                       native size.
        height_inches: Desired height in inches. If only height is given, width scales
                       proportionally.
        caption:       Optional caption text inserted as a new paragraph immediately after
                       the picture paragraph.
        caption_style: Paragraph style for the caption (default: 'Caption').

    Returns:
        True on success. Raises IndexError / ValueError if the anchor is not found.
    """
    from docx import Document
    from docx.shared import Inches

    doc = Document(str(path))
    paragraphs = doc.paragraphs

    # Resolve insertion anchor
    if after_index is not None:
        if after_index < 0 or after_index >= len(paragraphs):
            raise IndexError(
                f"Paragraph index {after_index} out of range "
                f"(document has {len(paragraphs)} paragraphs)."
            )
        anchor_para = paragraphs[after_index]
    elif after_anchor is not None:
        anchor_para = next(
            (p for p in paragraphs if after_anchor in p.text), None
        )
        if anchor_para is None:
            raise ValueError(f"Anchor text not found: {after_anchor!r}")
    else:
        raise ValueError("Either after_index or after_anchor must be provided.")

    # Build width/height args (None means use native / proportional scale)
    w = Inches(width_inches) if width_inches is not None else None
    h = Inches(height_inches) if height_inches is not None else None

    # Add picture paragraph at the end of the document body, then relocate it
    pic_para = doc.add_paragraph()
    run = pic_para.add_run()
    run.add_picture(str(image_path), width=w, height=h)
    body = doc.element.body
    body.remove(pic_para._element)
    anchor_para._element.addnext(pic_para._element)

    # Optionally add caption immediately after the picture paragraph
    if caption is not None:
        cap_para = doc.add_paragraph(caption, style=caption_style)
        body.remove(cap_para._element)
        pic_para._element.addnext(cap_para._element)

    doc.save(str(output))
    return True


def tracked_delete(path, delete_text, output, author=""):
    """Mark delete_text as a tracked deletion in the first paragraph that contains it.
    Returns the number of paragraphs where a deletion was marked.

    Note: character positions are derived from para.text; works correctly when
    no other tracked changes are present in the same paragraph.
    """
    from docx_revisions import RevisionDocument
    rdoc = RevisionDocument(str(path))
    count = 0
    for para in rdoc.paragraphs:
        if delete_text in para.text:
            start = para.text.find(delete_text)
            end = start + len(delete_text)
            para.add_tracked_deletion(start=start, end=end, author=author)
            count += 1
    rdoc.save(str(output))
    return count


def plain_delete(path, delete_text, output):
    """Plain delete of all occurrences of delete_text. Returns replacement count."""
    return plain_replace(path, delete_text, "", output)


# ---------------------------------------------------------------------------
# CLI command handlers
# ---------------------------------------------------------------------------

def cmd_read(args):
    print(read_text(args.file))


def cmd_paragraphs(args):
    for p in read_paragraphs(args.file):
        print(f"[{p['index']:3d}] ({p['style']}) {p['text']}")


def cmd_get_paragraph(args):
    """Print the exact text of paragraph N (suitable for piping into replace)."""
    try:
        p = get_paragraph(args.file, args.index)
    except IndexError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(p, ensure_ascii=False))
    else:
        print(p["text"])


def cmd_list_styles(args):
    styles = list_styles(args.file, style_type=args.type)
    if args.json:
        print(json.dumps(styles, indent=2))
    else:
        for s in styles:
            print(f"({s['type']:12s}) {s['name']}")


def cmd_comments(args):
    comments = read_comments(args.file)
    if not comments:
        print("No comments found.")
        return
    if args.json:
        print(json.dumps(comments, indent=2, default=str))
    else:
        for c in comments:
            print(f"#{c['id']} {c['author']} ({c['date']}): {c['text']}")


def cmd_revisions_list(args):
    revisions = list_revisions(args.file)
    if not revisions:
        print("No tracked changes found.")
        return
    if args.json:
        print(json.dumps(revisions, indent=2, default=str))
    else:
        for r in revisions:
            print(f"{r['type']:20s}  author={r['author']}  date={r['date']}  text={r['text']!r}")


def cmd_revisions_accept(args):
    out = _resolve_output(args, suffix="_accepted")
    accept_all(args.file, out)
    print(f"Saved: {out}")


def cmd_revisions_reject(args):
    out = _resolve_output(args, suffix="_rejected")
    reject_all(args.file, out)
    print(f"Saved: {out}")


def cmd_replace(args):
    out = _resolve_output(args)
    normalize = args.normalize_quotes
    if args.track:
        count = tracked_replace(args.file, args.old, args.new, out,
                                author=args.author, normalize=normalize)
    else:
        count = plain_replace(args.file, args.old, args.new, out, normalize=normalize)

    print(f"Replaced {count} occurrence(s). Saved: {out}")

    if count == 0 and not args.allow_no_match:
        if not normalize:
            near = _count_near_matches(args.file, args.old)
            if near:
                print(
                    f"hint: {near} near-match(es) found that differ only in quote/dash "
                    "style (e.g. \u2018\u2019\u201c\u201d\u2013\u2014 vs ASCII). "
                    "Re-run with --normalize-quotes to match.",
                    file=sys.stderr,
                )
        sys.exit(1)


def cmd_insert(args):
    out = _resolve_output(args)
    try:
        if args.track:
            found = tracked_insert(args.file, args.anchor, args.text, out, author=args.author)
        else:
            found = plain_insert(args.file, args.anchor, args.text, out, style=args.style)
    except KeyError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
    if found:
        print(f"Inserted. Saved: {out}")
    else:
        print(f"error: anchor text not found: {args.anchor!r}", file=sys.stderr)
        sys.exit(1)


def cmd_insert_picture(args):
    out = _resolve_output(args)
    after_index = args.after_paragraph
    after_anchor = args.after_anchor
    if after_index is None and after_anchor is None:
        print("error: one of --after-paragraph or --after-anchor is required.", file=sys.stderr)
        sys.exit(1)
    if after_index is not None and after_anchor is not None:
        print("error: --after-paragraph and --after-anchor are mutually exclusive.", file=sys.stderr)
        sys.exit(1)
    try:
        insert_picture(
            args.file, args.image, out,
            after_index=after_index,
            after_anchor=after_anchor,
            width_inches=args.width,
            height_inches=args.height,
            caption=args.caption,
            caption_style=args.caption_style,
        )
    except (IndexError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"Picture inserted. Saved: {out}")


def cmd_delete(args):
    out = _resolve_output(args)
    if args.track:
        count = tracked_delete(args.file, args.text, out, author=args.author)
    else:
        count = plain_delete(args.file, args.text, out)
    print(f"Deleted {count} occurrence(s). Saved: {out}")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_output(args, suffix=""):
    """Return output Path: args.output if given, else stem+suffix+.docx alongside input."""
    if getattr(args, "output", None):
        return Path(args.output)
    p = Path(args.file)
    return p.with_name(p.stem + suffix + p.suffix)


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        prog="docx_tool.py",
        description="Read, write, and track-change Word (.docx) files.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # read
    p = sub.add_parser("read", help="Print all paragraph text (accepted view, includes hyperlinks).")
    p.add_argument("file", help="Input .docx file.")
    p.set_defaults(func=cmd_read)

    # paragraphs
    p = sub.add_parser("paragraphs", help="List paragraphs with index and style name.")
    p.add_argument("file", help="Input .docx file.")
    p.set_defaults(func=cmd_paragraphs)

    # list-styles
    p = sub.add_parser("list-styles", help="List styles defined in the document.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument(
        "--type",
        default=None,
        choices=["paragraph", "character", "table", "numbering"],
        help="Filter by style type (default: show all).",
    )
    p.add_argument("--json", action="store_true", help="Output as JSON array.")
    p.set_defaults(func=cmd_list_styles)

    # get-paragraph
    p = sub.add_parser(
        "get-paragraph",
        help="Print the exact text of paragraph N (useful for building replace arguments).",
    )
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("index", type=int, help="Zero-based paragraph index.")
    p.add_argument("--json", action="store_true", help="Output as JSON object (includes style).")
    p.set_defaults(func=cmd_get_paragraph)

    # comments
    p = sub.add_parser("comments", help="Extract all reviewer comments.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("--json", action="store_true", help="Output as JSON array.")
    p.set_defaults(func=cmd_comments)

    # revisions
    p_rev = sub.add_parser("revisions", help="Tracked change operations.")
    rev_sub = p_rev.add_subparsers(dest="rev_command", required=True)

    p = rev_sub.add_parser("list", help="List all tracked changes.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("--json", action="store_true", help="Output as JSON array.")
    p.set_defaults(func=cmd_revisions_list)

    p = rev_sub.add_parser("accept", help="Accept all tracked changes and save.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("-o", "--output", help="Output path (default: <stem>_accepted.docx).")
    p.set_defaults(func=cmd_revisions_accept)

    p = rev_sub.add_parser("reject", help="Reject all tracked changes and save.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("-o", "--output", help="Output path (default: <stem>_rejected.docx).")
    p.set_defaults(func=cmd_revisions_reject)

    # replace
    p = sub.add_parser("replace", help="Find and replace text.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("old", help="Text to find.")
    p.add_argument("new", help="Replacement text.")
    p.add_argument("-o", "--output", help="Output path (default: overwrite input).")
    p.add_argument("--track", action="store_true", help="Record as tracked revision.")
    p.add_argument("--author", default="", help="Author name for tracked revision.")
    p.add_argument(
        "--normalize-quotes",
        action="store_true",
        help=(
            "Fold typographic quotes/dashes (\u2018\u2019\u201c\u201d\u2013\u2014) to ASCII "
            "equivalents before matching. Useful when the docx contains smart quotes "
            "but the search string uses straight quotes."
        ),
    )
    p.add_argument(
        "--allow-no-match",
        action="store_true",
        help="Exit 0 even when no replacements were made (default: exit 1 on 0 matches).",
    )
    p.set_defaults(func=cmd_replace)

    # insert
    p = sub.add_parser("insert", help="Insert text at/after an anchor paragraph.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("anchor", help="Substring that identifies the target paragraph.")
    p.add_argument("text", help="Text to insert.")
    p.add_argument("-o", "--output", help="Output path (default: overwrite input).")
    p.add_argument(
        "--track",
        action="store_true",
        help="Record as tracked insertion appended to anchor paragraph.",
    )
    p.add_argument("--author", default="", help="Author name for tracked revision.")
    p.add_argument(
        "--style",
        default=None,
        help=(
            "Paragraph style name for the inserted paragraph (e.g. 'Caption', 'Heading 1', "
            "'Body Text'). Ignored when --track is used (tracked insertions append within "
            "the anchor paragraph and inherit its style). Use `paragraphs` to see style "
            "names already in the document."
        ),
    )
    p.set_defaults(func=cmd_insert)

    # insert-picture
    p = sub.add_parser(
        "insert-picture",
        help="Insert an inline image after a paragraph (by index or anchor text).",
    )
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("image", help="Path to the image file (PNG, JPEG, GIF, BMP, TIFF).")
    p.add_argument("-o", "--output", help="Output path (default: overwrite input).")
    anchor_group = p.add_mutually_exclusive_group(required=True)
    anchor_group.add_argument(
        "--after-paragraph",
        type=int,
        metavar="N",
        dest="after_paragraph",
        help="Insert after zero-based paragraph index N.",
    )
    anchor_group.add_argument(
        "--after-anchor",
        metavar="TEXT",
        dest="after_anchor",
        help="Insert after the first paragraph whose text contains TEXT.",
    )
    p.add_argument(
        "--width",
        type=float,
        default=None,
        metavar="INCHES",
        help="Image width in inches. Height scales proportionally if --height is omitted.",
    )
    p.add_argument(
        "--height",
        type=float,
        default=None,
        metavar="INCHES",
        help="Image height in inches. Width scales proportionally if --width is omitted.",
    )
    p.add_argument(
        "--caption",
        default=None,
        help="Optional caption text inserted as a new paragraph immediately after the image.",
    )
    p.add_argument(
        "--caption-style",
        default="Caption",
        metavar="STYLE",
        dest="caption_style",
        help="Paragraph style for the caption (default: 'Caption').",
    )
    p.set_defaults(func=cmd_insert_picture)

    # delete
    p = sub.add_parser("delete", help="Delete matched text.")
    p.add_argument("file", help="Input .docx file.")
    p.add_argument("text", help="Text to delete.")
    p.add_argument("-o", "--output", help="Output path (default: overwrite input).")
    p.add_argument("--track", action="store_true", help="Record as tracked deletion.")
    p.add_argument("--author", default="", help="Author name for tracked revision.")
    p.set_defaults(func=cmd_delete)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
