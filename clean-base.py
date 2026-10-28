#!/usr/bin/env python3
import argparse
import datetime
import getpass
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PARTS: tuple[str, ...] = ("site", "app")
"""Frontend parts of the template: ``site`` (Jinja/Vue hybrid) and ``app`` (standalone Vue SPA)."""

VARIANTS: dict[str, frozenset[str]] = {
    "hybrid": frozenset({"site"}),
    "spa": frozenset({"app"}),
    "both": frozenset({"site", "app"}),
    "none": frozenset(),
}
"""Frontend variants and the parts each of them keeps."""

MARKER_RE: re.Pattern[str] = re.compile(r"\[(/?)frontend:([a-z]+)\]")


class MarkerError(ValueError):
    """A ``[frontend:…]`` marker is unknown or the blocks are unbalanced."""


def strip_frontend_blocks(text: str, keep: frozenset[str]) -> str:
    """
    Remove the marker lines and the content of all blocks whose part is not kept.

    A marker line contains ``[frontend:<part>]`` (opening) or ``[/frontend:<part>]`` (closing),
    in whatever comment syntax the file uses. Blocks must not be nested.

    :param text: The file content.
    :param keep: The parts whose block content stays.
    :return: The content without marker lines and without the blocks of removed parts.
    :raises MarkerError: On an unknown part, a nested, unclosed or unopened block.
    """
    out: list[str] = []
    current: str | None = None
    for lineno, line in enumerate(text.splitlines(keepends=True), start=1):
        if match := MARKER_RE.search(line):
            closing, part = match.group(1) == "/", match.group(2)
            if part not in PARTS:
                raise MarkerError(f"line {lineno}: unknown frontend part {part!r} in {match.group(0)}")
            if not closing and current is not None:
                raise MarkerError(f"line {lineno}: {match.group(0)} inside open block {current!r}")
            if closing and current != part:
                raise MarkerError(f"line {lineno}: {match.group(0)} without matching opening marker")
            current = None if closing else part
            continue
        if current is None or current in keep:
            out.append(line)
    if current is not None:
        raise MarkerError(f"block {current!r} is not closed")
    return "".join(out)


MARKER_FILES: tuple[str, ...] = (
    ".gitignore",
    "deploy/app.yaml",
    "deploy/html/viur_base.html",
    "deploy/main.py",
    "deploy/render/__init__.py",
    "viur-project.md",
)
"""Files containing ``[frontend:…]`` marker blocks."""

NPM_FILES: tuple[str, ...] = (
    "package.json",
    "package-lock.json",
    "icons.json",
    "eslint.config.mjs",
    "eslint-suppressions.json",
)
"""Files only needed with at least one Vue frontend; removed for the variant ``none``."""


def _keep_parts(variant: str) -> frozenset[str]:
    """
    Return the parts kept by a variant.

    :raises ValueError: On an unknown variant.
    """
    if variant not in VARIANTS:
        raise ValueError(f"unknown frontend variant {variant!r}, expected one of {', '.join(VARIANTS)}")
    return VARIANTS[variant]


def _dump_json_like(original: str, data: dict) -> str:
    """Serialize ``data`` with the indentation and trailing newline of ``original``."""
    second_line = original.splitlines()[1] if original.count("\n") > 1 else ""
    indent = (len(second_line) - len(second_line.lstrip(" "))) or 2
    return json.dumps(data, indent=indent, ensure_ascii=False) + ("\n" if original.endswith("\n") else "")


def _edit_package_json(text: str, keep: frozenset[str]) -> str:
    """Drop the scripts and workspaces of removed parts from ``package.json``."""
    data = json.loads(text)
    scripts = data.get("scripts", {})
    kept = [part for part in PARTS if part in keep]
    for name in list(scripts):
        if any(name.endswith(f":{part}") for part in PARTS if part not in keep):
            del scripts[name]
    for combined in ("build", "lock"):
        if combined in scripts:
            scripts[combined] = " && ".join(f"npm run {combined}:{part}" for part in kept)
    if "workspaces" in data:
        data["workspaces"] = [ws for ws in data["workspaces"] if ws.rsplit("/", 1)[-1] in keep]
    return text if data == json.loads(text) else _dump_json_like(text, data)


def _edit_project_json(text: str, keep: frozenset[str]) -> str:
    """Drop the builds of removed parts from ``project.json``."""
    data = json.loads(text)
    builds = data.get("default", {}).get("builds", {})
    for part in PARTS:
        if part not in keep:
            builds.pop(part, None)
    return text if data == json.loads(text) else _dump_json_like(text, data)


