# rclone — Full Reference

Binary: `~/.cursor/skills/rclone/bin/rclone`

Each entry contains the verbatim `--help` output. Grep for a subcommand:

```bash
grep -A 120 "^### \`copy\`" ~/.cursor/skills/rclone/reference.md
```

Increase `-A` if output appears truncated. Per-command blocks use quadruple backticks so nested triple-backtick fences inside upstream help do not break Markdown.

---

## Top-level

### `rclone`

```
Rclone syncs files to and from cloud storage providers as well as
mounting them, listing them in lots of different ways.

See the home page (https://rclone.org/) for installation, usage,
documentation, changelog and configuration walkthroughs.

Usage:
  rclone [flags]
  rclone [command]

Available commands:
  about       Get quota information from the remote.
  archive     Perform an action on an archive.
  authorize   Remote authorization.
  backend     Run a backend-specific command.
  bisync      Perform bidirectional synchronization between two paths.
  cat         Concatenates any files and sends them to stdout.
  check       Checks the files in the source and destination match.
  checksum    Checks the files in the destination against a SUM file.
  cleanup     Clean up the remote if possible.
  completion  Output completion script for a given shell.
  config      Enter an interactive configuration session.
  convmv      Convert file and directory names in place.
  copy        Copy files from source to dest, skipping identical files.
  copyto      Copy files from source to dest, skipping identical files.
  copyurl     Copy the contents of the URL supplied content to dest:path.
  cryptcheck  Cryptcheck checks the integrity of an encrypted remote.
  cryptdecode Cryptdecode returns unencrypted file names.
  dedupe      Interactively find duplicate filenames and delete/rename them.
  delete      Remove the files in path.
  deletefile  Remove a single file from remote.
  gendocs     Output markdown docs for rclone to the directory supplied.
  gitannex    Speaks with git-annex over stdin/stdout.
  hashsum     Produces a hashsum file for all the objects in the path.
  help        Show help for rclone commands, flags and backends.
  link        Generate public link to file/folder.
  listremotes List all the remotes in the config file and defined in environment variables.
  ls          List the objects in the path with size and path.
  lsd         List all directories/containers/buckets in the path.
  lsf         List directories and objects in remote:path formatted for parsing.
  lsjson      List directories and objects in the path in JSON format.
  lsl         List the objects in path with modification time, size and path.
  md5sum      Produces an md5sum file for all the objects in the path.
  mkdir       Make the path if it doesn't already exist.
  mount       Mount the remote as file system on a mountpoint.
  move        Move files from source to dest.
  moveto      Move file or directory from source to dest.
  ncdu        Explore a remote with a text based user interface.
  nfsmount    Mount the remote as file system on a mountpoint.
  obscure     Obscure password for use in the rclone config file.
  purge       Remove the path and all of its contents.
  rc          Run a command against a running rclone.
  rcat        Copies standard input to file on remote.
  rcd         Run rclone listening to remote control commands only.
  rmdir       Remove the empty directory at path.
  rmdirs      Remove empty directories under the path.
  selfupdate  Update the rclone binary.
  serve       Serve a remote over a protocol.
  settier     Changes storage class/tier of objects in remote.
  sha1sum     Produces an sha1sum file for all the objects in the path.
  size        Prints the total size and number of objects in remote:path.
  sync        Make source and dest identical, modifying destination only.
  test        Run a test command
  touch       Create new file or change file modification time.
  tree        List the contents of the remote in a tree like fashion.
  version     Show the version number.

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
```

## Global flags

### `help flags`

