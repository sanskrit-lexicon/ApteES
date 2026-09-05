_Created: 22-05-2026 · Last updated: 05-09-2026_

### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `ae.txt`.

I ran the same two-job recipe over `csl-orig/v02/ae/ae.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `issues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — please review the findings listed below.

## Markup fixer + audit for `ae.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>X</ab> Y</ab>` | `<ab>X Y</ab>` |
| `<s> word </s>` | `<s>word</s>` |
| `<ab> word </ab>` | `<ab>word</ab>` |
| `<lex> word </lex>` | `<lex>word</lex>` |

Whitespace trimming applies to all 5 paired tag(s) in `ae.txt`: `<s>`, `<ab>`, `<lex>`, `<i>`, `<ls>`. The original file is never modified — output goes to `ae_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format). **Output is byte-identical to source** (no auto-fixes triggered).

### Closing-tag inventory in current `ae.txt`

| Tag | Count |
|---|---:|
| `</s>` | 72 |
| `</856)>` | ? |
| `</ab>` | 35 |
| `</746)>` | ? |
| `</lex>` | 22 |
| `</879)>` | ? |
| `</i>` | 3 |
| `</028)>` | ? |
| `</ls>` | 1 |
| `</141)>` | ? |

### What it found in current `ae.txt`

- 0 whitespace trims — byte-identical to source.
- 207 within-line adjacent `</ab> <ab>` pairs for verification.
- 3 non-standard `<ab n="…">` attribute values: `n="Madalekha"` (1), `n="Vaināsika"` (1), `n="Manmatha Natha Dutt"` (1) — readable English expansions.
- 161 `{{old → new || …}}` correction records present.

### Usage

```
cd issues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/ae/ae.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `ae_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

1 `<ab n="?">` placeholder: 0; `<ab n="…">` non-standard: 3.

### Severity

`minor`

_Dr. Mārcis Gasūns_
