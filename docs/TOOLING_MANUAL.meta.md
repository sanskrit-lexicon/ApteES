# TOOLING_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/TOOLING_MANUAL.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/docs/TOOLING_MANUAL.md)
— purpose, provenance, improvement backlog and revision history of the manual
itself (not of the tools it documents).

## Purpose

Give a new operator/contributor a runnable understanding of ApteES's three
tool pipelines (ae_saninvert inversion + hwnorm1/n-gram validation,
hwspellcheck English-headword spellcheck, transcode SLP1↔Devanāgarī with its
round-trip proof), the reverse-direction data shape that motivates them, the
issue-folder pattern, and how everything chains into the csl-orig batched-PR
correction workflow.

## Audience

- **Operators** re-running the transcode or markup_fix tools, or reviving the
  inversion/spellcheck studies against fresh data;
- **Maintainers** touching the filters/transcoder tables (invariants + traps);
- **Correction authors** turning `…prob.txt` / `spellchkLine.txt` candidates
  into change files.

## Provenance

- Authored 11-07-2026 by Fable 5 (`claude-fable-5`) executing handoff
  [H521-Fable_ApteES_tooling_manual_10.07.26.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H521-Fable_ApteES_tooling_manual_10.07.26.md)
  (manual-coverage census batch H501–H531).