```
Usage:
  rclone help flags [<filter>] [flags]

Flags:
      --group string   Only include flags from specific group
  -h, --help           help for flags
      --name           Apply filter only on flag names

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Flags used for sync commands (flag group Sync):
      --backup-dir string               Make backups into hierarchy based in DIR
      --delete-after                    When synchronizing, delete files on destination after transferring (default)
      --delete-before                   When synchronizing, delete files on destination before transferring
      --delete-during                   When synchronizing, delete files during transfer
      --fix-case                        Force rename of case insensitive dest to match source
      --ignore-errors                   Delete even if there are I/O errors
      --list-cutoff int                 To save memory, sort directory listings on disk above this threshold (default 1000000)
      --max-delete int                  When synchronizing, limit the number of deletes (default -1)
      --max-delete-size SizeSuffix      When synchronizing, limit the total size of deletes (default off)
      --suffix string                   Suffix to add to changed files
      --suffix-keep-extension           Preserve the extension when using --suffix
      --track-renames                   When synchronizing, track file renames and do a server-side move if possible
      --track-renames-strategy string   Strategies to use when synchronizing using track-renames hash|modtime|leaf (default "hash")

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags used for check commands (flag group Check):
      --max-backlog int   Maximum number of objects in sync or check backlog (default 10000)

Flags for general networking and HTTP stuff (flag group Networking):
      --bind string                        Local address to bind to for outgoing connections, IPv4, IPv6 or name
      --bwlimit BwTimetable                Bandwidth limit in KiB/s, or use suffix B|K|M|G|T|P or a full timetable
      --bwlimit-file BwTimetable           Bandwidth limit per file in KiB/s, or use suffix B|K|M|G|T|P or a full timetable
      --ca-cert stringArray                CA certificate used to verify servers
      --client-cert string                 Client SSL certificate (PEM) for mutual TLS auth
      --client-key string                  Client SSL private key (PEM) for mutual TLS auth
      --client-pass string                 Password for client SSL private key (PEM) for mutual TLS auth (obscured) (obscured)
      --contimeout Duration                Connect timeout (default 1m0s)
      --disable-http-keep-alives           Disable HTTP keep-alives and use each connection once
      --disable-http2                      Disable HTTP/2 in the global transport
      --dscp string                        Set DSCP value to connections, value or name, e.g. CS1, LE, DF, AF21
      --expect-continue-timeout Duration   Timeout when using expect / 100-continue in HTTP (default 1s)
      --header stringArray                 Set HTTP header for all transactions
      --header-download stringArray        Set HTTP header for download transactions
      --header-upload stringArray          Set HTTP header for upload transactions
      --http-proxy string                  HTTP proxy URL
      --max-connections int                Maximum number of simultaneous backend API connections, 0 for unlimited
      --no-check-certificate               Do not verify the server SSL certificate (insecure)
      --no-gzip-encoding                   Don't set Accept-Encoding: gzip
      --timeout Duration                   IO idle timeout (default 5m0s)
      --tpslimit float                     Limit HTTP transactions per second to this
      --tpslimit-burst int                 Max burst of transactions for --tpslimit (default 1)
      --use-cookies                        Enable session cookiejar
      --user-agent string                  Set the user-agent to a specified string (default "rclone/")

Flags helpful for increasing performance (flag group Performance):
      --buffer-size SizeSuffix   In memory buffer size when reading files for each --transfer (default 16Mi)
      --checkers int             Number of checkers to run in parallel (default 8)
      --transfers int            Number of file transfers to run in parallel (default 4)

Flags for general configuration of rclone (flag group Config):
      --ask-password                        Allow prompt for password for encrypted configuration (default true)
      --auto-confirm                        If enabled, do not request console confirmation
      --cache-dir string                    Directory rclone will use for caching (default "/home/jupyter-will/.cache/rclone")
      --color AUTO|NEVER|ALWAYS             When to show colors (and other ANSI codes) AUTO|NEVER|ALWAYS (default AUTO)
      --config string                       Config file (default "/home/jupyter-will/.rclone.conf")
      --default-time Time                   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --disable string                      Disable a comma separated list of features (use --disable help to see a list)
  -n, --dry-run                             Do a trial run with no permanent changes
      --error-on-no-transfer                Sets exit code 9 if no files are transferred, useful in scripts
      --fs-cache-expire-duration Duration   Cache remotes for this long (0 to disable caching) (default 5m0s)
      --fs-cache-expire-interval Duration   Interval to check for expired remotes (default 1m0s)
      --human-readable                      Print numbers in a human-readable format, sizes with suffix Ki|Mi|Gi|Ti|Pi
  -i, --interactive                         Enable interactive mode
      --kv-lock-time Duration               Maximum time to keep key-value database locked by process (default 1s)
      --low-level-retries int               Number of low level retries to do (default 10)
      --max-buffer-memory SizeSuffix        If set, don't allocate more than this amount of memory as buffers (default off)
      --no-console                          Hide console window (supported on Windows only)
      --no-unicode-normalization            Don't normalize unicode characters in filenames
      --password-command SpaceSepList       Command for supplying password for encrypted configuration
      --retries int                         Retry operations this many times if they fail (default 3)
      --retries-sleep Duration              Interval between retrying operations if they fail, e.g. 500ms, 60s, 5m (0 to disable) (default 0s)
      --temp-dir string                     Directory rclone will use for temporary files (default "/tmp")
      --use-mmap                            Use mmap allocator (see docs)
      --use-server-modtime                  Use server modified time instead of object metadata

Flags for developers (flag group Debugging):
      --cpuprofile string   Write cpu profile to file
      --dump DumpFlags      List of items to dump from: headers, bodies, requests, responses, auth, filters, goroutines, openfiles, mapper
      --dump-bodies         Dump HTTP headers and bodies - may contain sensitive info
      --dump-headers        Dump HTTP headers - may contain sensitive info
      --memprofile string   Write memory profile to file

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Flags for logging and statistics (flag group Logging):
      --log-file string                     Log everything to this file
      --log-file-compress                   If set, compress rotated log files using gzip
      --log-file-max-age Duration           Maximum duration to retain old log files (eg "7d") (default 0s)
      --log-file-max-backups int            Maximum number of old log files to retain
      --log-file-max-size SizeSuffix        Maximum size of the log file before it's rotated (eg "10M") (default off)
      --log-format Bits                     Comma separated list of log format options (default date,time)
      --log-level LogLevel                  Log level DEBUG|INFO|NOTICE|ERROR (default NOTICE)
      --log-systemd                         Activate systemd integration for the logger
      --max-stats-groups int                Maximum number of stats groups to keep in memory, on max oldest is discarded (default 1000)
  -P, --progress                            Show progress during transfer
      --progress-terminal-title             Show progress on the terminal title (requires -P/--progress)
  -q, --quiet                               Print as little stuff as possible
      --stats Duration                      Interval between printing stats, e.g. 500ms, 60s, 5m (0 to disable) (default 1m0s)
      --stats-file-name-length int          Max file name length in stats (0 for no limit) (default 45)
      --stats-log-level LogLevel            Log level to show --stats output DEBUG|INFO|NOTICE|ERROR (default INFO)
      --stats-one-line                      Make the stats fit on one line
      --stats-one-line-date                 Enable --stats-one-line and add current date/time prefix
      --stats-one-line-date-format string   Enable --stats-one-line-date and use custom formatted date: Enclose date string in double quotes ("), see https://golang.org/pkg/time/#Time.Format
      --stats-unit string                   Show data rate in stats as either 'bits' or 'bytes' per second (default "bytes")
      --syslog                              Use Syslog for logging
      --syslog-facility string              Facility for syslog, e.g. KERN,USER (default "DAEMON")
      --use-json-log                        Use json log format
  -v, --verbose count                       Print lots more stuff (repeat for more)

Flags to control metadata (flag group Metadata):
  -M, --metadata                            If set, preserve metadata when copying objects
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --metadata-mapper SpaceSepList        Program to run to transforming metadata before upload
      --metadata-set stringArray            Add metadata key=value when uploading

Flags to control the Remote Control API (flag group RC):
      --rc                                 Enable the remote control server
      --rc-addr stringArray                IPaddress:Port or :Port to bind server to (default localhost:5572)
      --rc-allow-origin string             Origin which cross-domain request (CORS) can be executed from
      --rc-baseurl string                  Prefix for URLs - leave blank for root
      --rc-cert string                     TLS PEM key (concatenation of certificate and CA certificate)
      --rc-client-ca string                Client certificate authority to verify clients with
      --rc-enable-metrics                  Enable the Prometheus metrics path at the remote control server
      --rc-files string                    Path to local files to serve on the HTTP server
      --rc-htpasswd string                 A htpasswd file - if not provided no authentication is done
      --rc-job-expire-duration Duration    Expire finished async jobs older than this value (default 1m0s)
      --rc-job-expire-interval Duration    Interval to check for expired async jobs (default 10s)
      --rc-key string                      TLS PEM Private key
      --rc-max-header-bytes int            Maximum size of request header (default 4096)
      --rc-min-tls-version string          Minimum TLS version that is acceptable (default "tls1.0")
      --rc-no-auth                         Don't require auth for certain methods
      --rc-pass string                     Password for authentication
      --rc-realm string                    Realm for authentication
      --rc-salt string                     Password hashing salt (default "dlPL2MqE")
      --rc-serve                           Enable the serving of remote objects
      --rc-serve-no-modtime                Don't read the modification time (can speed things up)
      --rc-server-read-timeout Duration    Timeout for server reading data (default 1h0m0s)
      --rc-server-write-timeout Duration   Timeout for server writing data (default 1h0m0s)
      --rc-template string                 User-specified template
      --rc-user string                     User name for authentication
      --rc-user-from-header string         User name from a defined HTTP header
      --rc-web-fetch-url string            URL to fetch the releases for webgui (default "https://api.github.com/repos/rclone/rclone-webui-react/releases/latest")
      --rc-web-gui                         Launch WebGUI on localhost
      --rc-web-gui-force-update            Force update to latest version of web gui
      --rc-web-gui-no-open-browser         Don't open the browser automatically
      --rc-web-gui-update                  Check and update to latest version of web gui

Flags to control the Metrics HTTP endpoint. (flag group Metrics):
      --metrics-addr stringArray                IPaddress:Port or :Port to bind metrics server to
      --metrics-allow-origin string             Origin which cross-domain request (CORS) can be executed from
      --metrics-baseurl string                  Prefix for URLs - leave blank for root
      --metrics-cert string                     TLS PEM key (concatenation of certificate and CA certificate)
      --metrics-client-ca string                Client certificate authority to verify clients with
      --metrics-htpasswd string                 A htpasswd file - if not provided no authentication is done
      --metrics-key string                      TLS PEM Private key
      --metrics-max-header-bytes int            Maximum size of request header (default 4096)
      --metrics-min-tls-version string          Minimum TLS version that is acceptable (default "tls1.0")
      --metrics-pass string                     Password for authentication
      --metrics-realm string                    Realm for authentication
      --metrics-salt string                     Password hashing salt (default "dlPL2MqE")
      --metrics-server-read-timeout Duration    Timeout for server reading data (default 1h0m0s)
      --metrics-server-write-timeout Duration   Timeout for server writing data (default 1h0m0s)
      --metrics-template string                 User-specified template
      --metrics-user string                     User name for authentication
      --metrics-user-from-header string         User name from a defined HTTP header
      --rc-enable-metrics                       Enable the Prometheus metrics path at the remote control server

Backend-only flags (these can be set in the config file also) (flag group Backend):
      --alias-description string                            Description of the remote
      --alias-remote string                                 Remote or path to alias
      --archive-description string                          Description of the remote
      --archive-remote string                               Remote to wrap to read archives from
      --azureblob-access-tier string                        Access tier of blob: hot, cool, cold or archive
      --azureblob-account string                            Azure Storage Account Name
      --azureblob-archive-tier-delete                       Delete archive tier blobs before overwriting
      --azureblob-chunk-size SizeSuffix                     Upload chunk size (default 4Mi)
      --azureblob-client-certificate-password string        Password for the certificate file (optional) (obscured)
      --azureblob-client-certificate-path string            Path to a PEM or PKCS12 certificate file including the private key
      --azureblob-client-id string                          The ID of the client in use
      --azureblob-client-secret string                      One of the service principal's client secrets
      --azureblob-client-send-certificate-chain             Send the certificate chain when using certificate auth
      --azureblob-connection-string string                  Storage Connection String
      --azureblob-copy-concurrency int                      Concurrency for multipart copy (default 512)
      --azureblob-copy-cutoff SizeSuffix                    Cutoff for switching to multipart copy (default 8Mi)
      --azureblob-delete-snapshots string                   Set to specify how to deal with snapshots on blob deletion
      --azureblob-description string                        Description of the remote
      --azureblob-directory-markers                         Upload an empty object with a trailing slash when a new directory is created
      --azureblob-disable-checksum                          Don't store MD5 checksum with object metadata
      --azureblob-disable-instance-discovery                Skip requesting Microsoft Entra instance metadata
      --azureblob-encoding Encoding                         The encoding for the backend (default Slash,BackSlash,Del,Ctl,RightPeriod,InvalidUtf8)
      --azureblob-endpoint string                           Endpoint for the service
      --azureblob-env-auth                                  Read credentials from runtime (environment variables, CLI or MSI)
      --azureblob-key string                                Storage Account Shared Key
      --azureblob-list-chunk int                            Size of blob list (default 5000)
      --azureblob-msi-client-id string                      Object ID of the user-assigned MSI to use, if any
      --azureblob-msi-mi-res-id string                      Azure resource ID of the user-assigned MSI to use, if any
      --azureblob-msi-object-id string                      Object ID of the user-assigned MSI to use, if any
      --azureblob-no-check-container                        If set, don't attempt to check the container exists or create it
      --azureblob-no-head-object                            If set, do not do HEAD before GET when getting objects
      --azureblob-password string                           The user's password (obscured)
      --azureblob-public-access string                      Public access level of a container: blob or container
      --azureblob-sas-url string                            SAS URL for container level access only
      --azureblob-service-principal-file string             Path to file containing credentials for use with a service principal
      --azureblob-tenant string                             ID of the service principal's tenant. Also called its directory ID
      --azureblob-upload-concurrency int                    Concurrency for multipart uploads (default 16)
      --azureblob-upload-cutoff string                      Cutoff for switching to chunked upload (<= 256 MiB) (deprecated)
      --azureblob-use-az                                    Use Azure CLI tool az for authentication
      --azureblob-use-copy-blob                             Whether to use the Copy Blob API when copying to the same storage account (default true)
      --azureblob-use-emulator                              Uses local storage emulator if provided as 'true'
      --azureblob-use-msi                                   Use a managed service identity to authenticate (only works in Azure)
      --azureblob-username string                           User name (usually an email address)
      --azurefiles-account string                           Azure Storage Account Name
      --azurefiles-chunk-size SizeSuffix                    Upload chunk size (default 4Mi)
      --azurefiles-client-certificate-password string       Password for the certificate file (optional) (obscured)
      --azurefiles-client-certificate-path string           Path to a PEM or PKCS12 certificate file including the private key
      --azurefiles-client-id string                         The ID of the client in use
      --azurefiles-client-secret string                     One of the service principal's client secrets
      --azurefiles-client-send-certificate-chain            Send the certificate chain when using certificate auth
      --azurefiles-connection-string string                 Storage Connection String
      --azurefiles-description string                       Description of the remote
      --azurefiles-disable-instance-discovery               Skip requesting Microsoft Entra instance metadata
      --azurefiles-encoding Encoding                        The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Del,Ctl,RightPeriod,InvalidUtf8,Dot)
      --azurefiles-endpoint string                          Endpoint for the service
      --azurefiles-env-auth                                 Read credentials from runtime (environment variables, CLI or MSI)
      --azurefiles-key string                               Storage Account Shared Key
      --azurefiles-max-stream-size SizeSuffix               Max size for streamed files (default 10Gi)
      --azurefiles-msi-client-id string                     Object ID of the user-assigned MSI to use, if any
      --azurefiles-msi-mi-res-id string                     Azure resource ID of the user-assigned MSI to use, if any
      --azurefiles-msi-object-id string                     Object ID of the user-assigned MSI to use, if any
      --azurefiles-password string                          The user's password (obscured)
      --azurefiles-sas-url string                           SAS URL for container level access only
      --azurefiles-service-principal-file string            Path to file containing credentials for use with a service principal
      --azurefiles-share-name string                        Azure Files Share Name
      --azurefiles-tenant string                            ID of the service principal's tenant. Also called its directory ID
      --azurefiles-upload-concurrency int                   Concurrency for multipart uploads (default 16)
      --azurefiles-use-az                                   Use Azure CLI tool az for authentication
      --azurefiles-use-emulator                             Uses local storage emulator if provided as 'true'
      --azurefiles-use-msi                                  Use a managed service identity to authenticate (only works in Azure)
      --azurefiles-username string                          User name (usually an email address)
      --b2-account string                                   Account ID or Application Key ID
      --b2-chunk-size SizeSuffix                            Upload chunk size (default 96Mi)
      --b2-copy-cutoff SizeSuffix                           Cutoff for switching to multipart copy (default 4Gi)
      --b2-description string                               Description of the remote
      --b2-disable-checksum                                 Disable checksums for large (> upload cutoff) files
      --b2-download-auth-duration Duration                  Time before the public link authorization token will expire in s or suffix ms|s|m|h|d (default 1w)
      --b2-download-url string                              Custom endpoint for downloads
      --b2-encoding Encoding                                The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --b2-endpoint string                                  Endpoint for the service
      --b2-hard-delete                                      Permanently delete files on remote removal, otherwise hide files
      --b2-key string                                       Application Key
      --b2-lifecycle int                                    Set the number of days deleted files should be kept when creating a bucket
      --b2-sse-customer-algorithm string                    If using SSE-C, the server-side encryption algorithm used when storing this object in B2
      --b2-sse-customer-key string                          To use SSE-C, you may provide the secret encryption key encoded in a UTF-8 compatible string to encrypt/decrypt your data
      --b2-sse-customer-key-base64 string                   To use SSE-C, you may provide the secret encryption key encoded in Base64 format to encrypt/decrypt your data
      --b2-sse-customer-key-md5 string                      If using SSE-C you may provide the secret encryption key MD5 checksum (optional)
      --b2-test-mode string                                 A flag string for X-Bz-Test-Mode header for debugging
      --b2-upload-concurrency int                           Concurrency for multipart uploads (default 4)
      --b2-upload-cutoff SizeSuffix                         Cutoff for switching to chunked upload (default 200Mi)
      --b2-version-at Time                                  Show file versions as they were at the specified time (default off)
      --b2-versions                                         Include old versions in directory listings
      --box-access-token string                             Box App Primary Access Token
      --box-auth-url string                                 Auth server URL
      --box-box-config-file string                          Box App config.json location
      --box-box-sub-type string                              (default "user")
      --box-client-credentials                              Use client credentials OAuth flow
      --box-client-id string                                OAuth Client Id
      --box-client-secret string                            OAuth Client Secret
      --box-commit-retries int                              Max number of times to try committing a multipart file (default 100)
      --box-description string                              Description of the remote
      --box-encoding Encoding                               The encoding for the backend (default Slash,BackSlash,Del,Ctl,RightSpace,InvalidUtf8,Dot)
      --box-impersonate string                              Impersonate this user ID when using a service account
      --box-list-chunk int                                  Size of listing chunk 1-1000 (default 1000)
      --box-owned-by string                                 Only show items owned by the login (email address) passed in
      --box-root-folder-id string                           Fill in for rclone to use a non root folder as its starting point
      --box-token string                                    OAuth Access Token as a JSON blob
      --box-token-url string                                Token server url
      --box-upload-cutoff SizeSuffix                        Cutoff for switching to multipart upload (>= 50 MiB) (default 50Mi)
      --cache-chunk-clean-interval Duration                 How often should the cache perform cleanups of the chunk storage (default 1m0s)
      --cache-chunk-no-memory                               Disable the in-memory cache for storing chunks during streaming
      --cache-chunk-path string                             Directory to cache chunk files (default "/home/jupyter-will/.cache/rclone/cache-backend")
      --cache-chunk-size SizeSuffix                         The size of a chunk (partial file data) (default 5Mi)
      --cache-chunk-total-size SizeSuffix                   The total size that the chunks can take up on the local disk (default 10Gi)
      --cache-db-path string                                Directory to store file structure metadata DB (default "/home/jupyter-will/.cache/rclone/cache-backend")
      --cache-db-purge                                      Clear all the cached data for this remote on start
      --cache-db-wait-time Duration                         How long to wait for the DB to be available - 0 is unlimited (default 1s)
      --cache-description string                            Description of the remote
      --cache-info-age Duration                             How long to cache file structure information (directory listings, file size, times, etc.) (default 6h0m0s)
      --cache-plex-insecure string                          Skip all certificate verification when connecting to the Plex server
      --cache-plex-password string                          The password of the Plex user (obscured)
      --cache-plex-url string                               The URL of the Plex server
      --cache-plex-username string                          The username of the Plex user
      --cache-read-retries int                              How many times to retry a read from a cache storage (default 10)
      --cache-remote string                                 Remote to cache
      --cache-rps int                                       Limits the number of requests per second to the source FS (-1 to disable) (default -1)
      --cache-tmp-upload-path string                        Directory to keep temporary files until they are uploaded
      --cache-tmp-wait-time Duration                        How long should files be stored in local cache before being uploaded (default 15s)
      --cache-workers int                                   How many workers should run in parallel to download chunks (default 4)
      --cache-writes                                        Cache file data on writes through the FS
      --chunker-chunk-size SizeSuffix                       Files larger than chunk size will be split in chunks (default 2Gi)
      --chunker-description string                          Description of the remote
      --chunker-fail-hard                                   Choose how chunker should handle files with missing or invalid chunks
      --chunker-hash-type string                            Choose how chunker handles hash sums (default "md5")
      --chunker-remote string                               Remote to chunk/unchunk
      --cloudinary-adjust-media-files-extensions            Cloudinary handles media formats as a file attribute and strips it from the name, which is unlike most other file systems (default true)
      --cloudinary-api-key string                           Cloudinary API Key
      --cloudinary-api-secret string                        Cloudinary API Secret
      --cloudinary-cloud-name string                        Cloudinary Environment Name
      --cloudinary-description string                       Description of the remote
      --cloudinary-encoding Encoding                        The encoding for the backend (default Slash,LtGt,DoubleQuote,Question,Asterisk,Pipe,Hash,Percent,BackSlash,Del,Ctl,RightSpace,InvalidUtf8,Dot)
      --cloudinary-eventually-consistent-delay Duration     Wait N seconds for eventual consistency of the databases that support the backend operation (default 0s)
      --cloudinary-media-extensions stringArray             Cloudinary supported media extensions (default 3ds,3g2,3gp,ai,arw,avi,avif,bmp,bw,cr2,cr3,djvu,dng,eps3,fbx,flif,flv,gif,glb,gltf,hdp,heic,heif,ico,indd,jp2,jpe,jpeg,jpg,jxl,jxr,m2ts,mov,mp4,mpeg,mts,mxf,obj,ogv,pdf,ply,png,psd,svg,tga,tif,tiff,ts,u3ma,usdz,wdp,webm,webp,wmv)
      --cloudinary-upload-prefix string                     Specify the API endpoint for environments out of the US
      --cloudinary-upload-preset string                     Upload Preset to select asset manipulation on upload
      --combine-description string                          Description of the remote
      --combine-upstreams SpaceSepList                      Upstreams for combining
      --compress-description string                         Description of the remote
      --compress-level string                               GZIP (levels -2 to 9):
      --compress-mode string                                Compression mode (default "gzip")
      --compress-ram-cache-limit SizeSuffix                 Some remotes don't allow the upload of files with unknown size (default 20Mi)
      --compress-remote string                              Remote to compress
  -L, --copy-links                                          Follow symlinks and copy the pointed to item
      --crypt-description string                            Description of the remote
      --crypt-directory-name-encryption                     Option to either encrypt directory names or leave them intact (default true)
      --crypt-filename-encoding string                      How to encode the encrypted filename to text string (default "base32")
      --crypt-filename-encryption string                    How to encrypt the filenames (default "standard")
      --crypt-no-data-encryption                            Option to either encrypt file data or leave it unencrypted
      --crypt-pass-bad-blocks                               If set this will pass bad blocks through as all 0
      --crypt-password string                               Password or pass phrase for encryption (obscured)
      --crypt-password2 string                              Password or pass phrase for salt (obscured)
      --crypt-remote string                                 Remote to encrypt/decrypt
      --crypt-server-side-across-configs                    Deprecated: use --server-side-across-configs instead
      --crypt-show-mapping                                  For all files listed show how the names encrypt
      --crypt-strict-names                                  If set, this will raise an error when crypt comes across a filename that can't be decrypted
      --crypt-suffix string                                 If this is set it will override the default suffix of ".bin" (default ".bin")
      --doi-description string                              Description of the remote
      --doi-doi string                                      The DOI or the doi.org URL
      --doi-doi-resolver-api-url string                     The URL of the DOI resolver API to use
      --doi-provider string                                 DOI provider
      --drime-access-token string                           API Access token
      --drime-chunk-size SizeSuffix                         Chunk size to use for uploading (default 5Mi)
      --drime-description string                            Description of the remote
      --drime-encoding Encoding                             The encoding for the backend (default Slash,BackSlash,Del,Ctl,LeftSpace,RightSpace,InvalidUtf8,Dot)
      --drime-hard-delete                                   Delete files permanently rather than putting them into the trash
      --drime-list-chunk int                                Number of items to list in each call (default 1000)
      --drime-root-folder-id string                         ID of the root folder
      --drime-upload-concurrency int                        Concurrency for multipart uploads and copies (default 4)
      --drime-upload-cutoff SizeSuffix                      Cutoff for switching to chunked upload (default 200Mi)
      --drime-workspace-id string                           Account ID
      --drive-acknowledge-abuse                             Set to allow files which return cannotDownloadAbusiveFile to be downloaded
      --drive-allow-import-name-change                      Allow the filetype to change when uploading Google docs
      --drive-auth-owner-only                               Only consider files owned by the authenticated user
      --drive-auth-url string                               Auth server URL
      --drive-chunk-size SizeSuffix                         Upload chunk size (default 8Mi)
      --drive-client-credentials                            Use client credentials OAuth flow
      --drive-client-id string                              Google Application Client Id
      --drive-client-secret string                          OAuth Client Secret
      --drive-copy-shortcut-content                         Server side copy contents of shortcuts instead of the shortcut
      --drive-description string                            Description of the remote
      --drive-disable-http2                                 Disable drive using http2 (default true)
      --drive-encoding Encoding                             The encoding for the backend (default InvalidUtf8)
      --drive-env-auth                                      Get IAM credentials from runtime (environment variables or instance meta data if no env vars)
      --drive-export-formats string                         Comma separated list of preferred formats for downloading Google docs (default "docx,xlsx,pptx,svg")
      --drive-fast-list-bug-fix                             Work around a bug in Google Drive listing (default true)
      --drive-formats string                                Deprecated: See export_formats
      --drive-impersonate string                            Impersonate this user when using a service account
      --drive-import-formats string                         Comma separated list of preferred formats for uploading Google docs
      --drive-keep-revision-forever                         Keep new head revision of each file forever
      --drive-list-chunk int                                Size of listing chunk 100-1000, 0 to disable (default 1000)
      --drive-metadata-enforce-expansive-access             Whether the request should enforce expansive access rules
      --drive-metadata-labels Bits                          Control whether labels should be read or written in metadata (default off)
      --drive-metadata-owner Bits                           Control whether owner should be read or written in metadata (default read)
      --drive-metadata-permissions Bits                     Control whether permissions should be read or written in metadata (default off)
      --drive-pacer-burst int                               Number of API calls to allow without sleeping (default 100)
      --drive-pacer-min-sleep Duration                      Minimum time to sleep between API calls (default 100ms)
      --drive-resource-key string                           Resource key for accessing a link-shared file
      --drive-root-folder-id string                         ID of the root folder
      --drive-scope string                                  Comma separated list of scopes that rclone should use when requesting access from drive
      --drive-server-side-across-configs                    Deprecated: use --server-side-across-configs instead
      --drive-service-account-credentials string            Service Account Credentials JSON blob
      --drive-service-account-file string                   Service Account Credentials JSON file path
      --drive-shared-with-me                                Only show files that are shared with me
      --drive-show-all-gdocs                                Show all Google Docs including non-exportable ones in listings
      --drive-size-as-quota                                 Show sizes as storage quota usage, not actual size
      --drive-skip-checksum-gphotos                         Skip checksums on Google photos and videos only
      --drive-skip-dangling-shortcuts                       If set skip dangling shortcut files
      --drive-skip-gdocs                                    Skip google documents in all listings
      --drive-skip-shortcuts                                If set skip shortcut files
      --drive-starred-only                                  Only show files that are starred
      --drive-stop-on-download-limit                        Make download limit errors be fatal
      --drive-stop-on-upload-limit                          Make upload limit errors be fatal
      --drive-team-drive string                             ID of the Shared Drive (Team Drive)
      --drive-token string                                  OAuth Access Token as a JSON blob
      --drive-token-url string                              Token server url
      --drive-trashed-only                                  Only show files that are in the trash
      --drive-upload-cutoff SizeSuffix                      Cutoff for switching to chunked upload (default 8Mi)
      --drive-use-created-date                              Use file created date instead of modified date
      --drive-use-shared-date                               Use date file was shared instead of modified date
      --drive-use-trash                                     Send files to the trash instead of deleting permanently (default true)
      --drive-v2-download-min-size SizeSuffix               If Object's are greater, use drive v2 API to download (default off)
      --dropbox-auth-url string                             Auth server URL
      --dropbox-batch-mode string                           Upload file batching sync|async|off (default "sync")
      --dropbox-batch-size int                              Max number of files in upload batch
      --dropbox-batch-timeout Duration                      Max time to allow an idle upload batch before uploading (default 0s)
      --dropbox-chunk-size SizeSuffix                       Upload chunk size (< 150Mi) (default 48Mi)
      --dropbox-client-credentials                          Use client credentials OAuth flow
      --dropbox-client-id string                            OAuth Client Id
      --dropbox-client-secret string                        OAuth Client Secret
      --dropbox-description string                          Description of the remote
      --dropbox-encoding Encoding                           The encoding for the backend (default Slash,BackSlash,Del,RightSpace,InvalidUtf8,Dot)
      --dropbox-export-formats CommaSepList                 Comma separated list of preferred formats for exporting files (default html,md)
      --dropbox-impersonate string                          Impersonate this user when using a business account
      --dropbox-pacer-min-sleep Duration                    Minimum time to sleep between API calls (default 10ms)
      --dropbox-root-namespace string                       Specify a different Dropbox namespace ID to use as the root for all paths
      --dropbox-shared-files                                Instructs rclone to work on individual shared files
      --dropbox-shared-folders                              Instructs rclone to work on shared folders
      --dropbox-show-all-exports                            Show all exportable files in listings
      --dropbox-skip-exports                                Skip exportable files in all listings
      --dropbox-token string                                OAuth Access Token as a JSON blob
      --dropbox-token-url string                            Token server url
      --fichier-api-key string                              Your API Key, get it from https://1fichier.com/console/params.pl
      --fichier-cdn                                         Set if you wish to use CDN download links
      --fichier-description string                          Description of the remote
      --fichier-encoding Encoding                           The encoding for the backend (default Slash,LtGt,DoubleQuote,SingleQuote,BackQuote,Dollar,BackSlash,Del,Ctl,LeftSpace,RightSpace,InvalidUtf8,Dot)
      --fichier-file-password string                        If you want to download a shared file that is password protected, add this parameter (obscured)
      --fichier-folder-password string                      If you want to list the files in a shared folder that is password protected, add this parameter (obscured)
      --fichier-shared-folder string                        If you want to download a shared folder, add this parameter
      --filefabric-description string                       Description of the remote
      --filefabric-encoding Encoding                        The encoding for the backend (default Slash,Del,Ctl,InvalidUtf8,Dot)
      --filefabric-permanent-token string                   Permanent Authentication Token
      --filefabric-root-folder-id string                    ID of the root folder
      --filefabric-token string                             Session Token
      --filefabric-token-expiry string                      Token expiry time
      --filefabric-url string                               URL of the Enterprise File Fabric to connect to
      --filefabric-version string                           Version read from the file fabric
      --filelu-chunk-size SizeSuffix                        Chunk size to use for uploading. Used for multipart uploads (default 64Mi)
      --filelu-description string                           Description of the remote
      --filelu-encoding Encoding                            The encoding for the backend (default Slash,LtGt,DoubleQuote,SingleQuote,BackQuote,Dollar,Colon,Question,Asterisk,Pipe,Hash,Percent,BackSlash,CrLf,Del,Ctl,LeftSpace,LeftPeriod,LeftTilde,LeftCrLfHtVt,RightSpace,RightPeriod,RightCrLfHtVt,InvalidUtf8,Dot,SquareBracket,Semicolon,Exclamation)
      --filelu-key string                                   Your FileLu Rclone key from My Account
      --filelu-upload-cutoff SizeSuffix                     Cutoff for switching to chunked upload. Any files larger than this will be uploaded in chunks of chunk_size (default 500Mi)
      --filen-api-key string                                API Key for your Filen account (obscured)
      --filen-auth-version string                           Authentication Version (internal use only)
      --filen-base-folder-uuid string                       UUID of Account Root Directory (internal use only)
      --filen-description string                            Description of the remote
      --filen-email string                                  Email of your Filen account
      --filen-encoding Encoding                             The encoding for the backend (default Slash,Del,Ctl,InvalidUtf8,Dot)
      --filen-master-keys string                            Master Keys (internal use only)
      --filen-password string                               Password of your Filen account (obscured)
      --filen-private-key string                            Private RSA Key (internal use only)
      --filen-public-key string                             Public RSA Key (internal use only)
      --filen-upload-concurrency int                        Concurrency for chunked uploads (default 16)
      --filescom-api-key string                             The API key used to authenticate with Files.com
      --filescom-description string                         Description of the remote
      --filescom-encoding Encoding                          The encoding for the backend (default Slash,BackSlash,Del,Ctl,RightSpace,RightCrLfHtVt,InvalidUtf8,Dot)
      --filescom-password string                            The password used to authenticate with Files.com (obscured)
      --filescom-site string                                Your site subdomain (e.g. mysite) or custom domain (e.g. myfiles.customdomain.com)
      --filescom-username string                            The username used to authenticate with Files.com
      --ftp-allow-insecure-tls-ciphers                      Allow insecure TLS ciphers
      --ftp-ask-password                                    Allow asking for FTP password when needed
      --ftp-close-timeout Duration                          Maximum time to wait for a response to close (default 1m0s)
      --ftp-concurrency int                                 Maximum number of FTP simultaneous connections, 0 for unlimited
      --ftp-description string                              Description of the remote
      --ftp-disable-epsv                                    Disable using EPSV even if server advertises support
      --ftp-disable-mlsd                                    Disable using MLSD even if server advertises support
      --ftp-disable-tls13                                   Disable TLS 1.3 (workaround for FTP servers with buggy TLS)
      --ftp-disable-utf8                                    Disable using UTF-8 even if server advertises support
      --ftp-encoding Encoding                               The encoding for the backend (default Slash,Del,Ctl,RightSpace,Dot)
      --ftp-explicit-tls                                    Use Explicit FTPS (FTP over TLS)
      --ftp-force-list-hidden                               Use LIST -a to force listing of hidden files and folders. This will disable the use of MLSD
      --ftp-host string                                     FTP host to connect to
      --ftp-http-proxy string                               URL for HTTP CONNECT proxy
      --ftp-idle-timeout Duration                           Max time before closing idle connections (default 1m0s)
      --ftp-no-check-certificate                            Do not verify the TLS certificate of the server
      --ftp-no-check-upload                                 Don't check the upload is OK
      --ftp-pass string                                     FTP password (obscured)
      --ftp-port int                                        FTP port number (default 21)
      --ftp-shut-timeout Duration                           Maximum time to wait for data connection closing status (default 1m0s)
      --ftp-socks-proxy string                              Socks 5 proxy host
      --ftp-tls                                             Use Implicit FTPS (FTP over TLS)
      --ftp-tls-cache-size int                              Size of TLS session cache for all control and data connections (default 32)
      --ftp-user string                                     FTP username (default "root")
      --ftp-writing-mdtm                                    Use MDTM to set modification time (VsFtpd quirk)
      --gcs-access-token string                             Short-lived access token
      --gcs-anonymous                                       Access public buckets and objects without credentials
      --gcs-auth-url string                                 Auth server URL
      --gcs-bucket-acl string                               Access Control List for new buckets
      --gcs-bucket-policy-only                              Access checks should use bucket-level IAM policies
      --gcs-client-credentials                              Use client credentials OAuth flow
      --gcs-client-id string                                OAuth Client Id
      --gcs-client-secret string                            OAuth Client Secret
      --gcs-decompress                                      If set this will decompress gzip encoded objects
      --gcs-description string                              Description of the remote
      --gcs-directory-markers                               Upload an empty object with a trailing slash when a new directory is created
      --gcs-encoding Encoding                               The encoding for the backend (default Slash,CrLf,InvalidUtf8,Dot)
      --gcs-endpoint string                                 Custom endpoint for the storage API. Leave blank to use the provider default
      --gcs-env-auth                                        Get GCP IAM credentials from runtime (environment variables or instance meta data if no env vars)
      --gcs-location string                                 Location for the newly created buckets
      --gcs-no-check-bucket                                 If set, don't attempt to check the bucket exists or create it
      --gcs-object-acl string                               Access Control List for new objects
      --gcs-project-number string                           Project number
      --gcs-service-account-file string                     Service Account Credentials JSON file path
      --gcs-storage-class string                            The storage class to use when storing objects in Google Cloud Storage
      --gcs-token string                                    OAuth Access Token as a JSON blob
      --gcs-token-url string                                Token server url
      --gcs-user-project string                             User project
      --gofile-access-token string                          API Access token
      --gofile-account-id string                            Account ID
      --gofile-description string                           Description of the remote
      --gofile-encoding Encoding                            The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Del,Ctl,LeftPeriod,RightPeriod,InvalidUtf8,Dot,Exclamation)
      --gofile-list-chunk int                               Number of items to list in each call (default 1000)
      --gofile-root-folder-id string                        ID of the root folder
      --gphotos-auth-url string                             Auth server URL
      --gphotos-batch-mode string                           Upload file batching sync|async|off (default "sync")
      --gphotos-batch-size int                              Max number of files in upload batch
      --gphotos-batch-timeout Duration                      Max time to allow an idle upload batch before uploading (default 0s)
      --gphotos-client-credentials                          Use client credentials OAuth flow
      --gphotos-client-id string                            OAuth Client Id
      --gphotos-client-secret string                        OAuth Client Secret
      --gphotos-description string                          Description of the remote
      --gphotos-encoding Encoding                           The encoding for the backend (default Slash,CrLf,InvalidUtf8,Dot)
      --gphotos-include-archived                            Also view and download archived media
      --gphotos-proxy string                                Use the gphotosdl proxy for downloading the full resolution images
      --gphotos-read-only                                   Set to make the Google Photos backend read only
      --gphotos-read-size                                   Set to read the size of media items
      --gphotos-start-year int                              Year limits the photos to be downloaded to those which are uploaded after the given year (default 2000)
      --gphotos-token string                                OAuth Access Token as a JSON blob
      --gphotos-token-url string                            Token server url
      --hasher-auto-size SizeSuffix                         Auto-update checksum for files smaller than this size (disabled by default)
      --hasher-description string                           Description of the remote
      --hasher-hashes CommaSepList                          Comma separated list of supported checksum types (default md5,sha1)
      --hasher-max-age Duration                             Maximum time to keep checksums in cache (0 = no cache, off = cache forever) (default off)
      --hasher-remote string                                Remote to cache checksums for (e.g. myRemote:path)
      --hdfs-data-transfer-protection string                Kerberos data transfer protection: authentication|integrity|privacy
      --hdfs-description string                             Description of the remote
      --hdfs-encoding Encoding                              The encoding for the backend (default Slash,Colon,Del,Ctl,InvalidUtf8,Dot)
      --hdfs-namenode CommaSepList                          Hadoop name nodes and ports
      --hdfs-service-principal-name string                  Kerberos service principal name for the namenode
      --hdfs-username string                                Hadoop user name
      --hidrive-auth-url string                             Auth server URL
      --hidrive-chunk-size SizeSuffix                       Chunksize for chunked uploads (default 48Mi)
      --hidrive-client-credentials                          Use client credentials OAuth flow
      --hidrive-client-id string                            OAuth Client Id
      --hidrive-client-secret string                        OAuth Client Secret
      --hidrive-description string                          Description of the remote
      --hidrive-disable-fetching-member-count               Do not fetch number of objects in directories unless it is absolutely necessary
      --hidrive-encoding Encoding                           The encoding for the backend (default Slash,Dot)
      --hidrive-endpoint string                             Endpoint for the service (default "https://api.hidrive.strato.com/2.1")
      --hidrive-root-prefix string                          The root/parent folder for all paths (default "/")
      --hidrive-scope-access string                         Access permissions that rclone should use when requesting access from HiDrive (default "rw")
      --hidrive-scope-role string                           User-level that rclone should use when requesting access from HiDrive (default "user")
      --hidrive-token string                                OAuth Access Token as a JSON blob
      --hidrive-token-url string                            Token server url
      --hidrive-upload-concurrency int                      Concurrency for chunked uploads (default 4)
      --hidrive-upload-cutoff SizeSuffix                    Cutoff/Threshold for chunked uploads (default 96Mi)
      --http-description string                             Description of the remote
      --http-headers CommaSepList                           Set HTTP headers for all transactions
      --http-no-escape                                      Do not escape URL metacharacters in path names
      --http-no-head                                        Don't use HEAD requests
      --http-no-slash                                       Set this if the site doesn't end directories with /
      --http-url string                                     URL of HTTP host to connect to
      --iclouddrive-apple-id string                         Apple ID
      --iclouddrive-client-id string                        Client id (default "d39ba9916b7251055b22c7f910e2ea796ee65e98b2ddecea8f5dde8d9d1a815d")
      --iclouddrive-description string                      Description of the remote
      --iclouddrive-encoding Encoding                       The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --iclouddrive-password string                         Password (obscured)
      --imagekit-description string                         Description of the remote
      --imagekit-encoding Encoding                          The encoding for the backend (default Slash,LtGt,DoubleQuote,Dollar,Question,Hash,Percent,BackSlash,Del,Ctl,InvalidUtf8,Dot,SquareBracket)
      --imagekit-endpoint string                            You can find your ImageKit.io URL endpoint in your [dashboard](https://imagekit.io/dashboard/developer/api-keys)
      --imagekit-only-signed Restrict unsigned image URLs   If you have configured Restrict unsigned image URLs in your dashboard settings, set this to true
      --imagekit-private-key string                         You can find your ImageKit.io private key in your [dashboard](https://imagekit.io/dashboard/developer/api-keys)
      --imagekit-public-key string                          You can find your ImageKit.io public key in your [dashboard](https://imagekit.io/dashboard/developer/api-keys)
      --imagekit-upload-tags string                         Tags to add to the uploaded files, e.g. "tag1,tag2"
      --imagekit-versions                                   Include old versions in directory listings
      --internetarchive-access-key-id string                IAS3 Access Key
      --internetarchive-description string                  Description of the remote
      --internetarchive-disable-checksum                    Don't ask the server to test against MD5 checksum calculated by rclone (default true)
      --internetarchive-encoding Encoding                   The encoding for the backend (default Slash,LtGt,CrLf,Del,Ctl,InvalidUtf8,Dot)
      --internetarchive-endpoint string                     IAS3 Endpoint (default "https://s3.us.archive.org")
      --internetarchive-front-endpoint string               Host of InternetArchive Frontend (default "https://archive.org")
      --internetarchive-item-derive                         Whether to trigger derive on the IA item or not. If set to false, the item will not be derived by IA upon upload (default true)
      --internetarchive-item-metadata stringArray           Metadata to be set on the IA item, this is different from file-level metadata that can be set using --metadata-set
      --internetarchive-secret-access-key string            IAS3 Secret Key (password)
      --internetarchive-wait-archive Duration               Timeout for waiting the server's processing tasks (specifically archive and book_op) to finish (default 0s)
      --internxt-description string                         Description of the remote
      --internxt-email string                               Email of your Internxt account
      --internxt-encoding Encoding                          The encoding for the backend (default Slash,BackSlash,CrLf,RightPeriod,InvalidUtf8,Dot)
      --internxt-pass string                                Password (obscured)
      --internxt-skip-hash-validation                       Skip hash validation when downloading files (default true)
      --jottacloud-auth-url string                          Auth server URL
      --jottacloud-client-credentials                       Use client credentials OAuth flow
      --jottacloud-client-id string                         OAuth Client Id
      --jottacloud-client-secret string                     OAuth Client Secret
      --jottacloud-description string                       Description of the remote
      --jottacloud-encoding Encoding                        The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,Del,Ctl,InvalidUtf8,Dot)
      --jottacloud-hard-delete                              Delete files permanently rather than putting them into the trash
      --jottacloud-md5-memory-limit SizeSuffix              Files bigger than this will be cached on disk to calculate the MD5 if required (default 10Mi)
      --jottacloud-no-versions                              Avoid server side versioning by deleting files and recreating files instead of overwriting them
      --jottacloud-token string                             OAuth Access Token as a JSON blob
      --jottacloud-token-url string                         Token server url
      --jottacloud-trashed-only                             Only show files that are in the trash
      --jottacloud-upload-resume-limit SizeSuffix           Files bigger than this can be resumed if the upload fail's (default 10Mi)
      --koofr-description string                            Description of the remote
      --koofr-encoding Encoding                             The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --koofr-endpoint string                               The Koofr API endpoint to use
      --koofr-mountid string                                Mount ID of the mount to use
      --koofr-password string                               Your password for rclone generate one at https://app.koofr.net/app/admin/preferences/password (obscured)
      --koofr-provider string                               Choose your storage provider
      --koofr-setmtime                                      Does the backend support setting modification time (default true)
      --koofr-user string                                   Your user name
      --linkbox-description string                          Description of the remote
      --linkbox-token string                                Token from https://www.linkbox.to/admin/account
      --local-case-insensitive                              Force the filesystem to report itself as case insensitive
      --local-case-sensitive                                Force the filesystem to report itself as case sensitive
      --local-description string                            Description of the remote
      --local-encoding Encoding                             The encoding for the backend (default Slash,Dot)
      --local-hashes CommaSepList                           Comma separated list of supported checksum types
      --local-links                                         Translate symlinks to/from regular files with a '.rclonelink' extension for the local backend
      --local-no-check-updated                              Don't check to see if the files change during upload
      --local-no-clone                                      Disable reflink cloning for server-side copies
      --local-no-preallocate                                Disable preallocation of disk space for transferred files
      --local-no-set-modtime                                Disable setting modtime
      --local-no-sparse                                     Disable sparse files for multi-thread downloads
      --local-nounc                                         Disable UNC (long path names) conversion on Windows
      --local-time-type mtime|atime|btime|ctime             Set what kind of time is returned (default mtime)
      --local-unicode-normalization                         Apply unicode NFC normalization to paths and filenames
      --local-zero-size-links                               Assume the Stat size of links is zero (and read them instead) (deprecated)
      --mailru-auth-url string                              Auth server URL
      --mailru-check-hash                                   What should copy do if file checksum is mismatched or invalid (default true)
      --mailru-client-credentials                           Use client credentials OAuth flow
      --mailru-client-id string                             OAuth Client Id
      --mailru-client-secret string                         OAuth Client Secret
      --mailru-description string                           Description of the remote
      --mailru-encoding Encoding                            The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --mailru-pass string                                  Password (obscured)
      --mailru-speedup-enable                               Skip full upload if there is another file with same data hash (default true)
      --mailru-speedup-file-patterns string                 Comma separated list of file name patterns eligible for speedup (put by hash) (default "*.mkv,*.avi,*.mp4,*.mp3,*.zip,*.gz,*.rar,*.pdf")
      --mailru-speedup-max-disk SizeSuffix                  This option allows you to disable speedup (put by hash) for large files (default 3Gi)
      --mailru-speedup-max-memory SizeSuffix                Files larger than the size given below will always be hashed on disk (default 32Mi)
      --mailru-token string                                 OAuth Access Token as a JSON blob
      --mailru-token-url string                             Token server url
      --mailru-user string                                  User name (usually email)
      --mega-2fa string                                     The 2FA code of your MEGA account if the account is set up with one
      --mega-debug                                          Output more debug from Mega
      --mega-description string                             Description of the remote
      --mega-encoding Encoding                              The encoding for the backend (default Slash,InvalidUtf8,Dot)
      --mega-hard-delete                                    Delete files permanently rather than putting them into the trash
      --mega-pass string                                    Password (obscured)
      --mega-use-https                                      Use HTTPS for transfers
      --mega-user string                                    User name
      --memory-description string                           Description of the remote
      --memory-discard                                      If set all writes will be discarded and reads will return an error
      --netstorage-account string                           Set the NetStorage account name
      --netstorage-description string                       Description of the remote
      --netstorage-host string                              Domain+path of NetStorage host to connect to
      --netstorage-protocol string                          Select between HTTP or HTTPS protocol (default "https")
      --netstorage-secret string                            Set the NetStorage account secret/G2O key for authentication (obscured)
  -x, --one-file-system                                     Don't cross filesystem boundaries (unix/macOS only)
      --onedrive-access-scopes SpaceSepList                 Set scopes to be requested by rclone (default Files.Read Files.ReadWrite Files.Read.All Files.ReadWrite.All Sites.Read.All offline_access)
      --onedrive-auth-url string                            Auth server URL
      --onedrive-av-override                                Allows download of files the server thinks has a virus
      --onedrive-chunk-size SizeSuffix                      Chunk size to upload files with - must be multiple of 320k (327,680 bytes) (default 10Mi)
      --onedrive-client-credentials                         Use client credentials OAuth flow
      --onedrive-client-id string                           OAuth Client Id
      --onedrive-client-secret string                       OAuth Client Secret
      --onedrive-delta                                      If set rclone will use delta listing to implement recursive listings
      --onedrive-description string                         Description of the remote
      --onedrive-drive-id string                            The ID of the drive to use
      --onedrive-drive-type string                          The type of the drive (personal | business | documentLibrary)
      --onedrive-encoding Encoding                          The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Del,Ctl,LeftSpace,LeftTilde,RightSpace,RightPeriod,InvalidUtf8,Dot)
      --onedrive-expose-onenote-files                       Set to make OneNote files show up in directory listings
      --onedrive-hard-delete                                Permanently delete files on removal
      --onedrive-hash-type string                           Specify the hash in use for the backend (default "auto")
      --onedrive-link-password string                       Set the password for links created by the link command
      --onedrive-link-scope string                          Set the scope of the links created by the link command (default "anonymous")
      --onedrive-link-type string                           Set the type of the links created by the link command (default "view")
      --onedrive-list-chunk int                             Size of listing chunk (default 1000)
      --onedrive-metadata-permissions Bits                  Control whether permissions should be read or written in metadata (default off)
      --onedrive-no-versions                                Remove all versions on modifying operations
      --onedrive-region string                              Choose national cloud region for OneDrive (default "global")
      --onedrive-root-folder-id string                      ID of the root folder
      --onedrive-server-side-across-configs                 Deprecated: use --server-side-across-configs instead
      --onedrive-tenant string                              ID of the service principal's tenant. Also called its directory ID
      --onedrive-token string                               OAuth Access Token as a JSON blob
      --onedrive-token-url string                           Token server url
      --onedrive-upload-cutoff SizeSuffix                   Cutoff for switching to chunked upload (default off)
      --oos-attempt-resume-upload                           If true attempt to resume previously started multipart upload for the object
      --oos-chunk-size SizeSuffix                           Chunk size to use for uploading (default 5Mi)
      --oos-compartment string                              Specify compartment OCID, if you need to list buckets
      --oos-config-file string                              Path to OCI config file (default "~/.oci/config")
      --oos-config-profile string                           Profile name inside the oci config file (default "Default")
      --oos-copy-cutoff SizeSuffix                          Cutoff for switching to multipart copy (default 4.656Gi)
      --oos-copy-timeout Duration                           Timeout for copy (default 1m0s)
      --oos-description string                              Description of the remote
      --oos-disable-checksum                                Don't store MD5 checksum with object metadata
      --oos-encoding Encoding                               The encoding for the backend (default Slash,InvalidUtf8,Dot)
      --oos-endpoint string                                 Endpoint for Object storage API
      --oos-leave-parts-on-error                            If true avoid calling abort upload on a failure, leaving all successfully uploaded parts for manual recovery
      --oos-max-upload-parts int                            Maximum number of parts in a multipart upload (default 10000)
      --oos-namespace string                                Object storage namespace
      --oos-no-check-bucket                                 If set, don't attempt to check the bucket exists or create it
      --oos-provider string                                 Choose your Auth Provider (default "env_auth")
      --oos-region string                                   Object storage Region
      --oos-sse-customer-algorithm string                   If using SSE-C, the optional header that specifies "AES256" as the encryption algorithm
      --oos-sse-customer-key string                         To use SSE-C, the optional header that specifies the base64-encoded 256-bit encryption key to use to
      --oos-sse-customer-key-file string                    To use SSE-C, a file containing the base64-encoded string of the AES-256 encryption key associated
      --oos-sse-customer-key-sha256 string                  If using SSE-C, The optional header that specifies the base64-encoded SHA256 hash of the encryption
      --oos-sse-kms-key-id string                           if using your own master key in vault, this header specifies the
      --oos-storage-tier string                             The storage class to use when storing new objects in storage. https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm (default "Standard")
      --oos-upload-concurrency int                          Concurrency for multipart uploads (default 10)
      --oos-upload-cutoff SizeSuffix                        Cutoff for switching to chunked upload (default 200Mi)
      --opendrive-access string                             Files and folders will be uploaded with this access permission (default private) (default "private")
      --opendrive-chunk-size SizeSuffix                     Files will be uploaded in chunks this size (default 10Mi)
      --opendrive-description string                        Description of the remote
      --opendrive-encoding Encoding                         The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,LeftSpace,LeftCrLfHtVt,RightSpace,RightCrLfHtVt,InvalidUtf8,Dot)
      --opendrive-password string                           Password (obscured)
      --opendrive-username string                           Username
      --pcloud-auth-url string                              Auth server URL
      --pcloud-client-credentials                           Use client credentials OAuth flow
      --pcloud-client-id string                             OAuth Client Id
      --pcloud-client-secret string                         OAuth Client Secret
      --pcloud-description string                           Description of the remote
      --pcloud-encoding Encoding                            The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --pcloud-hostname string                              Hostname to connect to (default "api.pcloud.com")
      --pcloud-password string                              Your pcloud password (obscured)
      --pcloud-root-folder-id string                        Fill in for rclone to use a non root folder as its starting point (default "d0")
      --pcloud-token string                                 OAuth Access Token as a JSON blob
      --pcloud-token-url string                             Token server url
      --pcloud-username string                              Your pcloud username
      --pikpak-chunk-size SizeSuffix                        Chunk size for multipart uploads (default 5Mi)
      --pikpak-description string                           Description of the remote
      --pikpak-device-id string                             Device ID used for authorization
      --pikpak-encoding Encoding                            The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Ctl,LeftSpace,RightSpace,RightPeriod,InvalidUtf8,Dot)
      --pikpak-hash-memory-limit SizeSuffix                 Files bigger than this will be cached on disk to calculate hash if required (default 10Mi)
      --pikpak-no-media-link                                Use original file links instead of media links
      --pikpak-pass string                                  Pikpak password (obscured)
      --pikpak-root-folder-id string                        ID of the root folder
      --pikpak-trashed-only                                 Only show files that are in the trash
      --pikpak-upload-concurrency int                       Concurrency for multipart uploads (default 4)
      --pikpak-upload-cutoff SizeSuffix                     Cutoff for switching to chunked upload (default 200Mi)
      --pikpak-use-trash                                    Send files to the trash instead of deleting permanently (default true)
      --pikpak-user string                                  Pikpak username
      --pikpak-user-agent string                            HTTP user agent for pikpak (default "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0")
      --pixeldrain-api-key string                           API key for your pixeldrain account
      --pixeldrain-api-url string                           The API endpoint to connect to. In the vast majority of cases it's fine to leave (default "https://pixeldrain.com/api")
      --pixeldrain-description string                       Description of the remote
      --pixeldrain-root-folder-id string                    Root of the filesystem to use (default "me")
      --premiumizeme-auth-url string                        Auth server URL
      --premiumizeme-client-credentials                     Use client credentials OAuth flow
      --premiumizeme-client-id string                       OAuth Client Id
      --premiumizeme-client-secret string                   OAuth Client Secret
      --premiumizeme-description string                     Description of the remote
      --premiumizeme-encoding Encoding                      The encoding for the backend (default Slash,DoubleQuote,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --premiumizeme-token string                           OAuth Access Token as a JSON blob
      --premiumizeme-token-url string                       Token server url
      --protondrive-2fa string                              The 2FA code
      --protondrive-app-version string                      The app version string (default "macos-drive@1.0.0-alpha.1+rclone")
      --protondrive-description string                      Description of the remote
      --protondrive-enable-caching                          Caches the files and folders metadata to reduce API calls (default true)
      --protondrive-encoding Encoding                       The encoding for the backend (default Slash,LeftSpace,RightSpace,InvalidUtf8,Dot)
      --protondrive-mailbox-password string                 The mailbox password of your two-password proton account (obscured)
      --protondrive-original-file-size                      Return the file size before encryption (default true)
      --protondrive-otp-secret-key string                   The OTP secret key (obscured)
      --protondrive-password string                         The password of your proton account (obscured)
      --protondrive-replace-existing-draft                  Create a new revision when filename conflict is detected
      --protondrive-username string                         The username of your proton account
      --putio-auth-url string                               Auth server URL
      --putio-client-credentials                            Use client credentials OAuth flow
      --putio-client-id string                              OAuth Client Id
      --putio-client-secret string                          OAuth Client Secret
      --putio-description string                            Description of the remote
      --putio-encoding Encoding                             The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --putio-token string                                  OAuth Access Token as a JSON blob
      --putio-token-url string                              Token server url
      --qingstor-access-key-id string                       QingStor Access Key ID
      --qingstor-chunk-size SizeSuffix                      Chunk size to use for uploading (default 4Mi)
      --qingstor-connection-retries int                     Number of connection retries (default 3)
      --qingstor-description string                         Description of the remote
      --qingstor-encoding Encoding                          The encoding for the backend (default Slash,Ctl,InvalidUtf8)
      --qingstor-endpoint string                            Enter an endpoint URL to connection QingStor API
      --qingstor-env-auth                                   Get QingStor credentials from runtime
      --qingstor-secret-access-key string                   QingStor Secret Access Key (password)
      --qingstor-upload-concurrency int                     Concurrency for multipart uploads (default 1)
      --qingstor-upload-cutoff SizeSuffix                   Cutoff for switching to chunked upload (default 200Mi)
      --qingstor-zone string                                Zone to connect to
      --quatrix-api-key string                              API key for accessing Quatrix account
      --quatrix-description string                          Description of the remote
      --quatrix-effective-upload-time string                Wanted upload time for one chunk (default "4s")
      --quatrix-encoding Encoding                           The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --quatrix-hard-delete                                 Delete files permanently rather than putting them into the trash
      --quatrix-host string                                 Host name of Quatrix account
      --quatrix-maximal-summary-chunk-size SizeSuffix       The maximal summary for all chunks. It should not be less than 'transfers'*'minimal_chunk_size' (default 95.367Mi)
      --quatrix-minimal-chunk-size SizeSuffix               The minimal size for one chunk (default 9.537Mi)
      --quatrix-skip-project-folders                        Skip project folders in operations
      --s3-access-key-id string                             AWS Access Key ID
      --s3-acl string                                       Canned ACL used when creating buckets and storing or copying objects
      --s3-bucket-acl string                                Canned ACL used when creating buckets
      --s3-chunk-size SizeSuffix                            Chunk size to use for uploading (default 5Mi)
      --s3-copy-cutoff SizeSuffix                           Cutoff for switching to multipart copy (default 4.656Gi)
      --s3-decompress                                       If set this will decompress gzip encoded objects
      --s3-description string                               Description of the remote
      --s3-directory-bucket                                 Set to use AWS Directory Buckets
      --s3-directory-markers                                Upload an empty object with a trailing slash when a new directory is created
      --s3-disable-checksum                                 Don't store MD5 checksum with object metadata
      --s3-disable-http2                                    Disable usage of http2 for S3 backends
      --s3-download-url string                              Custom endpoint for downloads
      --s3-encoding Encoding                                The encoding for the backend (default Slash,InvalidUtf8,Dot)
      --s3-endpoint string                                  Endpoint for S3 API
      --s3-env-auth                                         Get AWS credentials from runtime (environment variables or EC2/ECS meta data if no env vars)
      --s3-force-path-style                                 If true use path style access if false use virtual hosted style (default true)
      --s3-ibm-api-key string                               IBM API Key to be used to obtain IAM token
      --s3-ibm-resource-instance-id string                  IBM service instance id
      --s3-leave-parts-on-error                             If true avoid calling abort upload on a failure, leaving all successfully uploaded parts on S3 for manual recovery
      --s3-list-chunk int                                   Size of listing chunk (response list for each ListObject S3 request) (default 1000)
      --s3-list-url-encode Tristate                         Whether to url encode listings: true/false/unset (default unset)
      --s3-list-version int                                 Version of ListObjects to use: 1,2 or 0 for auto
      --s3-location-constraint string                       Location constraint - must be set to match the Region
      --s3-max-upload-parts int                             Maximum number of parts in a multipart upload (default 10000)
      --s3-might-gzip Tristate                              Set this if the backend might gzip objects (default unset)
      --s3-no-check-bucket                                  If set, don't attempt to check the bucket exists or create it
      --s3-no-head                                          If set, don't HEAD uploaded objects to check integrity
      --s3-no-head-object                                   If set, do not do HEAD before GET when getting objects
      --s3-no-system-metadata                               Suppress setting and reading of system metadata
      --s3-profile string                                   Profile to use in the shared credentials file
      --s3-provider string                                  Choose your S3 provider
      --s3-region string                                    Region to connect to
      --s3-requester-pays                                   Enables requester pays option when interacting with S3 bucket
      --s3-role-arn string                                  ARN of the IAM role to assume
      --s3-role-external-id string                          External ID for assumed role
      --s3-role-session-duration string                     Session duration for assumed role
      --s3-role-session-name string                         Session name for assumed role
      --s3-sdk-log-mode Bits                                Set to debug the SDK (default Off)
      --s3-secret-access-key string                         AWS Secret Access Key (password)
      --s3-server-side-encryption string                    The server-side encryption algorithm used when storing this object in S3
      --s3-session-token string                             An AWS session token
      --s3-shared-credentials-file string                   Path to the shared credentials file
      --s3-sign-accept-encoding Tristate                    Set if rclone should include Accept-Encoding as part of the signature (default unset)
      --s3-sse-customer-algorithm string                    If using SSE-C, the server-side encryption algorithm used when storing this object in S3
      --s3-sse-customer-key string                          To use SSE-C you may provide the secret encryption key used to encrypt/decrypt your data
      --s3-sse-customer-key-base64 string                   If using SSE-C you must provide the secret encryption key encoded in base64 format to encrypt/decrypt your data
      --s3-sse-customer-key-md5 string                      If using SSE-C you may provide the secret encryption key MD5 checksum (optional)
      --s3-sse-kms-key-id string                            If using KMS ID you must provide the ARN of Key
      --s3-storage-class string                             The storage class to use when storing new objects in S3
      --s3-upload-concurrency int                           Concurrency for multipart uploads and copies (default 4)
      --s3-upload-cutoff SizeSuffix                         Cutoff for switching to chunked upload (default 200Mi)
      --s3-use-accelerate-endpoint                          If true use the AWS S3 accelerated endpoint
      --s3-use-accept-encoding-gzip Accept-Encoding: gzip   Whether to send Accept-Encoding: gzip header (default unset)
      --s3-use-already-exists Tristate                      Set if rclone should report BucketAlreadyExists errors on bucket creation (default unset)
      --s3-use-arn-region                                   If true, enables arn region support for the service
      --s3-use-data-integrity-protections Tristate          If true use AWS S3 data integrity protections (default unset)
      --s3-use-dual-stack                                   If true use AWS S3 dual-stack endpoint (IPv6 support)
      --s3-use-multipart-etag Tristate                      Whether to use ETag in multipart uploads for verification (default unset)
      --s3-use-multipart-uploads Tristate                   Set if rclone should use multipart uploads (default unset)
      --s3-use-presigned-request                            Whether to use a presigned request or PutObject for single part uploads
      --s3-use-unsigned-payload Tristate                    Whether to use an unsigned payload in PutObject (default unset)
      --s3-use-x-id Tristate                                Set if rclone should add x-id URL parameters (default unset)
      --s3-v2-auth                                          If true use v2 authentication
      --s3-version-at Time                                  Show file versions as they were at the specified time (default off)
      --s3-version-deleted                                  Show deleted file markers when using versions
      --s3-versions                                         Include old versions in directory listings
      --seafile-2fa                                         Two-factor authentication ('true' if the account has 2FA enabled)
      --seafile-create-library                              Should rclone create a library if it doesn't exist
      --seafile-description string                          Description of the remote
      --seafile-encoding Encoding                           The encoding for the backend (default Slash,DoubleQuote,BackSlash,Ctl,InvalidUtf8,Dot)
      --seafile-library string                              Name of the library
      --seafile-library-key string                          Library password (for encrypted libraries only) (obscured)
      --seafile-pass string                                 Password (obscured)
      --seafile-url string                                  URL of seafile host to connect to
      --seafile-user string                                 User name (usually email address)
      --sftp-ask-password                                   Allow asking for SFTP password when needed
      --sftp-blake3sum-command string                       The command used to read BLAKE3 hashes
      --sftp-chunk-size SizeSuffix                          Upload and download chunk size (default 32Ki)
      --sftp-ciphers SpaceSepList                           Space separated list of ciphers to be used for session encryption, ordered by preference
      --sftp-concurrency int                                The maximum number of outstanding requests for one file (default 64)
      --sftp-connections int                                Maximum number of SFTP simultaneous connections, 0 for unlimited
      --sftp-copy-is-hardlink                               Set to enable server side copies using hardlinks
      --sftp-crc32sum-command string                        The command used to read CRC-32 hashes
      --sftp-description string                             Description of the remote
      --sftp-disable-concurrent-reads                       If set don't use concurrent reads
      --sftp-disable-concurrent-writes                      If set don't use concurrent writes
      --sftp-disable-hashcheck                              Disable the execution of SSH commands to determine if remote file hashing is available
      --sftp-hashes CommaSepList                            Comma separated list of supported checksum types
      --sftp-host string                                    SSH host to connect to
      --sftp-host-key-algorithms SpaceSepList               Space separated list of host key algorithms, ordered by preference
      --sftp-http-proxy string                              URL for HTTP CONNECT proxy
      --sftp-idle-timeout Duration                          Max time before closing idle connections (default 1m0s)
      --sftp-key-exchange SpaceSepList                      Space separated list of key exchange algorithms, ordered by preference
      --sftp-key-file string                                Path to PEM-encoded private key file
      --sftp-key-file-pass string                           The passphrase to decrypt the PEM-encoded private key file (obscured)
      --sftp-key-pem string                                 Raw PEM-encoded private key
      --sftp-key-use-agent                                  When set forces the usage of the ssh-agent
      --sftp-known-hosts-file string                        Optional path to known_hosts file
      --sftp-macs SpaceSepList                              Space separated list of MACs (message authentication code) algorithms, ordered by preference
      --sftp-md5sum-command string                          The command used to read MD5 hashes
      --sftp-pass string                                    SSH password, leave blank to use ssh-agent (obscured)
      --sftp-path-override string                           Override path used by SSH shell commands
      --sftp-port int                                       SSH port number (default 22)
      --sftp-pubkey string                                  SSH public certificate for public certificate based authentication
      --sftp-pubkey-file string                             Optional path to public key file
      --sftp-server-command string                          Specifies the path or command to run a sftp server on the remote host
      --sftp-set-env SpaceSepList                           Environment variables to pass to sftp and commands
      --sftp-set-modtime                                    Set the modified time on the remote if set (default true)
      --sftp-sha1sum-command string                         The command used to read SHA-1 hashes
      --sftp-sha256sum-command string                       The command used to read SHA-256 hashes
      --sftp-shell-type string                              The type of SSH shell on remote server, if any
      --sftp-skip-links                                     Set to skip any symlinks and any other non regular files
      --sftp-socks-proxy string                             Socks 5 proxy host
      --sftp-ssh SpaceSepList                               Path and arguments to external ssh binary
      --sftp-subsystem string                               Specifies the SSH2 subsystem on the remote host (default "sftp")
      --sftp-use-fstat                                      If set use fstat instead of stat
      --sftp-use-insecure-cipher                            Enable the use of insecure ciphers and key exchange methods
      --sftp-user string                                    SSH username (default "root")
      --sftp-xxh128sum-command string                       The command used to read XXH128 hashes
      --sftp-xxh3sum-command string                         The command used to read XXH3 hashes
      --shade-api-key string                                An API key for your account
      --shade-chunk-size SizeSuffix                         Chunk size to use for uploading (default 64Mi)
      --shade-description string                            Description of the remote
      --shade-drive-id string                               The ID of your drive, see this in the drive settings. Individual rclone configs must be made per drive
      --shade-encoding Encoding                             The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --shade-endpoint string                               Endpoint for the service
      --shade-max-upload-parts int                          Maximum amount of parts in a multipart upload (default 10000)
      --shade-token string                                  JWT Token for performing Shade FS operations. Don't set this value - rclone will set it automatically
      --shade-token-expiry string                           JWT Token Expiration time. Don't set this value - rclone will set it automatically
      --shade-upload-concurrency int                        Concurrency for multipart uploads and copies. This is the number of chunks of the same file that are uploaded concurrently for multipart uploads and copies (default 4)
      --sharefile-auth-url string                           Auth server URL
      --sharefile-chunk-size SizeSuffix                     Upload chunk size (default 64Mi)
      --sharefile-client-credentials                        Use client credentials OAuth flow
      --sharefile-client-id string                          OAuth Client Id
      --sharefile-client-secret string                      OAuth Client Secret
      --sharefile-description string                        Description of the remote
      --sharefile-encoding Encoding                         The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Ctl,LeftSpace,LeftPeriod,RightSpace,RightPeriod,InvalidUtf8,Dot)
      --sharefile-endpoint string                           Endpoint for API calls
      --sharefile-root-folder-id string                     ID of the root folder
      --sharefile-token string                              OAuth Access Token as a JSON blob
      --sharefile-token-url string                          Token server url
      --sharefile-upload-cutoff SizeSuffix                  Cutoff for switching to multipart upload (default 128Mi)
      --sia-api-password string                             Sia Daemon API Password (obscured)
      --sia-api-url string                                  Sia daemon API URL, like http://sia.daemon.host:9980 (default "http://127.0.0.1:9980")
      --sia-description string                              Description of the remote
      --sia-encoding Encoding                               The encoding for the backend (default Slash,Question,Hash,Percent,Del,Ctl,InvalidUtf8,Dot)
      --sia-user-agent string                               Siad User Agent (default "Sia-Agent")
      --skip-links                                          Don't warn about skipped symlinks
      --skip-specials                                       Don't warn about skipped pipes, sockets and device objects
      --smb-case-insensitive                                Whether the server is configured to be case-insensitive (default true)
      --smb-description string                              Description of the remote
      --smb-domain string                                   Domain name for NTLM authentication (default "WORKGROUP")
      --smb-encoding Encoding                               The encoding for the backend (default Slash,LtGt,DoubleQuote,Colon,Question,Asterisk,Pipe,BackSlash,Ctl,RightSpace,RightPeriod,InvalidUtf8,Dot)
      --smb-hide-special-share                              Hide special shares (e.g. print$) which users aren't supposed to access (default true)
      --smb-host string                                     SMB server hostname to connect to
      --smb-idle-timeout Duration                           Max time before closing idle connections (default 1m0s)
      --smb-kerberos-ccache string                          Path to the Kerberos credential cache (krb5cc)
      --smb-pass string                                     SMB password (obscured)
      --smb-port int                                        SMB port number (default 445)
      --smb-spn string                                      Service principal name
      --smb-use-kerberos                                    Use Kerberos authentication
      --smb-user string                                     SMB username (default "root")
      --storj-access-grant string                           Access grant
      --storj-api-key string                                API key
      --storj-description string                            Description of the remote
      --storj-passphrase string                             Encryption passphrase
      --storj-provider string                               Choose an authentication method (default "existing")
      --storj-satellite-address string                      Satellite address (default "us1.storj.io")
      --sugarsync-access-key-id string                      Sugarsync Access Key ID
      --sugarsync-app-id string                             Sugarsync App ID
      --sugarsync-authorization string                      Sugarsync authorization
      --sugarsync-authorization-expiry string               Sugarsync authorization expiry
      --sugarsync-deleted-id string                         Sugarsync deleted folder id
      --sugarsync-description string                        Description of the remote
      --sugarsync-encoding Encoding                         The encoding for the backend (default Slash,Ctl,InvalidUtf8,Dot)
      --sugarsync-hard-delete                               Permanently delete files if true
      --sugarsync-private-access-key string                 Sugarsync Private Access Key
      --sugarsync-refresh-token string                      Sugarsync refresh token
      --sugarsync-root-id string                            Sugarsync root id
      --sugarsync-user string                               Sugarsync user
      --swift-application-credential-id string              Application Credential ID (OS_APPLICATION_CREDENTIAL_ID)
      --swift-application-credential-name string            Application Credential Name (OS_APPLICATION_CREDENTIAL_NAME)
      --swift-application-credential-secret string          Application Credential Secret (OS_APPLICATION_CREDENTIAL_SECRET)
      --swift-auth string                                   Authentication URL for server (OS_AUTH_URL)
      --swift-auth-token string                             Auth Token from alternate authentication - optional (OS_AUTH_TOKEN)
      --swift-auth-version int                              AuthVersion - optional - set to (1,2,3) if your auth URL has no version (ST_AUTH_VERSION)
      --swift-chunk-size SizeSuffix                         Above this size files will be chunked (default 5Gi)
      --swift-description string                            Description of the remote
      --swift-domain string                                 User domain - optional (v3 auth) (OS_USER_DOMAIN_NAME)
      --swift-encoding Encoding                             The encoding for the backend (default Slash,InvalidUtf8)
      --swift-endpoint-type string                          Endpoint type to choose from the service catalogue (OS_ENDPOINT_TYPE) (default "public")
      --swift-env-auth                                      Get swift credentials from environment variables in standard OpenStack form
      --swift-fetch-until-empty-page                        When paginating, always fetch unless we received an empty page
      --swift-key string                                    API key or password (OS_PASSWORD)
      --swift-leave-parts-on-error                          If true avoid calling abort upload on a failure
      --swift-no-chunk                                      Don't chunk files during streaming upload
      --swift-no-large-objects                              Disable support for static and dynamic large objects
      --swift-partial-page-fetch-threshold int              When paginating, fetch if the current page is within this percentage of the limit
      --swift-region string                                 Region name - optional (OS_REGION_NAME)
      --swift-storage-policy string                         The storage policy to use when creating a new container
      --swift-storage-url string                            Storage URL - optional (OS_STORAGE_URL)
      --swift-tenant string                                 Tenant name - optional for v1 auth, this or tenant_id required otherwise (OS_TENANT_NAME or OS_PROJECT_NAME)
      --swift-tenant-domain string                          Tenant domain - optional (v3 auth) (OS_PROJECT_DOMAIN_NAME)
      --swift-tenant-id string                              Tenant ID - optional for v1 auth, this or tenant required otherwise (OS_TENANT_ID)
      --swift-use-segments-container Tristate               Choose destination for large object segments (default unset)
      --swift-user string                                   User name to log in (OS_USERNAME)
      --swift-user-id string                                User ID to log in - optional - most swift systems use user and leave this blank (v3 auth) (OS_USER_ID)
      --ulozto-app-token string                             The application token identifying the app. An app API key can be either found in the API
      --ulozto-description string                           Description of the remote
      --ulozto-encoding Encoding                            The encoding for the backend (default Slash,BackSlash,Del,Ctl,InvalidUtf8,Dot)
      --ulozto-list-page-size int                           The size of a single page for list commands. 1-500 (default 500)
      --ulozto-password string                              The password for the user (obscured)
      --ulozto-root-folder-slug string                      If set, rclone will use this folder as the root folder for all operations. For example,
      --ulozto-username string                              The username of the principal to operate as
      --union-action-policy string                          Policy to choose upstream on ACTION category (default "epall")
      --union-cache-time int                                Cache time of usage and free space (in seconds) (default 120)
      --union-create-policy string                          Policy to choose upstream on CREATE category (default "epmfs")
      --union-description string                            Description of the remote
      --union-min-free-space SizeSuffix                     Minimum viable free space for lfs/eplfs policies (default 1Gi)
      --union-search-policy string                          Policy to choose upstream on SEARCH category (default "ff")
      --union-upstreams string                              List of space separated upstreams
      --webdav-auth-redirect                                Preserve authentication on redirect
      --webdav-bearer-token string                          Bearer token instead of user/pass (e.g. a Macaroon)
      --webdav-bearer-token-command string                  Command to run to get a bearer token
      --webdav-description string                           Description of the remote
      --webdav-encoding string                              The encoding for the backend
      --webdav-headers CommaSepList                         Set HTTP headers for all transactions
      --webdav-nextcloud-chunk-size SizeSuffix              Nextcloud upload chunk size (default 10Mi)
      --webdav-owncloud-exclude-mounts                      Exclude ownCloud mounted storages
      --webdav-owncloud-exclude-shares                      Exclude ownCloud shares
      --webdav-pacer-min-sleep Duration                     Minimum time to sleep between API calls (default 10ms)
      --webdav-pass string                                  Password (obscured)
      --webdav-unix-socket string                           Path to a unix domain socket to dial to, instead of opening a TCP connection directly
      --webdav-url string                                   URL of http host to connect to
      --webdav-user string                                  User name
      --webdav-vendor string                                Name of the WebDAV site/service/software you are using
      --yandex-auth-url string                              Auth server URL
      --yandex-client-credentials                           Use client credentials OAuth flow
      --yandex-client-id string                             OAuth Client Id
      --yandex-client-secret string                         OAuth Client Secret
      --yandex-description string                           Description of the remote
      --yandex-encoding Encoding                            The encoding for the backend (default Slash,Del,Ctl,InvalidUtf8,Dot)
      --yandex-hard-delete                                  Delete files permanently rather than putting them into the trash
      --yandex-spoof-ua                                     Set the user agent to match an official version of the yandex disk client. May help with upload performance (default true)
      --yandex-token string                                 OAuth Access Token as a JSON blob
      --yandex-token-url string                             Token server url
      --zoho-auth-url string                                Auth server URL
      --zoho-client-credentials                             Use client credentials OAuth flow
      --zoho-client-id string                               OAuth Client Id
      --zoho-client-secret string                           OAuth Client Secret
      --zoho-description string                             Description of the remote
      --zoho-encoding Encoding                              The encoding for the backend (default Del,Ctl,InvalidUtf8)
      --zoho-region string                                  Zoho region to connect to
      --zoho-token string                                   OAuth Access Token as a JSON blob
      --zoho-token-url string                               Token server url
      --zoho-upload-cutoff SizeSuffix                       Cutoff for switching to large file upload api (>= 10 MiB) (default 10Mi)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
```

