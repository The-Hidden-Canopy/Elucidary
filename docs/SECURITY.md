# Security and local data

Elucidary parses source without executing the scanned repository. File contents, comments, and strings are data, not instructions to run commands or change settings.

## Windows

The Windows desktop build is for trusted repositories only. Parser subprocesses and resource bounds are not a Windows security sandbox. Experimental Windows isolation code is excluded. Do not use the build to inspect hostile or unknown repositories.

## Workspace

The default Windows workspace is `%LOCALAPPDATA%/Elucidary`; other platforms use `~/.elucidary`. A custom location can be selected with `--workspace`.

Labels, remembered paths, review marks, and parser cache records are local. Cache records can contain source excerpts. Stopping a scan does not necessarily erase cache records already written before cancellation, even if an older status message suggests no results were kept. Close the application before manually removing a workspace; removing it also removes its labels and saved state. Do not share workspaces as part of a bug report without reviewing their contents.

No cloud account or telemetry service is needed. An optional local assistant can only be explicitly configured; no model is bundled, and actual model execution has not been validated for this release. Do not assume audience controls provide certified child protection.

## Reports

Use a minimal synthetic example when opening a public issue. Do not post credentials, proprietary source, personal paths, or workspace databases.
