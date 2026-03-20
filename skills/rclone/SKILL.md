---
name: rclone
description: Sync, copy, move, and list files against cloud and remote storage using
  rclone. Use when transferring data to or from S3, GCS, Google Drive, Dropbox, SFTP,
  WebDAV, Azure Blob, B2, OneDrive, or other rclone backends; comparing or verifying
  trees with check or checksum; configuring remotes; mounting remotes; bandwidth limits;
  dry-runs; or tasks mentioning rclone, remote paths (`remote:bucket/path`), sync vs
  copy, or cloud egress/ingress.
---

# rclone

## Environment

```bash
RCLONE=~/.cursor/skills/rclone/bin/rclone
```

Remote paths use the form `name:path` (e.g. `s3:my-bucket/data/`). Local paths are ordinary filesystem paths. Config defaults to `~/.config/rclone/rclone.conf`; override with `--config /path/to/rclone.conf` or `RCLONE_CONFIG`.

## Critical distinctions

| Command | Behavior |
|---|---|
| `copy` | Copies new/changed files to dest; **never deletes** extra files on dest |
| `sync` | Makes dest **identical** to source — **deletes** files on dest that are not on source |
| `move` | Like copy, then **removes** from source after successful copy |

Always prefer `copy` (or `check` first) when the destination must not lose files. Use `sync` only when a mirror is intended.

## Subcommands

**Configuration & auth**
- `config` — interactive wizard; create/edit remotes
- `authorize` — OAuth-style remote authorization
- `obscure` — hash a password/token for use in config
- `listremotes` — print configured remote names

**Transfer**
- `copy` — copy source → dest, skip unchanged
- `sync` — make dest match source (destructive on dest)
- `move` / `moveto` — copy then delete source
- `copyto` / `copyurl` — single destination file or URL → remote

**Listing & inspection**
- `ls` / `lsl` / `lsd` / `lsf` / `lsjson` / `tree` — list objects, dirs, or machine-readable JSON
- `size` — total size and object count
- `about` — quota / usage where supported
- `ncdu` — TUI disk usage explorer on a remote

**Integrity**
- `check` — compare source and dest (size/checksum)
- `checksum` / `md5sum` / `sha1sum` / `hashsum` — verify against SUM files or emit hashes
- `cryptcheck` — verify encrypted remote

**Maintenance**
- `delete` / `deletefile` / `purge` — remove objects or entire tree
- `mkdir` / `rmdir` / `rmdirs` — directory operations
- `cleanup` / `dedupe` / `settier` — backend-specific housekeeping
- `touch` — create file or set mtime

**Mount & serve**
- `mount` / `nfsmount` — FUSE (or NFS) mount of a remote
- `serve` — expose a remote over HTTP/FTP/WebDAV/SFTP/etc.

**Streaming & misc**
- `cat` / `rcat` — stream remote file to stdout / stdin → remote
- `link` — public share link when backend supports it
- `backend` — backend-specific subcommands (`rclone help backend <name>`)
- `bisync` — bidirectional sync (experimental workflow; read help carefully)
- `version` / `help` / `completion` — meta

## Common patterns

**Configure a new remote (interactive):**
```bash
$RCLONE config
```

**Copy local tree to a bucket (progress, safe default):**
```bash
$RCLONE copy -P /data/run42 s3:lab-archive/run42/
```

**Dry-run before sync (see what would change, including deletes):**
```bash
$RCLONE sync --dry-run /data/project remote:bucket/project/
```

**List bucket prefix:**
```bash
$RCLONE lsd remote:
$RCLONE ls remote:path/to/prefix/
$RCLONE lsjson remote:path/   # scripting
```

**Verify copy completed (exit non-zero on mismatch):**
```bash
$RCLONE check /data/run42 s3:lab-archive/run42/
```

**Limit bandwidth and parallelism (shared cluster):**
```bash
$RCLONE copy -P --bwlimit 50M --transfers 4 --checkers 8 /big local:backup/
```

**Use a dedicated config file (CI or project-specific):**
```bash
$RCLONE --config ./rclone.conf ls myremote:
```

**One-off S3-compatible endpoint (without saving config):**
```bash
$RCLONE copy -P /data s3:bucket/prefix/ \
  --s3-provider Other --s3-endpoint https://example.com \
  --s3-access-key-id "$KEY" --s3-secret-access-key "$SECRET"
```

## Full flag reference

To look up all flags for a specific subcommand:
```bash
grep -A 120 "^### \`copy\`" ~/.cursor/skills/rclone/reference.md
```
Global flags are under `### \`help flags\``. Top-level overview: `### \`rclone\``.

Full reference: [reference.md](reference.md)

## Patterns

Reusable real-world patterns accumulated over time. To search:
```bash
grep -A 20 "keyword" ~/.cursor/skills/rclone/patterns.md
```
[patterns.md](patterns.md)
