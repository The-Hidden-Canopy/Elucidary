# Elucidary

**Understand a repository, follow its connections, and learn from the source.**

Elucidary is a standalone desktop application from The Hidden Canopy LLC, released under **Apache 2.0** and the **[Open Canopy Contract](OPEN_CANOPY_CONTRACT.md)**. It runs locally without an account, subscription, browser, or local web server.

## What it does

- Scan a repository and browse its files, functions, classes, and written calls.
- Explore a visual map, follow possible callers, and jump back to the cited source.
- Read source-grounded explanations and practice questions at different levels.
- Add labels and review marks, reopen saved repositories, and compare rescans.
- Inspect coverage: unsupported, skipped, generated, binary, or unparsable files are reported.

Python, JavaScript, TypeScript/TSX/JSX, C/C++/CUDA, C#, and Rust source are supported with the included parser dependencies. Relationships inferred from syntax are marked as inferred. They are not proof that a call executes or resolves to that target at runtime.

## Run from source

Install Python 3.12 or later with Tk support. On Windows, the standard Python installer includes Tk.

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install ".[languages,javascript]"
.\.venv\Scripts\elucidary
```

On macOS/Linux, activate the virtual environment and run `pip install ".[languages,javascript]"`, then `elucidary`. These platforms are not release-validated here. Linux distributions may require their Python Tk package.

For packaged Windows builds, see [Releases](https://github.com/The-Hidden-Canopy/Elucidary/releases). Extract the entire archive and run `Elucidary.exe`; keep its accompanying folders together. An unsigned prerelease is an early build, not a signed production installer.

## Current boundaries

- **Scan trusted repositories only on Windows.** Parser isolation is not provided by the Windows desktop build. The application reads source without executing the scanned repository, but parser inputs are still a trust boundary.
- **No model is bundled.** Local-model integration is experimental and has not been validated with a real model in this release. Source-grounded explanations work without one.
- Large repositories can consume substantial memory. A rescan may temporarily require more memory than the initial scan.
- Cancellation stops work, but previously written local parser-cache entries can remain. Workspace files may contain source excerpts. See [security and local data](docs/SECURITY.md).
- Automated widget checks are not a complete manual accessibility or desktop acceptance review. No child-safety certification is claimed.

## Build, test, and provenance

See [BUILD.md](docs/BUILD.md) for reproducible commands and [PROVENANCE.md](docs/PROVENANCE.md) for the source boundary. The repository contains Elucidary's desktop/scanner code and the shared DASRE service dependencies it currently uses. The internal Python package name `verifier_lab` is retained for compatibility; the published application and entry point are Elucidary.

## License and attribution

[Apache License 2.0](LICENSE). [NOTICE](NOTICE) records project attribution and provenance. Third-party components retain their own licenses, listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The Open Canopy Contract states the project's commitments to users; it does not replace or restrict the Apache license.