## Backends

### `help backends`

```
All rclone backends:

  alias        Alias for an existing remote
  hdfs         Hadoop distributed file system
  local        Local Disk
  protondrive  Proton Drive
  storj        Storj Decentralized Cloud Storage
  tardigrade   Storj Decentralized Cloud Storage
  cloudinary   Cloudinary
  doi          DOI datasets
  fichier      1Fichier
  filelu       FileLu Cloud Storage
  filescom     Files.com
  ftp          FTP
  http         HTTP
  iclouddrive  iCloud Drive
  imagekit     ImageKit.io
  internetarchive Internet Archive
  koofr        Koofr, Digi Storage and other Koofr-compatible storage providers
  linkbox      Linkbox
  mega         Mega
  opendrive    OpenDrive
  pixeldrain   Pixeldrain Filesystem
  seafile      seafile
  sftp         SSH/SFTP
  sia          Sia Decentralized Cloud
  smb          SMB / CIFS
  ulozto       Uloz.to
  azurefiles   Microsoft Azure Files
  crypt        Encrypt/Decrypt a remote
  filen        Filen
  gofile       Gofile
  memory       In memory object storage system.
  netstorage   Akamai NetStorage
  qingstor     QingCloud Object Storage
  webdav       WebDAV
  filefabric   Enterprise File Fabric
  azureblob    Microsoft Azure Blob Storage
  drime        Drime
  quatrix      Quatrix by Maytech
  shade        Shade FS
  b2           Backblaze B2
  cache        Cache a remote
  chunker      Transparently chunk/split large files
  combine      Combine several remotes into one
  hasher       Better checksums for other remotes
  oos          Oracle Cloud Infrastructure Object Storage
  s3           Amazon S3 Compliant Storage Providers including AWS, Alibaba, ArvanCloud, BizflyCloud, Ceph, ChinaMobile, Cloudflare, Cubbit, DigitalOcean, Dreamhost, Exaba, FileLu, FlashBlade, GCS, Hetzner, HuaweiOBS, IBMCOS, IDrive, Intercolo, IONOS, Leviia, Liara, Linode, LyveCloud, Magalu, Mega, Minio, Netease, Outscale, OVHcloud, Petabox, Qiniu, Rabata, RackCorp, Rclone, Scaleway, SeaweedFS, Selectel, Servercore, SpectraLogic, StackPath, Storj, Synology, TencentCOS, Wasabi, Zata, Other
  sugarsync    Sugarsync
  swift        OpenStack Swift (Rackspace Cloud Files, Blomp Cloud Storage, Memset Memstore, OVH)
  union        Union merges the contents of several upstream fs
  compress     Compress a remote
  dropbox      Dropbox
  gphotos      Google Photos
  hidrive      HiDrive
  internxt     Internxt Drive
  jottacloud   Jottacloud
  mailru       Mail.ru Cloud
  onedrive     Microsoft OneDrive
  pcloud       Pcloud
  pikpak       PikPak
  premiumizeme premiumize.me
  putio        Put.io
  sharefile    Citrix Sharefile
  yandex       Yandex Disk
  zoho         Zoho
  box          Box
  archive      Read archives
  drive        Google Drive
  gcs          Google Cloud Storage (this is not Google Drive)

To see more info about a particular backend use:
  rclone help backend <name>
```

## Commands

### `about`

````
Prints quota information about a remote to standard
output. The output is typically used, free, quota and trash contents.

E.g. Typical output from `rclone about remote:` is:

```text
Total:   17 GiB
Used:    7.444 GiB
Free:    1.315 GiB
Trashed: 100.000 MiB
Other:   8.241 GiB
```

Where the fields are:

- Total: Total size available.
- Used: Total size used.
- Free: Total space available to this user.
- Trashed: Total space used by trash.
- Other: Total amount in other storage (e.g. Gmail, Google Photos).
- Objects: Total number of objects in the storage.

All sizes are in number of bytes.

Applying a `--full` flag to the command prints the bytes in full, e.g.

```text
Total:   18253611008
Used:    7993453766
Free:    1411001220
Trashed: 104857602
Other:   8849156022
```

A `--json` flag generates conveniently machine-readable output, e.g.

```json
{
  "total": 18253611008,
  "used": 7993453766,
  "trashed": 104857602,
  "other": 8849156022,
  "free": 1411001220
}
```

Not all backends print all fields. Information is not included if it is not
provided by a backend. Where the value is unlimited it is omitted.

