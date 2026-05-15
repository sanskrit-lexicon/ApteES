# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ApteES** is the corrections and tooling repository for the Cologne digitization of Apte's *English-Sanskrit Dictionary* (AE). The canonical source data lives in `csl-orig/v02/ae/ae.txt`. This repo holds per-issue correction workflows, Sanskrit spell-checking scripts, and transcoding utilities.

Assumed local directory layout:
```
$BASE/sanskrit-lexicon/
  ApteES/        ← this repo
$BASE/cologne/
  csl-orig/      ← source data (ae.txt at v02/ae/ae.txt)
  csl-pywork/    ← build tools
```

## Architecture

| Directory | Purpose |
|---|---|
| `issues/` | Per-issue correction workflows (`issueNNN/` pattern) |
| `ae_saninvert/` | Sanskrit spell-checking via n-gram inversion against MW headwords |
| `hwspellcheck/` | Headword spell-check utilities |
| `transcode/` | Transcoding `ae.txt` to Devanagari; punctuation normalization |

### Issue correction pattern (`issues/issueNNN/`)

Each issue folder follows the same workflow:
1. Copy current `ae.txt` to a local `temp_ae_0.txt` (not tracked by git)
2. Apply corrections incrementally as `temp_ae_1.txt`, `temp_ae_2.txt`, etc.
3. Rebuild XML with `generate_dict.sh` and validate with `xmlchk_xampp.sh`
4. Commit the corrected file to `csl-orig`, then sync to Cologne
5. Commit issue documentation back here

### Sanskrit spell-check pipeline (`ae_saninvert/`)

Uses n-gram matching against MW headwords to flag likely misspellings in the Sanskrit portion of AE entries:
1. `invert1.py` — inverts AE Sanskrit words to SLP1 token list
2. `ngram.py` — generates n-gram frequency tables from MW headwords
3. `invert2.py` — scores AE Sanskrit words against MW n-gram tables; produces `found` / `notfound` lists
4. `filter_ngram.py` — filters low-confidence n-gram matches

### Transcoding pipeline (`transcode/`)

Converts `ae.txt` encoding to Devanagari for display:
- `ae_transcode.py` — runs the transcoder on `ae.txt` → `ae_deva.txt`
- `transcoder/` — SLP1 → Devanagari mapping tables
- `punctuation/` — punctuation normalization filters

## Common Commands

### Apply line-level corrections (from any `issues/issueNNN/` dir)
```bash
python updateByLine.py <input_file> <changein_file> <output_file>
```
Change file format: paired `NNN old <original>` / `NNN new <replacement>` lines; `;` prefix for comments.

### Rebuild and validate XML (from `csl-pywork/v02/`)
```bash
cd $BASE/cologne/csl-pywork/v02
sh generate_dict.sh ae ../../AEScan/2020
sh xmlchk_xampp.sh ae
```

### Transcode to Devanagari (from `transcode/`)
```bash
python ae_transcode.py ae.txt ae_deva.txt
```

## Dependencies

- **Python 3**
- **ae.txt** — in `$BASE/cologne/csl-orig/v02/ae/ae.txt`
