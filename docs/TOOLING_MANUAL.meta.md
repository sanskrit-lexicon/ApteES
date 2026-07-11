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
  [H521-Fable_ApteES_tooling_manual_10.07.26.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/H521-Fable_ApteES_tooling_manual_10.07.26.md)
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

_Dr. Mārcis Gasūns_
