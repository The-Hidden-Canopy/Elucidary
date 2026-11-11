# Elucidary source provenance

This standalone publication starts from The Hidden Canopy's already-public DASRE commit `2ebd21659535b515de7bda757b4f5d8668934b9f`:

https://github.com/The-Hidden-Canopy/Digital-Agnostic-System-Reconciliation-Engine/commit/2ebd21659535b515de7bda757b4f5d8668934b9f

Elucidary was originally implemented inside that repository. This repository gives the application its own identity, build instructions, license/attribution surface, and release destination. It does not rename or replace DASRE.

The initial source selection matches the existing desktop payload: 64 Python modules under `src/verifier_lab`, required data and third-party license texts, the Windows builder/launcher, desktop/scanner/service tests, and one synthetic reference example. Shared service dependencies are retained because the desktop imports them. The browser workbench, verification CLI, and experimental Windows isolation/file-exchange prototypes are excluded.

The service-level repository-map tests are retained from DASRE. Their browser-only API test class and imports are omitted because this application does not ship the HTTP server. Other selected tests remain intact.

Publication-specific changes are the project metadata/documentation, license packaging, and release checks. Original notices are retained. No private repository contents, benchmark inventories, user workspaces, binary runtime, or local Git history are included in the source import.