- Modelled on the gold-standard operator manual
  [RussianRamayana Litpam-Indexator MANUAL.md](https://github.com/gasyoun/RussianRamayana/blob/main/Litpam-Indexator/docs/indesign-pipeline/MANUAL.md).
- Source material read first-hand (no subagents — the repo is small):
  README, CLAUDE.md, DATA_DICTIONARY, the three tool readmes, the
  punctuation-prep notes, and the six issue folders. Commands quoted
  verbatim; the recorded counts (11,363 headwords → 1,562 → 281 → 77 errors;
  155→2 bigram and 961→781 trigram candidates; 199/70/7 punctuation cases;
  270 periods) are from the executed runs' notes.
- Transcription-verified: paths/scripts confirmed on disk 11-07-2026; the
  transcode round-trip was not re-executed this pass (its committed output
  and proof procedure are documented in
  [transcode/readme.txt](https://github.com/sanskrit-lexicon/ApteES/blob/main/transcode/readme.txt)).

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Live-verify the transcode round-trip against the current csl-orig `ae.txt` and record the fresh diff-0 in the manual (cheapest full verification in the repo) | open |
| 2 | Refresh the 2016 hwnorm1 snapshot under [ae_saninvert/hwnorm1/](https://github.com/sanskrit-lexicon/ApteES/tree/main/ae_saninvert/hwnorm1) from the sibling repo and re-run the filter chain — the not-found analysis is a decade stale | open |
| 3 | Build the IAST edition (`ae_transcode.py slp1 roman1`-style) that the transcode readme left as an exercise | open |
| 4 | Modernize hwspellcheck: replace the unreproducible Google-Docs triage with a scripted wordlist pass, and update `readme.org`'s fossilized 2014 environment section | open |
| 5 | Rename `transcode/punctuation/updateByline.py` → `updateByLine.py` for consistency (with a readme note) | open |
| 6 | Point CLAUDE.md's Architecture table (currently self-referential "working files" rows) at this manual's tool walkthroughs | open |

## Known limitations

- The inversion and spellcheck walkthroughs document the 2014–2016 runs;
  re-running requires a freshly built `ae.xml` (external artifact) and a
  refreshed hwnorm1 — backlog #2.
- Issue folders are mapped one-line each; their readmes remain the running
  logs (issue13's print-change transfer is the most involved).
- No live re-execution this pass (see Provenance).

## Intended use / known misuse

- **For:** onboarding a new operator/contributor to run the three ApteES
  tool pipelines from the manual alone — transcode round-trip, ae_saninvert
  Sanskrit-side inversion + hwnorm1/n-gram validation, and hwspellcheck
  English-headword spellcheck — and to understand how their outputs feed the
  csl-orig batched-PR correction workflow via `updateByLine.py`.
- **For:** a maintainer deciding whether to re-run a pipeline, by reading
  which parts are re-runnable/deterministic (transcode) versus one-time
  2014–2016 studies whose *outputs*, not procedures, are the durable value
  (ae_saninvert, hwspellcheck).
- **Misuse — treating the recorded counts as current.** The 11,363→1,562→281→77
  headword-error chain and the 155→2/961→781 n-gram figures are from the
  *executed historical runs*, not live measurements; re-running against a
  freshly built `ae.xml` or a refreshed hwnorm1 snapshot (backlog #2) will
  produce different numbers — see [Known limitations](#known-limitations).
- **Misuse — running `invert1.py` without a locally built `ae.xml`.** The
  manual is explicit that this is an external artifact (produced by
  csl-pywork's `generate_dict.sh ae` or downloaded from the Cologne AE scan
  page); the tool is not self-contained.
- **Misuse — editing `csl-orig/v02/ae/ae.txt` directly from a candidate
  file.** Every pipeline in this manual terminates in a *change file*
  applied by `updateByLine.py` and delivered as a consolidated batch PR per
  the [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md)
  — the `…prob.txt`/`spellchkLine.txt` outputs are candidates for human
  review, not corrections to apply straight to the canonical text.
- **Not for:** general Sanskrit lexicographic guidance — see
  [README.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/README.md)
  for what the repo/dictionary is, and
  [CLAUDE.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/CLAUDE.md)
  for the AI/code-session entry-format contract; this manual covers
  operating the tools only.

## Maintenance & sunset plan

- **Owning repo:** [sanskrit-lexicon/ApteES](https://github.com/sanskrit-lexicon/ApteES)
  (the tool pipelines and this manual live together; no separate pipeline
  repo owns them).
- **Keeps it alive:** whichever operator next re-runs a pipeline against
  fresh inputs (a rebuilt `ae.xml`, a refreshed
  [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) snapshot, or the
  current `csl-orig` `ae.txt`) and records the new counts here, plus routine
  Cologne-org maintainers doing the census-batch upkeep that produced this
  manual (handoff [H521](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H521-Fable_ApteES_tooling_manual_10.07.26.md)).
  A human (Dr. Mārcis Gasūns) owns the org and arbitrates any backlog item
  above requiring a judgment call (e.g. whether to build the IAST edition,
  backlog #3).
- **Archived/ended looks like:** the manual becomes historical-only if
  ApteES's three tool pipelines are superseded by a newer, unified Cologne
  tooling stack (there is no such migration planned as of this writing), or
  if the AE dictionary text itself is fully corrected and the correction
  workflow it feeds is retired. Until then, the manual is maintained
  in place — updated counts/backlog items get folded into
  [docs/TOOLING_MANUAL.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/docs/TOOLING_MANUAL.md)
  and this metadoc's revision history, not rewritten from scratch.

## Deprecation status

`active`

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/README.md) — repo overview + worked change-file example
- [CLAUDE.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/CLAUDE.md) — code contract with the annotated entry format
- [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/DATA_DICTIONARY.md) — tag reference
- [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — canonical delivery procedure
- Sibling census-batch manuals: [AP](https://github.com/sanskrit-lexicon/AP/blob/main/docs/PIPELINE_MANUAL.md) · [AP90](https://github.com/sanskrit-lexicon/AP90/blob/master/docs/PIPELINE_MANUAL.md) · [PWK](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md) · [AMAR](https://github.com/sanskrit-lexicon/AMAR/blob/main/docs/CONVERSION_MANUAL.md)

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial manual + this metadoc authored (H521); all dirs read first-hand; 6 traps recorded | Fable 5 (`claude-fable-5`) |
| 11-07-2026 | template v2 backfill (H663) | Sonnet 5 (`claude-sonnet-5`) |

_Dr. Mārcis Gasūns_
