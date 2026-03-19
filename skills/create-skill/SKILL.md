---
name: create-skill
description: Conventions and checklist for adding a new bioinformatics tool skill to the damlab-skills repo. Use when asked to add a new tool skill, create a skill for a new tool, or when following damlab-skills repo standards.
---

# Adding a New Skill to damlab-skills

## Required files per skill

Every skill lives in its own directory `skills/<toolname>/` in the repo:

```
skills/<toolname>/
├── SKILL.md          # Subcommand index + common patterns + grep-lookup instructions
├── reference.md      # Verbatim --help output for every subcommand
├── patterns.md       # Reusable real-world patterns (stub at creation; grows over time)
├── environment.yaml  # Conda env definition (no version pin)
└── CHANGELOG.md      # Update history
```

## Step-by-step checklist

- [ ] Create `skills/<toolname>/environment.yaml`
- [ ] Create `skills/<toolname>/SKILL.md`
- [ ] Create `skills/<toolname>/reference.md`
- [ ] Create `skills/<toolname>/patterns.md`
- [ ] Create `skills/<toolname>/CHANGELOG.md`
- [ ] Add `<toolname>` to the `TOOL_SKILLS` array in `install.sh`
- [ ] Add a row to the skills table in `README.md`

---

## 1. environment.yaml

No version pin — always resolves latest from bioconda. The `name:` field is ignored at install time (env is created with `--prefix`); include it as documentation only.

```yaml
name: damlab-skill-<toolname>
channels:
  - bioconda
  - conda-forge
  - defaults
dependencies:
  - <toolname>
```

---

## 2. SKILL.md

### Frontmatter

```yaml
---
name: <toolname>
description: <Third-person, specific. Include WHAT the tool does and WHEN to use it.
  Mention key trigger terms: file types, task names, subcommand names.>
---
```

### Body structure

```markdown
# <Toolname>

## Environment

​```bash
<TOOLNAME>=~/.cursor/skills/<toolname>/bin/<toolname>
​```

## Subcommands

**<Category 1>**
- `subcommand` — one-line description
- `subcommand` — one-line description

**<Category 2>**
- `subcommand` — one-line description

## Common patterns
[5-8 most-used patterns with runnable examples using $<TOOLNAME>]

## Full flag reference

To look up all flags for a specific subcommand:
​```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/<toolname>/reference.md
​```
Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
​```bash
grep -A 20 "keyword" ~/.cursor/skills/<toolname>/patterns.md
​```
[patterns.md](patterns.md)
```

**Rules:**
- Define the binary path as a variable in the Environment section: `<TOOLNAME>=~/.cursor/skills/<toolname>/bin/<toolname>`
- This path is stable on any machine: `install.sh` creates a `bin/` symlink inside each skill dir pointing to the venv's `bin/` directory
- Use `$<TOOLNAME>` for every command example — never `conda run`
- Pipes between tools use direct paths on both sides: `$TOOL1 ... | $TOOL2 ...`
- Keep SKILL.md under 200 lines — put detailed flags in reference.md
- Each pattern should be a runnable example, not a prose description
- Include a multi-tool pipeline example if the tool is commonly piped
- The "Full flag reference" and "Patterns" sections replace any previous "Additional reference" footer
- Do NOT load reference.md or patterns.md in full — the agent greps them on demand to stay within context

---

## 3. reference.md

Contains the verbatim `--help` output for every subcommand, organized by functional category.

### Header

```markdown
# <Toolname> — Full Reference

Binary: `~/.cursor/skills/<toolname>/bin/<toolname>`

Each entry contains the verbatim `--help` output. Grep for a subcommand:
​```bash
grep -A 80 "^### \`subcommand\`" ~/.cursor/skills/<toolname>/reference.md
​```
Increase `-A` if output appears truncated.

---
```

### Per-subcommand entries

```markdown
## <Category>

### `subcommand`

​```
<verbatim output of: <toolname> subcommand --help 2>&1>
​```
```

**Rules:**
- Use `### \`subcommand\`` (level-3 heading with backtick-wrapped name) — the grep pattern in SKILL.md depends on this exact format
- Include the full `--help` output verbatim, including global flags if present
- Group subcommands under level-2 (`##`) category headings
- If global flags are identical for all subcommands, you may list them once at the top and abbreviate in per-subcommand entries

---

## 4. patterns.md

A stub at skill creation, grown over time by appending patterns as they arise naturally.

```markdown
# <Toolname> — Patterns

Reusable patterns collected from real tasks. Each entry has a title, context, and runnable example.

<!-- Add patterns below as they arise -->
```

Pattern entry format (add new ones at the bottom):
```markdown
### <Short descriptive title>

**Context:** <one sentence on when to use this>

​```bash
<runnable example>
​```
```

---

## 5. CHANGELOG.md

```markdown
# Changelog — <toolname>

## [Unreleased]

## [YYYY-MM-DD] — Initial skill
- Tool version: latest at install time (run `~/.cursor/skills/<toolname>/bin/<toolname> --version` to check)
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, patterns.md, environment.yaml
```

Format for subsequent entries:
```markdown
## [YYYY-MM-DD]
- Tool version: <version>
- Skill version: <semver>
- Changed: <what changed in the skill content>
- Updated: <if tool was upgraded>
```

---

## 6. install.sh and README.md

After creating the files, update two lines:

**`install.sh`** — add `<toolname>` to `TOOL_SKILLS`:
```bash
TOOL_SKILLS=(samtools seqkit csvtk <toolname>)
```

**`README.md`** — add a row to the skills table:
```markdown
| `<toolname>` | [<Toolname>](<url>) | <one-line description> |
```