def _frontend_changes(root: Path, variant: str) -> tuple[dict[Path, str], list[Path], list[str]]:
    """
    Compute all changes of a variant without touching the tree.

    :return: Files to write (path → new content), paths to delete, human-readable actions.
    :raises MarkerError: On invalid markers in any of ``MARKER_FILES``.
    """
    keep = _keep_parts(variant)
    writes: dict[Path, str] = {}
    deletes: list[Path] = []
    actions: list[str] = []

    for rel in MARKER_FILES:
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text()
        try:
            new = strip_frontend_blocks(text, keep)
        except MarkerError as exc:
            raise MarkerError(f"{rel}: {exc}") from exc
        if new != text:
            writes[path] = new
            actions.append(f"edit {rel}")

    for part in PARTS:
        if part not in keep and (root / "sources" / part).exists():
            deletes.append(root / "sources" / part)
            actions.append(f"delete sources/{part}/")

    edits = (("project.json", _edit_project_json),) if not keep else (
        ("package.json", _edit_package_json), ("project.json", _edit_project_json),
    )
    for rel, edit in edits:
        path = root / rel
        if path.is_file():
            text = path.read_text()
            new = edit(text, keep)
            if new != text:
                writes[path] = new
                actions.append(f"edit {rel}")

    if not keep:
        for rel in NPM_FILES:
            if (root / rel).exists():
                deletes.append(root / rel)
                actions.append(f"delete {rel}")
        sources = root / "sources"
        if sources.is_dir() and all(child in deletes for child in sources.iterdir()):
            deletes.append(sources)
            actions.append("delete sources/")

    return writes, deletes, actions


def plan_frontend_variant(root: Path, variant: str) -> list[str]:
    """
    Describe what :func:`apply_frontend_variant` would change, without writing anything.

    :param root: The project root.
    :param variant: One of :data:`VARIANTS`.
    :return: Human-readable actions.
    :raises MarkerError: On invalid markers.
    :raises ValueError: On an unknown variant.
    """
    return _frontend_changes(root, variant)[2]


def apply_frontend_variant(root: Path, variant: str) -> None:
    """
    Reduce the template to the frontend parts of a variant.

    All markers are validated before the first file is written.

    :param root: The project root.
    :param variant: One of :data:`VARIANTS`.
    :raises MarkerError: On invalid markers; nothing is changed then.
    :raises ValueError: On an unknown variant.
    """
    writes, deletes, _ = _frontend_changes(root, variant)
    for path, content in writes.items():
        path.write_text(content)
    for path in deletes:
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


TEMPLATE_ONLY: tuple[str, ...] = ("LICENSE", ".github", "tests")
"""Files and directories describing viur-base itself; never part of a new project (issue #145)."""

