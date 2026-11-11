# Third-party notices

Elucidary's own source and shared DASRE code use Apache 2.0. Separately installed or bundled dependencies keep their original licenses; the project license does not relicense them.

| Component | Version | License / notice location |
| --- | --- | --- |
| Esprima Python | 4.0.1 | BSD-2-Clause; `src/verifier_lab/third_party/esprima-LICENSE.txt` and installed distribution metadata |
| tree-sitter Python binding | 0.25.2 | MIT; `src/verifier_lab/third_party/tree-sitter-LICENSE.txt` and installed distribution metadata |
| tree-sitter TypeScript | 0.23.2 | MIT; `src/verifier_lab/third_party/tree-sitter-typescript-LICENSE.txt` |
| tree-sitter C++ | 0.23.4 | MIT; `src/verifier_lab/third_party/tree-sitter-cpp-LICENSE.txt` |
| tree-sitter C | 0.23.4 | MIT; `src/verifier_lab/third_party/tree-sitter-c-LICENSE.txt` |
| tree-sitter C# | 0.23.1 | MIT; `src/verifier_lab/third_party/tree-sitter-c-sharp-LICENSE.txt` |
| tree-sitter Rust | 0.23.2 | MIT; `src/verifier_lab/third_party/tree-sitter-rust-LICENSE.txt` |

The existing tree-sitter Python grammar notice is retained for provenance, although Python scanning uses the standard-library AST parser and does not bundle that grammar.

Windows folder builds also redistribute the Python interpreter and its standard library/Tk/runtime dependencies. Their terms must be carried with the binary distribution. Python's `runtime/LICENSE.txt`, the Tcl/Tk license files, and each parser's `.dist-info` license texts remain in the package. See the build's license inventory for the exact bundled versions and paths. No model weights or third-party repositories are bundled.

The Windows launcher is built with LLVM-MinGW. Its accompanying compiler/runtime notices are retained under `licenses/` in the folder build. `LICENSE_INVENTORY.json` lists bundled notice paths and hashes.

`licenses/PYTHON-3.12.10-LICENSE.html` preserves the official installed Python documentation license page, including incorporated-software notices such as Expat. The Windows preview uses CPython 3.12.10.

CPython 3.12.10's official Windows build recipe specifies XZ 5.2.5. Its liblzma component is public domain; the upstream summary is preserved in licenses/XZ-5.2.5-COPYING.txt. Sources: https://github.com/python/cpython/blob/v3.12.10/PCbuild/get_externals.bat and https://github.com/python/cpython-source-deps/blob/xz-5.2.5/COPYING .
