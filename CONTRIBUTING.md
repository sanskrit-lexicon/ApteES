# Contributing to ApteES

ApteES is part of the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon) project — corrections and enhancements for the Cologne digitisation of *Apte Sanskrit–English Dictionary (Extended)*.

> Inherits the [Sanskrit Lexicon org-wide contribution standard](https://github.com/sanskrit-lexicon/COLOGNE/blob/master/CONTRIBUTING.md). This file documents anything **repo-specific** on top of it.

## Reporting issues

Use the issue templates in `.github/ISSUE_TEMPLATE/`. Each issue gets exactly one **type** label, one **severity** label, and one **milestone** — see the [org-wide taxonomy](https://github.com/sanskrit-lexicon/COLOGNE/blob/master/CONTRIBUTING.md#issue-taxonomy--dictionary-repos).

Before opening:
1. Search existing issues (including closed) for similar patterns.
2. Verify the divergence against the canonical print edition.
3. Check `.ai_state.md` for in-progress work on the same area.

## Submitting a correction (PR)

Corrections are never made directly to source files — they are expressed as change files applied by scripts. See [`CLAUDE.md`](CLAUDE.md) for the change-file format and the `updateByLine.py` workflow.

PR checklist:
- [ ] Correction verified against the canonical print edition
- [ ] Change file uses the documented `NNN old / NNN new` format
- [ ] No unrelated changes mixed in
- [ ] Issue number referenced in the PR title or body
