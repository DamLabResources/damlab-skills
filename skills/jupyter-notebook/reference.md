# jupytext — Full Reference

Binary: `bin/jupytext` (relative to this skill directory).

Grep this file:

```bash
grep -A 120 "^usage: jupytext" "$(dirname <path-to-this-SKILL.md>)/reference.md"
```

---

## Versions (smoke install)

| Tool | Version |
|------|---------|
| jupytext | 1.19.1 |
| nbformat | 5.10.4 |
| nbconvert | 7.17.0 |
| jupyter_client | 8.8.0 |

---

## Global `jupytext --help`

```
usage: jupytext [-h] [--from INPUT_FORMAT] [--to OUTPUT_FORMAT] [-o OUTPUT]
                [--update] [--set-formats SET_FORMATS] [--sync]
                [--paired-paths] [--format-options FORMAT_OPTIONS]
                [--update-metadata UPDATE_METADATA] [--use-source-timestamp]
                [--check-source-is-newer] [--warn-only] [--test]
                [--test-strict] [--stop] [--pipe PIPE] [--diff]
                [--diff-format DIFF_FORMAT] [--check CHECK]
                [--pipe-fmt PIPE_FMT] [--set-kernel SET_KERNEL] [--execute]
                [--run-path RUN_PATH] [--quiet] [--show-changes] [--version]
                [--pre-commit] [--pre-commit-mode]
                [notebooks ...]

Jupyter Notebooks as Markdown Documents, Julia, Python or R Scripts

positional arguments:
  notebooks             One or more notebook(s). Notebook is read from stdin
                        when this argument is empty. (default: None)

options:
  -h, --help            show this help message and exit
  --from INPUT_FORMAT   Jupytext format for the input(s). Inferred from the
                        file extension and content when missing. (default:
                        None)
  --to OUTPUT_FORMAT    The destination format: 'ipynb', 'markdown' or
                        'script', or a file extension: 'md', 'Rmd', 'jl',
                        'py', 'R', ... or 'auto' (script extension matching
                        the notebook language), or a combination of an
                        extension and a format name, e.g. md:pandoc,
                        md:markdown, md:myst or py:light, py:sphinx,
                        py:hydrogen, py:marimo, py:nomarker, py:percent. The
                        default format for scripts is the 'percent' format,
                        which uses '# %%' as cell markers and is compatible
                        with VS Code and PyCharm. Alternatively, you can also
                        use the 'light' format, which uses fewer cell markers.
                        The main formats (MyST Markdown, Markdown, percent,
                        light) preserve notebooks and text documents in a
                        roundtrip. Use the --test and and --test-strict
                        commands to test the roundtrip on your files. Read
                        more about the available formats at https://jupytext.r
                        eadthedocs.io/en/latest/formats.html. NB: in addition
                        to the extensions listed above, you can also use
                        these: 'clj', 'coco', 'cpp', 'cs', 'do', 'fs', 'fsx',
                        'go', 'gp', 'groovy', 'hs', 'java', 'js', 'lgt',
                        'logtalk', 'lua', 'm', 'mac', 'markdown', 'ml', 'mnb',
                        'myst', 'mystnb', 'pro', 'ps1', 'q', 'qmd', 'r',
                        'resource', 'robot', 'rs', 'sage', 'sas', 'scala',
                        'scm', 'sh', 'sos', 'ss', 'tcl', 'ts', 'wolfram',
                        'xsh' (default: None)
  -o OUTPUT, --output OUTPUT
                        Destination file. Defaults to the original file, with
                        prefix/suffix/extension changed according to the
                        destination format. Use '-' to print the notebook on
                        stdout. (default: None)
  --update              Preserve the output cells when the destination
                        notebook is an .ipynb file that already exists
                        (default: False)
  --set-formats SET_FORMATS
                        Turn the notebook or text document to one or more
                        alternative representations with e.g. '--set-formats
                        ipynb,py:light'. The --set-formats option also
                        triggers the creation/update of all paired files
                        (default: None)
  --sync, -s            Synchronize the content of the paired representations
                        of the given notebook. Input cells are taken from the
                        file that was last modified, and outputs are read from
                        the ipynb file, if present. (default: False)
  --paired-paths, -p    List the locations of the alternative representations
                        for this notebook. (default: False)
  --format-options FORMAT_OPTIONS, --opt FORMAT_OPTIONS
                        Set format options with e.g. '--opt
                        comment_magics=true' or '--opt
                        notebook_metadata_filter=-kernelspec'. (default: None)
  --update-metadata UPDATE_METADATA
                        Update the notebook metadata with the desired
                        dictionary. Argument must be given in JSON format. For
                        instance, if you want to activate a pairing in the
                        generated file, use e.g. --update-metadata
                        '{"jupytext":{"formats":"ipynb,py:light"}}' See also
                        the --opt and --set-formats options for other ways to
                        operate on the Jupytext metadata. (default: {})
  --use-source-timestamp
                        Set the modification timestamp of the output file(s)
                        equalto that of the source file, and keep the source
                        file and its timestamp unchanged. (default: False)
  --check-source-is-newer
                        Check that the file given as argument is the most
                        recent of all paired files, and if applicable, checks
                        that it is newer than the destination file. (default:
                        False)
  --warn-only, -w       Only issue a warning and continue processing other
                        notebooks when the conversion of a given notebook
                        fails (default: False)
  --test                Test that the notebook is stable under a round trip
                        conversion, up to the expected changes (default:
                        False)
  --test-strict         Test that the notebook is strictly stable under a
                        round trip conversion (default: False)
  --stop, -x            In --test mode, stop on first round trip conversion
                        error, and report stack traceback (default: False)
  --pipe PIPE           Pipe the text representation (in format --pipe-fmt) of
                        the notebook into another program, and read the
                        notebook back. For instance, reformat your notebook
                        with: 'jupytext notebook.ipynb --pipe black' If you
                        want to reformat it and sync the paired
                        representation, execute: 'jupytext notebook.ipynb
                        --sync --pipe black' In case the program that you want
                        to execute does not accept pipes, use {} as a
                        placeholder for a temporary file name into which
                        jupytext will write the text representation of the
                        notebook, e.g.: jupytext notebook.ipynb --pipe 'black
                        {}' (default: None)
  --diff, -d            Show the differences between (the inputs) of two
                        notebooks (default: False)
  --diff-format DIFF_FORMAT
                        The text format used to show differences in --diff
                        (default: None)
  --check CHECK         Pipe the text representation (in format --pipe-fmt) of
                        the notebook into another program, and test that the
                        returned value is non zero. For instance, test that
                        your notebook is pep8 compliant with: 'jupytext
                        notebook.ipynb --check flake8' or run pytest on your
                        notebook with: 'jupytext notebook.ipynb --check
                        pytest' In case the program that you want to execute
                        does not accept pipes, use {} as a placeholder for a
                        temporary file name into which jupytext will write the
                        text representation of the notebook, e.g.: jupytext
                        notebook.ipynb --check 'pytest {}' (default: None)
  --pipe-fmt PIPE_FMT   The format in which the notebook should be piped to
                        other programs, when using the --pipe and/or --check
                        commands. (default: auto:percent)
  --set-kernel SET_KERNEL, -k SET_KERNEL
                        Set the kernel with the given name on the notebook.
                        Use '--set-kernel -' to set a kernel matching the
                        current environment on Python notebooks, and matching
                        the notebook language otherwise (get the list of
                        available kernels with 'jupyter kernelspec list')
                        (default: None)
  --execute             Execute the notebook with the given kernel. In the
                        --pre-commit-mode, the notebook is executed only if a
                        code cell changed, or if some execution outputs are
                        missing or not ordered. (default: False)
  --run-path RUN_PATH   Execute the notebook at the given path (defaults to
                        the notebook parent directory) (default: None)
  --quiet, -q           Quiet mode: do not comment about files being updated
                        or created (default: False)
  --show-changes        Display the diff for each output file (default: False)
  --version, -v         Show jupytext's version number and exit (default:
                        False)
  --pre-commit          Ignore the notebook argument, and instead apply
                        Jupytext on the notebooks found in the git index,
                        which have an extension that matches the (optional)
                        --from argument. (default: False)
  --pre-commit-mode     This is a mode that is compatible with the pre-commit
                        framework. In this mode, --sync won't use timestamp
                        but instead will determines the source notebook as the
                        element of the pair that is added to the git index. An
                        alert is raised if multiple inconsistent
                        representations are in the index. It also raises an
                        alert after updating the paired files or outputs if
                        those files need to be added to the index. Finally,
                        filepaths that aren't in the source format you are
                        trying to convert from are ignored. (default: False)
```

---

## nbformat — code cell output types

When reading `nbformat` cells, `outputs` entries may contain:

| `output_type` | Typical fields |
|---------------|----------------|
| `stream` | `name` (`stdout`/`stderr`), `text` (list of strings) |
| `execute_result` | `data` (e.g. `text/plain`, `text/html`), `execution_count` |
| `display_data` | `data` (same as above) |
| `error` | `ename`, `evalue`, `traceback` |
