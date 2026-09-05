_Created: 15-05-2026 · Last updated: 05-09-2026_

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ApteES** is the development and correction repository for **Vaman Shivram Apte's *The Student's English-Sanskrit Dictionary***, an English→Sanskrit dictionary, within the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) (CDSL).

- **Canonical source text**: [`csl-orig/v02/ae/ae.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/main/v02/ae/ae.txt) (English headwords) — corrections are applied to that file, not stored here.
- This repository holds **development artifacts**: corrections, markup, comparison, and per-issue working files.
- A **reverse-direction** dictionary: English headwords (in `{@…@}`) with Sanskrit equivalents (SLP1, in `<s>…</s>`) and circled sense markers (Ⓐ, Ⓑ …). One of several English→Sanskrit works in CDSL (alongside the Monier-Williams *MWE* 1851 and Borooah *BOR* 1877). Its markup differs from the Sanskrit→X dictionaries — see **Data format** in [CLAUDE.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/CLAUDE.md).

## Architecture

| Path | Purpose |
|---|---|
| `.github/` | GitHub Actions workflows + issue templates |
| `ae_saninvert/` | `ae_saninvert/` working files |
| `hwspellcheck/` | `hwspellcheck/` working files |
| `issues/` | Per-issue working files |
| `transcode/` | `transcode/` working files |

## Key commands

Corrections follow the CDSL `updateByLine.py` pattern, applied against the csl-orig source:

```sh
python updateByLine.py <input> <changefile> <output>
```

Change-file format (paired lines; `;`-prefixed comments):

```
1234 old <original line>
1234 new <replacement line>
```
Supports `new` (replace), `ins` (insert after), `del` (delete). All files UTF-8 (**no BOM**).

## Data format

ApteES entries use standard CDSL Sanskrit-lexicography markup. See [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/ApteES/blob/main/DATA_DICTIONARY.md) for the full tag reference.

| Tag | Role |
|---|---|
| `<L>NNNN<pc>PPP` | Entry begin, with print page-column ref |
| `<k1>`, `<k2>` | English headword |
| `{@…@}` | English headword / lemma display (italic) |
| `<s>…</s>` | Sanskrit equivalent (SLP1) |
| `Ⓐ Ⓑ …` | Circled sense / sub-sense markers |
| `<ab>…</ab>` | Grammatical abbreviation (e.g. `ex.`, `part.`, `dat.`) |
| `¦` | Headword / definition separator |
| `<LEND>` | Entry end |

Annotated example — the first entry of `ae.txt`:

```
<L>1<pc>001<k1>a<k2>a, an
{@A@}, {@An@}¦,Ⓐ(As an article) not <ab>ex.</ab>; ‘a man’ <s>naraH</s>.
Ⓑ{@2@} (One) <s>eka</s>.
Ⓑ{@3@} (Indefinite) <s>kiM</s> with <s>cit, cana</s> or <s>api</s>.
Ⓑ{@4@} With <ab>part.</ab>, <ab>ex.</ab> by <ab>dat.</ab> or <ab>inf.</ab>; ‘set out a-hunting’ <s>mfgayAyE</s> or <s>mfgayAM kartuM pratasTe</s>; ‘fell a-weeping’ <s>kraMdituM pravfttaH</s>.
Ⓑ{@5@} (Every) <s>prati</s> in <ab>comp.</ab>, or by repetition of word; ‘100 <ab>Rs.</ab> a day’ <s>pratidinaM</s> or <s>dine dine SatarUpakaM</s>.
Ⓑ{@6@} (Species) <s>viSezaH, BedaH</s>, in <ab>comp.</ab>; ‘dog is an animal’ <s>SvA prARiviSezaH</s>. 
<LEND>
```

## Dependencies

- Python 3 (correction and comparison scripts).
- No build step in this repo; XML and web display are generated centrally from `csl-orig` via `csl-pywork`.

## GitHub Issue Conventions

This repository uses the Cologne dictionary-repo issue taxonomy. Every issue has exactly one **type**, one **severity**, and one **milestone**:

- **Type** (9): link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **Severity** (3): minor, medium, hard
- **Milestone** (4): Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

See the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md) for label definitions and the type→milestone mapping.

_Dr. Mārcis Gasūns_
