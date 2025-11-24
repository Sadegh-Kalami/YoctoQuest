# YoctoQuest

A ruthless, linear path to learn the Yocto Project and BitBake. Work through folders in numeric order; each contains concise notes and tasks.

## How to use
- Keep this repo for docs, configs, and small scripts; keep build outputs outside (e.g., `~/yocto-build`).
- Start at `00-prerequisites`, finish the checklists, then move down the numbered modules.
- Log what you learn in `notes/learning-journal.md`; capture project-specific work under `10-projects/project-*`.
- Commit text and scripts only; never commit `build/`, `tmp/`, `downloads/`, or `sstate-cache/`.

## Learning path
- 00 Prerequisites: host readiness and tool install.
- 01 Fundamentals: what Yocto is and core concepts.
- 02 Build System: poky setup, first build, directory anatomy.
- 03 Recipes: syntax, writing, and examples.
- 04 Layers: structure, creation, and layer examples.
- 05 Images: image types and customization.
- 06 Advanced: bbappends, packaging, kernel tweaks.
- 07 BSP: machine configuration basics.
- 08 SDK: extensible SDK generation and use.
- 09 Debugging: common errors and techniques.
- 10 Projects: applied exercises and your own builds.
- Resources: glossary, links, cheat sheet.
- Notes: your learning journal.

## Quick start
1) Read `00-prerequisites/system-requirements.md` and confirm your host matches.
2) Install tools via `00-prerequisites/tools-installation.md`.
3) Set up a clean build dir outside the repo and clone `poky` (e.g., `~/yocto-build/poky`).
4) Follow `02-build-system/poky-setup.md` and run the first image build in `02-build-system/first-build.md`.

## Workflow guardrails
- Keep secrets and network creds out of the repo.
- Use branches for experiments; keep `main` readable as a guide.
- Record failures and fixes in `notes/learning-journal.md` so you can reuse them later.
