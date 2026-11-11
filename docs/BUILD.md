# Build and test Elucidary

Use Python 3.12+ with Tk. Create a virtual environment and install the project with `languages` and `javascript` extras as shown in the README.

## Tests

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -t . -v
python -m verifier_lab.elucidary_desktop --self-check --workspace "$env:TEMP/elucidary-self-check"
```

The suite includes real Tk widgets hidden from view, repository-scale fixtures, source/caller evidence, persistence, rescan/provider boundaries, and interrupted scans. A machine without a Tk display can skip widget tests; record skips rather than calling that a full desktop pass.

The browser API, document-verification CLI, and Windows isolation prototypes belong to DASRE and are not part of this standalone application's test scope. Linux sandbox execution and a real local model require separate validation.

## Windows folder build

Install the x86_64 UCRT LLVM-MinGW compiler from its official distribution, retaining its license and runtime notices. Ensure `gcc` is on PATH. Run from the activated environment containing the pinned parser dependencies:

```powershell
python tools/build_elucidary_windows.py --output ..\Elucidary-Windows --label "Elucidary 0.1.0 preview"
```

The builder refuses to overwrite an existing directory. It includes the interpreter/Tk, parser modules and notices, project license/NOTICE/Open Canopy Contract, application source, and launcher. It writes `BUILD.json` with commit, source state, and module digest. Keep all output files together. Building does not sign or publish the application.

Before distributing, verify the built folder from a clean extraction, inspect its licenses, run the packaged self-check, and run the unit/widget suite using the packaged interpreter and application source. Do not claim manual acceptance from scripted checks alone.