PLACEHOLDER_SUFFIXES: tuple[str, ...] = (
    ".py", ".yaml", ".html", ".md", ".sh", ".json", ".js", ".less", ".toml", ".lock", ".txt",
)
"""Files in which placeholders are replaced; `.txt` covers deploy/requirements.txt."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """
    Parse the command line; every value not given stays ``None`` and is asked for later.

    :param argv: Arguments without the program name, ``None`` for ``sys.argv[1:]``.
    """
    ap = argparse.ArgumentParser(
        description="Setting up a clean ViUR project base.",
        epilog="Values not given as argument are asked for interactively (defaults apply without a terminal).",
    )
    ap.add_argument("-A", "--app_id", help="The application-id that is placed in arbitrary places.")
    ap.add_argument("-a", "--author", help="The author's name that is placed in arbitrary places.")
    history = ap.add_mutually_exclusive_group()
    history.add_argument(
        "-c", "--clean-history", dest="clean_history", action="store_const", const=True,
        help="Clean the git history (default).",
    )
    history.add_argument(
        "--keep-history", dest="clean_history", action="store_const", const=False, help="Keep the git history.",
    )
    ap.add_argument(
        "-f", "--frontend", choices=tuple(VARIANTS),
        help="Frontend: hybrid (Vue on the Jinja pages), spa (standalone Vue app under /app), both (default), "
             "none (Jinja only).",
    )
    ap.add_argument(
        "--no-install", dest="install", action="store_false", help="Do not run `uv sync` at the end.",
    )
    ap.add_argument("-y", "--yes", action="store_true", help="Apply without asking for confirmation.")
    return ap.parse_args(argv)


def ask(question: str, default: str, choices: tuple[str, ...] | None = None) -> str:
    """
    Ask on the terminal until a valid answer is given.

    :param question: The question, without default or choices.
    :param default: The answer for an empty input.
    :param choices: The allowed answers (case-insensitive), ``None`` for free text.
    :return: The answer, lower-cased if ``choices`` are given.
    """
    hint = f" ({'/'.join(choices)})" if choices else ""
    while True:
        answer = input(f"{question}{hint} [{default}]: ").strip()
        if not answer:
            return default
        if choices is None:
            return answer
        if answer.lower() in choices:
            return answer.lower()
        print(f"Invalid answer {answer!r}, expected one of: {', '.join(choices)}")


def replace_placeholders(root: Path, replacements: dict[str, str]) -> None:
    """Replace all placeholders in the text files below ``root``."""
    for subdir, _dirs, files in os.walk(root):
        for file in files:
            path = Path(subdir) / file
            if not path.name.endswith(PLACEHOLDER_SUFFIXES):
                continue
            text = path.read_text()
            new = text
            for src, target in replacements.items():
                new = new.replace(src, target)
            if new != text:
                path.write_text(new)


def remove_template_files(root: Path) -> None:
    """Delete the files and directories that describe viur-base itself."""
    for rel in TEMPLATE_ONLY:
        path = root / rel
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


def clean_git_history(root: Path) -> None:
    """Replace the git history by a single orphan branch ``main`` whose index holds the current tree."""
    if not (root / ".git").exists():
        return
    print("Cleaning git history")
    subprocess.check_output("git checkout --orphan main_tmp", shell=True, cwd=root)
    print(subprocess.check_output("git branch -D main", shell=True, cwd=root).decode().rstrip("\n"))
    subprocess.check_output("git branch -m main", shell=True, cwd=root)
    # the orphan branch keeps the old index; stage the cleaned tree instead (removed files included)
    subprocess.check_output("git add -A", shell=True, cwd=root)
    branch = subprocess.check_output("git branch --show-current", shell=True, cwd=root).decode().rstrip("\n")
    print("Current branch is:", branch)
    print("---")


def bootstrap(root: Path, variant: str, install: bool) -> list[str]:
    """
    Set up the project environment with ``uv sync``; regenerate the npm lockfile for a single frontend.

    Failures are reported with the command to run manually; the project itself is already set up.

    :return: The commands still to be run manually.
    """
    steps: list[list[str]] = []
    manual: list[str] = []
    uv = shutil.which("uv") if install else None
    if uv:
        steps.append([uv, "sync"])
    else:
        manual.append("uv sync")
    npm = shutil.which("npm") if install else None
    if variant in ("hybrid", "spa"):
        if npm:
            steps.append([npm, "install", "--package-lock-only"])
        else:
            manual.append("npm install --package-lock-only")

    for cmd in steps:
        print(f"Running {' '.join(cmd)}", flush=True)
        try:
            subprocess.run(cmd, cwd=root, check=True)
        except (OSError, subprocess.CalledProcessError, KeyboardInterrupt) as exc:
            # also on Ctrl-C: the project is already rewritten and this script is gone, so finish the setup
            print(f"WARNING: {' '.join(cmd)} failed ({exc or 'interrupted'}); run it manually.")
            manual.append(" ".join([Path(cmd[0]).name, *cmd[1:]]))

    return manual


def main(argv: list[str] | None = None, *, interactive: bool | None = None) -> int:
    """
    Set up a new project from this template in the current directory.

    :param argv: Arguments without the program name, ``None`` for ``sys.argv[1:]``.
    :param interactive: Ask for missing values; ``None`` asks when stdin is a terminal.
    :return: The exit code.
    """
    args = parse_args(argv)
    if interactive is None:
        interactive = sys.stdin.isatty()
    root = Path.cwd()

    try:
        try:
            whoami = getpass.getuser()
        except Exception:
            whoami = "viur"

        app_id = args.app_id
        if app_id is None:
            app_id = ask("Application-id", root.name) if interactive else root.name
        author = args.author
        if author is None:
            author = ask("Author name", whoami) if interactive else whoami
        clean_history = args.clean_history
        if clean_history is None:
            clean_history = (ask("Clean the git history?", "y", ("y", "n")) == "y") if interactive else True
        frontend = args.frontend
        if frontend is None:
            frontend = ask("Frontend", "both", tuple(VARIANTS)) if interactive else "both"

        actions = plan_frontend_variant(root, frontend)
        print(f"Setting up {app_id!r} (author {author!r}, frontend {frontend!r}):", flush=True)
        for action in actions:
            print(f"  - {action}")
        print(f"  - delete {', '.join(TEMPLATE_ONLY)}")
        print(f"  - {'clean' if clean_history else 'keep'} the git history")
        print(f"  - {'run uv sync' if args.install else 'skip uv sync'}")
        if interactive and not args.yes and ask("Apply?", "y", ("y", "n")) != "y":
            print("Aborted, nothing changed.")
            return 1
    except (KeyboardInterrupt, EOFError):
        print("\nAborted, nothing changed.")
        return 130
    except MarkerError as exc:
        print(f"ERROR: {exc}; nothing changed.", file=sys.stderr)
        return 2

    apply_frontend_variant(root, frontend)
    replace_placeholders(root, {
        "{{app_id}}": app_id,
        "{{whoami}}": author,
        "{{timestamp}}": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        # valid package-name placeholder used for the project name in pyproject.toml/uv.lock
        # (uv rejects "{{app_id}}", and normalizes names to lowercase/hyphens in uv.lock,
        # so the token must be lowercase-hyphen to match in both files)
        "viur-base-appid": app_id,
    })
    remove_template_files(root)

    # Create a README.md; remove first, os.rename fails on Windows if the destination exists
    (root / "README.md").unlink(missing_ok=True)
    (root / "viur-project.md").rename(root / "README.md")
    (root / Path(__file__).name).unlink(missing_ok=True)  # remove yourself

    manual = bootstrap(root, frontend, args.install)
    if clean_history:
        clean_git_history(root)

    print()
    print("Well done! The project repository has been set up.")
    print("Next steps:")
    for cmd in [*manual, "uv run viur build release", "./viur-gcloud-setup.sh"]:
        print(f"    {cmd}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
