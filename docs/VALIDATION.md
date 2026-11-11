# Publication validation

Validation on Windows with CPython 3.12.10 and the complete pinned parser set:

- 124 tests run: 122 passed, 2 skipped. The skipped cases require symlink privileges and a packaged launcher; they are not reported as passed.
- Real hidden Tk widget checks exercised scan, navigation, labels, reopen, source search, large synthetic repositories, and cancellation.
- The separate Python wheel built successfully as `elucidary-0.1.0-py3-none-any.whl`.
- All selected Python files parsed; a focused source scan found no personal absolute paths, obvious credential markers, or private workspaces. This is a bounded publication audit, not a comprehensive security certification.
- The 64 application modules match the prior desktop payload. Standalone metadata, documents, notices and build packaging were added without changing application behavior.

The first run used an older environment missing C/C#/Rust grammars and had four related failures. Re-running with the complete pinned parser set produced the result above.

Unverified here: manual desktop acceptance, Linux isolation, real local-model execution, production signing, and GitHub Actions for the eventual published commit. Automated Tk teardown can emit callback cleanup warnings while tests pass; they are not treated as proof of complete UI acceptance.

Publication metadata tests and desktop self-check also passed after the wheel notice configuration was updated. Upstream license texts are preserved, including their whitespace.
