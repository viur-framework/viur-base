"""Tests for ``clean-base.py``; run with ``python -m unittest discover -s tests``."""
import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock
from pathlib import Path

ROOT: Path = Path(__file__).resolve().parent.parent


def _load_clean_base():
    """Load ``clean-base.py`` as a module (its file name is not importable)."""
    spec = importlib.util.spec_from_file_location("clean_base", ROOT / "clean-base.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cb = _load_clean_base()


class StripFrontendBlocksTest(unittest.TestCase):
    TEXT = (
        "a\n"
        "# [frontend:site]\n"
        "site-line\n"
        "# [/frontend:site]\n"
        "{# [frontend:app] #}\n"
        "app-line\n"
        "{# [/frontend:app] #}\n"
        "b\n"
    )

    def test_keep_site(self) -> None:
        self.assertEqual(cb.strip_frontend_blocks(self.TEXT, frozenset({"site"})), "a\nsite-line\nb\n")

    def test_keep_none(self) -> None:
        self.assertEqual(cb.strip_frontend_blocks(self.TEXT, frozenset()), "a\nb\n")

    def test_keep_both(self) -> None:
        self.assertEqual(
            cb.strip_frontend_blocks(self.TEXT, frozenset({"site", "app"})), "a\nsite-line\napp-line\nb\n"
        )

    def test_markdown_comment_syntax(self) -> None:
        text = "x\n<!-- [frontend:app] -->\n  - item\n<!-- [/frontend:app] -->\ny\n"
        self.assertEqual(cb.strip_frontend_blocks(text, frozenset()), "x\ny\n")

    def test_no_markers_unchanged(self) -> None:
        self.assertEqual(cb.strip_frontend_blocks("x\ny\n", frozenset()), "x\ny\n")

    def test_unknown_part_raises(self) -> None:
        with self.assertRaises(cb.MarkerError):
            cb.strip_frontend_blocks("# [frontend:foo]\n# [/frontend:foo]\n", frozenset())

    def test_unbalanced_raises(self) -> None:
        for text in (
            "# [frontend:site]\nx\n",
            "# [/frontend:site]\n",
            "# [frontend:site]\n# [frontend:app]\n# [/frontend:app]\n# [/frontend:site]\n",
            "# [frontend:site]\n# [/frontend:app]\n",
        ):
            with self.subTest(text=text), self.assertRaises(cb.MarkerError):
                cb.strip_frontend_blocks(text, frozenset())

    def test_variants(self) -> None:
        self.assertEqual(cb.PARTS, ("site", "app"))
        self.assertEqual(cb.VARIANTS, {
            "hybrid": frozenset({"site"}),
            "spa": frozenset({"app"}),
            "both": frozenset({"site", "app"}),
            "none": frozenset(),
        })


def _snapshot(root: Path) -> dict[str, bytes]:
    """Return the content of every file below ``root`` keyed by its relative path."""
    return {str(p.relative_to(root)): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


class FrontendVariantTest(unittest.TestCase):
    """Apply variants to a temporary copy of the template files they touch."""

    EXTRA_FILES: tuple[str, ...] = ("package.json", "package-lock.json", "project.json", "icons.json")

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for rel in (*cb.MARKER_FILES, *self.EXTRA_FILES):
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)
        for part in cb.PARTS:
            (self.root / "sources" / part / "src").mkdir(parents=True)
            (self.root / "sources" / part / "src" / "main.js").write_text("// x\n")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text()

    def json(self, rel: str) -> dict:
        return json.loads(self.read(rel))

    def assert_no_markers_left(self) -> None:
        for rel in cb.MARKER_FILES:
            self.assertNotIn("[frontend:", self.read(rel), rel)
            self.assertNotIn("[/frontend:", self.read(rel), rel)

    def test_guard_all_marker_files_listed(self) -> None:
        tracked = subprocess.run(
            ["git", "grep", "-l", r"\[frontend:"], cwd=ROOT, capture_output=True, text=True, check=False
        ).stdout.split()
        found = sorted(p for p in tracked if p != "clean-base.py" and not p.startswith("tests/"))
        self.assertEqual(found, sorted(cb.MARKER_FILES))

    def test_repo_markers_valid(self) -> None:
        for variant in cb.VARIANTS:
            with self.subTest(variant=variant):
                self.assertTrue(cb.plan_frontend_variant(ROOT, variant))

    def test_plan_writes_nothing(self) -> None:
        before = _snapshot(self.root)
        actions = cb.plan_frontend_variant(self.root, "none")
        self.assertEqual(_snapshot(self.root), before)
        self.assertTrue(any("sources/site" in a for a in actions))
        self.assertTrue(any("package.json" in a for a in actions))

    def test_hybrid(self) -> None:
        cb.apply_frontend_variant(self.root, "hybrid")
        self.assertTrue((self.root / "sources/site").is_dir())
        self.assertFalse((self.root / "sources/app").exists())
        pkg = self.json("package.json")
        self.assertEqual(pkg["workspaces"], ["sources/site"])
        self.assertEqual(pkg["scripts"]["build"], "npm run build:site")
        self.assertEqual(pkg["scripts"]["lock"], "npm run lock:site")
        self.assertFalse([k for k in pkg["scripts"] if k.endswith(":app")])
        builds = self.json("project.json")["default"]["builds"]
        self.assertIn("site", builds)
        self.assertNotIn("app", builds)
        self.assertNotIn("- url: /app", self.read("deploy/app.yaml"))
        self.assertIn("inject_vite()", self.read("deploy/html/viur_base.html"))
        self.assertIn("unsafe-eval", self.read("deploy/main.py"))
        self.assertNotIn("deploy/app\n", self.read(".gitignore"))
        self.assert_no_markers_left()

    def test_spa(self) -> None:
        cb.apply_frontend_variant(self.root, "spa")
        self.assertFalse((self.root / "sources/site").exists())
        self.assertTrue((self.root / "sources/app").is_dir())
        main_py = self.read("deploy/main.py")
        self.assertNotIn("unsafe-eval", main_py)
        self.assertNotIn("localhost:8081", main_py)
        self.assertIn("upgrade-insecure-requests", main_py)
        base_html = self.read("deploy/html/viur_base.html")
        self.assertNotIn("inject_vite", base_html)
        self.assertNotIn("accessibility-drawer", base_html)
        self.assertIn("style.min.css", base_html)
        self.assertNotIn("def inject_vite", self.read("deploy/render/__init__.py"))
        self.assertIn("- url: /app", self.read("deploy/app.yaml"))
        self.assertNotIn("8081", self.read("viur-project.md"))
        self.assertIn("8082", self.read("viur-project.md"))
        self.assertEqual(self.json("package.json")["workspaces"], ["sources/app"])
        self.assert_no_markers_left()

    def test_both_only_drops_marker_lines(self) -> None:
        originals = {rel: self.read(rel) for rel in cb.MARKER_FILES}
        cb.apply_frontend_variant(self.root, "both")
        for rel, text in originals.items():
            expected = "".join(line for line in text.splitlines(keepends=True) if not cb.MARKER_RE.search(line))
            self.assertEqual(self.read(rel), expected, rel)
        self.assertEqual(self.json("package.json"), json.loads((ROOT / "package.json").read_text()))
        self.assertEqual(self.read("project.json"), (ROOT / "project.json").read_text())

    def test_none(self) -> None:
        cb.apply_frontend_variant(self.root, "none")
        for rel in ("package.json", "package-lock.json", "icons.json", "sources"):
            self.assertFalse((self.root / rel).exists(), rel)
        builds = self.json("project.json")["default"]["builds"]
        self.assertNotIn("site", builds)
        self.assertNotIn("app", builds)
        self.assert_no_markers_left()

    def test_none_removes_eslint_files(self) -> None:
        for rel in ("eslint.config.mjs", "eslint-suppressions.json"):
            (self.root / rel).write_text("{}\n")
        cb.apply_frontend_variant(self.root, "none")
        self.assertFalse((self.root / "eslint.config.mjs").exists())
        self.assertFalse((self.root / "eslint-suppressions.json").exists())

    def test_apply_twice_is_noop(self) -> None:
        cb.apply_frontend_variant(self.root, "hybrid")
        once = _snapshot(self.root)
        cb.apply_frontend_variant(self.root, "hybrid")
        self.assertEqual(_snapshot(self.root), once)

    def test_bad_marker_writes_nothing(self) -> None:
        path = self.root / "deploy/html/viur_base.html"
        lines = path.read_text().splitlines(keepends=True)
        closing = next(i for i, line in enumerate(lines) if "[/frontend:site]" in line)
        path.write_text("".join(lines[:closing] + lines[closing + 1:]))
        before = _snapshot(self.root)
        with self.assertRaises(cb.MarkerError):
            cb.apply_frontend_variant(self.root, "spa")
        self.assertEqual(_snapshot(self.root), before)

    def test_unknown_variant(self) -> None:
        with self.assertRaises(ValueError):
            cb.apply_frontend_variant(self.root, "vue")


class CleanGitHistoryTest(unittest.TestCase):
    def test_index_matches_cleaned_tree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def git(*args: str) -> str:
                return subprocess.run(
                    ["git", "-c", "user.email=t@t", "-c", "user.name=t", *args],
                    cwd=root, capture_output=True, text=True, check=True,
                ).stdout

            git("init", "-q", "-b", "main")
            (root / "keep.txt").write_text("keep\n")
            (root / "LICENSE").write_text("license\n")
            git("add", "-A")
            git("commit", "-qm", "template")
            (root / "LICENSE").unlink()
            (root / "keep.txt").write_text("changed\n")
            with contextlib.redirect_stdout(io.StringIO()):
                cb.clean_git_history(root)
            self.assertEqual(git("branch", "--show-current").strip(), "main")
            self.assertEqual(git("status", "--porcelain").splitlines(), ["A  keep.txt"])
            self.assertEqual(git("show", ":keep.txt"), "changed\n")


class ParseArgsTest(unittest.TestCase):
    def test_defaults_none(self) -> None:
        a = cb.parse_args([])
        self.assertEqual(
            (a.app_id, a.author, a.clean_history, a.frontend, a.install, a.yes), (None, None, None, None, True, False)
        )

    def test_keep_history(self) -> None:
        self.assertIs(cb.parse_args(["--keep-history"]).clean_history, False)
        self.assertIs(cb.parse_args(["-c"]).clean_history, True)

    def test_frontend_choices(self) -> None:
        self.assertEqual(cb.parse_args(["--frontend", "spa"]).frontend, "spa")
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            cb.parse_args(["--frontend", "vue"])


class AskTest(unittest.TestCase):
    def test_empty_answer_gives_default(self) -> None:
        with mock.patch("builtins.input", return_value=""):
            self.assertEqual(cb.ask("Variant", "both", tuple(cb.VARIANTS)), "both")

    def test_repeats_on_invalid_choice(self) -> None:
        with mock.patch("builtins.input", side_effect=["vue", " SPA "]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(cb.ask("Variant", "both", tuple(cb.VARIANTS)), "spa")


class MainTest(unittest.TestCase):
    """Run ``main`` in a temporary copy of the whole template."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "myproject"
        files = subprocess.run(
            ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.split("\0")
        for rel in filter(None, files):
            source = ROOT / rel
            if source.is_file():
                target = self.root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        shutil.copy2(ROOT / "clean-base.py", self.root / "clean-base.py")
        (self.root / "tests").mkdir(exist_ok=True)
        (self.root / "tests" / "test_clean_base.py").write_text("# test\n")
        self._cwd = os.getcwd()
        os.chdir(self.root)
        self.before = _snapshot(self.root)
        self.run_mock = mock.patch.object(cb.subprocess, "run").start()
        self.addCleanup(mock.patch.stopall)

    def tearDown(self) -> None:
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def main(self, argv: list[str], *, interactive: bool, answers: list[str] | None = None) -> int:
        no_input = mock.Mock(side_effect=AssertionError("input() must not be called"))
        with mock.patch("builtins.input", mock.Mock(side_effect=answers) if answers is not None else no_input), \
                contextlib.redirect_stdout(io.StringIO()) as out:
            code = cb.main(argv, interactive=interactive)
        self.output = out.getvalue()
        return code

    def assert_template_files_removed(self) -> None:
        for rel in ("LICENSE", ".github", "tests", "clean-base.py", "viur-project.md"):
            self.assertFalse((self.root / rel).exists(), rel)

    def test_main_non_interactive_uses_defaults(self) -> None:
        self.assertEqual(self.main(["-A", "x"], interactive=False), 0)
        self.assertTrue((self.root / "sources/site").is_dir())
        self.assertTrue((self.root / "sources/app").is_dir())
        self.assert_template_files_removed()
        self.assertIn("Project:      x", (self.root / "deploy/main.py").read_text())

    def test_main_interactive_asks_missing(self) -> None:
        self.assertEqual(self.main(["-A", "x"], interactive=True, answers=["me", "", "spa", "y"]), 0)
        self.assertIn("Author:       me", (self.root / "deploy/main.py").read_text())
        self.assertFalse((self.root / "sources/site").exists())
        self.assertTrue((self.root / "sources/app").is_dir())

    def test_main_interactive_accepts_defaults(self) -> None:
        self.assertEqual(self.main([], interactive=True, answers=["", "", "", "", "y"]), 0)
        self.assertIn("Project:      myproject", (self.root / "deploy/main.py").read_text())
        self.assertTrue((self.root / "sources/site").is_dir())
        self.assertTrue((self.root / "sources/app").is_dir())

    def test_main_all_flags_no_prompt(self) -> None:
        argv = ["-A", "x", "-a", "me", "--keep-history", "--frontend", "none", "--no-install", "-y"]
        self.assertEqual(self.main(argv, interactive=True), 0)
        self.assertFalse((self.root / "package.json").exists())
        self.assert_template_files_removed()

    def test_main_decline_writes_nothing(self) -> None:
        self.assertEqual(self.main(["-A", "x"], interactive=True, answers=["", "", "", "n"]), 1)
        self.assertEqual(_snapshot(self.root), self.before)

    def test_main_keyboard_interrupt_writes_nothing(self) -> None:
        self.assertNotEqual(self.main(["-A", "x"], interactive=True, answers=[KeyboardInterrupt()]), 0)
        self.assertEqual(_snapshot(self.root), self.before)

    def test_main_end_of_input_writes_nothing(self) -> None:
        self.assertNotEqual(self.main(["-A", "x"], interactive=True, answers=["me", EOFError()]), 0)
        self.assertEqual(_snapshot(self.root), self.before)

    def test_main_bad_marker_writes_nothing(self) -> None:
        path = self.root / "deploy/main.py"
        path.write_text(path.read_text().replace("# [/frontend:site]\n", "", 1))
        before = _snapshot(self.root)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertNotEqual(self.main(["-A", "x", "-y"], interactive=False), 0)
        self.assertEqual(_snapshot(self.root), before)

    def test_bootstrap_runs_uv_sync(self) -> None:
        with mock.patch.object(cb.shutil, "which", side_effect=lambda name: f"/usr/bin/{name}"):
            self.assertEqual(self.main(["-A", "x", "--frontend", "hybrid"], interactive=False), 0)
        commands = [c.args[0] for c in self.run_mock.call_args_list]
        self.assertIn(["/usr/bin/uv", "sync"], commands)
        self.assertIn(["/usr/bin/npm", "install", "--package-lock-only"], commands)

    def test_bootstrap_without_uv(self) -> None:
        with mock.patch.object(cb.shutil, "which", return_value=None):
            self.assertEqual(self.main(["-A", "x"], interactive=False), 0)
        self.run_mock.assert_not_called()
        self.assertIn("uv sync", self.output)

    def test_interrupt_during_bootstrap_still_finishes(self) -> None:
        self.run_mock.side_effect = KeyboardInterrupt()
        with mock.patch.object(cb.shutil, "which", side_effect=lambda name: f"/usr/bin/{name}"), \
                mock.patch.object(cb, "clean_git_history") as history:
            self.assertEqual(self.main(["-A", "x"], interactive=False), 0)
        history.assert_called_once()
        self.assertIn("uv sync", self.output.split("Next steps:")[1])

    def test_no_install_skips_bootstrap(self) -> None:
        with mock.patch.object(cb.shutil, "which", side_effect=lambda name: f"/usr/bin/{name}"):
            self.assertEqual(self.main(["-A", "x", "--no-install"], interactive=False), 0)
        self.run_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
