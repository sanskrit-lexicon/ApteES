# ApteES - Apte English-Sanskrit Dictionary

<!-- BEGIN MANUAL: overview -->
ApteES is the working repository for the English-to-Sanskrit Apte dictionary
(`AE` in the CDSL dictionary codes).  The canonical source text lives in
[`csl-orig/v02/ae/ae.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/ae/ae.txt);
this repository keeps the inversion, spelling, markup, and issue-specific work
used to improve that source and its display.

## Primary data

| Item | Location | Notes |
|---|---|---|
| Canonical CDSL source | `csl-orig/v02/ae/ae.txt` | Target of accepted corrections. |
| Sanskrit inversion work | `ae_saninvert/` | Indexes Sanskrit words appearing in AE definitions. |
| Headword spell checking | `hwspellcheck/` | English headword spelling review using PyEnchant/Google Docs workflow notes. |
| Issue work | `issues/` | Issue-specific scripts and readmes. |
| Transcoding work | `transcode/` | Punctuation and notation conversion notes. |

## Directories

| Path | Purpose |
|---|---|
| `ae_saninvert/` | Builds inverted Sanskrit-word indexes from AE XML. |
| `hwspellcheck/` | English headword spell-checking and correction preparation. |
| `issues/` | One folder per active or historical issue; read `issues/readme.txt` first. |
| `transcode/` | Transcoding and punctuation experiments. |

## How work is done

The usual pattern is:

```text
AE source or XML -> local extract/check -> manual review -> change file/script -> csl-orig update
```

Do not treat generated candidate lists as corrections by themselves.  The
readmes in `ae_saninvert/` and `hwspellcheck/` show the expected review step:
suspects are separated into found/not-found, checked, and only then prepared as
changes.

## Common commands

Examples from existing notes:

```sh
python invert1.py ../../ae.xml invert1.txt
python invert2.py invert1.txt invert2.txt
python invert2_filter1.py 1 invert2.txt invert2_found1.txt invert2_notfound1.txt
python check1.py aehw2.txt aehw2_spellchk.txt
```

Several commands assume downloaded AE text/XML or an older local research
layout.  Confirm paths before rerunning.

## Data format

AE uses standard CDSL markup: `<L>` entry id, `<k1>` English headword,
`<k2>` secondary spelling when present, `<pc>` page/column, `<ls>` sources, and
`<ab>` abbreviations.  Sanskrit words inside the English-to-Sanskrit entries are
handled through the CDSL transliteration/display pipeline.

## Current status / open questions

- `ae_saninvert/` is discovery-oriented: not-found Sanskrit forms are candidates
  for review, not automatic errors.
- `hwspellcheck/` contains historical PyEnchant and Google Docs review notes;
  use them as provenance before re-running the spelling workflow.
- Issue folders are the safest entry point for recent changes.
<!-- END MANUAL: overview -->

## Issues

This repository uses the Sanskrit Lexicon unified issue taxonomy with:
- **9 type labels**: link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **3 severity levels**: minor, medium, hard
- **4 milestones**: Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

## GitHub Issue Conventions

All issues follow the unified taxonomy. See [CLAUDE.md](CLAUDE.md) for details.

---
*Updated by Cologne Issue Runbook*