Some backends does not support the `rclone about` command at all,
see complete list in [documentation](https://rclone.org/overview/#optional-features).

Usage:
  rclone about remote: [flags]

Flags:
      --full   Full numbers instead of human-readable
  -h, --help   help for about
      --json   Format output as JSON

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `archive`

````
Perform an action on an archive. Requires the use of a
subcommand to specify the protocol, e.g.

    rclone archive list remote:file.zip

Each subcommand has its own options which you can see in their help.

See [rclone archive create](/commands/rclone_archive_create/) for the
archive formats supported.

Usage:
  rclone archive <action> [opts] <source> [<destination>] [flags]
  rclone archive [command]

Available commands:
  create      Archive source file(s) to destination.
  extract     Extract archives from source to destination.
  list        List archive contents from source.

Flags:
  -h, --help   help for archive

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `authorize`

````
Remote authorization. Used to authorize a remote or headless
rclone from a machine with a browser. Use as instructed by rclone config.
See also the [remote setup documentation](/remote_setup).

The command requires 1-3 arguments:

- Name of a backend (e.g. "drive", "s3")
- Either a base64 encoded JSON blob obtained from a previous rclone config session
- Or a client_id and client_secret pair obtained from the remote service

Use --auth-no-open-browser to prevent rclone to open auth
link in default browser automatically.

Use --template to generate HTML output via a custom Go template. If a blank
string is provided as an argument to this flag, the default template is used.

Usage:
  rclone authorize <backendname> [base64_json_blob | client_id client_secret] [flags]

Flags:
      --auth-no-open-browser   Do not automatically open auth link in default browser
  -h, --help                   help for authorize
      --template string        The path to a custom Go template for generating HTML responses

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `backend`

````
This runs a backend-specific command. The commands themselves (except
for "help" and "features") are defined by the backends and you should
see the backend docs for definitions.

You can discover what commands a backend implements by using

```console
rclone backend help remote:
rclone backend help <backendname>
```

You can also discover information about the backend using (see
[operations/fsinfo](/rc/#operations-fsinfo) in the remote control docs
for more info).

```console
rclone backend features remote:
```

Pass options to the backend command with -o. This should be key=value or key, e.g.:

```console
rclone backend stats remote:path stats -o format=json -o long
```

Pass arguments to the backend by placing them on the end of the line

```console
rclone backend cleanup remote:path file1 file2 file3
```

Note to run these commands on a running backend then see
[backend/command](/rc/#backend-command) in the rc docs.

Usage:
  rclone backend <command> remote:path [opts] <args> [flags]

Flags:
  -h, --help                 help for backend
      --json                 Always output in JSON format
  -o, --option stringArray   Option in the form name=value or name

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `bisync`

````
Perform bidirectional synchronization between two paths.

[Bisync](https://rclone.org/bisync/) provides a
bidirectional cloud sync solution in rclone.
It retains the Path1 and Path2 filesystem listings from the prior run.
On each successive run it will:

- list files on Path1 and Path2, and check for changes on each side.
  Changes include `New`, `Newer`, `Older`, and `Deleted` files.
- Propagate changes on Path1 to Path2, and vice-versa.

Bisync is considered an **advanced command**, so use with care.
Make sure you have read and understood the entire [manual](https://rclone.org/bisync)
(especially the [Limitations](https://rclone.org/bisync/#limitations) section)
before using, or data loss can result. Questions can be asked in the
[Rclone Forum](https://forum.rclone.org/).

See [full bisync description](https://rclone.org/bisync/) for details.

Usage:
  rclone bisync remote1:path1 remote2:path2 [flags]

Flags:
      --backup-dir1 string                   --backup-dir for Path1. Must be a non-overlapping path on the same remote.
      --backup-dir2 string                   --backup-dir for Path2. Must be a non-overlapping path on the same remote.
      --check-access                         Ensure expected RCLONE_TEST files are found on both Path1 and Path2 filesystems, else abort.
      --check-filename string                Filename for --check-access (default: RCLONE_TEST)
      --check-sync string                    Controls comparison of final listings: true|false|only (default: true) (default "true")
      --compare string                       Comma-separated list of bisync-specific compare options ex. 'size,modtime,checksum' (default: 'size,modtime')
      --conflict-loser ConflictLoserAction   Action to take on the loser of a sync conflict (when there is a winner) or on both files (when there is no winner): , num, pathname, delete (default: num)
      --conflict-resolve string              Automatically resolve conflicts by preferring the version that is: none, path1, path2, newer, older, larger, smaller (default: none) (default "none")
      --conflict-suffix string               Suffix to use when renaming a --conflict-loser. Can be either one string or two comma-separated strings to assign different suffixes to Path1/Path2. (default: 'conflict')
      --create-empty-src-dirs                Sync creation and deletion of empty directories. (Not compatible with --remove-empty-dirs)
      --download-hash                        Compute hash by downloading when otherwise unavailable. (warning: may be slow and use lots of data!)
      --filters-file string                  Read filtering patterns from a file
      --force                                Bypass --max-delete safety check and run the sync. Consider using with --verbose
  -h, --help                                 help for bisync
      --ignore-listing-checksum              Do not use checksums for listings (add --ignore-checksum to additionally skip post-copy checksum checks)
      --max-lock Duration                    Consider lock files older than this to be expired (default: 0 (never expire)) (minimum: 2m) (default 0s)
      --no-cleanup                           Retain working files (useful for troubleshooting and testing).
      --no-slow-hash                         Ignore listing checksums only on backends where they are slow
      --recover                              Automatically recover from interruptions without requiring --resync.
      --remove-empty-dirs                    Remove ALL empty directories at the final cleanup step.
      --resilient                            Allow future runs to retry after certain less-serious errors, instead of requiring --resync.
  -1, --resync                               Performs the resync run. Equivalent to --resync-mode path1. Consider using --verbose or --dry-run first.
      --resync-mode string                   During resync, prefer the version that is: path1, path2, newer, older, larger, smaller (default: path1 if --resync, otherwise none for no resync.) (default "none")
      --slow-hash-sync-only                  Ignore slow checksums for listings and deltas, but still consider them during sync calls.
      --workdir string                       Use custom working dir - useful for testing. (default: {WORKDIR})

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `cat`

````
Sends any files to standard output.

You can use it like this to output a single file

```sh
rclone cat remote:path/to/file
```

Or like this to output any file in dir or its subdirectories.

```sh
rclone cat remote:path/to/dir
```

Or like this to output any .txt files in dir or its subdirectories.

```sh
rclone --include "*.txt" cat remote:path/to/dir
```

Use the `--head` flag to print characters only at the start, `--tail` for
the end and `--offset` and `--count` to print a section in the middle.
Note that if offset is negative it will count from the end, so
`--offset -1 --count 1` is equivalent to `--tail 1`.

Use the `--separator` flag to print a separator value between files. Be sure to
shell-escape special characters. For example, to print a newline between
files, use:

- bash:

  ```sh
  rclone --include "*.txt" --separator $'\n' cat remote:path/to/dir
  ```

- powershell:

  ```powershell
  rclone --include "*.txt" --separator "`n" cat remote:path/to/dir
  ```

Usage:
  rclone cat remote:path [flags]

Flags:
      --count int          Only print N characters (default -1)
      --discard            Discard the output instead of printing
      --head int           Only print the first N characters
  -h, --help               help for cat
      --offset int         Start printing at offset N (or from end if -ve)
      --separator string   Separator to use between objects when printing multiple files
      --tail int           Only print the last N characters

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `check`

````
Checks the files in the source and destination match.  It compares
sizes and hashes (MD5 or SHA1) and logs a report of files that don't
match.  It doesn't alter the source or destination.

For the [crypt](/crypt/) remote there is a dedicated command,
[cryptcheck](/commands/rclone_cryptcheck/), that are able to check
the checksums of the encrypted files.

If you supply the `--size-only` flag, it will only compare the sizes not
the hashes as well.  Use this for a quick check.

If you supply the `--download` flag, it will download the data from
both remotes and check them against each other on the fly.  This can
be useful for remotes that don't support hashes or if you really want
to check all the data.

If you supply the `--checkfile HASH` flag with a valid hash name,
the `source:path` must point to a text file in the SUM format.

If you supply the `--one-way` flag, it will only check that files in
the source match the files in the destination, not the other way
around. This means that extra files in the destination that are not in
the source will not be detected.

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match`
and `--error` flags write paths, one per line, to the file name (or
stdout if it is `-`) supplied. What they write is described in the
help below. For example `--differ` will write all paths which are
present on both the source and destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The default number of parallel checks is 8. See the [--checkers](/docs/#checkers-int)
option for more information.

Usage:
  rclone check source:path dest:path [flags]

Flags:
  -C, --checkfile string        Treat source:path as a SUM file with hashes of given type
      --combined string         Make a combined report of changes to this file
      --differ string           Report all non-matching files to this file
      --download                Check by downloading rather than with hash
      --error string            Report all files with errors (hashing or reading) to this file
  -h, --help                    help for check
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
      --one-way                 Check one way only, source files must exist on remote

Flags used for check commands (flag group Check):
      --max-backlog int   Maximum number of objects in sync or check backlog (default 10000)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `checksum`

````
Checks that hashsums of destination files match the SUM file.
It compares hashes (MD5, SHA1, etc) and logs a report of files which
don't match.  It doesn't alter the file system.

The sumfile is treated as the source and the dst:path is treated as
the destination for the purposes of the output.

If you supply the `--download` flag, it will download the data from the remote
and calculate the content hash on the fly.  This can be useful for remotes
that don't support hashes or if you really want to check all the data.

Note that hash values in the SUM file are treated as case insensitive.

If you supply the `--one-way` flag, it will only check that files in
the source match the files in the destination, not the other way
around. This means that extra files in the destination that are not in
the source will not be detected.

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match`
and `--error` flags write paths, one per line, to the file name (or
stdout if it is `-`) supplied. What they write is described in the
help below. For example `--differ` will write all paths which are
present on both the source and destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The default number of parallel checks is 8. See the [--checkers](/docs/#checkers-int)
option for more information.

Usage:
  rclone checksum <hash> sumfile dst:path [flags]

Flags:
      --combined string         Make a combined report of changes to this file
      --differ string           Report all non-matching files to this file
      --download                Check by hashing the contents
      --error string            Report all files with errors (hashing or reading) to this file
  -h, --help                    help for checksum
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
      --one-way                 Check one way only, source files must exist on remote

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `cleanup`

````
Clean up the remote if possible.  Empty the trash or delete old file
versions. Not supported by all remotes.

Usage:
  rclone cleanup remote:path [flags]

Flags:
  -h, --help   help for cleanup

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `completion`

````
Generates a shell completion script for rclone.
Run with `--help` to list the supported shells.

Usage:
  rclone completion [command]

Aliases:
  completion, genautocomplete

Available commands:
  bash        Output bash completion script for rclone.
  fish        Output fish completion script for rclone.
  powershell  Output powershell completion script for rclone.
  zsh         Output zsh completion script for rclone.

Flags:
  -h, --help   help for completion

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `config`

````
Enter an interactive configuration session where you can setup new
remotes and manage existing ones. You may also set or remove a
password to protect your configuration.

Usage:
  rclone config [flags]
  rclone config [command]

Available commands:
  create      Create a new remote with name, type and options.
  delete      Delete an existing remote.
  disconnect  Disconnects user from remote
  dump        Dump the config file as JSON.
  edit        Enter an interactive configuration session.
  encryption  set, remove and check the encryption for the config file
  file        Show path of configuration file in use.
  password    Update password in an existing remote.
  paths       Show paths used for configuration, cache, temp etc.
  providers   List in JSON format all the providers and options.
  reconnect   Re-authenticates user with remote.
  redacted    Print redacted (decrypted) config file, or the redacted config for a single remote.
  show        Print (decrypted) config file, or the config for a single remote.
  string      Print connection string for a single remote.
  touch       Ensure configuration file exists.
  update      Update options in an existing remote.
  userinfo    Prints info about logged in user of remote.

Flags:
  -h, --help   help for config

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `convmv`

````
convmv supports advanced path name transformations for converting and renaming
files and directories by applying prefixes, suffixes, and other alterations.

| Command | Description |
|------|------|
| `--name-transform prefix=XXXX` | Prepends XXXX to the file name. |
| `--name-transform suffix=XXXX` | Appends XXXX to the file name after the extension. |
| `--name-transform suffix_keep_extension=XXXX` | Appends XXXX to the file name while preserving the original file extension. |
| `--name-transform trimprefix=XXXX` | Removes XXXX if it appears at the start of the file name. |
| `--name-transform trimsuffix=XXXX` | Removes XXXX if it appears at the end of the file name. |
| `--name-transform regex=pattern/replacement` | Applies a regex-based transformation. |
| `--name-transform replace=old:new` | Replaces occurrences of old with new in the file name. |
| `--name-transform date={YYYYMMDD}` | Appends or prefixes the specified date format. |
| `--name-transform truncate=N` | Truncates the file name to a maximum of N characters. |
| `--name-transform truncate_keep_extension=N` | Truncates the file name to a maximum of N characters while preserving the original file extension. |
| `--name-transform truncate_bytes=N` | Truncates the file name to a maximum of N bytes (not characters). |
| `--name-transform truncate_bytes_keep_extension=N` | Truncates the file name to a maximum of N bytes (not characters) while preserving the original file extension. |
| `--name-transform base64encode` | Encodes the file name in Base64. |
| `--name-transform base64decode` | Decodes a Base64-encoded file name. |
| `--name-transform encoder=ENCODING` | Converts the file name to the specified encoding (e.g., ISO-8859-1, Windows-1252, Macintosh). |
| `--name-transform decoder=ENCODING` | Decodes the file name from the specified encoding. |
| `--name-transform charmap=MAP` | Applies a character mapping transformation. |
| `--name-transform lowercase` | Converts the file name to lowercase. |
| `--name-transform uppercase` | Converts the file name to UPPERCASE. |
| `--name-transform titlecase` | Converts the file name to Title Case. |
| `--name-transform ascii` | Strips non-ASCII characters. |
| `--name-transform url` | URL-encodes the file name. |
| `--name-transform nfc` | Converts the file name to NFC Unicode normalization form. |
| `--name-transform nfd` | Converts the file name to NFD Unicode normalization form. |
| `--name-transform nfkc` | Converts the file name to NFKC Unicode normalization form. |
| `--name-transform nfkd` | Converts the file name to NFKD Unicode normalization form. |
| `--name-transform command=/path/to/my/programfile names.` | Executes an external program to transform. |

Conversion modes:

```text
none
nfc
nfd
nfkc
nfkd
replace
prefix
suffix
suffix_keep_extension
trimprefix
trimsuffix
index
date
truncate
truncate_keep_extension
truncate_bytes
truncate_bytes_keep_extension
base64encode
base64decode
encoder
decoder
ISO-8859-1
Windows-1252
Macintosh
charmap
lowercase
uppercase
titlecase
ascii
url
regex
command
```

Char maps:

```text
IBM-Code-Page-037
IBM-Code-Page-437
IBM-Code-Page-850
IBM-Code-Page-852
IBM-Code-Page-855
Windows-Code-Page-858
IBM-Code-Page-860
IBM-Code-Page-862
IBM-Code-Page-863
IBM-Code-Page-865
IBM-Code-Page-866
IBM-Code-Page-1047
IBM-Code-Page-1140
ISO-8859-1
ISO-8859-2
ISO-8859-3
ISO-8859-4
ISO-8859-5
ISO-8859-6
ISO-8859-7
ISO-8859-8
ISO-8859-9
ISO-8859-10
ISO-8859-13
ISO-8859-14
ISO-8859-15
ISO-8859-16
KOI8-R
KOI8-U
Macintosh
Macintosh-Cyrillic
Windows-874
Windows-1250
Windows-1251
Windows-1252
Windows-1253
Windows-1254
Windows-1255
Windows-1256
Windows-1257
Windows-1258
X-User-Defined
```

Encoding masks:

```text
Asterisk
BackQuote
BackSlash
Colon
CrLf
Ctl
Del
Dollar
Dot
DoubleQuote
Exclamation
Hash
InvalidUtf8
LeftCrLfHtVt
LeftPeriod
LeftSpace
LeftTilde
LtGt
None
Percent
Pipe
Question
Raw
RightCrLfHtVt
RightPeriod
RightSpace
Semicolon
SingleQuote
Slash
SquareBracket
```

Examples:

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,uppercase"
// Output: STORIES/THE QUICK BROWN FOX!.TXT
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,replace=Fox:Turtle" --name-transform "all,replace=Quick:Slow"
// Output: stories/The Slow Brown Turtle!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,base64encode"
// Output: c3Rvcmllcw==/VGhlIFF1aWNrIEJyb3duIEZveCEudHh0
```

```console
rclone convmv "c3Rvcmllcw==/VGhlIFF1aWNrIEJyb3duIEZveCEudHh0" --name-transform "all,base64decode"
// Output: stories/The Quick Brown Fox!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox Went to the Café!.txt" --name-transform "all,nfc"
// Output: stories/The Quick Brown Fox Went to the Café!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox Went to the Café!.txt" --name-transform "all,nfd"
// Output: stories/The Quick Brown Fox Went to the Café!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,ascii"
// Output: stories/The Quick Brown Fox!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,trimsuffix=.txt"
// Output: stories/The Quick Brown Fox!
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,prefix=OLD_"
// Output: OLD_stories/OLD_The Quick Brown Fox!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox Went to the Café!.txt" --name-transform "all,charmap=ISO-8859-7"
// Output: stories/The Quick Brown _ Fox Went to the Caf_!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox: A Memoir [draft].txt" --name-transform "all,encoder=Colon,SquareBracket"
// Output: stories/The Quick Brown Fox： A Memoir ［draft］.txt
```

```console
rclone convmv "stories/The Quick Brown Fox Went to the Café!.txt" --name-transform "all,truncate=21"
// Output: stories/The Quick Brown Fox
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,command=echo"
// Output: stories/The Quick Brown Fox!.txt
```

```console
rclone convmv "stories/The Quick Brown Fox!" --name-transform "date=-{YYYYMMDD}"
// Output: stories/The Quick Brown Fox!-20260217
```

```console
rclone convmv "stories/The Quick Brown Fox!" --name-transform "date=-{macfriendlytime}"
// Output: stories/The Quick Brown Fox!-2026-02-17 0454PM
```

```console
rclone convmv "stories/The Quick Brown Fox!.txt" --name-transform "all,regex=[\\.\\w]/ab"
// Output: ababababababab/ababab ababababab ababababab ababab!abababab
```

The regex command generally accepts Perl-style regular expressions, the exact
syntax is defined in the [Go regular expression reference](https://golang.org/pkg/regexp/syntax/).
The replacement string may contain capturing group variables, referencing
capturing groups using the syntax `$name` or `${name}`, where the name can
refer to a named capturing group or it can simply be the index as a number.
To insert a literal $, use $$.

Multiple transformations can be used in sequence, applied
in the order they are specified on the command line.

The `--name-transform` flag is also available in `sync`, `copy`, and `move`.

### Files vs Directories

By default `--name-transform` will only apply to file names. The means only the
leaf file name will be transformed. However some of the transforms would be
better applied to the whole path or just directories. To choose which which
part of the file path is affected some tags can be added to the `--name-transform`.

| Tag | Effect |
|------|------|
| `file` | Only transform the leaf name of files (DEFAULT) |
| `dir` | Only transform name of directories - these may appear anywhere in the path |
| `all` | Transform the entire path for files and directories |

This is used by adding the tag into the transform name like this:
`--name-transform file,prefix=ABC` or `--name-transform dir,prefix=DEF`.

For some conversions using all is more likely to be useful, for example
`--name-transform all,nfc`.

Note that `--name-transform` may not add path separators `/` to the name.
This will cause an error.

### Ordering and Conflicts

- Transformations will be applied in the order specified by the user.
  - If the `file` tag is in use (the default) then only the leaf name of files
    will be transformed.
  - If the `dir` tag is in use then directories anywhere in the path will be
    transformed
  - If the `all` tag is in use then directories and files anywhere in the path
    will be transformed
  - Each transformation will be run one path segment at a time.
  - If a transformation adds a `/` or ends up with an empty path segment then
    that will be an error.
- It is up to the user to put the transformations in a sensible order.
  - Conflicting transformations, such as `prefix` followed by `trimprefix` or
    `nfc` followed by `nfd`, are possible.
  - Instead of enforcing mutual exclusivity, transformations are applied in
    sequence as specified by the user, allowing for intentional use cases
    (e.g., trimming one prefix before adding another).
  - Users should be aware that certain combinations may lead to unexpected
    results and should verify transformations using `--dry-run` before execution.

### Race Conditions and Non-Deterministic Behavior

Some transformations, such as `replace=old:new`, may introduce conflicts where
multiple source files map to the same destination name. This can lead to race
conditions when performing concurrent transfers. It is up to the user to
anticipate these.

- If two files from the source are transformed into the same name at the
  destination, the final state may be non-deterministic.
- Running rclone check after a sync using such transformations may erroneously
  report missing or differing files due to overwritten results.

To minimize risks, users should:

- Carefully review transformations that may introduce conflicts.
- Use `--dry-run` to inspect changes before executing a sync (but keep in mind
  that it won't show the effect of non-deterministic transformations).
- Avoid transformations that cause multiple distinct source files to map to the
  same destination name.
- Consider disabling concurrency with `--transfers=1` if necessary.
- Certain transformations (e.g. `prefix`) will have a multiplying effect every
  time they are used. Avoid these when using `bisync`.

Usage:
  rclone convmv dest:path --name-transform XXX [flags]

Flags:
      --create-empty-src-dirs   Create empty source dirs on destination after move
      --delete-empty-src-dirs   Delete empty source dirs after move
  -h, --help                    help for convmv

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `copy`

````
Copy the source to the destination.  Does not transfer files that are
identical on source and destination, testing by size and modification
time or MD5SUM.  Doesn't delete files from the destination. If you
want to also delete files from destination, to make it match source,
use the [sync](/commands/rclone_sync/) command instead.

Note that it is always the contents of the directory that is synced,
not the directory itself. So when source:path is a directory, it's the
contents of source:path that are copied, not the directory name and
contents.

To copy single files, use the [copyto](/commands/rclone_copyto/)
command instead.

If dest:path doesn't exist, it is created and the source:path contents
go there.

For example

```sh
rclone copy source:sourcepath dest:destpath
```

Let's say there are two files in sourcepath

```text
sourcepath/one.txt
sourcepath/two.txt
```

This copies them to

```text
destpath/one.txt
destpath/two.txt
```

Not to

```text
destpath/sourcepath/one.txt
destpath/sourcepath/two.txt
```

If you are familiar with `rsync`, rclone always works as if you had
written a trailing `/` - meaning "copy the contents of this directory".
This applies to all commands and whether you are talking about the
source or destination.

See the [--no-traverse](/docs/#no-traverse) option for controlling
whether rclone lists the destination directory or not.  Supplying this
option when copying a small number of files into a large destination
can speed transfers up greatly.

For example, if you have many files in /path/to/src but only a few of
them change every day, you can copy all the files which have changed
recently very efficiently like this:

```sh
rclone copy --max-age 24h --no-traverse /path/to/src remote:
```

Rclone will sync the modification times of files and directories if
the backend supports it. If metadata syncing is required then use the
`--metadata` flag.

Note that the modification time and metadata for the root directory
will **not** be synced. See [issue #7652](https://github.com/rclone/rclone/issues/7652)
for more info.

**Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics.

**Note**: Use the `--dry-run` or the `--interactive`/`-i` flag to test without
copying anything.

### Logger Flags

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match` and `--error`
flags write paths, one per line, to the file name (or stdout if it is `-`)
supplied. What they write is described in the help below. For example
`--differ` will write all paths which are present on both the source and
destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The `--dest-after` flag writes a list file using the same format flags
as [`lsf`](/commands/rclone_lsf/#synopsis) (including [customizable options
for hash, modtime, etc.](/commands/rclone_lsf/#synopsis))
Conceptually it is similar to rsync's `--itemize-changes`, but not identical
-- it should output an accurate list of what will be on the destination
after the command is finished.

When the `--no-traverse` flag is set, all logs involving files that exist only
on the destination will be incomplete or completely missing.

Note that these logger flags have a few limitations, and certain scenarios
are not currently supported:

- `--max-duration` / `CutoffModeHard`
- `--compare-dest` / `--copy-dest`
- server-side moves of an entire dir at once
- High-level retries, because there would be duplicates (use `--retries 1` to disable)
- Possibly some unusual error scenarios

Note also that each file is logged during execution, as opposed to after, so it
is most useful as a predictor of what SHOULD happen to each file
(which may or may not match what actually DID).

Usage:
  rclone copy source:path dest:path [flags]

Flags:
      --absolute                Put a leading / in front of path names
      --combined string         Make a combined report of changes to this file
      --create-empty-src-dirs   Create empty source dirs on destination after copy
      --csv                     Output in CSV format
      --dest-after string       Report all files that exist on the dest post-sync
      --differ string           Report all non-matching files to this file
  -d, --dir-slash               Append a slash to directory names (default true)
      --dirs-only               Only list directories
      --error string            Report all files with errors (hashing or reading) to this file
      --files-only              Only list files (default true)
  -F, --format string           Output format - see lsf help for details (default "p")
      --hash h                  Use this hash when h is used in the format MD5|SHA-1|DropboxHash (default "md5")
  -h, --help                    help for copy
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
  -s, --separator string        Separator for the items in the format (default ";")
  -t, --timeformat string       Specify a custom time format - see docs for details (default: 2006-01-02 15:04:05)

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `copyto`

````
If source:path is a file or directory then it copies it to a file or
directory named dest:path.

This can be used to upload single files to other than their current
name.  If the source is a directory then it acts exactly like the
[copy](/commands/rclone_copy/) command.

So

```console
rclone copyto src dst
```

where src and dst are rclone paths, either `remote:path` or
`/path/to/local` or `C:\windows\path\if\on\windows`.

This will:

```text
if src is file
    copy it to dst, overwriting an existing file if it exists
if src is directory
    copy it to dst, overwriting existing files if they exist
    see copy command for full details
```

This doesn't transfer files that are identical on src and dst, testing
by size and modification time or MD5SUM.  It doesn't delete files from
the destination.

*If you are looking to copy just a byte range of a file, please see
`rclone cat --offset X --count Y`.*

**Note**: Use the `-P`/`--progress` flag to view
real-time transfer statistics.

### Logger Flags

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match` and `--error`
flags write paths, one per line, to the file name (or stdout if it is `-`)
supplied. What they write is described in the help below. For example
`--differ` will write all paths which are present on both the source and
destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The `--dest-after` flag writes a list file using the same format flags
as [`lsf`](/commands/rclone_lsf/#synopsis) (including [customizable options
for hash, modtime, etc.](/commands/rclone_lsf/#synopsis))
Conceptually it is similar to rsync's `--itemize-changes`, but not identical
-- it should output an accurate list of what will be on the destination
after the command is finished.

When the `--no-traverse` flag is set, all logs involving files that exist only
on the destination will be incomplete or completely missing.

Note that these logger flags have a few limitations, and certain scenarios
are not currently supported:

- `--max-duration` / `CutoffModeHard`
- `--compare-dest` / `--copy-dest`
- server-side moves of an entire dir at once
- High-level retries, because there would be duplicates (use `--retries 1` to disable)
- Possibly some unusual error scenarios

Note also that each file is logged during execution, as opposed to after, so it
is most useful as a predictor of what SHOULD happen to each file
(which may or may not match what actually DID).

Usage:
  rclone copyto source:path dest:path [flags]

Flags:
      --absolute                Put a leading / in front of path names
      --combined string         Make a combined report of changes to this file
      --csv                     Output in CSV format
      --dest-after string       Report all files that exist on the dest post-sync
      --differ string           Report all non-matching files to this file
  -d, --dir-slash               Append a slash to directory names (default true)
      --dirs-only               Only list directories
      --error string            Report all files with errors (hashing or reading) to this file
      --files-only              Only list files (default true)
  -F, --format string           Output format - see lsf help for details (default "p")
      --hash h                  Use this hash when h is used in the format MD5|SHA-1|DropboxHash (default "md5")
  -h, --help                    help for copyto
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
  -s, --separator string        Separator for the items in the format (default ";")
  -t, --timeformat string       Specify a custom time format - see docs for details (default: 2006-01-02 15:04:05)

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `copyurl`

````
Download a URL's content and copy it to the destination without saving
it in temporary storage.

Setting `--auto-filename` will attempt to automatically determine the
filename from the URL (after any redirections) and used in the
destination path.

With `--header-filename` in addition, if a specific filename is
set in HTTP headers, it will be used instead of the name from the URL.
With `--print-filename` in addition, the resulting file name will be
printed.

Setting `--no-clobber` will prevent overwriting file on the
destination if there is one with the same name.

Setting `--stdout` or making the output file name `-`
will cause the output to be written to standard output.

Setting `--urls` allows you to input a CSV file of URLs in format: URL,
FILENAME. If `--urls` is in use then replace the URL in the arguments with the
file containing the URLs, e.g.:
```sh
rclone copyurl --urls myurls.csv remote:dir
```
Missing filenames will be autogenerated equivalent to using `--auto-filename`.
Note that `--stdout` and `--print-filename` are incompatible with `--urls`.
This will do `--transfers` copies in parallel. Note that if `--auto-filename`
is desired for all URLs then a file with only URLs and no filename can be used.

Each FILENAME in the CSV file can start with a relative path which will be appended
to the destination path provided at the command line. For example, running the command
shown above with the following CSV file will write two files to the destination: 
`remote:dir/local/path/bar.json` and `remote:dir/another/local/directory/qux.json`
```csv
https://example.org/foo/bar.json,local/path/bar.json
https://example.org/qux/baz.json,another/local/directory/qux.json
```

### Troubleshooting

If you can't get `rclone copyurl` to work then here are some things you can try:

- `--disable-http2` rclone will use HTTP2 if available - try disabling it
- `--bind 0.0.0.0` rclone will use IPv6 if available - try disabling it
- `--bind ::0` to disable IPv4
- `--user agent curl` - some sites have whitelists for curl's user-agent - try that
- Make sure the site works with `curl` directly

Usage:
  rclone copyurl https://example.com dest:path [flags]

Flags:
  -a, --auto-filename     Get the file name from the URL and use it for destination file path
      --header-filename   Get the file name from the Content-Disposition header
  -h, --help              help for copyurl
      --no-clobber        Prevent overwriting file with same name
  -p, --print-filename    Print the resulting name from --auto-filename
      --stdout            Write the output to stdout rather than a file
      --urls              Use a CSV file of links to process multiple URLs

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `cryptcheck`

````
Checks a remote against an [encrypted](/crypt/) remote. This is the equivalent
of running rclone [check](/commands/rclone_check/), but able to check the
checksums of the encrypted remote.

For it to work the underlying remote of the cryptedremote must support
some kind of checksum.

It works by reading the nonce from each file on the cryptedremote: and
using that to encrypt each file on the remote:.  It then checks the
checksum of the underlying file on the cryptedremote: against the
checksum of the file it has just encrypted.

Use it like this

```console
rclone cryptcheck /path/to/files encryptedremote:path
```

You can use it like this also, but that will involve downloading all
the files in `remote:path`.

```console
rclone cryptcheck remote:path encryptedremote:path
```

After it has run it will log the status of the `encryptedremote:`.

If you supply the `--one-way` flag, it will only check that files in
the source match the files in the destination, not the other way
around. This means that extra files in the destination that are not in
the source will not be detected.

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match`
and `--error` flags write paths, one per line, to the file name (or
stdout if it is `-`) supplied. What they write is described in the
help below. For example `--differ` will write all paths which are
present on both the source and destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The default number of parallel checks is 8. See the [--checkers](/docs/#checkers-int)
option for more information.

Usage:
  rclone cryptcheck remote:path cryptedremote:path [flags]

Flags:
      --combined string         Make a combined report of changes to this file
      --differ string           Report all non-matching files to this file
      --error string            Report all files with errors (hashing or reading) to this file
  -h, --help                    help for cryptcheck
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
      --one-way                 Check one way only, source files must exist on remote

Flags used for check commands (flag group Check):
      --max-backlog int   Maximum number of objects in sync or check backlog (default 10000)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `cryptdecode`

````
Returns unencrypted file names when provided with a list of encrypted file
names. List limit is 10 items.

If you supply the `--reverse` flag, it will return encrypted file names.

use it like this

```console
rclone cryptdecode encryptedremote: encryptedfilename1 encryptedfilename2
rclone cryptdecode --reverse encryptedremote: filename1 filename2
```

Another way to accomplish this is by using the `rclone backend encode` (or `decode`)
command. See the documentation on the [crypt](/crypt/) overlay for more info.

Usage:
  rclone cryptdecode encryptedremote: encryptedfilename [flags]

Flags:
  -h, --help      help for cryptdecode
      --reverse   Reverse cryptdecode, encrypts filenames

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `dedupe`

````
By default `dedupe` interactively finds files with duplicate
names and offers to delete all but one or rename them to be
different. This is known as deduping by name.

Deduping by name is only useful with a small group of backends (e.g. Google Drive,
Opendrive) that can have duplicate file names. It can be run on wrapping backends
(e.g. crypt) if they wrap a backend which supports duplicate file
names.

However if `--by-hash` is passed in then dedupe will find files with
duplicate hashes instead which will work on any backend which supports
at least one hash. This can be used to find files with duplicate
content. This is known as deduping by hash.

If deduping by name, first rclone will merge directories with the same
name.  It will do this iteratively until all the identically named
directories have been merged.

Next, if deduping by name, for every group of duplicate file names /
hashes, it will delete all but one identical file it finds without
confirmation.  This means that for most duplicated files the
`dedupe` command will not be interactive.

`dedupe` considers files to be identical if they have the
same file path and the same hash. If the backend does not support
hashes (e.g. crypt wrapping Google Drive) then they will never be found
to be identical. If you use the `--size-only` flag then files
will be considered identical if they have the same size (any hash will be
ignored). This can be useful on crypt backends which do not support hashes.

Next rclone will resolve the remaining duplicates. Exactly which
action is taken depends on the dedupe mode. By default, rclone will
interactively query the user for each one.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`-i` flag.

Here is an example run.

Before - with duplicates

```console
$ rclone lsl drive:dupes
  6048320 2016-03-05 16:23:16.798000000 one.txt
  6048320 2016-03-05 16:23:11.775000000 one.txt
   564374 2016-03-05 16:23:06.731000000 one.txt
  6048320 2016-03-05 16:18:26.092000000 one.txt
  6048320 2016-03-05 16:22:46.185000000 two.txt
  1744073 2016-03-05 16:22:38.104000000 two.txt
   564374 2016-03-05 16:22:52.118000000 two.txt
```

Now the `dedupe` session

```console
$ rclone dedupe drive:dupes
2016/03/05 16:24:37 Google drive root 'dupes': Looking for duplicates using interactive mode.
one.txt: Found 4 files with duplicate names
one.txt: Deleting 2/3 identical duplicates (MD5 "1eedaa9fe86fd4b8632e2ac549403b36")
one.txt: 2 duplicates remain
  1:      6048320 bytes, 2016-03-05 16:23:16.798000000, MD5 1eedaa9fe86fd4b8632e2ac549403b36
  2:       564374 bytes, 2016-03-05 16:23:06.731000000, MD5 7594e7dc9fc28f727c42ee3e0749de81
s) Skip and do nothing
k) Keep just one (choose which in next step)
r) Rename all to be different (by changing file.jpg to file-1.jpg)
s/k/r> k
Enter the number of the file to keep> 1
one.txt: Deleted 1 extra copies
two.txt: Found 3 files with duplicate names
two.txt: 3 duplicates remain
  1:       564374 bytes, 2016-03-05 16:22:52.118000000, MD5 7594e7dc9fc28f727c42ee3e0749de81
  2:      6048320 bytes, 2016-03-05 16:22:46.185000000, MD5 1eedaa9fe86fd4b8632e2ac549403b36
  3:      1744073 bytes, 2016-03-05 16:22:38.104000000, MD5 851957f7fb6f0bc4ce76be966d336802
s) Skip and do nothing
k) Keep just one (choose which in next step)
r) Rename all to be different (by changing file.jpg to file-1.jpg)
s/k/r> r
two-1.txt: renamed from: two.txt
two-2.txt: renamed from: two.txt
two-3.txt: renamed from: two.txt
```

The result being

```console
$ rclone lsl drive:dupes
  6048320 2016-03-05 16:23:16.798000000 one.txt
   564374 2016-03-05 16:22:52.118000000 two-1.txt
  6048320 2016-03-05 16:22:46.185000000 two-2.txt
  1744073 2016-03-05 16:22:38.104000000 two-3.txt
```

Dedupe can be run non interactively using the `--dedupe-mode` flag
or by using an extra parameter with the same value

- `--dedupe-mode interactive` - interactive as above.
- `--dedupe-mode skip` - removes identical files then skips anything left.
- `--dedupe-mode first` - removes identical files then keeps the first one.
- `--dedupe-mode newest` - removes identical files then keeps the newest one.
- `--dedupe-mode oldest` - removes identical files then keeps the oldest one.
- `--dedupe-mode largest` - removes identical files then keeps the largest one.
- `--dedupe-mode smallest` - removes identical files then keeps the smallest one.
- `--dedupe-mode rename` - removes identical files then renames the rest to be different.
- `--dedupe-mode list` - lists duplicate dirs and files only and changes nothing.

For example, to rename all the identically named photos in your Google Photos
directory, do

```console
rclone dedupe --dedupe-mode rename "drive:Google Photos"
```

Or

```console
rclone dedupe rename "drive:Google Photos"
```

Usage:
  rclone dedupe [mode] remote:path [flags]

Flags:
      --by-hash              Find identical hashes rather than names
      --dedupe-mode string   Dedupe mode interactive|skip|first|newest|oldest|largest|smallest|rename (default "interactive")
  -h, --help                 help for dedupe

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `delete`

````
Remove the files in path.  Unlike [purge](/commands/rclone_purge/) it
obeys include/exclude filters so can be used to selectively delete files.

`rclone delete` only deletes files but leaves the directory structure
alone. If you want to delete a directory and all of its contents use
the [purge](/commands/rclone_purge/) command.

If you supply the `--rmdirs` flag, it will remove all empty directories along
with it. You can also use the separate command [rmdir](/commands/rclone_rmdir/)
or [rmdirs](/commands/rclone_rmdirs/) to delete empty directories only.

For example, to delete all files bigger than 100 MiB, you may first want to
check what would be deleted (use either):

```sh
rclone --min-size 100M lsl remote:path
rclone --dry-run --min-size 100M delete remote:path
```

Then proceed with the actual delete:

```sh
rclone --min-size 100M delete remote:path
```

That reads "delete everything with a minimum size of 100 MiB", hence
delete all files bigger than 100 MiB.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`-i` flag.

Usage:
  rclone delete remote:path [flags]

Flags:
  -h, --help     help for delete
      --rmdirs   rmdirs removes empty directories but leaves root intact

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `deletefile`

````
Remove a single file from remote.  Unlike `delete` it cannot be used to
remove a directory and it doesn't obey include/exclude filters - if the
specified file exists, it will always be removed.

Usage:
  rclone deletefile remote:path [flags]

Flags:
  -h, --help   help for deletefile

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `gendocs`

````
This produces markdown docs for the rclone commands to the directory
supplied.  These are in a format suitable for hugo to render into the
rclone.org website.

Usage:
  rclone gendocs output_directory [flags]

Flags:
  -h, --help   help for gendocs

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `gitannex`

````
Rclone's `gitannex` subcommand enables [git-annex] to store and retrieve content
from an rclone remote. It is meant to be run by git-annex, not directly by
users.

[git-annex]: https://git-annex.branchable.com/

### Installation on Linux

1. Skip this step if your version of git-annex is [10.20240430] or newer.
   Otherwise, you must create a symlink somewhere on your PATH with a particular
   name. This symlink helps git-annex tell rclone it wants to run the "gitannex"
   subcommand.

   Create the helper symlink in "$HOME/bin":

   ```console
   ln -s "$(realpath rclone)" "$HOME/bin/git-annex-remote-rclone-builtin"

   Verify the new symlink is on your PATH:

   ```console
   which git-annex-remote-rclone-builtin
   ```

   [10.20240430]: https://git-annex.branchable.com/news/version_10.20240430/

2. Add a new remote to your git-annex repo. This new remote will connect
   git-annex with the `rclone gitannex` subcommand.

   Start by asking git-annex to describe the remote's available configuration
   parameters.

   If you skipped step 1:

   ```console
   git annex initremote MyRemote type=rclone --whatelse
   ```

   If you created a symlink in step 1:

   ```console
   git annex initremote MyRemote type=external externaltype=rclone-builtin --whatelse
    ```

   > **NOTE**: If you're porting an existing [git-annex-remote-rclone] remote to
   > use `rclone gitannex`, you can probably reuse the configuration parameters
   > verbatim without renaming them. Check parameter synonyms with `--whatelse`
   > as shown above.
   >
   > [git-annex-remote-rclone]: https://github.com/git-annex-remote-rclone/git-annex-remote-rclone

   The following example creates a new git-annex remote named "MyRemote" that
   will use the rclone remote named "SomeRcloneRemote". That rclone remote must
   be one configured in your rclone.conf file, which can be located with `rclone
   config file`.

   ```console
   git annex initremote MyRemote         \
       type=external                     \
       externaltype=rclone-builtin       \
       encryption=none                   \
       rcloneremotename=SomeRcloneRemote \
       rcloneprefix=git-annex-content    \
       rclonelayout=nodir
   ```

3. Before you trust this command with your precious data, be sure to **test the
   remote**. This command is very new and has not been tested on many rclone
   backends. Caveat emptor!

   ```console
   git annex testremote MyRemote
   ```

Happy annexing!

Usage:
  rclone gitannex [flags]

Aliases:
  gitannex, git-annex-remote-rclone-builtin

Flags:
  -h, --help   help for gitannex

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `hashsum`

````
Produces a hash file for all the objects in the path using the hash
named.  The output is in the same format as the standard
md5sum/sha1sum tool.

By default, the hash is requested from the remote.  If the hash is
not supported by the remote, no hash will be returned.  With the
download flag, the file will be downloaded from the remote and
hashed locally enabling any hash for any remote.

For the MD5 and SHA1 algorithms there are also dedicated commands,
[md5sum](/commands/rclone_md5sum/) and [sha1sum](/commands/rclone_sha1sum/).

This command can also hash data received on standard input (stdin),
by not passing a remote:path, or by passing a hyphen as remote:path
when there is data to read (if not, the hyphen will be treated literally,
as a relative path).

Run without a hash to see the list of all supported hashes, e.g.

```console
$ rclone hashsum
Supported hashes are:
- md5
- sha1
- whirlpool
- crc32
- sha256
- sha512
- blake3
- xxh3
- xxh128
```

Then

```console
rclone hashsum MD5 remote:path
```

Note that hash names are case insensitive and values are output in lower case.

Usage:
  rclone hashsum [<hash> remote:path] [flags]

Flags:
      --base64               Output base64 encoded hashsum
  -C, --checkfile string     Validate hashes against a given SUM file instead of printing them
      --download             Download the file and hash it locally; if this flag is not specified, the hash is requested from the remote
  -h, --help                 help for hashsum
      --output-file string   Output hashsums to a file rather than the terminal

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `help`

````
Rclone syncs files to and from cloud storage providers as well as
mounting them, listing them in lots of different ways.

See the home page (https://rclone.org/) for installation, usage,
documentation, changelog and configuration walkthroughs.

Usage:
  rclone help [flags]
  rclone help [command]

Available commands:
  backend     List full info about a backend
  backends    List the backends available
  flags       Show the global flags for rclone

Flags:
  -h, --help   help for help

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `link`

````
Create, retrieve or remove a public link to the given file or folder.

```console
rclone link remote:path/to/file
rclone link remote:path/to/folder/
rclone link --unlink remote:path/to/folder/
rclone link --expire 1d remote:path/to/file
```

If you supply the --expire flag, it will set the expiration time
otherwise it will use the default (100 years). **Note** not all
backends support the --expire flag - if the backend doesn't support it
then the link returned won't expire.

Use the --unlink flag to remove existing public links to the file or
folder. **Note** not all backends support "--unlink" flag - those that
don't will just ignore it.

If successful, the last line of the output will contain the
link. Exact capabilities depend on the remote, but the link will
always by default be created with the least constraints - e.g. no
expiry, no password protection, accessible without account.

Usage:
  rclone link remote:path [flags]

Flags:
      --expire Duration   The amount of time that the link will be valid (default off)
  -h, --help              help for link
      --unlink            Remove existing public link to file/folder

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `listremotes`

````
Lists all the available remotes from the config file, or the remotes matching
an optional filter.

Prints the result in human-readable format by default, and as a simple list of
remote names, or if used with flag `--long` a tabular format including
the remote names, types and descriptions. Using flag `--json` produces
machine-readable output instead, which always includes all attributes - including
the source (file or environment).

Result can be filtered by a filter argument which applies to all attributes,
and/or filter flags specific for each attribute. The values must be specified
according to regular rclone filtering pattern syntax.

Usage:
  rclone listremotes [<filter>] [flags]

Flags:
      --description string   Filter remotes by description
  -h, --help                 help for listremotes
      --json                 Format output as JSON
      --long                 Show type and description in addition to name
      --name string          Filter remotes by name
      --order-by string      Instructions on how to order the result, e.g. 'type,name=descending'
      --source string        Filter remotes by source, e.g. 'file' or 'environment'
      --type string          Filter remotes by type

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `ls`

````
Lists the objects in the source path to standard output in a human
readable format with size and path. Recurses by default.

E.g.

```console
$ rclone ls swift:bucket
    60295 bevajer5jef
    90613 canole
    94467 diwogej7
    37600 fubuwic
```

Any of the filtering options can be applied to this command.

There are several related list commands

- `ls` to list size and path of objects only
- `lsl` to list modification time, size and path of objects only
- `lsd` to list directories only
- `lsf` to list objects and directories in easy to parse format
- `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human-readable.
`lsf` is designed to be human and machine-readable.
`lsjson` is designed to be machine-readable.

Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default -
use `-R` to make them recurse.

List commands prefer a recursive method that uses more memory but fewer
transactions by default. Use `--disable ListR` to suppress the behavior.
See [`--fast-list`](/docs/#fast-list) for more details.

Listing a nonexistent directory will produce an error except for
remotes which can't have empty directories (e.g. s3, swift, or gcs -
the bucket-based remotes).

Usage:
  rclone ls remote:path [flags]

Flags:
  -h, --help   help for ls

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `lsd`

````
Lists the directories in the source path to standard output. Does not
recurse by default.  Use the `-R` flag to recurse.

This command lists the total size of the directory (if known, -1 if
not), the modification time (if known, the current time if not), the
number of objects in the directory (if known, -1 if not) and the name
of the directory, E.g.

```console
$ rclone lsd swift:
      494000 2018-04-26 08:43:20     10000 10000files
          65 2018-04-26 08:43:20         1 1File
```

Or

```console
$ rclone lsd drive:test
          -1 2016-10-17 17:41:53        -1 1000files
          -1 2017-01-03 14:40:54        -1 2500files
          -1 2017-07-08 14:39:28        -1 4000files
```

If you just want the directory names use `rclone lsf --dirs-only`.

Any of the filtering options can be applied to this command.

There are several related list commands

- `ls` to list size and path of objects only
- `lsl` to list modification time, size and path of objects only
- `lsd` to list directories only
- `lsf` to list objects and directories in easy to parse format
- `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human-readable.
`lsf` is designed to be human and machine-readable.
`lsjson` is designed to be machine-readable.

Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default -
use `-R` to make them recurse.

List commands prefer a recursive method that uses more memory but fewer
transactions by default. Use `--disable ListR` to suppress the behavior.
See [`--fast-list`](/docs/#fast-list) for more details.

Listing a nonexistent directory will produce an error except for
remotes which can't have empty directories (e.g. s3, swift, or gcs -
the bucket-based remotes).

Usage:
  rclone lsd remote:path [flags]

Flags:
  -h, --help        help for lsd
  -R, --recursive   Recurse into the listing

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `lsf`

````
List the contents of the source path (directories and objects) to
standard output in a form which is easy to parse by scripts.  By
default this will just be the names of the objects and directories,
one per line.  The directories will have a / suffix.

E.g.

```console
$ rclone lsf swift:bucket
bevajer5jef
canole
diwogej7
ferejej3gux/
fubuwic
```

Use the `--format` option to control what gets listed.  By default this
is just the path, but you can use these parameters to control the
output:

```text
p - path
s - size
t - modification time
h - hash
i - ID of object
o - Original ID of underlying object
m - MimeType of object if known
e - encrypted name
T - tier of storage if known, e.g. "Hot" or "Cool"
M - Metadata of object in JSON blob format, eg {"key":"value"}
```

So if you wanted the path, size and modification time, you would use
`--format "pst"`, or maybe `--format "tsp"` to put the path last.

E.g.

```console
$ rclone lsf  --format "tsp" swift:bucket
2016-06-25 18:55:41;60295;bevajer5jef
2016-06-25 18:55:43;90613;canole
2016-06-25 18:55:43;94467;diwogej7
2018-04-26 08:50:45;0;ferejej3gux/
2016-06-25 18:55:40;37600;fubuwic
```

If you specify "h" in the format you will get the MD5 hash by default,
use the `--hash` flag to change which hash you want.  Note that this
can be returned as an empty string if it isn't available on the object
(and for directories), "ERROR" if there was an error reading it from
the object and "UNSUPPORTED" if that object does not support that hash
type.

For example, to emulate the md5sum command you can use

```console
rclone lsf -R --hash MD5 --format hp --separator "  " --files-only .
```

E.g.

```console
$ rclone lsf -R --hash MD5 --format hp --separator "  " --files-only swift:bucket
7908e352297f0f530b84a756f188baa3  bevajer5jef
cd65ac234e6fea5925974a51cdd865cc  canole
03b5341b4f234b9d984d03ad076bae91  diwogej7
8fd37c3810dd660778137ac3a66cc06d  fubuwic
99713e14a4c4ff553acaf1930fad985b  gixacuh7ku
```

(Though "rclone md5sum ." is an easier way of typing this.)

By default the separator is ";" this can be changed with the
`--separator` flag.  Note that separators aren't escaped in the path so
putting it last is a good strategy.

E.g.

```console
$ rclone lsf  --separator "," --format "tshp" swift:bucket
2016-06-25 18:55:41,60295,7908e352297f0f530b84a756f188baa3,bevajer5jef
2016-06-25 18:55:43,90613,cd65ac234e6fea5925974a51cdd865cc,canole
2016-06-25 18:55:43,94467,03b5341b4f234b9d984d03ad076bae91,diwogej7
2018-04-26 08:52:53,0,,ferejej3gux/
2016-06-25 18:55:40,37600,8fd37c3810dd660778137ac3a66cc06d,fubuwic
```

You can output in CSV standard format.  This will escape things in "
if they contain,

E.g.

```console
$ rclone lsf --csv --files-only --format ps remote:path
test.log,22355
test.sh,449
"this file contains a comma, in the file name.txt",6
```

Note that the `--absolute` parameter is useful for making lists of files
to pass to an rclone copy with the `--files-from-raw` flag.

For example, to find all the files modified within one day and copy
those only (without traversing the whole directory structure):

```console
rclone lsf --absolute --files-only --max-age 1d /path/to/local > new_files
rclone copy --files-from-raw new_files /path/to/local remote:path
```

The default time format is `'2006-01-02 15:04:05'`.
[Other formats](https://pkg.go.dev/time#pkg-constants) can be specified with
the `--time-format` flag. Examples:

```console
rclone lsf remote:path --format pt --time-format 'Jan 2, 2006 at 3:04pm (MST)'
rclone lsf remote:path --format pt --time-format '2006-01-02 15:04:05.000000000'
rclone lsf remote:path --format pt --time-format '2006-01-02T15:04:05.999999999Z07:00'
rclone lsf remote:path --format pt --time-format RFC3339
rclone lsf remote:path --format pt --time-format DateOnly
rclone lsf remote:path --format pt --time-format max
rclone lsf remote:path --format pt --time-format unix
rclone lsf remote:path --format pt --time-format unixnano
```

`--time-format max` will automatically truncate `2006-01-02 15:04:05.000000000`
to the maximum precision supported by the remote.

Any of the filtering options can be applied to this command.

There are several related list commands

- `ls` to list size and path of objects only
- `lsl` to list modification time, size and path of objects only
- `lsd` to list directories only
- `lsf` to list objects and directories in easy to parse format
- `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human-readable.
`lsf` is designed to be human and machine-readable.
`lsjson` is designed to be machine-readable.

Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default -
use `-R` to make them recurse.

List commands prefer a recursive method that uses more memory but fewer
transactions by default. Use `--disable ListR` to suppress the behavior.
See [`--fast-list`](/docs/#fast-list) for more details.

Listing a nonexistent directory will produce an error except for
remotes which can't have empty directories (e.g. s3, swift, or gcs -
the bucket-based remotes).

Usage:
  rclone lsf remote:path [flags]

Flags:
      --absolute             Put a leading / in front of path names
      --csv                  Output in CSV format
  -d, --dir-slash            Append a slash to directory names (default true)
      --dirs-only            Only list directories
      --files-only           Only list files
  -F, --format string        Output format - see  help for details (default "p")
      --hash h               Use this hash when h is used in the format MD5|SHA-1|DropboxHash (default "md5")
  -h, --help                 help for lsf
  -R, --recursive            Recurse into the listing
  -s, --separator string     Separator for the items in the format (default ";")
  -t, --time-format string   Specify a custom time format - see docs for details (default: 2006-01-02 15:04:05)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `lsjson`

````
List directories and objects in the path in JSON format.

The output is an array of Items, where each Item looks like this:

```json
{
  "Hashes" : {
    "SHA-1" : "f572d396fae9206628714fb2ce00f72e94f2258f",
    "MD5" : "b1946ac92492d2347c6235b4d2611184",
    "DropboxHash" : "ecb65bb98f9d905b70458986c39fcbad7715e5f2fcc3b1f07767d7c83e2438cc"
  },
  "ID": "y2djkhiujf83u33",
  "OrigID": "UYOJVTUW00Q1RzTDA",
  "IsBucket" : false,
  "IsDir" : false,
  "MimeType" : "application/octet-stream",
  "ModTime" : "2017-05-31T16:15:57.034468261+01:00",
  "Name" : "file.txt",
  "Encrypted" : "v0qpsdq8anpci8n929v3uu9338",
  "EncryptedPath" : "kja9098349023498/v0qpsdq8anpci8n929v3uu9338",
  "Path" : "full/path/goes/here/file.txt",
  "Size" : 6,
  "Tier" : "hot",
}
```

The exact set of properties included depends on the backend:

- The property IsBucket will only be included for bucket-based remotes, and only
  for directories that are buckets. It will always be omitted when value is not true.
- Properties Encrypted and EncryptedPath will only be included for encrypted
  remotes, and (as mentioned below) only if the `--encrypted` option is set.

Different options may also affect which properties are included:

- If `--hash` is not specified, the Hashes property will be omitted. The
  types of hash can be specified with the `--hash-type` parameter (which
  may be repeated). If `--hash-type` is set then it implies `--hash`.
- If `--no-modtime` is specified then ModTime will be blank. This can
  speed things up on remotes where reading the ModTime takes an extra
  request (e.g. s3, swift).
- If `--no-mimetype` is specified then MimeType will be blank. This can
  speed things up on remotes where reading the MimeType takes an extra
  request (e.g. s3, swift).
- If `--encrypted` is not specified the Encrypted and EncryptedPath
  properties will be omitted - even for encrypted remotes.
- If `--metadata` is set then an additional Metadata property will be
  returned. This will have [metadata](/docs/#metadata) in rclone standard format
  as a JSON object.

The default is to list directories and files/objects, but this can be changed
with the following options:

- If `--dirs-only` is specified then directories will be returned
  only, no files/objects.
- If `--files-only` is specified then files will be returned only,
  no directories.

If `--stat` is set then the output is not an array of items,
but instead a single JSON blob will be returned about the item pointed to.
This will return an error if the item isn't found, however on bucket based
backends (like s3, gcs, b2, azureblob etc) if the item isn't found it will
return an empty directory, as it isn't possible to tell empty directories
from missing directories there.

The Path field will only show folders below the remote path being listed.
If "remote:path" contains the file "subfolder/file.txt", the Path for "file.txt"
will be "subfolder/file.txt", not "remote:path/subfolder/file.txt".
When used without `--recursive` the Path will always be the same as Name.

The time is in RFC3339 format with up to nanosecond precision.  The
number of decimal digits in the seconds will depend on the precision
that the remote can hold the times, so if times are accurate to the
nearest millisecond (e.g. Google Drive) then 3 digits will always be
shown ("2017-05-31T16:15:57.034+01:00") whereas if the times are
accurate to the nearest second (Dropbox, Box, WebDav, etc.) no digits
will be shown ("2017-05-31T16:15:57+01:00").

The whole output can be processed as a JSON blob, or alternatively it
can be processed line by line as each item is written on individual lines
(except with `--stat`).

Any of the filtering options can be applied to this command.

There are several related list commands

- `ls` to list size and path of objects only
- `lsl` to list modification time, size and path of objects only
- `lsd` to list directories only
- `lsf` to list objects and directories in easy to parse format
- `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human-readable.
`lsf` is designed to be human and machine-readable.
`lsjson` is designed to be machine-readable.

Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default -
use `-R` to make them recurse.

List commands prefer a recursive method that uses more memory but fewer
transactions by default. Use `--disable ListR` to suppress the behavior.
See [`--fast-list`](/docs/#fast-list) for more details.

Listing a nonexistent directory will produce an error except for
remotes which can't have empty directories (e.g. s3, swift, or gcs -
the bucket-based remotes).

Usage:
  rclone lsjson remote:path [flags]

Flags:
      --dirs-only               Show only directories in the listing
      --encrypted               Show the encrypted names
      --files-only              Show only files in the listing
      --hash                    Include hashes in the output (may take longer)
      --hash-type stringArray   Show only this hash type (may be repeated)
  -h, --help                    help for lsjson
  -M, --metadata                Add metadata to the listing
      --no-mimetype             Don't read the mime type (can speed things up)
      --no-modtime              Don't read the modification time (can speed things up)
      --original                Show the ID of the underlying Object
  -R, --recursive               Recurse into the listing
      --stat                    Just return the info for the pointed to file

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `lsl`

````
Lists the objects in the source path to standard output in a human
readable format with modification time, size and path. Recurses by default.

E.g.

```console
$ rclone lsl swift:bucket
    60295 2016-06-25 18:55:41.062626927 bevajer5jef
    90613 2016-06-25 18:55:43.302607074 canole
    94467 2016-06-25 18:55:43.046609333 diwogej7
    37600 2016-06-25 18:55:40.814629136 fubuwic
```

Any of the filtering options can be applied to this command.

There are several related list commands

- `ls` to list size and path of objects only
- `lsl` to list modification time, size and path of objects only
- `lsd` to list directories only
- `lsf` to list objects and directories in easy to parse format
- `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human-readable.
`lsf` is designed to be human and machine-readable.
`lsjson` is designed to be machine-readable.

Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default -
use `-R` to make them recurse.

List commands prefer a recursive method that uses more memory but fewer
transactions by default. Use `--disable ListR` to suppress the behavior.
See [`--fast-list`](/docs/#fast-list) for more details.

Listing a nonexistent directory will produce an error except for
remotes which can't have empty directories (e.g. s3, swift, or gcs -
the bucket-based remotes).

Usage:
  rclone lsl remote:path [flags]

Flags:
  -h, --help   help for lsl

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `md5sum`

````
Produces an md5sum file for all the objects in the path.  This
is in the same format as the standard md5sum tool produces.

By default, the hash is requested from the remote.  If MD5 is
not supported by the remote, no hash will be returned.  With the
download flag, the file will be downloaded from the remote and
hashed locally enabling MD5 for any remote.

For other algorithms, see the [hashsum](/commands/rclone_hashsum/)
command. Running `rclone md5sum remote:path` is equivalent
to running `rclone hashsum MD5 remote:path`.

This command can also hash data received on standard input (stdin),
by not passing a remote:path, or by passing a hyphen as remote:path
when there is data to read (if not, the hyphen will be treated literally,
as a relative path).

Usage:
  rclone md5sum remote:path [flags]

Flags:
      --base64               Output base64 encoded hashsum
  -C, --checkfile string     Validate hashes against a given SUM file instead of printing them
      --download             Download the file and hash it locally; if this flag is not specified, the hash is requested from the remote
  -h, --help                 help for md5sum
      --output-file string   Output hashsums to a file rather than the terminal

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `mkdir`

````
Make the path if it doesn't already exist.

Usage:
  rclone mkdir remote:path [flags]

Flags:
  -h, --help   help for mkdir

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `mount`

````
Rclone mount allows Linux, FreeBSD, macOS and Windows to
mount any of Rclone's cloud storage systems as a file system with FUSE.

First set up your remote using `rclone config`. Check it works with `rclone ls` etc.

On Linux and macOS, you can run mount in either foreground or background (aka
daemon) mode. Mount runs in foreground mode by default. Use the `--daemon` flag
to force background mode. On Windows you can run mount in foreground only,
the flag is ignored.

In background mode rclone acts as a generic Unix mount program: the main
program starts, spawns background rclone process to setup and maintain the
mount, waits until success or timeout and exits with appropriate code
(killing the child process if it fails).

On Linux/macOS/FreeBSD start the mount like this, where `/path/to/local/mount`
is an **empty** **existing** directory:

```console
rclone mount remote:path/to/files /path/to/local/mount
```

On Windows you can start a mount in different ways. See [below](#mounting-modes-on-windows)
for details. If foreground mount is used interactively from a console window,
rclone will serve the mount and occupy the console so another window should be
used to work with the mount until rclone is interrupted e.g. by pressing Ctrl-C.

The following examples will mount to an automatically assigned drive,
to specific drive letter `X:`, to path `C:\path\parent\mount`
(where parent directory or drive must exist, and mount must **not** exist,
and is not supported when [mounting as a network drive](#mounting-modes-on-windows)),
and the last example will mount as network share `\\cloud\remote` and map it to an
automatically assigned drive:

```console
rclone mount remote:path/to/files *
rclone mount remote:path/to/files X:
rclone mount remote:path/to/files C:\path\parent\mount
rclone mount remote:path/to/files \\cloud\remote
```

When the program ends while in foreground mode, either via Ctrl+C or receiving
a SIGINT or SIGTERM signal, the mount should be automatically stopped.

When running in background mode the user will have to stop the mount manually:

```console
# Linux
fusermount -u /path/to/local/mount
#... or on some systems
fusermount3 -u /path/to/local/mount
# OS X or Linux when using nfsmount
umount /path/to/local/mount
```

The umount operation can fail, for example when the mountpoint is busy.
When that happens, it is the user's responsibility to stop the mount manually.

The size of the mounted file system will be set according to information retrieved
from the remote, the same as returned by the [rclone about](https://rclone.org/commands/rclone_about/)
command. Remotes with unlimited storage may report the used size only,
then an additional 1 PiB of free space is assumed. If the remote does not
[support](https://rclone.org/overview/#optional-features) the about feature
at all, then 1 PiB is set as both the total and the free size.

### Installing on Windows

To run `rclone mount on Windows`, you will need to
download and install [WinFsp](https://winfsp.dev).

[WinFsp](https://github.com/winfsp/winfsp) is an open-source
Windows File System Proxy which makes it easy to write user space file
systems for Windows.  It provides a FUSE emulation layer which rclone
uses combination with [cgofuse](https://github.com/winfsp/cgofuse).
Both of these packages are by Bill Zissimopoulos who was very helpful
during the implementation of rclone mount for Windows.

#### Mounting modes on windows

Unlike other operating systems, Microsoft Windows provides a different filesystem
type for network and fixed drives. It optimises access on the assumption fixed
disk drives are fast and reliable, while network drives have relatively high latency
and less reliability. Some settings can also be differentiated between the two types,
for example that Windows Explorer should just display icons and not create preview
thumbnails for image and video files on network drives.

In most cases, rclone will mount the remote as a normal, fixed disk drive by default.
However, you can also choose to mount it as a remote network drive, often described
as a network share. If you mount an rclone remote using the default, fixed drive
mode and experience unexpected program errors, freezes or other issues, consider
mounting as a network drive instead.

When mounting as a fixed disk drive you can either mount to an unused drive letter,
or to a path representing a **nonexistent** subdirectory of an **existing** parent
directory or drive. Using the special value `*` will tell rclone to
automatically assign the next available drive letter, starting with Z: and moving
backward. Examples:

```console
rclone mount remote:path/to/files *
rclone mount remote:path/to/files X:
rclone mount remote:path/to/files C:\path\parent\mount
rclone mount remote:path/to/files X:
```

Option `--volname` can be used to set a custom volume name for the mounted
file system. The default is to use the remote name and path.

To mount as network drive, you can add option `--network-mode`
to your mount command. Mounting to a directory path is not supported in
this mode, it is a limitation Windows imposes on junctions, so the remote must always
be mounted to a drive letter.

```console
rclone mount remote:path/to/files X: --network-mode
```

A volume name specified with `--volname` will be used to create the network share
path. A complete UNC path, such as `\\cloud\remote`, optionally with path
`\\cloud\remote\madeup\path`, will be used as is. Any other
string will be used as the share part, after a default prefix `\\server\`.
If no volume name is specified then `\\server\share` will be used.
You must make sure the volume name is unique when you are mounting more than one
drive, or else the mount command will fail. The share name will treated as the
volume label for the mapped drive, shown in Windows Explorer etc, while the complete
`\\server\share` will be reported as the remote UNC path by
`net use` etc, just like a normal network drive mapping.

If you specify a full network share UNC path with `--volname`, this will implicitly
set the `--network-mode` option, so the following two examples have same result:

```console
rclone mount remote:path/to/files X: --network-mode
rclone mount remote:path/to/files X: --volname \\server\share
```

You may also specify the network share UNC path as the mountpoint itself. Then rclone
will automatically assign a drive letter, same as with `*` and use that as
mountpoint, and instead use the UNC path specified as the volume name, as if it were
specified with the `--volname` option. This will also implicitly set
the `--network-mode` option. This means the following two examples have same result:

```console
rclone mount remote:path/to/files \\cloud\remote
rclone mount remote:path/to/files * --volname \\cloud\remote
```

There is yet another way to enable network mode, and to set the share path,
and that is to pass the "native" libfuse/WinFsp option directly:
`--fuse-flag --VolumePrefix=\server\share`. Note that the path
must be with just a single backslash prefix in this case.

*Note:* In previous versions of rclone this was the only supported method.

[Read more about drive mapping](https://en.wikipedia.org/wiki/Drive_mapping)

See also [Limitations](#limitations) section below.

#### Windows filesystem permissions

The FUSE emulation layer on Windows must convert between the POSIX-based
permission model used in FUSE, and the permission model used in Windows,
based on access-control lists (ACL).

The mounted filesystem will normally get three entries in its access-control list
(ACL), representing permissions for the POSIX permission scopes: Owner, group and
others. By default, the owner and group will be taken from the current user, and
the built-in group "Everyone" will be used to represent others. The user/group can
be customized with FUSE options "UserName" and "GroupName",
e.g. `-o UserName=user123 -o GroupName="Authenticated Users"`.
The permissions on each entry will be set according to [options](#options)
`--dir-perms` and `--file-perms`, which takes a value in traditional Unix
[numeric notation](https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation).

The default permissions corresponds to `--file-perms 0666 --dir-perms 0777`,
i.e. read and write permissions to everyone. This means you will not be able
to start any programs from the mount. To be able to do that you must add
execute permissions, e.g. `--file-perms 0777 --dir-perms 0777` to add it
to everyone. If the program needs to write files, chances are you will
have to enable [VFS File Caching](#vfs-file-caching) as well (see also
[limitations](#limitations)). Note that the default write permission have
some restrictions for accounts other than the owner, specifically it lacks
the "write extended attributes", as explained next.

The mapping of permissions is not always trivial, and the result you see in
Windows Explorer may not be exactly like you expected. For example, when setting
a value that includes write access for the group or others scope, this will be
mapped to individual permissions "write attributes", "write data" and
"append data", but not "write extended attributes". Windows will then show this
as basic permission "Special" instead of "Write", because "Write" also covers
the "write extended attributes" permission. When setting digit 0 for group or
others, to indicate no permissions, they will still get individual permissions
"read attributes", "read extended attributes" and "read permissions". This is
done for compatibility reasons, e.g. to allow users without additional
permissions to be able to read basic metadata about files like in Unix.

WinFsp 2021 (version 1.9) introduced a new FUSE option "FileSecurity",
that allows the complete specification of file security descriptors using
[SDDL](https://docs.microsoft.com/en-us/windows/win32/secauthz/security-descriptor-string-format).
With this you get detailed control of the resulting permissions, compared
to use of the POSIX permissions described above, and no additional permissions
will be added automatically for compatibility with Unix. Some example use
cases will following.

If you set POSIX permissions for only allowing access to the owner,
using `--file-perms 0600 --dir-perms 0700`, the user group and the built-in
"Everyone" group will still be given some special permissions, as described
above. Some programs may then (incorrectly) interpret this as the file being
accessible by everyone, for example an SSH client may warn about "unprotected
private key file". You can work around this by specifying
`-o FileSecurity="D:P(A;;FA;;;OW)"`, which sets file all access (FA) to the
owner (OW), and nothing else.

When setting write permissions then, except for the owner, this does not
include the "write extended attributes" permission, as mentioned above.
This may prevent applications from writing to files, giving permission denied
error instead. To set working write permissions for the built-in "Everyone"
group, similar to what it gets by default but with the addition of the
"write extended attributes", you can specify
`-o FileSecurity="D:P(A;;FRFW;;;WD)"`, which sets file read (FR) and file
write (FW) to everyone (WD). If file execute (FX) is also needed, then change
to `-o FileSecurity="D:P(A;;FRFWFX;;;WD)"`, or set file all access (FA) to
get full access permissions, including delete, with
`-o FileSecurity="D:P(A;;FA;;;WD)"`.

#### Windows caveats

Drives created as Administrator are not visible to other accounts,
not even an account that was elevated to Administrator with the
User Account Control (UAC) feature. A result of this is that if you mount
to a drive letter from a Command Prompt run as Administrator, and then try
to access the same drive from Windows Explorer (which does not run as
Administrator), you will not be able to see the mounted drive.

If you don't need to access the drive from applications running with
administrative privileges, the easiest way around this is to always
create the mount from a non-elevated command prompt.

To make mapped drives available to the user account that created them
regardless if elevated or not, there is a special Windows setting called
[linked connections](https://docs.microsoft.com/en-us/troubleshoot/windows-client/networking/mapped-drives-not-available-from-elevated-command#detail-to-configure-the-enablelinkedconnections-registry-entry)
that can be enabled.

It is also possible to make a drive mount available to everyone on the system,
by running the process creating it as the built-in SYSTEM account.
There are several ways to do this: One is to use the command-line
utility [PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec),
from Microsoft's Sysinternals suite, which has option `-s` to start
processes as the SYSTEM account. Another alternative is to run the mount
command from a Windows Scheduled Task, or a Windows Service, configured
to run as the SYSTEM account. A third alternative is to use the
[WinFsp.Launcher infrastructure](https://github.com/winfsp/winfsp/wiki/WinFsp-Service-Architecture)).
Read more in the [install documentation](https://rclone.org/install/).
Note that when running rclone as another user, it will not use
the configuration file from your profile unless you tell it to
with the [`--config`](https://rclone.org/docs/#config-string) option.
Note also that it is now the SYSTEM account that will have the owner
permissions, and other accounts will have permissions according to the
group or others scopes. As mentioned above, these will then not get the
"write extended attributes" permission, and this may prevent writing to
files. You can work around this with the FileSecurity option, see
example above.

Note that mapping to a directory path, instead of a drive letter,
does not suffer from the same limitations.

### Mounting on macOS

Mounting on macOS can be done either via [built-in NFS server](/commands/rclone_serve_nfs/),
[macFUSE](https://osxfuse.github.io/) (also known as osxfuse) or
[FUSE-T](https://www.fuse-t.org/).macFUSE is a traditional FUSE driver utilizing
a macOS kernel extension (kext). FUSE-T is an alternative FUSE system which
"mounts" via an NFSv4 local server.

#### Unicode Normalization

It is highly recommended to keep the default of `--no-unicode-normalization=false`
for all `mount` and `serve` commands on macOS. For details, see [vfs-case-sensitivity](https://rclone.org/commands/rclone_mount/#vfs-case-sensitivity).

#### NFS mount

This method spins up an NFS server using [serve nfs](/commands/rclone_serve_nfs/)
command and mounts it to the specified mountpoint. If you run this in background
mode using |--daemon|, you will need to send SIGTERM signal to the rclone process
using |kill| command to stop the mount.

Note that `--nfs-cache-handle-limit` controls the maximum number of cached file
handles stored by the `nfsmount` caching handler. This should not be set too low
or you may experience errors when trying to access files. The default is 1000000,
but consider lowering this limit if the server's system resource usage causes problems.

#### macFUSE Notes

If installing macFUSE using [dmg packages](https://github.com/osxfuse/osxfuse/releases)
from the website, rclone will locate the macFUSE libraries without any further intervention.
If however, macFUSE is installed using the [macports](https://www.macports.org/)
package manager, the following addition steps are required.

```console
sudo mkdir /usr/local/lib
cd /usr/local/lib
sudo ln -s /opt/local/lib/libfuse.2.dylib
```

#### FUSE-T Limitations, Caveats, and Notes

There are some limitations, caveats, and notes about how it works. These are
current as  of FUSE-T version 1.0.14.

##### ModTime update on read

As per the [FUSE-T wiki](https://github.com/macos-fuse-t/fuse-t/wiki#caveats):

> File access and modification times cannot be set separately as it seems to be an
> issue with the NFS client which always modifies both. Can be reproduced with
> 'touch -m' and 'touch -a' commands

This means that viewing files with various tools, notably macOS Finder, will cause
rlcone to update the modification time of the file. This may make rclone upload a
full new copy of the file.

##### Read Only mounts

When mounting with `--read-only`, attempts to write to files will fail *silently*
as opposed to with a clear warning as in macFUSE.

## Mounting on Linux

On newer versions of Ubuntu, you may encounter the following error when running
`rclone mount`:

> NOTICE: mount helper error: fusermount3: mount failed: Permission denied
> CRITICAL: Fatal error: failed to mount FUSE fs: fusermount: exit status 1
This may be due to newer [Apparmor](https://wiki.ubuntu.com/AppArmor) restrictions,
which can be disabled with `sudo aa-disable /usr/bin/fusermount3` (you may need to
`sudo apt install apparmor-utils` beforehand).

### Limitations

Without the use of `--vfs-cache-mode` this can only write files
sequentially, it can only seek when reading.  This means that many
applications won't work with their files on an rclone mount without
`--vfs-cache-mode writes` or `--vfs-cache-mode full`.
See the [VFS File Caching](#vfs-file-caching) section for more info.
When using NFS mount on macOS, if you don't specify |--vfs-cache-mode|
the mount point will be read-only.

Bucket-based remotes - Azure Blob, Swift, S3, Google Cloud Storage and B2 -
can't store empty directories. Of these, only Azure Blob, Google Cloud Storage
and S3 can preserve them when you add `--xxx-directory_markers`; otherwise,
empty directories will vanish once they drop out of the directory cache.

When `rclone mount` is invoked on Unix with `--daemon` flag, the main rclone
program will wait for the background mount to become ready or until the timeout
specified by the `--daemon-wait` flag. On Linux it can check mount status using
ProcFS so the flag in fact sets **maximum** time to wait, while the real wait
can be less. On macOS / BSD the time to wait is constant and the check is
performed only at the end. We advise you to set wait time on macOS reasonably.

Only supported on Linux, FreeBSD, OS X and Windows at the moment.

### rclone mount vs rclone sync/copy

File systems expect things to be 100% reliable, whereas cloud storage
systems are a long way from 100% reliable. The rclone sync/copy
commands cope with this with lots of retries.  However rclone mount
can't use retries in the same way without making local copies of the
uploads. Look at the [VFS File Caching](#vfs-file-caching)
for solutions to make mount more reliable.

### Attribute caching

You can use the flag `--attr-timeout` to set the time the kernel caches
the attributes (size, modification time, etc.) for directory entries.

The default is `1s` which caches files just long enough to avoid
too many callbacks to rclone from the kernel.

In theory 0s should be the correct value for filesystems which can
change outside the control of the kernel. However this causes quite a
few problems such as
[rclone using too much memory](https://github.com/rclone/rclone/issues/2157),
[rclone not serving files to samba](https://forum.rclone.org/t/rclone-1-39-vs-1-40-mount-issue/5112)
and [excessive time listing directories](https://github.com/rclone/rclone/issues/2095#issuecomment-371141147).

The kernel can cache the info about a file for the time given by
`--attr-timeout`. You may see corruption if the remote file changes
length during this window.  It will show up as either a truncated file
or a file with garbage on the end.  With `--attr-timeout 1s` this is
very unlikely but not impossible.  The higher you set `--attr-timeout`
the more likely it is.  The default setting of "1s" is the lowest
setting which mitigates the problems above.

If you set it higher (`10s` or `1m` say) then the kernel will call
back to rclone less often making it more efficient, however there is
more chance of the corruption issue above.

If files don't change on the remote outside of the control of rclone
then there is no chance of corruption.

This is the same as setting the attr_timeout option in mount.fuse.

### Filters

Note that all the rclone filters can be used to select a subset of the
files to be visible in the mount.

### systemd

When running rclone mount as a systemd service, it is possible
to use Type=notify. In this case the service will enter the started state
after the mountpoint has been successfully set up.
Units having the rclone mount service specified as a requirement
will see all files and folders immediately in this mode.

Note that systemd runs mount units without any environment variables including
`PATH` or `HOME`. This means that tilde (`~`) expansion will not work
and you should provide `--config` and `--cache-dir` explicitly as absolute
paths via rclone arguments.
Since mounting requires the `fusermount` or `fusermount3` program,
rclone will use the fallback PATH of `/bin:/usr/bin` in this scenario.
Please ensure that `fusermount`/`fusermount3` is present on this PATH.

### Rclone as Unix mount helper

The core Unix program `/bin/mount` normally takes the `-t FSTYPE` argument
then runs the `/sbin/mount.FSTYPE` helper program passing it mount options
as `-o key=val,...` or `--opt=...`. Automount (classic or systemd) behaves
in a similar way.

rclone by default expects GNU-style flags `--key val`. To run it as a mount
helper you should symlink rclone binary to `/sbin/mount.rclone` and optionally
`/usr/bin/rclonefs`, e.g. `ln -s /usr/bin/rclone /sbin/mount.rclone`.
rclone will detect it and translate command-line arguments appropriately.

Now you can run classic mounts like this:

```console
mount sftp1:subdir /mnt/data -t rclone -o vfs_cache_mode=writes,sftp_key_file=/path/to/pem
```

or create systemd mount units:

```ini
# /etc/systemd/system/mnt-data.mount
[Unit]
Description=Mount for /mnt/data
[Mount]
Type=rclone
What=sftp1:subdir
Where=/mnt/data
Options=rw,_netdev,allow_other,args2env,vfs-cache-mode=writes,config=/etc/rclone.conf,cache-dir=/var/rclone
```

optionally accompanied by systemd automount unit

```ini
# /etc/systemd/system/mnt-data.automount
[Unit]
Description=AutoMount for /mnt/data
[Automount]
Where=/mnt/data
TimeoutIdleSec=600
[Install]
WantedBy=multi-user.target
```

or add in `/etc/fstab` a line like

```console
sftp1:subdir /mnt/data rclone rw,noauto,nofail,_netdev,x-systemd.automount,args2env,vfs_cache_mode=writes,config=/etc/rclone.conf,cache_dir=/var/cache/rclone 0 0
```

or use classic Automountd.
Remember to provide explicit `config=...,cache-dir=...` as a workaround for
mount units being run without `HOME`.

Rclone in the mount helper mode will split `-o` argument(s) by comma, replace `_`
by `-` and prepend `--` to get the command-line flags. Options containing commas
or spaces can be wrapped in single or double quotes. Any inner quotes inside outer
quotes of the same type should be doubled.

Mount option syntax includes a few extra options treated specially:

- `env.NAME=VALUE` will set an environment variable for the mount process.
  This helps with Automountd and Systemd.mount which don't allow setting
  custom environment for mount helpers.
  Typically you will use `env.HTTPS_PROXY=proxy.host:3128` or `env.HOME=/root`
- `command=cmount` can be used to run `cmount` or any other rclone command
  rather than the default `mount`.
- `args2env` will pass mount options to the mount helper running in background
  via environment variables instead of command line arguments. This allows to
  hide secrets from such commands as `ps` or `pgrep`.
- `vv...` will be transformed into appropriate `--verbose=N`
- standard mount options like `x-systemd.automount`, `_netdev`, `nosuid` and alike
  are intended only for Automountd and ignored by rclone.

### VFS - Virtual File System

This command uses the VFS layer. This adapts the cloud storage objects
that rclone uses into something which looks much more like a disk
filing system.

Cloud storage objects have lots of properties which aren't like disk
files - you can't extend them or write to the middle of them, so the
VFS layer has to deal with that. Because there is no one right way of
doing this there are various options explained below.

The VFS layer also implements a directory cache - this caches info
about files and directories (but not the data) in memory.

### VFS Directory Cache

Using the `--dir-cache-time` flag, you can control how long a
directory should be considered up to date and not refreshed from the
backend. Changes made through the VFS will appear immediately or
invalidate the cache.

```text
    --dir-cache-time duration   Time to cache directory entries for (default 5m0s)
    --poll-interval duration    Time to wait between polling for changes. Must be smaller than dir-cache-time. Only on supported remotes. Set to 0 to disable (default 1m0s)
```

However, changes made directly on the cloud storage by the web
interface or a different copy of rclone will only be picked up once
the directory cache expires if the backend configured does not support
polling for changes. If the backend supports polling, changes will be
picked up within the polling interval.

You can send a `SIGHUP` signal to rclone for it to flush all
directory caches, regardless of how old they are.  Assuming only one
rclone instance is running, you can reset the cache like this:

```console
kill -SIGHUP $(pidof rclone)
```

If you configure rclone with a [remote control](/rc) then you can use
rclone rc to flush the whole directory cache:

```console
rclone rc vfs/forget
```

Or individual files or directories:

```console
rclone rc vfs/forget file=path/to/file dir=path/to/dir
```

### VFS File Buffering

The `--buffer-size` flag determines the amount of memory,
that will be used to buffer data in advance.

Each open file will try to keep the specified amount of data in memory
at all times. The buffered data is bound to one open file and won't be
shared.

This flag is a upper limit for the used memory per open file.  The
buffer will only use memory for data that is downloaded but not not
yet read. If the buffer is empty, only a small amount of memory will
be used.

The maximum memory used by rclone for buffering can be up to
`--buffer-size * open files`.

### VFS File Caching

These flags control the VFS file caching options. File caching is
necessary to make the VFS layer appear compatible with a normal file
system. It can be disabled at the cost of some compatibility.

For example you'll need to enable VFS caching if you want to read and
write simultaneously to a file.  See below for more details.

Note that the VFS cache is separate from the cache backend and you may
find that you need one or the other or both.

```text
    --cache-dir string                     Directory rclone will use for caching.
    --vfs-cache-mode CacheMode             Cache mode off|minimal|writes|full (default off)
    --vfs-cache-max-age duration           Max time since last access of objects in the cache (default 1h0m0s)
    --vfs-cache-max-size SizeSuffix        Max total size of objects in the cache (default off)
    --vfs-cache-min-free-space SizeSuffix  Target minimum free space on the disk containing the cache (default off)
    --vfs-cache-poll-interval duration     Interval to poll the cache for stale objects (default 1m0s)
    --vfs-write-back duration              Time to writeback files after last use when using cache (default 5s)
```

If run with `-vv` rclone will print the location of the file cache.  The
files are stored in the user cache file area which is OS dependent but
can be controlled with `--cache-dir` or setting the appropriate
environment variable.

The cache has 4 different modes selected by `--vfs-cache-mode`.
The higher the cache mode the more compatible rclone becomes at the
cost of using disk space.

Note that files are written back to the remote only when they are
closed and if they haven't been accessed for `--vfs-write-back`
seconds. If rclone is quit or dies with files that haven't been
uploaded, these will be uploaded next time rclone is run with the same
flags.

If using `--vfs-cache-max-size` or `--vfs-cache-min-free-space` note
that the cache may exceed these quotas for two reasons. Firstly
because it is only checked every `--vfs-cache-poll-interval`. Secondly
because open files cannot be evicted from the cache. When
`--vfs-cache-max-size` or `--vfs-cache-min-free-space` is exceeded,
rclone will attempt to evict the least accessed files from the cache
first. rclone will start with files that haven't been accessed for the
longest. This cache flushing strategy is efficient and more relevant
files are likely to remain cached.

The `--vfs-cache-max-age` will evict files from the cache
after the set time since last access has passed. The default value of
1 hour will start evicting files from cache that haven't been accessed
for 1 hour. When a cached file is accessed the 1 hour timer is reset to 0
and will wait for 1 more hour before evicting. Specify the time with
standard notation, s, m, h, d, w .

You **should not** run two copies of rclone using the same VFS cache
with the same or overlapping remotes if using `--vfs-cache-mode > off`.
This can potentially cause data corruption if you do. You can work
around this by giving each rclone its own cache hierarchy with
`--cache-dir`. You don't need to worry about this if the remotes in
use don't overlap.

#### --vfs-cache-mode off

In this mode (the default) the cache will read directly from the remote and write
directly to the remote without caching anything on disk.

This will mean some operations are not possible

- Files can't be opened for both read AND write
- Files opened for write can't be seeked
- Existing files opened for write must have O_TRUNC set
- Files open for read with O_TRUNC will be opened write only
- Files open for write only will behave as if O_TRUNC was supplied
- Open modes O_APPEND, O_TRUNC are ignored
- If an upload fails it can't be retried

#### --vfs-cache-mode minimal

This is very similar to "off" except that files opened for read AND
write will be buffered to disk.  This means that files opened for
write will be a lot more compatible, but uses the minimal disk space.

These operations are not possible

- Files opened for write only can't be seeked
- Existing files opened for write must have O_TRUNC set
- Files opened for write only will ignore O_APPEND, O_TRUNC
- If an upload fails it can't be retried

#### --vfs-cache-mode writes

In this mode files opened for read only are still read directly from
the remote, write only and read/write files are buffered to disk
first.

This mode should support all normal file system operations.

If an upload fails it will be retried at exponentially increasing
intervals up to 1 minute.

#### --vfs-cache-mode full

In this mode all reads and writes are buffered to and from disk. When
data is read from the remote this is buffered to disk as well.

In this mode the files in the cache will be sparse files and rclone
will keep track of which bits of the files it has downloaded.

So if an application only reads the starts of each file, then rclone
will only buffer the start of the file. These files will appear to be
their full size in the cache, but they will be sparse files with only
the data that has been downloaded present in them.

This mode should support all normal file system operations and is
otherwise identical to `--vfs-cache-mode` writes.

When reading a file rclone will read `--buffer-size` plus
`--vfs-read-ahead` bytes ahead.  The `--buffer-size` is buffered in memory
whereas the `--vfs-read-ahead` is buffered on disk.

When using this mode it is recommended that `--buffer-size` is not set
too large and `--vfs-read-ahead` is set large if required.

**IMPORTANT** not all file systems support sparse files. In particular
FAT/exFAT do not. Rclone will perform very badly if the cache
directory is on a filesystem which doesn't support sparse files and it
will log an ERROR message if one is detected.

#### Fingerprinting

Various parts of the VFS use fingerprinting to see if a local file
copy has changed relative to a remote file. Fingerprints are made
from:

- size
- modification time
- hash

where available on an object.

On some backends some of these attributes are slow to read (they take
an extra API call per object, or extra work per object).

For example `hash` is slow with the `local` and `sftp` backends as
they have to read the entire file and hash it, and `modtime` is slow
with the `s3`, `swift`, `ftp` and `qinqstor` backends because they
need to do an extra API call to fetch it.

If you use the `--vfs-fast-fingerprint` flag then rclone will not
include the slow operations in the fingerprint. This makes the
fingerprinting less accurate but much faster and will improve the
opening time of cached files.

If you are running a vfs cache over `local`, `s3` or `swift` backends
then using this flag is recommended.

Note that if you change the value of this flag, the fingerprints of
the files in the cache may be invalidated and the files will need to
be downloaded again.

### VFS Chunked Reading

When rclone reads files from a remote it reads them in chunks. This
means that rather than requesting the whole file rclone reads the
chunk specified.  This can reduce the used download quota for some
remotes by requesting only chunks from the remote that are actually
read, at the cost of an increased number of requests.

These flags control the chunking:

```text
    --vfs-read-chunk-size SizeSuffix        Read the source objects in chunks (default 128M)
    --vfs-read-chunk-size-limit SizeSuffix  Max chunk doubling size (default off)
    --vfs-read-chunk-streams int            The number of parallel streams to read at once
```

The chunking behaves differently depending on the `--vfs-read-chunk-streams` parameter.

#### `--vfs-read-chunk-streams` == 0

Rclone will start reading a chunk of size `--vfs-read-chunk-size`,
and then double the size for each read. When `--vfs-read-chunk-size-limit` is
specified, and greater than `--vfs-read-chunk-size`, the chunk size for each
open file will get doubled only until the specified value is reached. If the
value is "off", which is the default, the limit is disabled and the chunk size
will grow indefinitely.

With `--vfs-read-chunk-size 100M` and `--vfs-read-chunk-size-limit 0`
the following parts will be downloaded: 0-100M, 100M-200M, 200M-300M, 300M-400M
and so on. When `--vfs-read-chunk-size-limit 500M` is specified, the result would
be 0-100M, 100M-300M, 300M-700M, 700M-1200M, 1200M-1700M and so on.

Setting `--vfs-read-chunk-size` to `0` or "off" disables chunked reading.

The chunks will not be buffered in memory.

#### `--vfs-read-chunk-streams` > 0

Rclone reads `--vfs-read-chunk-streams` chunks of size
`--vfs-read-chunk-size` concurrently. The size for each read will stay
constant.

This improves performance performance massively on high latency links
or very high bandwidth links to high performance object stores.

Some experimentation will be needed to find the optimum values of
`--vfs-read-chunk-size` and `--vfs-read-chunk-streams` as these will
depend on the backend in use and the latency to the backend.

For high performance object stores (eg AWS S3) a reasonable place to
start might be `--vfs-read-chunk-streams 16` and
`--vfs-read-chunk-size 4M`. In testing with AWS S3 the performance
scaled roughly as the `--vfs-read-chunk-streams` setting.

Similar settings should work for high latency links, but depending on
the latency they may need more `--vfs-read-chunk-streams` in order to
get the throughput.

### VFS Performance

These flags may be used to enable/disable features of the VFS for
performance or other reasons. See also the [chunked reading](#vfs-chunked-reading)
feature.

In particular S3 and Swift benefit hugely from the `--no-modtime` flag
(or use `--use-server-modtime` for a slightly different effect) as each
read of the modification time takes a transaction.

```text
    --no-checksum     Don't compare checksums on up/download.
    --no-modtime      Don't read/write the modification time (can speed things up).
    --no-seek         Don't allow seeking in files.
    --read-only       Only allow read-only access.
```

Sometimes rclone is delivered reads or writes out of order. Rather
than seeking rclone will wait a short time for the in sequence read or
write to come in. These flags only come into effect when not using an
on disk cache file.

```text
    --vfs-read-wait duration   Time to wait for in-sequence read before seeking (default 20ms)
    --vfs-write-wait duration  Time to wait for in-sequence write before giving error (default 1s)
```

When using VFS write caching (`--vfs-cache-mode` with value writes or full),
the global flag `--transfers` can be set to adjust the number of parallel uploads
of modified files from the cache (the related global flag `--checkers` has no
effect on the VFS).

```text
    --transfers int  Number of file transfers to run in parallel (default 4)
```

### Symlinks

By default the VFS does not support symlinks. However this may be
enabled with either of the following flags:

```text
    --links      Translate symlinks to/from regular files with a '.rclonelink' extension.
    --vfs-links  Translate symlinks to/from regular files with a '.rclonelink' extension for the VFS
```

As most cloud storage systems do not support symlinks directly, rclone
stores the symlink as a normal file with a special extension. So a
file which appears as a symlink `link-to-file.txt` would be stored on
cloud storage as `link-to-file.txt.rclonelink` and the contents would
be the path to the symlink destination.

Note that `--links` enables symlink translation globally in rclone -
this includes any backend which supports the concept (for example the
local backend). `--vfs-links` just enables it for the VFS layer.

This scheme is compatible with that used by the
[local backend with the --local-links flag](/local/#symlinks-junction-points).

The `--vfs-links` flag has been designed for `rclone mount`, `rclone
nfsmount` and `rclone serve nfs`.

It hasn't been tested with the other `rclone serve` commands yet.

A limitation of the current implementation is that it expects the
caller to resolve sub-symlinks. For example given this directory tree

```text
.
├── dir
│   └── file.txt
└── linked-dir -> dir
```

The VFS will correctly resolve `linked-dir` but not
`linked-dir/file.txt`. This is not a problem for the tested commands
but may be for other commands.

**Note** that there is an outstanding issue with symlink support
[issue #8245](https://github.com/rclone/rclone/issues/8245) with duplicate
files being created when symlinks are moved into directories where
there is a file of the same name (or vice versa).

### VFS Case Sensitivity

Linux file systems are case-sensitive: two files can differ only
by case, and the exact case must be used when opening a file.

File systems in modern Windows are case-insensitive but case-preserving:
although existing files can be opened using any case, the exact case used
to create the file is preserved and available for programs to query.
It is not allowed for two files in the same directory to differ only by case.

Usually file systems on macOS are case-insensitive. It is possible to make macOS
file systems case-sensitive but that is not the default.

The `--vfs-case-insensitive` VFS flag controls how rclone handles these
two cases. If its value is "false", rclone passes file names to the remote
as-is. If the flag is "true" (or appears without a value on the
command line), rclone may perform a "fixup" as explained below.

The user may specify a file name to open/delete/rename/etc with a case
different than what is stored on the remote. If an argument refers
to an existing file with exactly the same name, then the case of the existing
file on the disk will be used. However, if a file name with exactly the same
name is not found but a name differing only by case exists, rclone will
transparently fixup the name. This fixup happens only when an existing file
is requested. Case sensitivity of file names created anew by rclone is
controlled by the underlying remote.

Note that case sensitivity of the operating system running rclone (the target)
may differ from case sensitivity of a file system presented by rclone (the source).
The flag controls whether "fixup" is performed to satisfy the target.

If the flag is not provided on the command line, then its default value depends
on the operating system where rclone runs: "true" on Windows and macOS, "false"
otherwise. If the flag is provided without a value, then it is "true".

The `--no-unicode-normalization` flag controls whether a similar "fixup" is
performed for filenames that differ but are [canonically
equivalent](https://en.wikipedia.org/wiki/Unicode_equivalence) with respect to
unicode. Unicode normalization can be particularly helpful for users of macOS,
which prefers form NFD instead of the NFC used by most other platforms. It is
therefore highly recommended to keep the default of `false` on macOS, to avoid
encoding compatibility issues.

In the (probably unlikely) event that a directory has multiple duplicate
filenames after applying case and unicode normalization, the `--vfs-block-norm-dupes`
flag allows hiding these duplicates. This comes with a performance tradeoff, as
rclone will have to scan the entire directory for duplicates when listing a
directory. For this reason, it is recommended to leave this disabled if not
needed. However, macOS users may wish to consider using it, as otherwise, if a
remote directory contains both NFC and NFD versions of the same filename, an odd
situation will occur: both versions of the file will be visible in the mount,
and both will appear to be editable, however, editing either version will
actually result in only the NFD version getting edited under the hood. `--vfs-block-
norm-dupes` prevents this confusion by detecting this scenario, hiding the
duplicates, and logging an error, similar to how this is handled in `rclone
sync`.

### VFS Disk Options

This flag allows you to manually set the statistics about the filing system.
It can be useful when those statistics cannot be read correctly automatically.

```text
    --vfs-disk-space-total-size    Manually set the total disk space size (example: 256G, default: -1)
```

### Alternate report of used bytes

Some backends, most notably S3, do not report the amount of bytes used.
If you need this information to be available when running `df` on the
filesystem, then pass the flag `--vfs-used-is-size` to rclone.
With this flag set, instead of relying on the backend to report this
information, rclone will scan the whole remote similar to `rclone size`
and compute the total used space itself.

**WARNING**: Contrary to `rclone size`, this flag ignores filters so that the
result is accurate. However, this is very inefficient and may cost lots of API
calls resulting in extra charges. Use it as a last resort and only with caching.

### VFS Metadata

If you use the `--vfs-metadata-extension` flag you can get the VFS to
expose files which contain the [metadata](/docs/#metadata) as a JSON
blob. These files will not appear in the directory listing, but can be
`stat`-ed and opened and once they have been they **will** appear in
directory listings until the directory cache expires.

Note that some backends won't create metadata unless you pass in the
`--metadata` flag.

For example, using `rclone mount` with `--metadata --vfs-metadata-extension .metadata`
we get

```console
$ ls -l /mnt/
total 1048577
-rw-rw-r-- 1 user user 1073741824 Mar  3 16:03 1G

$ cat /mnt/1G.metadata
{
        "atime": "2025-03-04T17:34:22.317069787Z",
        "btime": "2025-03-03T16:03:37.708253808Z",
        "gid": "1000",
        "mode": "100664",
        "mtime": "2025-03-03T16:03:39.640238323Z",
        "uid": "1000"
}

$ ls -l /mnt/
total 1048578
-rw-rw-r-- 1 user user 1073741824 Mar  3 16:03 1G
-rw-rw-r-- 1 user user        185 Mar  3 16:03 1G.metadata
```

If the file has no metadata it will be returned as `{}` and if there
is an error reading the metadata the error will be returned as
`{"error":"error string"}`.

Usage:
  rclone mount remote:path /path/to/mountpoint [flags]

Flags:
      --allow-non-empty                        Allow mounting over a non-empty directory (not supported on Windows)
      --allow-other                            Allow access to other users (not supported on Windows)
      --allow-root                             Allow access to root user (not supported on Windows)
      --async-read                             Use asynchronous reads (not supported on Windows) (default true)
      --attr-timeout Duration                  Time for which file/directory attributes are cached (default 1s)
      --daemon                                 Run mount in background and exit parent process (as background output is suppressed, use --log-file with --log-format=pid,... to monitor) (not supported on Windows)
      --daemon-timeout Duration                Time limit for rclone to respond to kernel (not supported on Windows) (default 0s)
      --daemon-wait Duration                   Time to wait for ready mount from daemon (maximum time on Linux, constant sleep time on OSX/BSD) (not supported on Windows) (default 1m0s)
      --debug-fuse                             Debug the FUSE internals - needs -v
      --default-permissions                    Makes kernel enforce access control based on the file mode (not supported on Windows)
      --devname string                         Set the device name - default is remote:path
      --dir-cache-time Duration                Time to cache directory entries for (default 5m0s)
      --dir-perms FileMode                     Directory permissions (default 777)
      --direct-io                              Use Direct IO, disables caching of data
      --file-perms FileMode                    File permissions (default 666)
      --fuse-flag stringArray                  Flags or arguments to be passed direct to libfuse/WinFsp (repeat if required)
      --gid uint32                             Override the gid field set by the filesystem (not supported on Windows)
  -h, --help                                   help for mount
      --link-perms FileMode                    Link permissions (default 666)
      --max-read-ahead SizeSuffix              The number of bytes that can be prefetched for sequential reads (not supported on Windows) (default 128Ki)
      --mount-case-insensitive Tristate        Tell the OS the mount is case insensitive (true) or sensitive (false) regardless of the backend (auto) (default unset)
      --network-mode                           Mount as remote network drive, instead of fixed disk drive (supported on Windows only)
      --no-checksum                            Don't compare checksums on up/download
      --no-modtime                             Don't read/write the modification time (can speed things up)
      --no-seek                                Don't allow seeking in files
      --noappledouble                          Ignore Apple Double (._) and .DS_Store files (supported on OSX only) (default true)
      --noapplexattr                           Ignore all "com.apple.*" extended attributes (supported on OSX only)
  -o, --option stringArray                     Option for libfuse/WinFsp (repeat if required)
      --poll-interval Duration                 Time to wait between polling for changes, must be smaller than dir-cache-time and only on supported remotes (set 0 to disable) (default 1m0s)
      --read-only                              Only allow read-only access
      --uid uint32                             Override the uid field set by the filesystem (not supported on Windows)
      --umask FileMode                         Override the permission bits set by the filesystem (not supported on Windows) (default 002)
      --vfs-block-norm-dupes                   If duplicate filenames exist in the same directory (after normalization), log an error and hide the duplicates (may have a performance cost)
      --vfs-cache-max-age Duration             Max time since last access of objects in the cache (default 1h0m0s)
      --vfs-cache-max-size SizeSuffix          Max total size of objects in the cache (default off)
      --vfs-cache-min-free-space SizeSuffix    Target minimum free space on the disk containing the cache (default off)
      --vfs-cache-mode CacheMode               Cache mode off|minimal|writes|full (default off)
      --vfs-cache-poll-interval Duration       Interval to poll the cache for stale objects (default 1m0s)
      --vfs-case-insensitive                   If a file name not found, find a case insensitive match
      --vfs-disk-space-total-size SizeSuffix   Specify the total space of disk (default off)
      --vfs-fast-fingerprint                   Use fast (less accurate) fingerprints for change detection
      --vfs-links                              Translate symlinks to/from regular files with a '.rclonelink' extension for the VFS
      --vfs-metadata-extension string          Set the extension to read metadata from
      --vfs-read-ahead SizeSuffix              Extra read ahead over --buffer-size when using cache-mode full
      --vfs-read-chunk-size SizeSuffix         Read the source objects in chunks (default 128Mi)
      --vfs-read-chunk-size-limit SizeSuffix   If greater than --vfs-read-chunk-size, double the chunk size after each chunk read, until the limit is reached ('off' is unlimited) (default off)
      --vfs-read-chunk-streams int             The number of parallel streams to read at once
      --vfs-read-wait Duration                 Time to wait for in-sequence read before seeking (default 20ms)
      --vfs-refresh                            Refreshes the directory cache recursively in the background on start
      --vfs-used-is-size rclone size           Use the rclone size algorithm for Used size
      --vfs-write-back Duration                Time to writeback files after last use when using cache (default 5s)
      --vfs-write-wait Duration                Time to wait for in-sequence write before giving error (default 1s)
      --volname string                         Set the volume name (supported on Windows and OSX only)
      --write-back-cache                       Makes kernel buffer writes before sending them to rclone (without this, writethrough caching is used) (not supported on Windows)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `move`

````
Moves the contents of the source directory to the destination
directory. Rclone will error if the source and destination overlap and
the remote does not support a server-side directory move operation.

To move single files, use the [moveto](/commands/rclone_moveto/)
command instead.

If no filters are in use and if possible this will server-side move
`source:path` into `dest:path`. After this `source:path` will no
longer exist.

Otherwise for each file in `source:path` selected by the filters (if
any) this will move it into `dest:path`.  If possible a server-side
move will be used, otherwise it will copy it (server-side if possible)
into `dest:path` then delete the original (if no errors on copy) in
`source:path`.

If you want to delete empty source directories after move, use the
`--delete-empty-src-dirs` flag.

See the [--no-traverse](/docs/#no-traverse) option for controlling
whether rclone lists the destination directory or not.  Supplying this
option when moving a small number of files into a large destination
can speed transfers up greatly.

Rclone will sync the modification times of files and directories if
the backend supports it. If metadata syncing is required then use the
`--metadata` flag.

Note that the modification time and metadata for the root directory
will **not** be synced. See <https://github.com/rclone/rclone/issues/7652>
for more info.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`-i` flag.

**Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics.

### Logger Flags

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match` and `--error`
flags write paths, one per line, to the file name (or stdout if it is `-`)
supplied. What they write is described in the help below. For example
`--differ` will write all paths which are present on both the source and
destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The `--dest-after` flag writes a list file using the same format flags
as [`lsf`](/commands/rclone_lsf/#synopsis) (including [customizable options
for hash, modtime, etc.](/commands/rclone_lsf/#synopsis))
Conceptually it is similar to rsync's `--itemize-changes`, but not identical
-- it should output an accurate list of what will be on the destination
after the command is finished.

When the `--no-traverse` flag is set, all logs involving files that exist only
on the destination will be incomplete or completely missing.

Note that these logger flags have a few limitations, and certain scenarios
are not currently supported:

- `--max-duration` / `CutoffModeHard`
- `--compare-dest` / `--copy-dest`
- server-side moves of an entire dir at once
- High-level retries, because there would be duplicates (use `--retries 1` to disable)
- Possibly some unusual error scenarios

Note also that each file is logged during execution, as opposed to after, so it
is most useful as a predictor of what SHOULD happen to each file
(which may or may not match what actually DID).

Usage:
  rclone move source:path dest:path [flags]

Flags:
      --absolute                Put a leading / in front of path names
      --combined string         Make a combined report of changes to this file
      --create-empty-src-dirs   Create empty source dirs on destination after move
      --csv                     Output in CSV format
      --delete-empty-src-dirs   Delete empty source dirs after move
      --dest-after string       Report all files that exist on the dest post-sync
      --differ string           Report all non-matching files to this file
  -d, --dir-slash               Append a slash to directory names (default true)
      --dirs-only               Only list directories
      --error string            Report all files with errors (hashing or reading) to this file
      --files-only              Only list files (default true)
  -F, --format string           Output format - see lsf help for details (default "p")
      --hash h                  Use this hash when h is used in the format MD5|SHA-1|DropboxHash (default "md5")
  -h, --help                    help for move
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
  -s, --separator string        Separator for the items in the format (default ";")
  -t, --timeformat string       Specify a custom time format - see docs for details (default: 2006-01-02 15:04:05)

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `moveto`

````
If source:path is a file or directory then it moves it to a file or
directory named dest:path.

This can be used to rename files or upload single files to other than
their existing name.  If the source is a directory then it acts exactly
like the [move](/commands/rclone_move/) command.

So

```console
rclone moveto src dst
```

where src and dst are rclone paths, either remote:path or
/path/to/local or C:\windows\path\if\on\windows.

This will:

```text
if src is file
    move it to dst, overwriting an existing file if it exists
if src is directory
    move it to dst, overwriting existing files if they exist
    see move command for full details
```

This doesn't transfer files that are identical on src and dst, testing
by size and modification time or MD5SUM.  src will be deleted on
successful transfer.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`-i` flag.

**Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics.

### Logger Flags

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match` and `--error`
flags write paths, one per line, to the file name (or stdout if it is `-`)
supplied. What they write is described in the help below. For example
`--differ` will write all paths which are present on both the source and
destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The `--dest-after` flag writes a list file using the same format flags
as [`lsf`](/commands/rclone_lsf/#synopsis) (including [customizable options
for hash, modtime, etc.](/commands/rclone_lsf/#synopsis))
Conceptually it is similar to rsync's `--itemize-changes`, but not identical
-- it should output an accurate list of what will be on the destination
after the command is finished.

When the `--no-traverse` flag is set, all logs involving files that exist only
on the destination will be incomplete or completely missing.

Note that these logger flags have a few limitations, and certain scenarios
are not currently supported:

- `--max-duration` / `CutoffModeHard`
- `--compare-dest` / `--copy-dest`
- server-side moves of an entire dir at once
- High-level retries, because there would be duplicates (use `--retries 1` to disable)
- Possibly some unusual error scenarios

Note also that each file is logged during execution, as opposed to after, so it
is most useful as a predictor of what SHOULD happen to each file
(which may or may not match what actually DID).

Usage:
  rclone moveto source:path dest:path [flags]

Flags:
      --absolute                Put a leading / in front of path names
      --combined string         Make a combined report of changes to this file
      --csv                     Output in CSV format
      --dest-after string       Report all files that exist on the dest post-sync
      --differ string           Report all non-matching files to this file
  -d, --dir-slash               Append a slash to directory names (default true)
      --dirs-only               Only list directories
      --error string            Report all files with errors (hashing or reading) to this file
      --files-only              Only list files (default true)
  -F, --format string           Output format - see lsf help for details (default "p")
      --hash h                  Use this hash when h is used in the format MD5|SHA-1|DropboxHash (default "md5")
  -h, --help                    help for moveto
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
  -s, --separator string        Separator for the items in the format (default ";")
  -t, --timeformat string       Specify a custom time format - see docs for details (default: 2006-01-02 15:04:05)

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `ncdu`

````
This displays a text based user interface allowing the navigation of a
remote. It is most useful for answering the question - "What is using
all my disk space?".

{{< asciinema 157793 >}}

To make the user interface it first scans the entire remote given and
builds an in memory representation.  rclone ncdu can be used during
this scanning phase and you will see it building up the directory
structure as it goes along.

You can interact with the user interface using key presses,
press '?' to toggle the help on and off. The supported keys are:

```text
 ↑,↓ or k,j to Move
 →,l to enter
 ←,h to return
 g toggle graph
 c toggle counts
 a toggle average size in directory
 m toggle modified time
 u toggle human-readable format
 n,s,C,A,M sort by name,size,count,asize,mtime
 d delete file/directory
 v select file/directory
 V enter visual select mode
 D delete selected files/directories
 Y display current path
 ^L refresh screen (fix screen corruption)
 r recalculate file sizes
 ? to toggle help on and off
 ESC to close the menu box
 q/^c to quit
```

Listed files/directories may be prefixed by a one-character flag,
some of them combined with a description in brackets at end of line.
These flags have the following meaning:

```text
e means this is an empty directory, i.e. contains no files (but
  may contain empty subdirectories)
~ means this is a directory where some of the files (possibly in
  subdirectories) have unknown size, and therefore the directory
  size may be underestimated (and average size inaccurate, as it
  is average of the files with known sizes).
. means an error occurred while reading a subdirectory, and
  therefore the directory size may be underestimated (and average
  size inaccurate)
! means an error occurred while reading this directory
```

This an homage to the [ncdu tool](https://dev.yorhel.nl/ncdu) but for
rclone remotes.  It is missing lots of features at the moment
but is useful as it stands. Unlike ncdu it does not show excluded files.

Note that it might take some time to delete big files/directories. The
UI won't respond in the meantime since the deletion is done synchronously.

For a non-interactive listing of the remote, see the
[tree](/commands/rclone_tree/) command. To just get the total size of
the remote you can also use the [size](/commands/rclone_size/) command.

Usage:
  rclone ncdu remote:path [flags]

Flags:
  -h, --help   help for ncdu

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `nfsmount`

````
Rclone nfsmount allows Linux, FreeBSD, macOS and Windows to
mount any of Rclone's cloud storage systems as a file system with FUSE.

First set up your remote using `rclone config`. Check it works with `rclone ls` etc.

On Linux and macOS, you can run mount in either foreground or background (aka
daemon) mode. Mount runs in foreground mode by default. Use the `--daemon` flag
to force background mode. On Windows you can run mount in foreground only,
the flag is ignored.

In background mode rclone acts as a generic Unix mount program: the main
program starts, spawns background rclone process to setup and maintain the
mount, waits until success or timeout and exits with appropriate code
(killing the child process if it fails).

On Linux/macOS/FreeBSD start the mount like this, where `/path/to/local/mount`
is an **empty** **existing** directory:

```console
rclone nfsmount remote:path/to/files /path/to/local/mount
```

On Windows you can start a mount in different ways. See [below](#mounting-modes-on-windows)
for details. If foreground mount is used interactively from a console window,
rclone will serve the mount and occupy the console so another window should be
used to work with the mount until rclone is interrupted e.g. by pressing Ctrl-C.

The following examples will mount to an automatically assigned drive,
to specific drive letter `X:`, to path `C:\path\parent\mount`
(where parent directory or drive must exist, and mount must **not** exist,
and is not supported when [mounting as a network drive](#mounting-modes-on-windows)),
and the last example will mount as network share `\\cloud\remote` and map it to an
automatically assigned drive:

```console
rclone nfsmount remote:path/to/files *
rclone nfsmount remote:path/to/files X:
rclone nfsmount remote:path/to/files C:\path\parent\mount
rclone nfsmount remote:path/to/files \\cloud\remote
```

When the program ends while in foreground mode, either via Ctrl+C or receiving
a SIGINT or SIGTERM signal, the mount should be automatically stopped.

When running in background mode the user will have to stop the mount manually:

```console
# Linux
fusermount -u /path/to/local/mount
#... or on some systems
fusermount3 -u /path/to/local/mount
# OS X or Linux when using nfsmount
umount /path/to/local/mount
```

The umount operation can fail, for example when the mountpoint is busy.
When that happens, it is the user's responsibility to stop the mount manually.

The size of the mounted file system will be set according to information retrieved
from the remote, the same as returned by the [rclone about](https://rclone.org/commands/rclone_about/)
command. Remotes with unlimited storage may report the used size only,
then an additional 1 PiB of free space is assumed. If the remote does not
[support](https://rclone.org/overview/#optional-features) the about feature
at all, then 1 PiB is set as both the total and the free size.

### Installing on Windows

To run `rclone nfsmount on Windows`, you will need to
download and install [WinFsp](https://winfsp.dev).

[WinFsp](https://github.com/winfsp/winfsp) is an open-source
Windows File System Proxy which makes it easy to write user space file
systems for Windows.  It provides a FUSE emulation layer which rclone
uses combination with [cgofuse](https://github.com/winfsp/cgofuse).
Both of these packages are by Bill Zissimopoulos who was very helpful
during the implementation of rclone nfsmount for Windows.

#### Mounting modes on windows

Unlike other operating systems, Microsoft Windows provides a different filesystem
type for network and fixed drives. It optimises access on the assumption fixed
disk drives are fast and reliable, while network drives have relatively high latency
and less reliability. Some settings can also be differentiated between the two types,
for example that Windows Explorer should just display icons and not create preview
thumbnails for image and video files on network drives.

In most cases, rclone will mount the remote as a normal, fixed disk drive by default.
However, you can also choose to mount it as a remote network drive, often described
as a network share. If you mount an rclone remote using the default, fixed drive
mode and experience unexpected program errors, freezes or other issues, consider
mounting as a network drive instead.

When mounting as a fixed disk drive you can either mount to an unused drive letter,
or to a path representing a **nonexistent** subdirectory of an **existing** parent
directory or drive. Using the special value `*` will tell rclone to
automatically assign the next available drive letter, starting with Z: and moving
backward. Examples:

```console
rclone nfsmount remote:path/to/files *
rclone nfsmount remote:path/to/files X:
rclone nfsmount remote:path/to/files C:\path\parent\mount
rclone nfsmount remote:path/to/files X:
```

Option `--volname` can be used to set a custom volume name for the mounted
file system. The default is to use the remote name and path.

To mount as network drive, you can add option `--network-mode`
to your nfsmount command. Mounting to a directory path is not supported in
this mode, it is a limitation Windows imposes on junctions, so the remote must always
be mounted to a drive letter.

```console
rclone nfsmount remote:path/to/files X: --network-mode
```

A volume name specified with `--volname` will be used to create the network share
path. A complete UNC path, such as `\\cloud\remote`, optionally with path
`\\cloud\remote\madeup\path`, will be used as is. Any other
string will be used as the share part, after a default prefix `\\server\`.
If no volume name is specified then `\\server\share` will be used.
You must make sure the volume name is unique when you are mounting more than one
drive, or else the mount command will fail. The share name will treated as the
volume label for the mapped drive, shown in Windows Explorer etc, while the complete
`\\server\share` will be reported as the remote UNC path by
`net use` etc, just like a normal network drive mapping.

If you specify a full network share UNC path with `--volname`, this will implicitly
set the `--network-mode` option, so the following two examples have same result:

```console
rclone nfsmount remote:path/to/files X: --network-mode
rclone nfsmount remote:path/to/files X: --volname \\server\share
```

You may also specify the network share UNC path as the mountpoint itself. Then rclone
will automatically assign a drive letter, same as with `*` and use that as
mountpoint, and instead use the UNC path specified as the volume name, as if it were
specified with the `--volname` option. This will also implicitly set
the `--network-mode` option. This means the following two examples have same result:

```console
rclone nfsmount remote:path/to/files \\cloud\remote
rclone nfsmount remote:path/to/files * --volname \\cloud\remote
```

There is yet another way to enable network mode, and to set the share path,
and that is to pass the "native" libfuse/WinFsp option directly:
`--fuse-flag --VolumePrefix=\server\share`. Note that the path
must be with just a single backslash prefix in this case.

*Note:* In previous versions of rclone this was the only supported method.

[Read more about drive mapping](https://en.wikipedia.org/wiki/Drive_mapping)

See also [Limitations](#limitations) section below.

#### Windows filesystem permissions

The FUSE emulation layer on Windows must convert between the POSIX-based
permission model used in FUSE, and the permission model used in Windows,
based on access-control lists (ACL).

The mounted filesystem will normally get three entries in its access-control list
(ACL), representing permissions for the POSIX permission scopes: Owner, group and
others. By default, the owner and group will be taken from the current user, and
the built-in group "Everyone" will be used to represent others. The user/group can
be customized with FUSE options "UserName" and "GroupName",
e.g. `-o UserName=user123 -o GroupName="Authenticated Users"`.
The permissions on each entry will be set according to [options](#options)
`--dir-perms` and `--file-perms`, which takes a value in traditional Unix
[numeric notation](https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation).

The default permissions corresponds to `--file-perms 0666 --dir-perms 0777`,
i.e. read and write permissions to everyone. This means you will not be able
to start any programs from the mount. To be able to do that you must add
execute permissions, e.g. `--file-perms 0777 --dir-perms 0777` to add it
to everyone. If the program needs to write files, chances are you will
have to enable [VFS File Caching](#vfs-file-caching) as well (see also
[limitations](#limitations)). Note that the default write permission have
some restrictions for accounts other than the owner, specifically it lacks
the "write extended attributes", as explained next.

The mapping of permissions is not always trivial, and the result you see in
Windows Explorer may not be exactly like you expected. For example, when setting
a value that includes write access for the group or others scope, this will be
mapped to individual permissions "write attributes", "write data" and
"append data", but not "write extended attributes". Windows will then show this
as basic permission "Special" instead of "Write", because "Write" also covers
the "write extended attributes" permission. When setting digit 0 for group or
others, to indicate no permissions, they will still get individual permissions
"read attributes", "read extended attributes" and "read permissions". This is
done for compatibility reasons, e.g. to allow users without additional
permissions to be able to read basic metadata about files like in Unix.

WinFsp 2021 (version 1.9) introduced a new FUSE option "FileSecurity",
that allows the complete specification of file security descriptors using
[SDDL](https://docs.microsoft.com/en-us/windows/win32/secauthz/security-descriptor-string-format).
With this you get detailed control of the resulting permissions, compared
to use of the POSIX permissions described above, and no additional permissions
will be added automatically for compatibility with Unix. Some example use
cases will following.

If you set POSIX permissions for only allowing access to the owner,
using `--file-perms 0600 --dir-perms 0700`, the user group and the built-in
"Everyone" group will still be given some special permissions, as described
above. Some programs may then (incorrectly) interpret this as the file being
accessible by everyone, for example an SSH client may warn about "unprotected
private key file". You can work around this by specifying
`-o FileSecurity="D:P(A;;FA;;;OW)"`, which sets file all access (FA) to the
owner (OW), and nothing else.

When setting write permissions then, except for the owner, this does not
include the "write extended attributes" permission, as mentioned above.
This may prevent applications from writing to files, giving permission denied
error instead. To set working write permissions for the built-in "Everyone"
group, similar to what it gets by default but with the addition of the
"write extended attributes", you can specify
`-o FileSecurity="D:P(A;;FRFW;;;WD)"`, which sets file read (FR) and file
write (FW) to everyone (WD). If file execute (FX) is also needed, then change
to `-o FileSecurity="D:P(A;;FRFWFX;;;WD)"`, or set file all access (FA) to
get full access permissions, including delete, with
`-o FileSecurity="D:P(A;;FA;;;WD)"`.

#### Windows caveats

Drives created as Administrator are not visible to other accounts,
not even an account that was elevated to Administrator with the
User Account Control (UAC) feature. A result of this is that if you mount
to a drive letter from a Command Prompt run as Administrator, and then try
to access the same drive from Windows Explorer (which does not run as
Administrator), you will not be able to see the mounted drive.

If you don't need to access the drive from applications running with
administrative privileges, the easiest way around this is to always
create the mount from a non-elevated command prompt.

To make mapped drives available to the user account that created them
regardless if elevated or not, there is a special Windows setting called
[linked connections](https://docs.microsoft.com/en-us/troubleshoot/windows-client/networking/mapped-drives-not-available-from-elevated-command#detail-to-configure-the-enablelinkedconnections-registry-entry)
that can be enabled.

It is also possible to make a drive mount available to everyone on the system,
by running the process creating it as the built-in SYSTEM account.
There are several ways to do this: One is to use the command-line
utility [PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec),
from Microsoft's Sysinternals suite, which has option `-s` to start
processes as the SYSTEM account. Another alternative is to run the mount
command from a Windows Scheduled Task, or a Windows Service, configured
to run as the SYSTEM account. A third alternative is to use the
[WinFsp.Launcher infrastructure](https://github.com/winfsp/winfsp/wiki/WinFsp-Service-Architecture)).
Read more in the [install documentation](https://rclone.org/install/).
Note that when running rclone as another user, it will not use
the configuration file from your profile unless you tell it to
with the [`--config`](https://rclone.org/docs/#config-string) option.
Note also that it is now the SYSTEM account that will have the owner
permissions, and other accounts will have permissions according to the
group or others scopes. As mentioned above, these will then not get the
"write extended attributes" permission, and this may prevent writing to
files. You can work around this with the FileSecurity option, see
example above.

Note that mapping to a directory path, instead of a drive letter,
does not suffer from the same limitations.

### Mounting on macOS

Mounting on macOS can be done either via [built-in NFS server](/commands/rclone_serve_nfs/),
[macFUSE](https://osxfuse.github.io/) (also known as osxfuse) or
[FUSE-T](https://www.fuse-t.org/).macFUSE is a traditional FUSE driver utilizing
a macOS kernel extension (kext). FUSE-T is an alternative FUSE system which
"mounts" via an NFSv4 local server.

#### Unicode Normalization

It is highly recommended to keep the default of `--no-unicode-normalization=false`
for all `mount` and `serve` commands on macOS. For details, see [vfs-case-sensitivity](https://rclone.org/commands/rclone_mount/#vfs-case-sensitivity).

#### NFS mount

This method spins up an NFS server using [serve nfs](/commands/rclone_serve_nfs/)
command and mounts it to the specified mountpoint. If you run this in background
mode using |--daemon|, you will need to send SIGTERM signal to the rclone process
using |kill| command to stop the mount.

Note that `--nfs-cache-handle-limit` controls the maximum number of cached file
handles stored by the `nfsmount` caching handler. This should not be set too low
or you may experience errors when trying to access files. The default is 1000000,
but consider lowering this limit if the server's system resource usage causes problems.

#### macFUSE Notes

If installing macFUSE using [dmg packages](https://github.com/osxfuse/osxfuse/releases)
from the website, rclone will locate the macFUSE libraries without any further intervention.
If however, macFUSE is installed using the [macports](https://www.macports.org/)
package manager, the following addition steps are required.

```console
sudo mkdir /usr/local/lib
cd /usr/local/lib
sudo ln -s /opt/local/lib/libfuse.2.dylib
```

#### FUSE-T Limitations, Caveats, and Notes

There are some limitations, caveats, and notes about how it works. These are
current as  of FUSE-T version 1.0.14.

##### ModTime update on read

As per the [FUSE-T wiki](https://github.com/macos-fuse-t/fuse-t/wiki#caveats):

> File access and modification times cannot be set separately as it seems to be an
> issue with the NFS client which always modifies both. Can be reproduced with
> 'touch -m' and 'touch -a' commands

This means that viewing files with various tools, notably macOS Finder, will cause
rlcone to update the modification time of the file. This may make rclone upload a
full new copy of the file.

##### Read Only mounts

When mounting with `--read-only`, attempts to write to files will fail *silently*
as opposed to with a clear warning as in macFUSE.

## Mounting on Linux

On newer versions of Ubuntu, you may encounter the following error when running
`rclone mount`:

> NOTICE: mount helper error: fusermount3: mount failed: Permission denied
> CRITICAL: Fatal error: failed to mount FUSE fs: fusermount: exit status 1
This may be due to newer [Apparmor](https://wiki.ubuntu.com/AppArmor) restrictions,
which can be disabled with `sudo aa-disable /usr/bin/fusermount3` (you may need to
`sudo apt install apparmor-utils` beforehand).

### Limitations

Without the use of `--vfs-cache-mode` this can only write files
sequentially, it can only seek when reading.  This means that many
applications won't work with their files on an rclone mount without
`--vfs-cache-mode writes` or `--vfs-cache-mode full`.
See the [VFS File Caching](#vfs-file-caching) section for more info.
When using NFS mount on macOS, if you don't specify |--vfs-cache-mode|
the mount point will be read-only.

Bucket-based remotes - Azure Blob, Swift, S3, Google Cloud Storage and B2 -
can't store empty directories. Of these, only Azure Blob, Google Cloud Storage
and S3 can preserve them when you add `--xxx-directory_markers`; otherwise,
empty directories will vanish once they drop out of the directory cache.

When `rclone mount` is invoked on Unix with `--daemon` flag, the main rclone
program will wait for the background mount to become ready or until the timeout
specified by the `--daemon-wait` flag. On Linux it can check mount status using
ProcFS so the flag in fact sets **maximum** time to wait, while the real wait
can be less. On macOS / BSD the time to wait is constant and the check is
performed only at the end. We advise you to set wait time on macOS reasonably.

Only supported on Linux, FreeBSD, OS X and Windows at the moment.

### rclone nfsmount vs rclone sync/copy

File systems expect things to be 100% reliable, whereas cloud storage
systems are a long way from 100% reliable. The rclone sync/copy
commands cope with this with lots of retries.  However rclone nfsmount
can't use retries in the same way without making local copies of the
uploads. Look at the [VFS File Caching](#vfs-file-caching)
for solutions to make nfsmount more reliable.

### Attribute caching

You can use the flag `--attr-timeout` to set the time the kernel caches
the attributes (size, modification time, etc.) for directory entries.

The default is `1s` which caches files just long enough to avoid
too many callbacks to rclone from the kernel.

In theory 0s should be the correct value for filesystems which can
change outside the control of the kernel. However this causes quite a
few problems such as
[rclone using too much memory](https://github.com/rclone/rclone/issues/2157),
[rclone not serving files to samba](https://forum.rclone.org/t/rclone-1-39-vs-1-40-mount-issue/5112)
and [excessive time listing directories](https://github.com/rclone/rclone/issues/2095#issuecomment-371141147).

The kernel can cache the info about a file for the time given by
`--attr-timeout`. You may see corruption if the remote file changes
length during this window.  It will show up as either a truncated file
or a file with garbage on the end.  With `--attr-timeout 1s` this is
very unlikely but not impossible.  The higher you set `--attr-timeout`
the more likely it is.  The default setting of "1s" is the lowest
setting which mitigates the problems above.

If you set it higher (`10s` or `1m` say) then the kernel will call
back to rclone less often making it more efficient, however there is
more chance of the corruption issue above.

If files don't change on the remote outside of the control of rclone
then there is no chance of corruption.

This is the same as setting the attr_timeout option in mount.fuse.

### Filters

Note that all the rclone filters can be used to select a subset of the
files to be visible in the mount.

### systemd

When running rclone nfsmount as a systemd service, it is possible
to use Type=notify. In this case the service will enter the started state
after the mountpoint has been successfully set up.
Units having the rclone nfsmount service specified as a requirement
will see all files and folders immediately in this mode.

Note that systemd runs mount units without any environment variables including
`PATH` or `HOME`. This means that tilde (`~`) expansion will not work
and you should provide `--config` and `--cache-dir` explicitly as absolute
paths via rclone arguments.
Since mounting requires the `fusermount` or `fusermount3` program,
rclone will use the fallback PATH of `/bin:/usr/bin` in this scenario.
Please ensure that `fusermount`/`fusermount3` is present on this PATH.

### Rclone as Unix mount helper

The core Unix program `/bin/mount` normally takes the `-t FSTYPE` argument
then runs the `/sbin/mount.FSTYPE` helper program passing it mount options
as `-o key=val,...` or `--opt=...`. Automount (classic or systemd) behaves
in a similar way.

rclone by default expects GNU-style flags `--key val`. To run it as a mount
helper you should symlink rclone binary to `/sbin/mount.rclone` and optionally
`/usr/bin/rclonefs`, e.g. `ln -s /usr/bin/rclone /sbin/mount.rclone`.
rclone will detect it and translate command-line arguments appropriately.

Now you can run classic mounts like this:

```console
mount sftp1:subdir /mnt/data -t rclone -o vfs_cache_mode=writes,sftp_key_file=/path/to/pem
```

or create systemd mount units:

```ini
# /etc/systemd/system/mnt-data.mount
[Unit]
Description=Mount for /mnt/data
[Mount]
Type=rclone
What=sftp1:subdir
Where=/mnt/data
Options=rw,_netdev,allow_other,args2env,vfs-cache-mode=writes,config=/etc/rclone.conf,cache-dir=/var/rclone
```

optionally accompanied by systemd automount unit

```ini
# /etc/systemd/system/mnt-data.automount
[Unit]
Description=AutoMount for /mnt/data
[Automount]
Where=/mnt/data
TimeoutIdleSec=600
[Install]
WantedBy=multi-user.target
```

or add in `/etc/fstab` a line like

```console
sftp1:subdir /mnt/data rclone rw,noauto,nofail,_netdev,x-systemd.automount,args2env,vfs_cache_mode=writes,config=/etc/rclone.conf,cache_dir=/var/cache/rclone 0 0
```

or use classic Automountd.
Remember to provide explicit `config=...,cache-dir=...` as a workaround for
mount units being run without `HOME`.

Rclone in the mount helper mode will split `-o` argument(s) by comma, replace `_`
by `-` and prepend `--` to get the command-line flags. Options containing commas
or spaces can be wrapped in single or double quotes. Any inner quotes inside outer
quotes of the same type should be doubled.

Mount option syntax includes a few extra options treated specially:

- `env.NAME=VALUE` will set an environment variable for the mount process.
  This helps with Automountd and Systemd.mount which don't allow setting
  custom environment for mount helpers.
  Typically you will use `env.HTTPS_PROXY=proxy.host:3128` or `env.HOME=/root`
- `command=cmount` can be used to run `cmount` or any other rclone command
  rather than the default `mount`.
- `args2env` will pass mount options to the mount helper running in background
  via environment variables instead of command line arguments. This allows to
  hide secrets from such commands as `ps` or `pgrep`.
- `vv...` will be transformed into appropriate `--verbose=N`
- standard mount options like `x-systemd.automount`, `_netdev`, `nosuid` and alike
  are intended only for Automountd and ignored by rclone.

### VFS - Virtual File System

This command uses the VFS layer. This adapts the cloud storage objects
that rclone uses into something which looks much more like a disk
filing system.

Cloud storage objects have lots of properties which aren't like disk
files - you can't extend them or write to the middle of them, so the
VFS layer has to deal with that. Because there is no one right way of
doing this there are various options explained below.

The VFS layer also implements a directory cache - this caches info
about files and directories (but not the data) in memory.

### VFS Directory Cache

Using the `--dir-cache-time` flag, you can control how long a
directory should be considered up to date and not refreshed from the
backend. Changes made through the VFS will appear immediately or
invalidate the cache.

```text
    --dir-cache-time duration   Time to cache directory entries for (default 5m0s)
    --poll-interval duration    Time to wait between polling for changes. Must be smaller than dir-cache-time. Only on supported remotes. Set to 0 to disable (default 1m0s)
```

However, changes made directly on the cloud storage by the web
interface or a different copy of rclone will only be picked up once
the directory cache expires if the backend configured does not support
polling for changes. If the backend supports polling, changes will be
picked up within the polling interval.

You can send a `SIGHUP` signal to rclone for it to flush all
directory caches, regardless of how old they are.  Assuming only one
rclone instance is running, you can reset the cache like this:

```console
kill -SIGHUP $(pidof rclone)
```

If you configure rclone with a [remote control](/rc) then you can use
rclone rc to flush the whole directory cache:

```console
rclone rc vfs/forget
```

Or individual files or directories:

```console
rclone rc vfs/forget file=path/to/file dir=path/to/dir
```

### VFS File Buffering

The `--buffer-size` flag determines the amount of memory,
that will be used to buffer data in advance.

Each open file will try to keep the specified amount of data in memory
at all times. The buffered data is bound to one open file and won't be
shared.

This flag is a upper limit for the used memory per open file.  The
buffer will only use memory for data that is downloaded but not not
yet read. If the buffer is empty, only a small amount of memory will
be used.

The maximum memory used by rclone for buffering can be up to
`--buffer-size * open files`.

### VFS File Caching

These flags control the VFS file caching options. File caching is
necessary to make the VFS layer appear compatible with a normal file
system. It can be disabled at the cost of some compatibility.

For example you'll need to enable VFS caching if you want to read and
write simultaneously to a file.  See below for more details.

Note that the VFS cache is separate from the cache backend and you may
find that you need one or the other or both.

```text
    --cache-dir string                     Directory rclone will use for caching.
    --vfs-cache-mode CacheMode             Cache mode off|minimal|writes|full (default off)
    --vfs-cache-max-age duration           Max time since last access of objects in the cache (default 1h0m0s)
    --vfs-cache-max-size SizeSuffix        Max total size of objects in the cache (default off)
    --vfs-cache-min-free-space SizeSuffix  Target minimum free space on the disk containing the cache (default off)
    --vfs-cache-poll-interval duration     Interval to poll the cache for stale objects (default 1m0s)
    --vfs-write-back duration              Time to writeback files after last use when using cache (default 5s)
```

If run with `-vv` rclone will print the location of the file cache.  The
files are stored in the user cache file area which is OS dependent but
can be controlled with `--cache-dir` or setting the appropriate
environment variable.

The cache has 4 different modes selected by `--vfs-cache-mode`.
The higher the cache mode the more compatible rclone becomes at the
cost of using disk space.

Note that files are written back to the remote only when they are
closed and if they haven't been accessed for `--vfs-write-back`
seconds. If rclone is quit or dies with files that haven't been
uploaded, these will be uploaded next time rclone is run with the same
flags.

If using `--vfs-cache-max-size` or `--vfs-cache-min-free-space` note
that the cache may exceed these quotas for two reasons. Firstly
because it is only checked every `--vfs-cache-poll-interval`. Secondly
because open files cannot be evicted from the cache. When
`--vfs-cache-max-size` or `--vfs-cache-min-free-space` is exceeded,
rclone will attempt to evict the least accessed files from the cache
first. rclone will start with files that haven't been accessed for the
longest. This cache flushing strategy is efficient and more relevant
files are likely to remain cached.

The `--vfs-cache-max-age` will evict files from the cache
after the set time since last access has passed. The default value of
1 hour will start evicting files from cache that haven't been accessed
for 1 hour. When a cached file is accessed the 1 hour timer is reset to 0
and will wait for 1 more hour before evicting. Specify the time with
standard notation, s, m, h, d, w .

You **should not** run two copies of rclone using the same VFS cache
with the same or overlapping remotes if using `--vfs-cache-mode > off`.
This can potentially cause data corruption if you do. You can work
around this by giving each rclone its own cache hierarchy with
`--cache-dir`. You don't need to worry about this if the remotes in
use don't overlap.

#### --vfs-cache-mode off

In this mode (the default) the cache will read directly from the remote and write
directly to the remote without caching anything on disk.

This will mean some operations are not possible

- Files can't be opened for both read AND write
- Files opened for write can't be seeked
- Existing files opened for write must have O_TRUNC set
- Files open for read with O_TRUNC will be opened write only
- Files open for write only will behave as if O_TRUNC was supplied
- Open modes O_APPEND, O_TRUNC are ignored
- If an upload fails it can't be retried

#### --vfs-cache-mode minimal

This is very similar to "off" except that files opened for read AND
write will be buffered to disk.  This means that files opened for
write will be a lot more compatible, but uses the minimal disk space.

These operations are not possible

- Files opened for write only can't be seeked
- Existing files opened for write must have O_TRUNC set
- Files opened for write only will ignore O_APPEND, O_TRUNC
- If an upload fails it can't be retried

#### --vfs-cache-mode writes

In this mode files opened for read only are still read directly from
the remote, write only and read/write files are buffered to disk
first.

This mode should support all normal file system operations.

If an upload fails it will be retried at exponentially increasing
intervals up to 1 minute.

#### --vfs-cache-mode full

In this mode all reads and writes are buffered to and from disk. When
data is read from the remote this is buffered to disk as well.

In this mode the files in the cache will be sparse files and rclone
will keep track of which bits of the files it has downloaded.

So if an application only reads the starts of each file, then rclone
will only buffer the start of the file. These files will appear to be
their full size in the cache, but they will be sparse files with only
the data that has been downloaded present in them.

This mode should support all normal file system operations and is
otherwise identical to `--vfs-cache-mode` writes.

When reading a file rclone will read `--buffer-size` plus
`--vfs-read-ahead` bytes ahead.  The `--buffer-size` is buffered in memory
whereas the `--vfs-read-ahead` is buffered on disk.

When using this mode it is recommended that `--buffer-size` is not set
too large and `--vfs-read-ahead` is set large if required.

**IMPORTANT** not all file systems support sparse files. In particular
FAT/exFAT do not. Rclone will perform very badly if the cache
directory is on a filesystem which doesn't support sparse files and it
will log an ERROR message if one is detected.

#### Fingerprinting

Various parts of the VFS use fingerprinting to see if a local file
copy has changed relative to a remote file. Fingerprints are made
from:

- size
- modification time
- hash

where available on an object.

On some backends some of these attributes are slow to read (they take
an extra API call per object, or extra work per object).

For example `hash` is slow with the `local` and `sftp` backends as
they have to read the entire file and hash it, and `modtime` is slow
with the `s3`, `swift`, `ftp` and `qinqstor` backends because they
need to do an extra API call to fetch it.

If you use the `--vfs-fast-fingerprint` flag then rclone will not
include the slow operations in the fingerprint. This makes the
fingerprinting less accurate but much faster and will improve the
opening time of cached files.

If you are running a vfs cache over `local`, `s3` or `swift` backends
then using this flag is recommended.

Note that if you change the value of this flag, the fingerprints of
the files in the cache may be invalidated and the files will need to
be downloaded again.

### VFS Chunked Reading

When rclone reads files from a remote it reads them in chunks. This
means that rather than requesting the whole file rclone reads the
chunk specified.  This can reduce the used download quota for some
remotes by requesting only chunks from the remote that are actually
read, at the cost of an increased number of requests.

These flags control the chunking:

```text
    --vfs-read-chunk-size SizeSuffix        Read the source objects in chunks (default 128M)
    --vfs-read-chunk-size-limit SizeSuffix  Max chunk doubling size (default off)
    --vfs-read-chunk-streams int            The number of parallel streams to read at once
```

The chunking behaves differently depending on the `--vfs-read-chunk-streams` parameter.

#### `--vfs-read-chunk-streams` == 0

Rclone will start reading a chunk of size `--vfs-read-chunk-size`,
and then double the size for each read. When `--vfs-read-chunk-size-limit` is
specified, and greater than `--vfs-read-chunk-size`, the chunk size for each
open file will get doubled only until the specified value is reached. If the
value is "off", which is the default, the limit is disabled and the chunk size
will grow indefinitely.

With `--vfs-read-chunk-size 100M` and `--vfs-read-chunk-size-limit 0`
the following parts will be downloaded: 0-100M, 100M-200M, 200M-300M, 300M-400M
and so on. When `--vfs-read-chunk-size-limit 500M` is specified, the result would
be 0-100M, 100M-300M, 300M-700M, 700M-1200M, 1200M-1700M and so on.

Setting `--vfs-read-chunk-size` to `0` or "off" disables chunked reading.

The chunks will not be buffered in memory.

#### `--vfs-read-chunk-streams` > 0

Rclone reads `--vfs-read-chunk-streams` chunks of size
`--vfs-read-chunk-size` concurrently. The size for each read will stay
constant.

This improves performance performance massively on high latency links
or very high bandwidth links to high performance object stores.

Some experimentation will be needed to find the optimum values of
`--vfs-read-chunk-size` and `--vfs-read-chunk-streams` as these will
depend on the backend in use and the latency to the backend.

For high performance object stores (eg AWS S3) a reasonable place to
start might be `--vfs-read-chunk-streams 16` and
`--vfs-read-chunk-size 4M`. In testing with AWS S3 the performance
scaled roughly as the `--vfs-read-chunk-streams` setting.

Similar settings should work for high latency links, but depending on
the latency they may need more `--vfs-read-chunk-streams` in order to
get the throughput.

### VFS Performance

These flags may be used to enable/disable features of the VFS for
performance or other reasons. See also the [chunked reading](#vfs-chunked-reading)
feature.

In particular S3 and Swift benefit hugely from the `--no-modtime` flag
(or use `--use-server-modtime` for a slightly different effect) as each
read of the modification time takes a transaction.

```text
    --no-checksum     Don't compare checksums on up/download.
    --no-modtime      Don't read/write the modification time (can speed things up).
    --no-seek         Don't allow seeking in files.
    --read-only       Only allow read-only access.
```

Sometimes rclone is delivered reads or writes out of order. Rather
than seeking rclone will wait a short time for the in sequence read or
write to come in. These flags only come into effect when not using an
on disk cache file.

```text
    --vfs-read-wait duration   Time to wait for in-sequence read before seeking (default 20ms)
    --vfs-write-wait duration  Time to wait for in-sequence write before giving error (default 1s)
```

When using VFS write caching (`--vfs-cache-mode` with value writes or full),
the global flag `--transfers` can be set to adjust the number of parallel uploads
of modified files from the cache (the related global flag `--checkers` has no
effect on the VFS).

```text
    --transfers int  Number of file transfers to run in parallel (default 4)
```

### Symlinks

By default the VFS does not support symlinks. However this may be
enabled with either of the following flags:

```text
    --links      Translate symlinks to/from regular files with a '.rclonelink' extension.
    --vfs-links  Translate symlinks to/from regular files with a '.rclonelink' extension for the VFS
```

As most cloud storage systems do not support symlinks directly, rclone
stores the symlink as a normal file with a special extension. So a
file which appears as a symlink `link-to-file.txt` would be stored on
cloud storage as `link-to-file.txt.rclonelink` and the contents would
be the path to the symlink destination.

Note that `--links` enables symlink translation globally in rclone -
this includes any backend which supports the concept (for example the
local backend). `--vfs-links` just enables it for the VFS layer.

This scheme is compatible with that used by the
[local backend with the --local-links flag](/local/#symlinks-junction-points).

The `--vfs-links` flag has been designed for `rclone mount`, `rclone
nfsmount` and `rclone serve nfs`.

It hasn't been tested with the other `rclone serve` commands yet.

A limitation of the current implementation is that it expects the
caller to resolve sub-symlinks. For example given this directory tree

```text
.
├── dir
│   └── file.txt
└── linked-dir -> dir
```

The VFS will correctly resolve `linked-dir` but not
`linked-dir/file.txt`. This is not a problem for the tested commands
but may be for other commands.

**Note** that there is an outstanding issue with symlink support
[issue #8245](https://github.com/rclone/rclone/issues/8245) with duplicate
files being created when symlinks are moved into directories where
there is a file of the same name (or vice versa).

### VFS Case Sensitivity

Linux file systems are case-sensitive: two files can differ only
by case, and the exact case must be used when opening a file.

File systems in modern Windows are case-insensitive but case-preserving:
although existing files can be opened using any case, the exact case used
to create the file is preserved and available for programs to query.
It is not allowed for two files in the same directory to differ only by case.

Usually file systems on macOS are case-insensitive. It is possible to make macOS
file systems case-sensitive but that is not the default.

The `--vfs-case-insensitive` VFS flag controls how rclone handles these
two cases. If its value is "false", rclone passes file names to the remote
as-is. If the flag is "true" (or appears without a value on the
command line), rclone may perform a "fixup" as explained below.

The user may specify a file name to open/delete/rename/etc with a case
different than what is stored on the remote. If an argument refers
to an existing file with exactly the same name, then the case of the existing
file on the disk will be used. However, if a file name with exactly the same
name is not found but a name differing only by case exists, rclone will
transparently fixup the name. This fixup happens only when an existing file
is requested. Case sensitivity of file names created anew by rclone is
controlled by the underlying remote.

Note that case sensitivity of the operating system running rclone (the target)
may differ from case sensitivity of a file system presented by rclone (the source).
The flag controls whether "fixup" is performed to satisfy the target.

If the flag is not provided on the command line, then its default value depends
on the operating system where rclone runs: "true" on Windows and macOS, "false"
otherwise. If the flag is provided without a value, then it is "true".

The `--no-unicode-normalization` flag controls whether a similar "fixup" is
performed for filenames that differ but are [canonically
equivalent](https://en.wikipedia.org/wiki/Unicode_equivalence) with respect to
unicode. Unicode normalization can be particularly helpful for users of macOS,
which prefers form NFD instead of the NFC used by most other platforms. It is
therefore highly recommended to keep the default of `false` on macOS, to avoid
encoding compatibility issues.

In the (probably unlikely) event that a directory has multiple duplicate
filenames after applying case and unicode normalization, the `--vfs-block-norm-dupes`
flag allows hiding these duplicates. This comes with a performance tradeoff, as
rclone will have to scan the entire directory for duplicates when listing a
directory. For this reason, it is recommended to leave this disabled if not
needed. However, macOS users may wish to consider using it, as otherwise, if a
remote directory contains both NFC and NFD versions of the same filename, an odd
situation will occur: both versions of the file will be visible in the mount,
and both will appear to be editable, however, editing either version will
actually result in only the NFD version getting edited under the hood. `--vfs-block-
norm-dupes` prevents this confusion by detecting this scenario, hiding the
duplicates, and logging an error, similar to how this is handled in `rclone
sync`.

### VFS Disk Options

This flag allows you to manually set the statistics about the filing system.
It can be useful when those statistics cannot be read correctly automatically.

```text
    --vfs-disk-space-total-size    Manually set the total disk space size (example: 256G, default: -1)
```

### Alternate report of used bytes

Some backends, most notably S3, do not report the amount of bytes used.
If you need this information to be available when running `df` on the
filesystem, then pass the flag `--vfs-used-is-size` to rclone.
With this flag set, instead of relying on the backend to report this
information, rclone will scan the whole remote similar to `rclone size`
and compute the total used space itself.

**WARNING**: Contrary to `rclone size`, this flag ignores filters so that the
result is accurate. However, this is very inefficient and may cost lots of API
calls resulting in extra charges. Use it as a last resort and only with caching.

### VFS Metadata

If you use the `--vfs-metadata-extension` flag you can get the VFS to
expose files which contain the [metadata](/docs/#metadata) as a JSON
blob. These files will not appear in the directory listing, but can be
`stat`-ed and opened and once they have been they **will** appear in
directory listings until the directory cache expires.

Note that some backends won't create metadata unless you pass in the
`--metadata` flag.

For example, using `rclone mount` with `--metadata --vfs-metadata-extension .metadata`
we get

```console
$ ls -l /mnt/
total 1048577
-rw-rw-r-- 1 user user 1073741824 Mar  3 16:03 1G

$ cat /mnt/1G.metadata
{
        "atime": "2025-03-04T17:34:22.317069787Z",
        "btime": "2025-03-03T16:03:37.708253808Z",
        "gid": "1000",
        "mode": "100664",
        "mtime": "2025-03-03T16:03:39.640238323Z",
        "uid": "1000"
}

$ ls -l /mnt/
total 1048578
-rw-rw-r-- 1 user user 1073741824 Mar  3 16:03 1G
-rw-rw-r-- 1 user user        185 Mar  3 16:03 1G.metadata
```

If the file has no metadata it will be returned as `{}` and if there
is an error reading the metadata the error will be returned as
`{"error":"error string"}`.

Usage:
  rclone nfsmount remote:path /path/to/mountpoint [flags]

Flags:
      --addr string                            IPaddress:Port or :Port to bind server to
      --allow-non-empty                        Allow mounting over a non-empty directory (not supported on Windows)
      --allow-other                            Allow access to other users (not supported on Windows)
      --allow-root                             Allow access to root user (not supported on Windows)
      --async-read                             Use asynchronous reads (not supported on Windows) (default true)
      --attr-timeout Duration                  Time for which file/directory attributes are cached (default 1s)
      --daemon                                 Run mount in background and exit parent process (as background output is suppressed, use --log-file with --log-format=pid,... to monitor) (not supported on Windows)
      --daemon-timeout Duration                Time limit for rclone to respond to kernel (not supported on Windows) (default 0s)
      --daemon-wait Duration                   Time to wait for ready mount from daemon (maximum time on Linux, constant sleep time on OSX/BSD) (not supported on Windows) (default 1m0s)
      --debug-fuse                             Debug the FUSE internals - needs -v
      --default-permissions                    Makes kernel enforce access control based on the file mode (not supported on Windows)
      --devname string                         Set the device name - default is remote:path
      --dir-cache-time Duration                Time to cache directory entries for (default 5m0s)
      --dir-perms FileMode                     Directory permissions (default 777)
      --direct-io                              Use Direct IO, disables caching of data
      --file-perms FileMode                    File permissions (default 666)
      --fuse-flag stringArray                  Flags or arguments to be passed direct to libfuse/WinFsp (repeat if required)
      --gid uint32                             Override the gid field set by the filesystem (not supported on Windows)
  -h, --help                                   help for nfsmount
      --link-perms FileMode                    Link permissions (default 666)
      --max-read-ahead SizeSuffix              The number of bytes that can be prefetched for sequential reads (not supported on Windows) (default 128Ki)
      --mount-case-insensitive Tristate        Tell the OS the mount is case insensitive (true) or sensitive (false) regardless of the backend (auto) (default unset)
      --network-mode                           Mount as remote network drive, instead of fixed disk drive (supported on Windows only)
      --nfs-cache-dir string                   The directory the NFS handle cache will use if set
      --nfs-cache-handle-limit int             max file handles cached simultaneously (min 5) (default 1000000)
      --nfs-cache-type memory|disk|symlink     Type of NFS handle cache to use (default memory)
      --no-checksum                            Don't compare checksums on up/download
      --no-modtime                             Don't read/write the modification time (can speed things up)
      --no-seek                                Don't allow seeking in files
      --noappledouble                          Ignore Apple Double (._) and .DS_Store files (supported on OSX only) (default true)
      --noapplexattr                           Ignore all "com.apple.*" extended attributes (supported on OSX only)
  -o, --option stringArray                     Option for libfuse/WinFsp (repeat if required)
      --poll-interval Duration                 Time to wait between polling for changes, must be smaller than dir-cache-time and only on supported remotes (set 0 to disable) (default 1m0s)
      --read-only                              Only allow read-only access
      --sudo                                   Use sudo to run the mount/umount commands as root.
      --uid uint32                             Override the uid field set by the filesystem (not supported on Windows)
      --umask FileMode                         Override the permission bits set by the filesystem (not supported on Windows) (default 002)
      --vfs-block-norm-dupes                   If duplicate filenames exist in the same directory (after normalization), log an error and hide the duplicates (may have a performance cost)
      --vfs-cache-max-age Duration             Max time since last access of objects in the cache (default 1h0m0s)
      --vfs-cache-max-size SizeSuffix          Max total size of objects in the cache (default off)
      --vfs-cache-min-free-space SizeSuffix    Target minimum free space on the disk containing the cache (default off)
      --vfs-cache-mode CacheMode               Cache mode off|minimal|writes|full (default off)
      --vfs-cache-poll-interval Duration       Interval to poll the cache for stale objects (default 1m0s)
      --vfs-case-insensitive                   If a file name not found, find a case insensitive match
      --vfs-disk-space-total-size SizeSuffix   Specify the total space of disk (default off)
      --vfs-fast-fingerprint                   Use fast (less accurate) fingerprints for change detection
      --vfs-links                              Translate symlinks to/from regular files with a '.rclonelink' extension for the VFS
      --vfs-metadata-extension string          Set the extension to read metadata from
      --vfs-read-ahead SizeSuffix              Extra read ahead over --buffer-size when using cache-mode full
      --vfs-read-chunk-size SizeSuffix         Read the source objects in chunks (default 128Mi)
      --vfs-read-chunk-size-limit SizeSuffix   If greater than --vfs-read-chunk-size, double the chunk size after each chunk read, until the limit is reached ('off' is unlimited) (default off)
      --vfs-read-chunk-streams int             The number of parallel streams to read at once
      --vfs-read-wait Duration                 Time to wait for in-sequence read before seeking (default 20ms)
      --vfs-refresh                            Refreshes the directory cache recursively in the background on start
      --vfs-used-is-size rclone size           Use the rclone size algorithm for Used size
      --vfs-write-back Duration                Time to writeback files after last use when using cache (default 5s)
      --vfs-write-wait Duration                Time to wait for in-sequence write before giving error (default 1s)
      --volname string                         Set the volume name (supported on Windows and OSX only)
      --write-back-cache                       Makes kernel buffer writes before sending them to rclone (without this, writethrough caching is used) (not supported on Windows)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `obscure`

````
In the rclone config file, human-readable passwords are
obscured. Obscuring them is done by encrypting them and writing them
out in base64. This is **not** a secure way of encrypting these
passwords as rclone can decrypt them - it is to prevent "eyedropping" -
namely someone seeing a password in the rclone config file by accident.

Many equally important things (like access tokens) are not obscured in
the config file. However it is very hard to shoulder surf a 64
character hex token.

This command can also accept a password through STDIN instead of an
argument by passing a hyphen as an argument. This will use the first
line of STDIN as the password not including the trailing newline.

```console
echo 'secretpassword' | rclone obscure -
```

If there is no data on STDIN to read, rclone obscure will default to
obfuscating the hyphen itself.

If you want to encrypt the config file then please use config file
encryption - see [rclone config](/commands/rclone_config/) for more
info.

Usage:
  rclone obscure password [flags]

Flags:
  -h, --help   help for obscure

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `purge`

````
Remove the path and all of its contents.  Note that this does not obey
include/exclude filters - everything will be removed.  Use the
[delete](/commands/rclone_delete/) command if you want to selectively
delete files. To delete empty directories only, use command
[rmdir](/commands/rclone_rmdir/) or [rmdirs](/commands/rclone_rmdirs/).

The concurrency of this operation is controlled by the `--checkers` global flag.
However, some backends will implement this command directly, in which
case `--checkers` will be ignored.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`-i` flag.

Usage:
  rclone purge remote:path [flags]

Flags:
  -h, --help   help for purge

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `rc`

````
This runs a command against a running rclone.  Use the `--url` flag to
specify an non default URL to connect on.  This can be either a
":port" which is taken to mean <http://localhost:port> or a
"host:port" which is taken to mean <http://host:port>.

A username and password can be passed in with `--user` and `--pass`.

Note that `--rc-addr`, `--rc-user`, `--rc-pass` will be read also for
`--url`, `--user`, `--pass`.

The `--unix-socket` flag can be used to connect over a unix socket like this

```sh
# start server on /tmp/my.socket
rclone rcd --rc-addr unix:///tmp/my.socket
# Connect to it
rclone rc --unix-socket /tmp/my.socket core/stats
```

Arguments should be passed in as parameter=value.

The result will be returned as a JSON object by default.

The `--json` parameter can be used to pass in a JSON blob as an input
instead of key=value arguments.  This is the only way of passing in
more complicated values.

The `-o`/`--opt` option can be used to set a key "opt" with key, value
options in the form `-o key=value` or `-o key`. It can be repeated as
many times as required. This is useful for rc commands which take the
"opt" parameter which by convention is a dictionary of strings.

```text
-o key=value -o key2
```

Will place this in the "opt" value

```json
{"key":"value", "key2","")
```

The `-a`/`--arg` option can be used to set strings in the "arg" value. It
can be repeated as many times as required. This is useful for rc
commands which take the "arg" parameter which by convention is a list
of strings.

```text
-a value -a value2
```

Will place this in the "arg" value

```json
["value", "value2"]
```

Use `--loopback` to connect to the rclone instance running `rclone rc`.
This is very useful for testing commands without having to run an
rclone rc server, e.g.:

```sh
rclone rc --loopback operations/about fs=/
```

Use `rclone rc` to see a list of all possible commands.

Usage:
  rclone rc commands parameter [flags]

Flags:
  -a, --arg stringArray      Argument placed in the "arg" array
  -h, --help                 help for rc
      --json string          Input JSON - use instead of key=value args
      --loopback             If set connect to this rclone instance not via HTTP
      --no-output            If set, don't output the JSON result
  -o, --opt stringArray      Option in the form name=value or name placed in the "opt" array
      --pass string          Password to use to connect to rclone remote control
      --unix-socket string   Path to a unix domain socket to dial to, instead of opening a TCP connection directly
      --url string           URL to connect to rclone remote control (default "http://localhost:5572/")
      --user string          Username to use to rclone remote control

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `rcat`

````
Reads from standard input (stdin) and copies it to a single remote file.

```console
echo "hello world" | rclone rcat remote:path/to/file
ffmpeg - | rclone rcat remote:path/to/file
```

If the remote file already exists, it will be overwritten.

rcat will try to upload small files in a single request, which is
usually more efficient than the streaming/chunked upload endpoints,
which use multiple requests. Exact behaviour depends on the remote.
What is considered a small file may be set through
`--streaming-upload-cutoff`. Uploading only starts after
the cutoff is reached or if the file ends before that. The data
must fit into RAM. The cutoff needs to be small enough to adhere
the limits of your remote, please see there. Generally speaking,
setting this cutoff too high will decrease your performance.

Use the `--size` flag to preallocate the file in advance at the remote end
and actually stream it, even if remote backend doesn't support streaming.

`--size` should be the exact size of the input stream in bytes. If the
size of the stream is different in length to the `--size` passed in
then the transfer will likely fail.

Note that the upload cannot be retried because the data is not stored.
If the backend supports multipart uploading then individual chunks can
be retried. If you need to transfer a lot of data, you may be better
off caching it locally and then `rclone move` it to the
destination which can use retries.

Usage:
  rclone rcat remote:path [flags]

Flags:
  -h, --help       help for rcat
      --size int   File size hint to preallocate (default -1)

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `rcd`

````
This runs rclone so that it only listens to remote control commands.

This is useful if you are controlling rclone via the rc API.

If you pass in a path to a directory, rclone will serve that directory
for GET requests on the URL passed in.  It will also open the URL in
the browser when rclone is run.

See the [rc documentation](/rc/) for more info on the rc flags.

### Server options

Use `--rc-addr` to specify which IP address and port the server should
listen on, eg `--rc-addr 1.2.3.4:8000` or `--rc-addr :8080` to listen to all
IPs.  By default it only listens on localhost.  You can use port
:0 to let the OS choose an available port.

If you set `--rc-addr` to listen on a public or LAN accessible IP address
then using Authentication is advised - see the next section for info.

You can use a unix socket by setting the url to `unix:///path/to/socket`
or just by using an absolute path name.

`--rc-addr` may be repeated to listen on multiple IPs/ports/sockets.
Socket activation, described further below, can also be used to accomplish the same.

`--rc-server-read-timeout` and `--rc-server-write-timeout` can be used to
control the timeouts on the server.  Note that this is the total time
for a transfer.

`--rc-max-header-bytes` controls the maximum number of bytes the server will
accept in the HTTP header.

`--rc-baseurl` controls the URL prefix that rclone serves from.  By default
rclone will serve from the root.  If you used `--rc-baseurl "/rclone"` then
rclone would serve from a URL starting with "/rclone/".  This is
useful if you wish to proxy rclone serve.  Rclone automatically
inserts leading and trailing "/" on `--rc-baseurl`, so `--rc-baseurl "rclone"`,
`--rc-baseurl "/rclone"` and `--rc-baseurl "/rclone/"` are all treated
identically.

`--rc-disable-zip` may be set to disable the zipping download option.

#### TLS (SSL)

By default this will serve over http.  If you want you can serve over
https.  You will need to supply the `--rc-cert` and `--rc-key` flags.
If you wish to do client side certificate validation then you will need to
supply `--rc-client-ca` also.

`--rc-cert` must be set to the path of a file containing
either a PEM encoded certificate, or a concatenation of that with the CA
certificate. `--rc-key` must be set to the path of a file
with the PEM encoded private key. If setting `--rc-client-ca`,
it should be set to the path of a file with PEM encoded client certificate
authority certificates.

`--rc-min-tls-version` is minimum TLS version that is acceptable. Valid
values are "tls1.0", "tls1.1", "tls1.2" and "tls1.3" (default "tls1.0").

### Socket activation

Instead of the listening addresses specified above, rclone will listen to all
FDs passed by the service manager, if any (and ignore any arguments passed
by `--rc-addr`).

This allows rclone to be a socket-activated service.
It can be configured with .socket and .service unit files as described in
<https://www.freedesktop.org/software/systemd/man/latest/systemd.socket.html>.

Socket activation can be tested ad-hoc with the `systemd-socket-activate`command

```console
systemd-socket-activate -l 8000 -- rclone serve
```

This will socket-activate rclone on the first connection to port 8000 over TCP.

#### Template

`--rc-template` allows a user to specify a custom markup template for HTTP
and WebDAV serve functions.  The server exports the following markup
to be used within the template to server pages:

| Parameter   | Subparameter | Description |
| :---------- | :----------- | :---------- |
| .Name       |              | The full path of a file/directory. |
| .Title      |              | Directory listing of '.Name'. |
| .Sort       |              | The current sort used. This is changeable via '?sort=' parameter. Possible values: namedirfirst, name, size, time (default namedirfirst). |
| .Order      |              | The current ordering used. This is changeable via '?order=' parameter. Possible values: asc, desc (default asc). |
| .Query      |              | Currently unused. |
| .Breadcrumb |              | Allows for creating a relative navigation. |
|             | .Link        | The link of the Text relative to the root. |
|             | .Text        | The Name of the directory. |
| .Entries    |              | Information about a specific file/directory. |
|             | .URL         | The url of an entry. |
|             | .Leaf        | Currently same as '.URL' but intended to be just the name. |
|             | .IsDir       | Boolean for if an entry is a directory or not. |
|             | .Size        | Size in bytes of the entry. |
|             | .ModTime     | The UTC timestamp of an entry. |

The server also makes the following functions available so that they can be used
within the template. These functions help extend the options for dynamic
rendering of HTML. They can be used to render HTML based on specific conditions.

| Function   | Description |
| :---------- | :---------- |
| afterEpoch  | Returns the time since the epoch for the given time. |
| contains    | Checks whether a given substring is present or not in a given string. |
| hasPrefix   | Checks whether the given string begins with the specified prefix. |
| hasSuffix   | Checks whether the given string end with the specified suffix. |

#### Authentication

By default this will serve files without needing a login.

You can either use an htpasswd file which can take lots of users, or
set a single username and password with the `--rc-user` and `--rc-pass` flags.

Alternatively, you can have the reverse proxy manage authentication and use the
username provided in the configured header with `--user-from-header`  (e.g., `--rc-user-from-header=x-remote-user`).
Ensure the proxy is trusted and headers cannot be spoofed, as misconfiguration
may lead to unauthorized access.

If either of the above authentication methods is not configured and client
certificates are required by the `--client-ca` flag passed to the server, the
client certificate common name will be considered as the username.

Use `--rc-htpasswd /path/to/htpasswd` to provide an htpasswd file.  This is
in standard apache format and supports MD5, SHA1 and BCrypt for basic
authentication.  Bcrypt is recommended.

To create an htpasswd file:

```console
touch htpasswd
htpasswd -B htpasswd user
htpasswd -B htpasswd anotherUser
```

The password file can be updated while rclone is running.

Use `--rc-realm` to set the authentication realm.

Use `--rc-salt` to change the password hashing salt from the default.

Usage:
  rclone rcd <path to files to serve>* [flags]

Flags:
  -h, --help   help for rcd

Flags to control the Remote Control API (flag group RC):
      --rc                                 Enable the remote control server
      --rc-addr stringArray                IPaddress:Port or :Port to bind server to (default localhost:5572)
      --rc-allow-origin string             Origin which cross-domain request (CORS) can be executed from
      --rc-baseurl string                  Prefix for URLs - leave blank for root
      --rc-cert string                     TLS PEM key (concatenation of certificate and CA certificate)
      --rc-client-ca string                Client certificate authority to verify clients with
      --rc-enable-metrics                  Enable the Prometheus metrics path at the remote control server
      --rc-files string                    Path to local files to serve on the HTTP server
      --rc-htpasswd string                 A htpasswd file - if not provided no authentication is done
      --rc-job-expire-duration Duration    Expire finished async jobs older than this value (default 1m0s)
      --rc-job-expire-interval Duration    Interval to check for expired async jobs (default 10s)
      --rc-key string                      TLS PEM Private key
      --rc-max-header-bytes int            Maximum size of request header (default 4096)
      --rc-min-tls-version string          Minimum TLS version that is acceptable (default "tls1.0")
      --rc-no-auth                         Don't require auth for certain methods
      --rc-pass string                     Password for authentication
      --rc-realm string                    Realm for authentication
      --rc-salt string                     Password hashing salt (default "dlPL2MqE")
      --rc-serve                           Enable the serving of remote objects
      --rc-serve-no-modtime                Don't read the modification time (can speed things up)
      --rc-server-read-timeout Duration    Timeout for server reading data (default 1h0m0s)
      --rc-server-write-timeout Duration   Timeout for server writing data (default 1h0m0s)
      --rc-template string                 User-specified template
      --rc-user string                     User name for authentication
      --rc-user-from-header string         User name from a defined HTTP header
      --rc-web-fetch-url string            URL to fetch the releases for webgui (default "https://api.github.com/repos/rclone/rclone-webui-react/releases/latest")
      --rc-web-gui                         Launch WebGUI on localhost
      --rc-web-gui-force-update            Force update to latest version of web gui
      --rc-web-gui-no-open-browser         Don't open the browser automatically
      --rc-web-gui-update                  Check and update to latest version of web gui

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `rmdir`

````
This removes empty directory given by path. Will not remove the path if it
has any objects in it, not even empty subdirectories. Use
command [rmdirs](/commands/rclone_rmdirs/) (or [delete](/commands/rclone_delete/)
with option `--rmdirs`) to do that.

To delete a path and any objects in it, use [purge](/commands/rclone_purge/) command.

Usage:
  rclone rmdir remote:path [flags]

Flags:
  -h, --help   help for rmdir

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `rmdirs`

````
This recursively removes any empty directories (including directories
that only contain empty directories), that it finds under the path.
The root path itself will also be removed if it is empty, unless
you supply the `--leave-root` flag.

Use command [rmdir](/commands/rclone_rmdir/) to delete just the empty
directory given by path, not recurse.

This is useful for tidying up remotes that rclone has left a lot of
empty directories in. For example the [delete](/commands/rclone_delete/)
command will delete files but leave the directory structure (unless
used with option `--rmdirs`).

This will delete `--checkers` directories concurrently so
if you have thousands of empty directories consider increasing this number.

To delete a path and any objects in it, use the [purge](/commands/rclone_purge/)
command.

Usage:
  rclone rmdirs remote:path [flags]

Flags:
  -h, --help         help for rmdirs
      --leave-root   Do not remove root directory if empty

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `selfupdate`

````
This command downloads the latest release of rclone and replaces the
currently running binary. The download is verified with a hashsum and
cryptographically signed signature; see [the release signing
docs](/release_signing/) for details.

If used without flags (or with implied `--stable` flag), this command
will install the latest stable release. However, some issues may be fixed
(or features added) only in the latest beta release. In such cases you should
run the command with the `--beta` flag, i.e. `rclone selfupdate --beta`.
You can check in advance what version would be installed by adding the
`--check` flag, then repeat the command without it when you are satisfied.

Sometimes the rclone team may recommend you a concrete beta or stable
rclone release to troubleshoot your issue or add a bleeding edge feature.
The `--version VER` flag, if given, will update to the concrete version
instead of the latest one. If you omit micro version from `VER` (for
example `1.53`), the latest matching micro version will be used.

Upon successful update rclone will print a message that contains a previous
version number. You will need it if you later decide to revert your update
for some reason. Then you'll have to note the previous version and run the
following command: `rclone selfupdate [--beta] OLDVER`.
If the old version contains only dots and digits (for example `v1.54.0`)
then it's a stable release so you won't need the `--beta` flag. Beta releases
have an additional information similar to `v1.54.0-beta.5111.06f1c0c61`.
(if you are a developer and use a locally built rclone, the version number
will end with `-DEV`, you will have to rebuild it as it obviously can't
be distributed).

If you previously installed rclone via a package manager, the package may
include local documentation or configure services. You may wish to update
with the flag `--package deb` or `--package rpm` (whichever is correct for
your OS) to update these too. This command with the default `--package zip`
will update only the rclone executable so the local manual may become
inaccurate after it.

The [rclone mount](/commands/rclone_mount/) command may
or may not support extended FUSE options depending on the build and OS.
`selfupdate` will refuse to update if the capability would be discarded.

Note: Windows forbids deletion of a currently running executable so this
command will rename the old executable to 'rclone.old.exe' upon success.

Please note that this command was not available before rclone version 1.55.
If it fails for you with the message `unknown command "selfupdate"` then
you will need to update manually following the
[install documentation](https://rclone.org/install/).

Usage:
  rclone selfupdate [flags]

Aliases:
  selfupdate, self-update

Flags:
      --beta             Install beta release
      --check            Check for latest release, do not download
  -h, --help             help for selfupdate
      --output string    Save the downloaded binary at a given path (default: replace running binary)
      --package string   Package format: zip|deb|rpm (default: zip)
      --stable           Install stable release (this is the default)
      --version string   Install the given rclone version (default: latest)

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `serve`

````
Serve a remote over a given protocol. Requires the use of a
subcommand to specify the protocol, e.g.

```console
rclone serve http remote:
```

When the "--metadata" flag is enabled, the following metadata fields will be provided as headers:
- "content-disposition"
- "cache-control" 
- "content-language"
- "content-encoding"
Note: The availability of these fields depends on whether the remote supports metadata.

Each subcommand has its own options which you can see in their help.

Usage:
  rclone serve <protocol> [opts] <remote> [flags]
  rclone serve [command]

Available commands:
  dlna        Serve remote:path over DLNA
  docker      Serve any remote on docker's volume plugin API.
  ftp         Serve remote:path over FTP.
  http        Serve the remote over HTTP.
  nfs         Serve the remote as an NFS mount
  restic      Serve the remote for restic's REST API.
  s3          Serve remote:path over s3.
  sftp        Serve the remote over SFTP.
  webdav      Serve remote:path over WebDAV.

Flags:
  -h, --help   help for serve

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `settier`

````
Changes storage tier or class at remote if supported. Few cloud storage
services provides different storage classes on objects, for example
AWS S3 and Glacier, Azure Blob storage - Hot, Cool and Archive,
Google Cloud Storage, Regional Storage, Nearline, Coldline etc.

Note that, certain tier changes make objects not available to access immediately.
For example tiering to archive in azure blob storage makes objects in frozen state,
user can restore by setting tier to Hot/Cool, similarly S3 to Glacier makes object
inaccessible.true

You can use it to tier single object

```console
rclone settier Cool remote:path/file
```

Or use rclone filters to set tier on only specific files

```console
rclone --include "*.txt" settier Hot remote:path/dir
```

Or just provide remote directory and all files in directory will be tiered

```console
rclone settier tier remote:path/dir
```

Usage:
  rclone settier tier remote:path [flags]

Flags:
  -h, --help   help for settier

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `sha1sum`

````
Produces an sha1sum file for all the objects in the path.  This
is in the same format as the standard sha1sum tool produces.

By default, the hash is requested from the remote.  If SHA-1 is
not supported by the remote, no hash will be returned.  With the
download flag, the file will be downloaded from the remote and
hashed locally enabling SHA-1 for any remote.

For other algorithms, see the [hashsum](/commands/rclone_hashsum/)
command. Running `rclone sha1sum remote:path` is equivalent
to running `rclone hashsum SHA1 remote:path`.

This command can also hash data received on standard input (stdin),
by not passing a remote:path, or by passing a hyphen as remote:path
when there is data to read (if not, the hyphen will be treated literally,
as a relative path).

This command can also hash data received on STDIN, if not passing
a remote:path.

Usage:
  rclone sha1sum remote:path [flags]

Flags:
      --base64               Output base64 encoded hashsum
  -C, --checkfile string     Validate hashes against a given SUM file instead of printing them
      --download             Download the file and hash it locally; if this flag is not specified, the hash is requested from the remote
  -h, --help                 help for sha1sum
      --output-file string   Output hashsums to a file rather than the terminal

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `size`

````
Counts objects in the path and calculates the total size. Prints the
result to standard output.

By default the output is in human-readable format, but shows values in
both human-readable format as well as the raw numbers (global option
`--human-readable` is not considered). Use option `--json`
to format output as JSON instead.

Recurses by default, use `--max-depth 1` to stop the
recursion.

Some backends do not always provide file sizes, see for example
[Google Photos](/googlephotos/#size) and
[Google Docs](/drive/#limitations-of-google-docs).
Rclone will then show a notice in the log indicating how many such
files were encountered, and count them in as empty files in the output
of the size command.

Usage:
  rclone size remote:path [flags]

Flags:
  -h, --help   help for size
      --json   Format output as JSON

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `sync`

````
Sync the source to the destination, changing the destination
only.  Doesn't transfer files that are identical on source and
destination, testing by size and modification time or MD5SUM.
Destination is updated to match source, including deleting files
if necessary (except duplicate objects, see below). If you don't
want to delete files from destination, use the
[copy](/commands/rclone_copy/) command instead.

**Important**: Since this can cause data loss, test first with the
`--dry-run` or the `--interactive`/`i` flag.

```sh
rclone sync --interactive SOURCE remote:DESTINATION
```

Files in the destination won't be deleted if there were any errors at any
point. Duplicate objects (files with the same name, on those providers that
support it) are not yet handled. Files that are excluded won't be deleted
unless `--delete-excluded` is used. Symlinks won't be transferred or
deleted from local file systems unless `--links` is used.

It is always the contents of the directory that is synced, not the
directory itself. So when source:path is a directory, it's the contents of
source:path that are copied, not the directory name and contents.  See
extended explanation in the [copy](/commands/rclone_copy/) command if unsure.

If dest:path doesn't exist, it is created and the source:path contents
go there.

It is not possible to sync overlapping remotes. However, you may exclude
the destination from the sync with a filter rule or by putting an
exclude-if-present file inside the destination directory and sync to a
destination that is inside the source directory.

Rclone will sync the modification times of files and directories if
the backend supports it. If metadata syncing is required then use the
`--metadata` flag.

Note that the modification time and metadata for the root directory
will **not** be synced. See <https://github.com/rclone/rclone/issues/7652>
for more info.

**Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics

**Note**: Use the `rclone dedupe` command to deal with "Duplicate
object/directory found in source/destination - ignoring" errors.
See [this forum post](https://forum.rclone.org/t/sync-not-clearing-duplicates/14372)
for more info.

### Logger Flags

The `--differ`, `--missing-on-dst`, `--missing-on-src`, `--match` and `--error`
flags write paths, one per line, to the file name (or stdout if it is `-`)
supplied. What they write is described in the help below. For example
`--differ` will write all paths which are present on both the source and
destination but different.

The `--combined` flag will write a file (or stdout) which contains all
file paths with a symbol and then a space and then the path to tell
you what happened to it. These are reminiscent of diff files.

- `= path` means path was found in source and destination and was identical
- `- path` means path was missing on the source, so only in the destination
- `+ path` means path was missing on the destination, so only in the source
- `* path` means path was present in source and destination but different.
- `! path` means there was an error reading or hashing the source or dest.

The `--dest-after` flag writes a list file using the same format flags
as [`lsf`](/commands/rclone_lsf/#synopsis) (including [customizable options
for hash, modtime, etc.](/commands/rclone_lsf/#synopsis))
Conceptually it is similar to rsync's `--itemize-changes`, but not identical
-- it should output an accurate list of what will be on the destination
after the command is finished.

When the `--no-traverse` flag is set, all logs involving files that exist only
on the destination will be incomplete or completely missing.

Note that these logger flags have a few limitations, and certain scenarios
are not currently supported:

- `--max-duration` / `CutoffModeHard`
- `--compare-dest` / `--copy-dest`
- server-side moves of an entire dir at once
- High-level retries, because there would be duplicates (use `--retries 1` to disable)
- Possibly some unusual error scenarios

Note also that each file is logged during execution, as opposed to after, so it
is most useful as a predictor of what SHOULD happen to each file
(which may or may not match what actually DID).

Usage:
  rclone sync source:path dest:path [flags]

Flags:
      --absolute                Put a leading / in front of path names
      --combined string         Make a combined report of changes to this file
      --create-empty-src-dirs   Create empty source dirs on destination after sync
      --csv                     Output in CSV format
      --dest-after string       Report all files that exist on the dest post-sync
      --differ string           Report all non-matching files to this file
  -d, --dir-slash               Append a slash to directory names (default true)
      --dirs-only               Only list directories
      --error string            Report all files with errors (hashing or reading) to this file
      --files-only              Only list files (default true)
  -F, --format string           Output format - see lsf help for details (default "p")
      --hash h                  Use this hash when h is used in the format MD5|SHA-1|DropboxHash (default "md5")
  -h, --help                    help for sync
      --match string            Report all matching files to this file
      --missing-on-dst string   Report all files missing from the destination to this file
      --missing-on-src string   Report all files missing from the source to this file
  -s, --separator string        Separator for the items in the format (default ";")
  -t, --timeformat string       Specify a custom time format - see docs for details (default: 2006-01-02 15:04:05)

Flags for anything which can copy a file (flag group Copy):
      --check-first                                 Do all the checks before starting transfers
  -c, --checksum                                    Check for changes with size & checksum (if available, or fallback to size only)
      --compare-dest stringArray                    Include additional server-side paths during comparison
      --copy-dest stringArray                       Implies --compare-dest but also copies files from paths into destination
      --cutoff-mode HARD|SOFT|CAUTIOUS              Mode to stop transfers when reaching the max transfer limit HARD|SOFT|CAUTIOUS (default HARD)
      --ignore-case-sync                            Ignore case when synchronizing
      --ignore-checksum                             Skip post copy check of checksums
      --ignore-existing                             Skip all files that exist on destination
      --ignore-size                                 Ignore size when skipping use modtime or checksum
  -I, --ignore-times                                Don't skip items that match size and time - transfer all unconditionally
      --immutable                                   Do not modify files, fail if existing files have been modified
      --inplace                                     Download directly to destination file instead of atomic download to temp/rename
  -l, --links                                       Translate symlinks to/from regular files with a '.rclonelink' extension
      --max-backlog int                             Maximum number of objects in sync or check backlog (default 10000)
      --max-duration Duration                       Maximum duration rclone will transfer data for (default 0s)
      --max-transfer SizeSuffix                     Maximum size of data to transfer (default off)
  -M, --metadata                                    If set, preserve metadata when copying objects
      --modify-window Duration                      Max time diff to be considered the same (default 1ns)
      --multi-thread-chunk-size SizeSuffix          Chunk size for multi-thread downloads / uploads, if not set by filesystem (default 64Mi)
      --multi-thread-cutoff SizeSuffix              Use multi-thread downloads for files above this size (default 256Mi)
      --multi-thread-streams int                    Number of streams to use for multi-thread downloads (default 4)
      --multi-thread-write-buffer-size SizeSuffix   In memory buffer size for writing when in multi-thread mode (default 128Ki)
      --name-transform stringArray                  Transform paths during the copy process
      --no-check-dest                               Don't check the destination, copy regardless
      --no-traverse                                 Don't traverse destination file system on copy
      --no-update-dir-modtime                       Don't update directory modification times
      --no-update-modtime                           Don't update destination modtime if files identical
      --order-by string                             Instructions on how to order the transfers, e.g. 'size,descending'
      --partial-suffix string                       Add partial-suffix to temporary file name when --inplace is not used (default ".partial")
      --refresh-times                               Refresh the modtime of remote files
      --server-side-across-configs                  Allow server-side operations (e.g. copy) to work across different configs
      --size-only                                   Skip based on size only, not modtime or checksum
      --streaming-upload-cutoff SizeSuffix          Cutoff for switching to chunked upload if file size is unknown, upload starts after reaching cutoff or when file ends (default 100Ki)
  -u, --update                                      Skip files that are newer on the destination

Flags used for sync commands (flag group Sync):
      --backup-dir string               Make backups into hierarchy based in DIR
      --delete-after                    When synchronizing, delete files on destination after transferring (default)
      --delete-before                   When synchronizing, delete files on destination before transferring
      --delete-during                   When synchronizing, delete files during transfer
      --fix-case                        Force rename of case insensitive dest to match source
      --ignore-errors                   Delete even if there are I/O errors
      --list-cutoff int                 To save memory, sort directory listings on disk above this threshold (default 1000000)
      --max-delete int                  When synchronizing, limit the number of deletes (default -1)
      --max-delete-size SizeSuffix      When synchronizing, limit the total size of deletes (default off)
      --suffix string                   Suffix to add to changed files
      --suffix-keep-extension           Preserve the extension when using --suffix
      --track-renames                   When synchronizing, track file renames and do a server-side move if possible
      --track-renames-strategy string   Strategies to use when synchronizing using track-renames hash|modtime|leaf (default "hash")

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `test`

````
Rclone test is used to run test commands.

Select which test command you want with the subcommand, eg

```console
rclone test memory remote:
```

Each subcommand has its own options which you can see in their help.

**NB** Be careful running these commands, they may do strange things
so reading their documentation first is recommended.

Usage:
  rclone test [command]

Available commands:
  changenotify Log any change notify requests for the remote passed in.
  histogram    Makes a histogram of file name characters.
  info         Discovers file name or other limitations for paths.
  makefile     Make files with random contents of the size given
  makefiles    Make a random file hierarchy in a directory
  memory       Load all the objects at remote:path into memory and report memory stats.
  speed        Run a speed test to the remote

Flags:
  -h, --help   help for test

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `touch`

````
Set the modification time on file(s) as specified by remote:path to
have the current time.

If remote:path does not exist then a zero sized file will be created,
unless `--no-create` or `--recursive` is provided.

If `--recursive` is used then recursively sets the modification
time on all existing files that is found under the path. Filters are supported,
and you can test with the `--dry-run` or the `--interactive`/`-i` flag.
This will touch `--transfers` files concurrently.

If `--timestamp` is used then sets the modification time to that
time instead of the current time. Times may be specified as one of:

- 'YYMMDD' - e.g. 17.10.30
- 'YYYY-MM-DDTHH:MM:SS' - e.g. 2006-01-02T15:04:05
- 'YYYY-MM-DDTHH:MM:SS.SSS' - e.g. 2006-01-02T15:04:05.123456789

Note that value of `--timestamp` is in UTC. If you want local time
then add the `--localtime` flag.

Usage:
  rclone touch remote:path [flags]

Flags:
  -h, --help               help for touch
      --localtime          Use localtime for timestamp, not UTC
  -C, --no-create          Do not create the file if it does not exist (implied with --recursive)
  -R, --recursive          Recursively touch all files
  -t, --timestamp string   Use specified time instead of the current time of day

Important flags useful for most commands (flag group Important):
  -n, --dry-run         Do a trial run with no permanent changes
  -i, --interactive     Enable interactive mode
  -v, --verbose count   Print lots more stuff (repeat for more)

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `tree`

````
Lists the contents of a remote in a similar way to the unix tree command.

For example

```text
$ rclone tree remote:path
/
├── file1
├── file2
├── file3
└── subdir
    ├── file4
    └── file5

1 directories, 5 files
```

You can use any of the filtering options with the tree command (e.g.
`--include` and `--exclude`.  You can also use `--fast-list`.

The tree command has many options for controlling the listing which
are compatible with the tree command, for example you can include file
sizes with `--size`.  Note that not all of them have
short options as they conflict with rclone's short options.

For a more interactive navigation of the remote see the
[ncdu](/commands/rclone_ncdu/) command.

Usage:
  rclone tree remote:path [flags]

Flags:
  -a, --all             All files are listed (list . files too)
  -d, --dirs-only       List directories only
      --dirsfirst       List directories before files (-U disables)
      --full-path       Print the full path prefix for each file
  -h, --help            help for tree
      --level int       Descend only level directories deep
  -D, --modtime         Print the date of last modification.
      --noindent        Don't print indentation lines
      --noreport        Turn off file/directory count at end of tree listing
  -o, --output string   Output to file instead of stdout
  -p, --protections     Print the protections for each file.
  -Q, --quote           Quote filenames with double quotes.
  -s, --size            Print the size in bytes of each file.
      --sort string     Select sort: name,version,size,mtime,ctime
      --sort-ctime      Sort files by last status change time
  -t, --sort-modtime    Sort files by last modification time
  -r, --sort-reverse    Reverse the order of the sort
  -U, --unsorted        Leave files unsorted
      --version         Sort files alphanumerically by version

Flags for filtering directory listings (flag group Filter):
      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --hash-filter string                  Partition filenames by hash k/n or randomly @/n
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

Flags for listing directories (flag group Listing):
      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

### `version`

````
Show the rclone version number, the go version, the build target
OS and architecture, the runtime OS and kernel version and bitness,
build tags and the type of executable (static or dynamic).

For example:

```console
$ rclone version
rclone v1.55.0
- os/version: ubuntu 18.04 (64 bit)
- os/kernel: 4.15.0-136-generic (x86_64)
- os/type: linux
- os/arch: amd64
- go/version: go1.16
- go/linking: static
- go/tags: none
```

Note: before rclone version 1.55 the os/type and os/arch lines were merged,
      and the "go/version" line was tagged as "go version".

If you supply the --check flag, then it will do an online check to
compare your version with the latest release and the latest beta.

```console
$ rclone version --check
yours:  1.42.0.6
latest: 1.42          (released 2018-06-16)
beta:   1.42.0.5      (released 2018-06-17)
```

Or

```console
$ rclone version --check
yours:  1.41
latest: 1.42          (released 2018-06-16)
  upgrade: https://downloads.rclone.org/v1.42
beta:   1.42.0.5      (released 2018-06-17)
  upgrade: https://beta.rclone.org/v1.42-005-g56e1e820
```

If you supply the --deps flag then rclone will print a list of all the
packages it depends on and their versions along with some other
information about the build.

Usage:
  rclone version [flags]

Flags:
      --check   Check for new version
      --deps    Show the Go dependencies
  -h, --help    help for version

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
````

