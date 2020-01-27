This folder currently is a work in progress.

1. Initialize and update all submodules
2. Download a pyodide release tarball from https://github.com/mausbrand/pyodide/releases/tag/2019-09-24
3. Install the contents into the empty `pyodide/` folder
4. Run `python3 gen_files_json.py` inside this directory to re-generate `files.json`, which contains all files the vi depends on.

The entire process will be optimized.
