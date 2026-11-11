"""Create a local, self-contained Windows desktop folder; does not publish or sign."""
from __future__ import annotations

import argparse
import datetime
import hashlib
import importlib.metadata
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ("esprima", "tree_sitter", "tree_sitter_typescript", "tree_sitter_cpp", "tree_sitter_c", "tree_sitter_c_sharp", "tree_sitter_rust")
DIST_PREFIXES = ("esprima-", "tree_sitter-", "tree_sitter_typescript-", "tree_sitter_cpp-", "tree_sitter_c-", "tree_sitter_c_sharp-", "tree_sitter_rust-")
# Left out of the desktop folder: the browser workbench and the experimental exchange and isolation prototypes.
EXCLUDED = ("__pycache__", "*.pyc", "server.py", "cli.py", "web", "file_exchange.py", "graph_reply_schema.py",
            "windows_reply_guard.py", "windows_acl_plan.py")
BOOTSTRAP = """from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / 'app'))
from verifier_lab.elucidary_desktop import main
raise SystemExit(main())
"""


def _source_revision():
    """The commit the folder was built from, and whether the working tree differed from it."""
    try:
        commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                                    capture_output=True, text=True, check=True).stdout.strip())
        return commit, dirty
    except (OSError, subprocess.CalledProcessError):
        return None, None


def build(output: Path, label: str | None = None):
    if sys.platform != "win32":
        raise ValueError("This builder requires a Windows Python runtime")
    output = output.absolute()
    if output.exists():
        raise ValueError("Refusing to overwrite an existing output path")
    compiler = shutil.which("gcc")
    if not compiler:
        raise ValueError("A Windows gcc compiler is required for the desktop launcher")
    # Modified for standalone publication: retain the launcher runtime notices.
    compiler_root = Path(compiler).resolve().parent.parent
    compiler_license = compiler_root / "LICENSE.TXT"
    runtime_notices = compiler_root / "x86_64-w64-mingw32" / "share" / "mingw32"
    if not compiler_license.is_file() or not (runtime_notices / "COPYING.MinGW-w64-runtime.txt").is_file():
        raise ValueError("Use LLVM-MinGW with its LICENSE.TXT and x86_64 MinGW runtime notices installed")
    base = Path(sys.base_prefix)
    package_dirs = []
    for name in PACKAGES:
        spec = importlib.util.find_spec(name)
        if not spec or not spec.submodule_search_locations:
            raise ValueError(f"Required local package is unavailable: {name}")
        package_dirs.append(Path(next(iter(spec.submodule_search_locations))))
    output.mkdir(parents=True)
    runtime = output / "runtime"; runtime.mkdir()
    runtime_dll = f"python{sys.version_info.major}{sys.version_info.minor}.dll"
    for name in ("python.exe", "pythonw.exe", runtime_dll, "python3.dll", "vcruntime140.dll", "vcruntime140_1.dll", "LICENSE.txt"):
        source = base / name
        if source.exists(): shutil.copy2(source, runtime / name)
    shutil.copytree(base / "DLLs", runtime / "DLLs", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    shutil.copytree(base / "Lib", runtime / "Lib", ignore=shutil.ignore_patterns("site-packages", "__pycache__", "*.pyc", "test", "tests"))
    shutil.copytree(base / "tcl", runtime / "tcl", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    site = runtime / "Lib" / "site-packages"; site.mkdir()
    for source in package_dirs:
        shutil.copytree(source, site / source.name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "test", "tests"))
    for source in {p.parent for p in package_dirs}:
        for entry in source.iterdir():
            if entry.is_dir() and entry.name.endswith(".dist-info") and entry.name.startswith(DIST_PREFIXES):
                shutil.copytree(entry, site / entry.name, dirs_exist_ok=True)
    licenses = output / "licenses"
    shutil.copytree(ROOT / "licenses", licenses)
    shutil.copy2(compiler_license, licenses / "LLVM-MinGW-LICENSE.TXT")
    for notice in runtime_notices.glob("COPYING*"):
        if notice.is_file(): shutil.copy2(notice, licenses / notice.name)
    app = output / "app"; app.mkdir()
    shutil.copytree(ROOT / "src" / "verifier_lab", app / "verifier_lab", ignore=shutil.ignore_patterns(*EXCLUDED))
    # Modified for standalone Elucidary: include attribution and Open Canopy terms.
    for name in ("LICENSE", "NOTICE", "OPEN_CANOPY_CONTRACT.md", "THIRD_PARTY_NOTICES.md", "README.md"):
        shutil.copy2(ROOT / name, output / name)
    shutil.copytree(ROOT / "docs", output / "docs")
    (output / "run.pyw").write_text(BOOTSTRAP, encoding="utf-8")
    subprocess.run([compiler, "-O2", "-static", "-municode", "-mwindows", str(ROOT / "tools" / "elucidary_windows_launcher.c"),
                    "-o", str(output / "Elucidary.exe")], check=True)
    commit, dirty = _source_revision()
    modules = sorted(path for path in (app / "verifier_lab").rglob("*.py"))
    digest = hashlib.sha256()
    for path in modules:
        digest.update(path.relative_to(app).as_posix().encode("utf-8") + b"\0" + hashlib.sha256(path.read_bytes()).digest())
    (output / "BUILD.json").write_text(json.dumps({
        "label": label, "built_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_commit": commit, "source_tree_differed_from_commit": dirty,
        "application_modules": len(modules), "application_sha256": digest.hexdigest(),
        "python": sys.version.split()[0],
        "bundled_parsers": {name: importlib.metadata.version(name.replace("_", "-")) for name in PACKAGES},
        "signed": False, "note": "Unsigned Elucidary preview. Parsing on Windows is for trusted repositories only; no parser sandbox and no local model are included.",
    }, indent=1), encoding="utf-8")
    notice_files = sorted(path for path in output.rglob("*") if path.is_file() and
                          ("license" in path.name.lower() or path.name.lower().startswith(("copying", "notice"))
                           or path.name == "OPEN_CANOPY_CONTRACT.md"))
    (output / "LICENSE_INVENTORY.json").write_text(json.dumps({
        "notice": "Third-party components retain their own licenses. Paths are relative to this distribution.",
        "files": [{"path": path.relative_to(output).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                  for path in notice_files],
    }, indent=2), encoding="utf-8")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--label", help="a name for this build, recorded in BUILD.json")
    args = parser.parse_args()
    try:
        print(build(args.output, args.label))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Desktop build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
