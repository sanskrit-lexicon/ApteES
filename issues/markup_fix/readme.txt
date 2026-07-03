Counterpart of PWG/pwgissues/issue174/08_markup_fix.py
(see https://github.com/sanskrit-lexicon/PWG/issues/175
 and https://github.com/sanskrit-lexicon/PWK/issues/113).

Files in this folder:
  08_markup_fix.py        -- fixer + audit script for ae.txt
  test_markup_fix.py      -- synthetic tests
  ae_fixed.txt             -- byte-identical to source
  markup_fix_changes.txt  -- updateByLine log of auto-fixes
  markup_audit.txt        -- audit findings requiring human review
  ISSUE_COMMENT.md        -- GitHub issue body
  comment_markup_fix.md   -- same as ISSUE_COMMENT.md
  readme.txt              -- this file

Usage:
  python 08_markup_fix.py            # uses csl-orig/v02/ae/ae.txt by default
  python 08_markup_fix.py IN OUT     # custom paths
  python test_markup_fix.py          # run synthetic tests
