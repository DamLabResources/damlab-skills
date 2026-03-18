---
name: create-skill
description: Conventions and checklist for adding a new bioinformatics tool skill to the damlab-skills repo. Use when asked to add a new tool skill, create a skill for a new tool, or when following damlab-skills repo standards.
---

# Adding a New Skill to damlab-skills

## Required files per skill

Every skill lives in its own directory `<toolname>/` at the repo root:

```
<toolname>/
├── SKILL.md          # Core patterns — kept under 150 lines
├── reference.md      # Full subcommand/flag reference
├── environment.yaml  # Conda env definition (no version pin)
└── CHANGELOG.md      # Update history
```

## Step-by-step checklist

- [ ] Create `<toolname>/environment.yaml`
- [ ] Create `<toolname>/SKILL.md`
- [ ] Create `<toolname>/reference.md`
- [ ] Create `<toolname>/CHANGELOG.md`
- [ ] Add `<toolname>` to the `TOOL_SKILLS` array in `install.sh`
- [ ] Add a row to the skills table in `README.md`

---

## 1. environment.yaml

Name must follow the convention `damlab-skill-<toolname>`. No version pin — always resolves latest from bioconda.

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
conda run -n damlab-skill-<toolname> <tool> [args]

## Common patterns
[5-8 most-used patterns with runnable examples]

## Additional reference
- Full subcommand reference: [reference.md](reference.md)
```

**Rules:**
- Use `conda run -n damlab-skill-<toolname> <tool>` for every command example
- Keep SKILL.md under 150 lines — put detailed flags in reference.md
- Each pattern should be a runnable example, not a prose description
- Include a multi-tool pipeline example if the tool is commonly piped (e.g. samtools → seqkit)

---

## 3. reference.md

Organize by subcommand or functional group. For each subcommand, list:
- One-line description
- Key flags with brief explanations
- A representative example

Aim for completeness over brevity here — this is the reference the agent reads on demand.

---

## 4. CHANGELOG.md

```markdown
# Changelog — <toolname>

## [Unreleased]

## [YYYY-MM-DD] — Initial skill
- Tool version: latest at install time (run `conda run -n damlab-skill-<toolname> <tool> --version` to check)
- Skill version: 1.0.0
- Added: initial SKILL.md, reference.md, environment.yaml
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

## 5. install.sh and README.md

After creating the files, update two lines:

**`install.sh`** — add `<toolname>` to `TOOL_SKILLS`:
```bash
TOOL_SKILLS=(samtools seqkit csvtk <toolname>)
```

**`README.md`** — add a row to the skills table:
```markdown
| `<toolname>` | [<Toolname>](<url>) | <one-line description> |
```
