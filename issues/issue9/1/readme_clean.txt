# 1/cleanup 
cd issue9
# initialise temp_ae_1.txt
cp 0/temp_ae_0.txt 1/temp_ae_00.txt
cd 1

---------
-- 01
487 matches for "-$" in buffer: temp_ae_00.txt
---
78 matches for "^-{"
22 matches for "}-$"
113 matches for "‘.\.-<LB>[^‘]+’" in buffer: temp_ae_00.txt

These are irregular.
cp temp_ae_00.txt temp_ae_01.txt
Manual changes to ae_01
‘\(.\)\.-<LB>\([^‘]+’\)  ->  ‘\1. \2<LB>  [Emacs regex replacement]

There remain 41 matches for "^-{" of form "{%" or "{@"

python diff_to_changes_dict.py temp_ae_00.txt temp_ae_01.txt changes_01.txt
418 changes written to changes_01.txt

----------
02
321 matches for "-$" in buffer: temp_ae_01.txt
---
Example:
OLD:
{#-vfj#} 10 (acc.); ‘has a. ed from eat-
-ing flesh’ {#nivfttamAMso janakaH#} (U. 4).
NEW:
{#-vfj#} 10 (acc.); ‘has a. ed from eating
flesh’ {#nivfttamAMso janakaH#} (U. 4).
---
Example: intervening [Page  (9 cases)
OLD:
{#-yAta, sahita, sa#} in comp.; ‘a. by maid-
[Page24]
-servants’ {#saKIgaRaparivftA, saKIparivArA#}.
NEW:
{#-yAta, sahita, sa#} in comp.; ‘a. by maidservants’ 
[Page24]
{#saKIgaRaparivftA, saKIparivArA#}.


python clean/hyphen_merge.py 01 temp_ae_01.txt changes_02.txt
286 entries changed
589 changes written to change2_02.txt


python updateByLine.py temp_ae_01.txt changes_02.txt temp_ae_02.txt
589 change transactions from changes_02.txt

-------------------------------------------------------------
03
7285 matches for "-#}<LB>{#-" in buffer: temp_ae_02.txt

Example:
OLD:
{@Abandon,@}¦ {%v. t.%} {#tyaj#} 1 P, {#hA#} 3 P, {#vi-ut-#}
{#-sfj#} 6 P, {#ujJ#} 6 P, {#apAs#} 4 P, {#rah#} 1 P,
NEW:
{@Abandon,@}¦ {%v. t.%} {#tyaj#} 1 P, {#hA#} 3 P, {#vi-ut-sfj#} 
6 P, {#ujJ#} 6 P, {#apAs#} 4 P, {#rah#} 1 P,
---
Example:
OLD:
to his fate’ {#dEvADInaH kftaH, yadBAvi tadBa-#}
{#-vatu ityuktvA sa parityaktaH#}. {@-ment,@} {%s.%}
NEW:
to his fate’ {#dEvADInaH kftaH, yadBAvi tadBa-vatu ityuktvA sa parityaktaH#}.
{@-ment,@} {%s.%}

NOTE: How to know this is better written as 'taBavatu' (no -) ?
Thus we keep 1 of the '-' 
---
Example:  no '-' on next line:
OLD:
6 P, {#samas#} 4 P, {#hras#} c. {@-ion,@} {%s.%} {#saMkzepaH-#}
{#paNaM#}.
NEW:
6 P, {#samas#} 4 P, {#hras#} c. {@-ion,@} {%s.%} {#saMkzepaH-paNaM#}.
EMPTY LINE

python clean/hyphen_merge.py 02 temp_ae_02.txt changes_03.txt
change_groups_02: 4138 entries changed
change_groups_02a: 29 entries changed
change_groups_02b: 215 entries changed
change_groups_02c: 12 entries changed
change_groups_02d: 37 entries changed


python updateByLine.py temp_ae_02.txt changes_03.txt temp_ae_03.txt
15917 change transactions from changes_03.txt

-------------------------------------------------------------
04
89 matches for "-#}$" in buffer: temp_ae_03.txt
lines ending in '-#}' handled manually
Also '-{@' -> '{@-'  ~15
Also '-{#' -> '{#-'  ~20
cp temp_ae_03.txt temp_ae_04.txt
edit temp_ae_04.txt manually
When done:
python diff_to_changes_dict.py temp_ae_03.txt temp_ae_04.txt changes_04.txt
260 changes written to changes_04.txt

There are still numerous Devanagari segments ending in '-',
but none at the end of a line.

TODO:
232 matches in 230 lines for "-#}" in buffer: temp_ae_04.txt
 Not sure how to change these.
 Apte's use of '-' is either not-systematic of
based on a system that Jim doesn't understand.
-------------------------------------------------------------
05
Miscellaneous corrections (typos)
cp temp_ae_04.txt temp_ae_05.txt
# manual edit of 05


10856 matches in 10093 lines for "<p>" in buffer: temp_ae_05.txt
10903 matches in 10126 lines for "</p>"
(- 10903 10856) 47
# note use of '//' in command-line argument.
python clean/unbalanced.py '<p>' '<//p>' temp_ae_04.txt temp_ae_05work.txt
145
python clean/unbalanced.py '<p>' '<//p>' temp_ae_05work.txt temp_ae_05worka.txt
9
python clean/unbalanced.py '<p>' '<//p>' temp_ae_05worka.txt temp_ae_05workb.txt
1
python clean/unbalanced.py '<p>' '<//p>' temp_ae_05workb.txt temp_ae_05workc.txt
0
# all done
mv temp_ae_05workc.txt temp_ae_05.txt
# edit temp_ae_05.txt
  and replace <p> by ‘   AND replace </p> by ’
  Also several other changes.

python diff_to_changes_dict.py temp_ae_04.txt temp_ae_05.txt changes_05.txt
642 changes

-----------
Now, There may be other changes to 05 in future.

python diff_to_changes_dict.py temp_ae_04.txt temp_ae_05workd.txt changes_05.txt

-------------------------------------------------------------
06
global punctuation changes
---

python clean/punct.py 01 temp_ae_05.txt changes_06.txt
Case 01a, 11271 entries changed: ",@}¦" -> "@}¦,"
Case 01a1, 29 entries changed: "\.@}¦" -> "@}¦,"
Case 01b, 322 entries changed: ";@}" -> "@};"
Case 01c, 4853 entries changed: ",@}" -> "@},"
Case 01d, 3330 entries changed: ";#}" -> "#};"
Case 01e, 4248 entries changed: ",#}" -> "#},"
Case 01f, 414 entries changed: ";%}" -> "%};"
Case 01g, 2376 entries changed: ",%}" -> "%},"
Case 01h, 1397 entries changed: "{@([A-Z][^@]+)\.@}" -> "{@\1@}."
Case 01i, 205 entries changed: "{@([^@]+)-@}\n{@-([^@]+)@}([,;.]) " -> "{@\1\2@}\3\n"
Case 01j, 4 entries changed: "{@([^@]+)-@}\n{@-([^@]+)([.])@} " -> "{@\1\2@}\3\n"
Case 01k, 2423 entries changed: "{%-" -> "- {%"
Case 01l, 21 entries changed: ";’" -> "’;"
Case 01m, 97 entries changed: ",’" -> "’,"

35280 change transactions written to changes_06.txt

python updateByLine.py temp_ae_05.txt changes_06.txt temp_ae_06.txt
35280 change transactions from changes_06.txt

-------------------------------------------------------------
07 clean up {%X%}

python clean/regex_instances.py 1 '{%.*?%}' temp_ae_06.txt temp_regex_italics_06.txt
166 lines written to temp_regex_italics.txt (distinct instances of italics)
34079 total number of instancees of italics.

cp temp_regex_italics.txt replacements_06.txt
# fill in the changes

# generate changes based on the replacements
python clean/punct.py 02 temp_ae_06.txt changes_07.txt replacements_06.txt
88835 lines read from temp_ae_06.txt
22990 groups 11364 entries
136 lines read from replacements_06.txt
change_groups_02: 971 entries changed
1020 changes written to changes_07.txt


python updateByLine.py temp_ae_06.txt changes_07.txt temp_ae_07.txt
1020 change transactions from changes_07.txt

python clean/regex_instances.py 2 '{%.*?%}' temp_ae_07.txt temp_regex_italics_07.txt
34 distinct instances found of regex= {%.*?%}
34779 total instances

-------------------------------------------------------------
08
Close quotes
3136 matches for "‘[^’]*$" in buffer: temp_ae_07.txt
3135 matches for "^[^‘]*’" in buffer: temp_ae_07.txt

’ occurs followed by
space, end of line, semicolon, period

python clean/quote_merge.py 01 temp_ae_07.txt changes_08.txt

python updateByLine.py temp_ae_07.txt changes_08.txt temp_ae_08.txt
5990 change transactions from changes_08.txt
START
-------------------------------------------------------------
09
Close parens
696 matches for "([^)]*$" in buffer: temp_ae_08.txt

Added about 300 manual changes to temp_ae_05.txt to resolve
valid coding of parentheses.

The identification was helped by
a) changing parens to <F>,</F>
python clean/xmlbalance.py '(,<F>;),<//F>' temp_ae_08.txt temp_ae_08work.txt
b) Noting unbalanced 
python clean/unbalanced.py '<F>' '<//F>' temp_ae_08work.txt temp_ae_08worka.txt
and constructing/validating the 08work version based on temp_ae_08work.txt

Now ready to merge so no open parentheses at end of lines.
python clean/paren_merge.py 01 temp_ae_08.txt changes_09.txt

python updateByLine.py temp_ae_08.txt changes_09.txt temp_ae_09.txt
1144 change transactions from changes_09.txt


python clean/regex_instances.py 2 '{%.*?%}' temp_ae_09.txt regex_italics_09.txt
34 distinct instances found of regex= {%.*?%}
34779 total instances

python clean/regex_instances.py 2 '‘.*?’' temp_ae_09.txt regex_quote_09.txt
10379 distinct instances found of regex= ‘.*?’
10917 total instances

-------------------------------------------------------------
05-15-2024
# push to github.
# Request Andhrabharati comments

*************************************************************
05-17-2024
Version 10 for further manual corrections
cp temp_ae_09.txt temp_ae_10.txt

---
35 matches in 34 lines for "@[0-9]@} [APU]\b" in buffer: temp_ae_09.txt
None in temp_ae_10
---
538 matches in 514 lines for "‘[^.’]+’" in buffer: temp_ae_09.txt
413 matches in 390 lines for "‘[^.’]+’" in buffer: temp_ae_10.txt
---
13 matches for "{@[^@]*‘" in buffer: temp_ae_09.txt
None in temp_ae_10
---
26 matches for "‘[^’]*\[Page" in buffer: temp_ae_09.txt
None in temp_ae_10
---
3 matches for "([^)]*\[Page" in buffer: temp_ae_09.txt
---
æ changed - 12 instances changed to modern spelling. print changes
---
5 matches for "œ" in buffer: temp_ae_10.txt  print changes
 Change to modern spelling.
---
# mark_lnums helps identify lines needing attention.
cp temp_ae_10.txt tempprev_ae_10.txt  # save prior copy, to be safe!

# mark certain lines to begin with temporary markup'** ' Overwrite temp_ae_10.txt
#python clean/marklnum.py '01' tempprev_ae_10.txt temp_ae_10.txt
python clean/marklnum.py '02' tempprev_ae_10.txt temp_ae_10.txt
# manual edit temp_ae_10.txt
# When done,remove the '** ' temporary markup from temp_ae_10.txt
---
'\n.' -> '.\n'  ~1200 instances.

python diff_to_changes_dict.py temp_ae_09.txt temp_ae_10.txt changes_10.txt
2998 changes written to changes_10.txt

-------------------------------------------------------------
11
422 matches for "{%See%}\n{@" in buffer: temp_ae_10.txt

python clean/see_merge.py 01 temp_ae_10.txt changes_11.txt
change_groups_01: 406 entries changed
842 changes written to changes_11.txt

python updateByLine.py temp_ae_10.txt changes_11.txt temp_ae_11.txt
842 change transactions from changes_11.txt

-------------------------------------------------------------
12
361 matches for "\. [0-9]+@}" in buffer: temp_ae_11.txt
{@House. 2@}
513 matches in 506 lines for "{@[^-][^@]+ -" in buffer: temp_ae_11.txt
{@Abhor. -ion@}

python clean/bold.py 01 temp_ae_11.txt changes_12.txt
Case 01a, 320 entries changed: "\. ([0-9]+)@}" -> "@}. {@\1@}"
Case 01b, 461 entries changed: "{@([^-][^@]+) -" -> "{@\1@} {@-"
Case 01c, 13 entries changed: "{@(-[A-Z][a-z]+), (-[A-Z][a-z]+)@}" -> "{@\1@}, {
Case 01d, 433 entries changed: "\.@}" -> "@}."
Case 01e, 103 entries changed: ",@}" -> "@},"
Case 01f, 142 entries changed: "{@([A-Z][a-z]*), ([A-Z][a-z]*)@}¦" -> "{@\1@}, {@\2@}¦"
Case 01g, 13 entries changed: "{@-([A-Z][a-z]*), ?([A-Z][a-z]*)@}" -> "{@-1@}, {@\2@}"
Case 01h, 222 entries changed: "{@-([a-z]*), ?-([a-z]*)@}" -> "{@-\1@}, {@-\2@}"
Case 01i, 125 entries changed: "{%See%} {@([A-Z][a-z]*), ?([A-Z][a-z]*)@}" -> "{%See%} {@\1@}, {@\2@}"
Case 01j, 68 entries changed: "{@(-[a-z]*), ?(-[A-Z][a-z]*)@}" -> "{@\1@}, {@\2@}"
Case 01k, 23 entries changed: "{@(-[A-Z][a-z]*), ?(-[a-z]*)@}" -> "{@\1@}, {@\2@}"
Case 01l, 121 entries changed: "{@([0-9]+) ([A-Z][a-z]*)@}" -> "{@\1@} {@\2@}"
Case 01m, 26 entries changed: "{@(-[a-z]+), ([A-Z][a-z]+)@}" -> "{@\1@}, {@-\2@}"

python updateByLine.py temp_ae_11.txt changes_12.txt temp_ae_12.txt
1624 change transactions from changes_12.txt

python clean/regex_instances.py 2 '{@[^@]*?@}' temp_ae_12.txt temp_regex_bold_12.txt
14291 distinct instances found of regex= {@[^@]*?@}
33897 total instances

-------------------------------------------------------------
uploading version 12.

-------------------------------------------------------------
05-20-2024
cp temp_ae_12.txt temp_ae_13.txt
Manual editing

python diff_to_changes_dict.py temp_ae_12.txt temp_ae_13.txt changes_13.txt
118

python clean/needtomerge.py 01 temp_ae_13.txt temp_needtomerge_13.txt

python clean/regex_instances.py 2 '..¦....' temp_ae_13.txt temp_regex_brokenbar_13.txt

python clean/regex_instances.py 2 '¦, {%.*?%}' temp_ae_13.txt temp_regex_brokenbar_13.txt
---
print change:
<L>759<pc>027<k1>bamboo<k2>bamboo
{@Bamboo@}¦, {%v.%} -> {%m.%}
---
TODO: should be the same!
grep -E "¦" temp_ae_13.txt | wc -l
11358

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue9/1 (master)
$ grep -E "<L>" temp_ae_13.txt | wc -l
11363

-------------------------------------------------------------
Notes to AB:
---
old:
<L>10463<pc>471<k1>to<k2>to
{@To@}¦{@-night@}, {%adv.%} {#adya rAtrO, naktaM#}.
new:
<L>10463<pc>471<k1>to<k2>to
{@To@}¦{@-night@}, {%adv.%} {#adya rAtrO, naktaM#}.
---
-------------------------------------------------------------
05-22-2024
ABmark directory
Ref: https://github.com/sanskrit-lexicon/ApteES/files/15392949/temp_ae_09D.zip
---
temp_ae_09D.txt  Andhrabharati markup of cdsl version 9. See issues/9 comments.
temp_ae_09D_cdsl.txt  Change of three symbols for emacs ease.
see ABmark/readme.txt for details.
---
cp temp_ae_09D_cdsl.txt temp_ae_09D_cdsl_1.txt
manual edit temp_ae_09D_cdsl_1.txt for changes

----------------------------------------------

---
# Resolve some differences in headwords
python clean/hwcmp.py temp_ae_13.txt ABmark/temp_ae_09D_cdsl_1.txt hwcmp_13_ABmark.txt
## make changes to both input files until there are no
differences in metalines.
----

# differences in the text preceding broken-bar.
python clean/hwcmpbb.py temp_ae_13.txt ABmark/temp_ae_09D_cdsl_1.txt hwcmpbb_13_ABmark.txt
# about 300 differences found.
# For now, don't resolve these differences.
# version 13 has been changed since the version 9 that
# AB worked with.
----

# differences in 'extra' headwords after broken bar.
# First, resolve the differences in number of extra
# headwords.
# not used: python clean/hwxnum.py temp_ae_13.txt ABmark/temp_ae_09D_cdsl_1.txt hwxnum_13_ABmark.txt

python clean/hwsections.py 1 temp_ae_13.txt ABmark/temp_ae_09D_cdsl_1.txt temp_hwsections_13_1.txt
540 ndifferences in write_diffs_1

# make changes to the two files to resolve these differences
Rerun,
python clean/hwsections.py 1 temp_ae_13.txt ABmark/temp_ae_09D_cdsl_1.txt temp_hwsections_13_1a.txt
# no differences.  So this analysis is complete.

9064 Ⓝ,
----------------------------------------
13a.  Multiple-subhws.
cp temp_ae_13.txt temp_ae_13a.txt
cp ABmark/temp_ae_09D_cdsl_1.txt ABmark/temp_ae_09D_cdsl_1a.txt
# manual changes to temp_ae_13a.txt and to
# ABmark/temp_ae_09D_cdsl_1a.txt

After changes made,
python diff_to_changes_dict.py temp_ae_13.txt temp_ae_13a.txt changes_13a.txt
182 changes written to changes_13a.txt
---
# Emacs regex-replace in temp_ae_13a.txt
\({@-[^@]*@}[,]\)<LB>\({@-[^@]*@}[, ]+\) → \1 \2
---
# Emacs regex-replace in ABmark/temp_ae_09D_cdsl_1a.txt
" , •➔✦{% → ,➔ •"   replaced 1034 occurrences

1110 matches for "^➔✦" in buffer: temp_ae_09D_cdsl_1a.txt

1002 matches for ", •<LB>➔✦{%" in buffer: temp_ae_09D_cdsl_1a.txt

9068 matches in 8807 lines for "Ⓝ" in buffer: temp_ae_09D_cdsl_1a.txt
8886 matches in 8642 lines for "Ⓝ[^•Ⓝ➔]*?➔" in buffer: temp_ae_09D_cdsl_1a.txt
8886 matches in 8642 lines for "Ⓝ[^•]*?➔" in buffer: temp_ae_09D_cdsl_1a.txt

# Emacs regex-replace in ABmark/temp_ae_09D_cdsl_1a.txt
"\(Ⓝ{@[^@]*@},\) •<LB>➔" → "\1➔ •<LB>"  replace 56 occurrences
8942 matches in 8642 lines for "Ⓝ[^•]*?➔" in buffer: temp_ae_09D_cdsl_1a.txt

89 matches for "Ⓝ{@[^@]*@}, •<LB>{@[^@]*@},➔" in buffer: temp_ae_09D_cdsl_1a.txt
# Emacs regex-replace in ABmark/temp_ae_09D_cdsl_1a.txt
"\(Ⓝ{@[^@]*@},\) •<LB>\({@[^@]*@},➔\) → \1 \2 •<LB>
  Replaced 89 occurrences

9031 matches in 8774 lines for "Ⓝ[^•]*?➔" in buffer: temp_ae_09D_cdsl_1a.txt


391 matches for "Ⓝ{@[^@]*@}, {@" in buffer: temp_ae_09D_cdsl_1.txt

python clean/hwsections.py 2 temp_ae_13a.txt ABmark/temp_ae_09D_cdsl_1.txt temp_hwsections_13_2.txt

python clean/hwsections.py 3  ABmark/temp_ae_09D_cdsl_1a.txt ABmark/temp_ae_09D_cdsl_1a.txt temp_hwsections_13_3.txt

Reorg of ABmark/temp_ae_09D_cdsl_1a.txt by Jim at
<L>574<pc>021<k1>aspire
<L>1007<pc>034<k1>bigotry
<L>1697<pc>057<k1>chirp
# now:
9068 matches in 8807 lines for "Ⓝ[^•]*?➔" in buffer: temp_ae_09D_cdsl_1a.txt
9068 matches in 8807 lines for "Ⓝ" in buffer: temp_ae_09D_cdsl_1a.txt

python clean/hwsections.py 2 temp_ae_13a.txt ABmark/temp_ae_09D_cdsl_1a.txt temp_hwsections_13a_1a.txt

----------------------------------------
13b
Add ⓃX➔ markup to 13a.
cp temp_ae_13a.txt temp_ae_13b.txt
After changes, generate changes file.
python diff_to_changes_dict.py temp_ae_13a.txt temp_ae_13b.txt changes_13b.txt
8859 changes written to changes_13b.txt
--- 3 subhws  5 instances
Example: {@-a@}, {@-b@}, {@-c@} -> Ⓝ{@_a@}, {@_b@}, {@_c@}➔
"{@-\([^@]*\)@}, {@-\([^@]*\)@}, {@-\([^@]*\)@}" →
"Ⓝ{@_\1@}, {@_\2@}, {@_\3@}➔"

--- 2 subhws  478 instances
Example: {@-a@}, {@-b@} -> Ⓝ{@_a@}, {@_b@}➔
"{@-\([^@]*\)@}, {@-\([^@]*\)@}" →
"Ⓝ{@_\1@}, {@_\2@}➔"

--- 1 subhws  8646 instances
Example: {@-a@} -> Ⓝ{@_a@}➔
"{@-\([^@]*\)@}" →
"Ⓝ{@_\1@}➔"

9129 matches in 8851 lines for "Ⓝ" in buffer: temp_ae_13b.txt
whereas AB has
9068 matches in 8807 lines for "Ⓝ" in buffer: temp_ae_09D_cdsl_1a.txt

(- 9129 9068) = 61  'extra' Ⓝ  in 13b. Why?

python clean/hwsections.py 4 temp_ae_13b.txt ABmark/temp_ae_09D_cdsl_1a.txt temp_hwsections_4_13b_1a.txt
61 ndifferences 
# these 61 diffs resolved by edition 13b and also AB-1a.
9068 matches in 8803 lines for "Ⓝ" in buffer: temp_ae_13b.txt
9068 matches in 8807 lines for "Ⓝ" in buffer: temp_ae_09D_cdsl_1a.txt

So now same number of Ⓝ in 13b and AB-1a
and Ⓝ.*?➔ is on same line for both 13b and AB-1a, with 9068 for both.

-----------
#check that same number of {@X@} within each Ⓝ.*?➔

python clean/hwsections.py 5 temp_ae_13b.txt ABmark/temp_ae_09D_cdsl_1a.txt temp_hwsections_5_13b_1a.txt
# differences resolved
-----------
#check that same number of {@X@} within bbline before ¦ agrees

python clean/hwsections.py 6 temp_ae_13b.txt ABmark/temp_ae_09D_cdsl_1a.txt temp_hwsections_6_13b_1a.txt
45 ndifferences
# Edit 13b and AB-1a to resolve diffs
Done.

python diff_to_changes_dict.py temp_ae_13a.txt temp_ae_13b.txt changes_13b.txt

-----------------
13c
cp temp_ae_13b.txt temp_ae_13c.txt  # move trailing comma inside
Many changes.  After 13c is finished, generate change file
python diff_to_changes_dict.py temp_ae_13b.txt temp_ae_13c.txt changes_13c.txt
8684 changes written to changes_13c.txt

BEGIN: notes on the changes made in 13c.

# "Ⓝ\([^➔]*\)➔," -> "Ⓝ\1,➔"  8939 replacements.

# Also change (to avoid duplicate L's in version 15 below
In preparation for future steps where ⓃX➔, lines will be new entries
Make these changes in 13c, and also in ABmark/temp_ae_09D_cdsl_1a.txt
---
<L>5754.1<pc>239<k1>invincible<k2>invincible<e>1
<L>5754.5<pc>239<k1>invincible<k2>invincible<e>1
---
<L>9035.1<pc><k1>ruffian<k2>ruffian
<L>9035.5<pc><k1>ruffian<k2>ruffian
---
<L>9036.1<pc>403<k1>rug<k2>rug
<L>9036.5<pc>403<k1>rug<k2>rug
---
<L>10018.1<pc>454<k1>suburb<k2>suburb
<L>10018.5<pc>454<k1>suburb<k2>suburb
---
<L>11310.1<pc>499<k1>wrist<k2>wrist
<L>11310.5<pc>499<k1>wrist<k2>wrist
----------------------------------------
----------------------------------------
misc. observations
20427 matches in 19964 lines for "➔✦" in buffer: temp_ae_09D_cdsl_1.txt
19737 matches in 19319 lines for "➔✦{%" in buffer: temp_ae_09D_cdsl_1.txt

690 matches in 675 lines for "➔✦[^{]" in buffer: temp_ae_09D_cdsl_1.txt

397 matches in 396 lines for "{@-[^@]*@}, {@-" in buffer: temp_ae_13.txt


python clean/regex_instances.py 1 '{%.*?%}' temp_ae_06.txt temp_regex_italics_06.txt

END: notes on the changes made in 13c.

------------
notes re version 13. A few 'reorg' by AB
---
<L>4807<pc>198<k1>haste<k2>haste
AB 09D  reorganizes near the (two) '-en' forms
<L>6311<pc>268<k1>loose  Similarly  '-en'
<L>7099<pc>307<k1>niggard Similar with -ly
<L>8483<pc>371<k1>push Similarly with -ing
<L>9375<pc>421<k1>shake  similarly -ing
<L>9445<pc>424<k1>shudder   similarly -ing
<L>9609<pc>432<k1>snatch similarly -ing
<L>9912<pc>448<k1>stoop similarly -ing
<L>10142<pc>460<k1>swell similarly -ing
and a few more ...
---
***************************************
version 14
the AB version has expanded the '-ly' type headwords, both for the
main entry (before ¦) and in Ⓝ.*? subheadwords.
Apply these expansions to version 13c.

python clean/hwexpand.py temp_ae_13c.txt ABmark/temp_ae_09D_cdsl_1a.txt temp_ae_14.txt
replacehws_main: 250 groups changed
replacehws_sub: 4670 groups changed

python diff_to_changes_dict.py temp_ae_13c.txt temp_ae_14.txt changes_14.txt
9051 changes written to changes_14.txt

****************************************
The subgoal now is to generate 'entries' using the subentries ⓃX➔

python clean/hwcount.py 1 temp_ae_14.txt temp_hwcout_1_14.txt
26 entries have 10 or more subentries.  Max # subentries is 20. (hw='set')
# this info will be useful when generating L-numbers for the new subentries.

python clean/subhws.py temp_ae_14.txt temp_ae_15.txt

-----
version ab2 #so we can do 'sh redolocal.sh ab1a'

cp ABmark/temp_ae_09D_cdsl_1a.txt temp_ae_ab1a.txt

python clean/subhws.py temp_ae_ab1a.txt temp_ae_ab2.txt

---------------
# compare headwords of 15 and ab2
python clean/hwcmp.py temp_ae_15.txt temp_ae_ab2.txt  temp_hwcmp_15_ab2.txt
# There are several differences.
# revise versions 13c to resolve differences.
# Then recreate versions 14 and 15

Now the metalines are the same for versions 15 and ab2 !

# compare the bb line (^.*¦)
python clean/hwcmpbb.py temp_ae_15.txt temp_ae_ab2.txt temp_hwcmpbb_15_ab2.txt
# 5 written to temp_hwcmpbb_15_ab2.txt
Some revisions.
After revision, versions 15 and ab2 agree in the text before ¦

----------------------------------------
05-27-2024  upload
zip temp_ae_15.zip temp_ae_15.txt
zip temp_ae_ab2.zip temp_ae_ab2.txt

git add .
git commit -m "versions 15 and ab2. <e>1 and <e>2. #9"
git push

----------------------------------------
Remove unneeded lines  THIS SECTION SKIPPED

Create version 14 and temp_ae_09D_cdsl_2.txt
# remove blank lines, and lines between entries.
python clean/removelines.py temp_ae_13.txt temp_ae_14x.txt
88835 lines read from temp_ae_13.txt
23000 groups 11359 entries
75066 written to temp_ae_14x.txt
---------------
python clean/removelines.py ABmark/temp_ae_09D_cdsl_1a.txt ABmark/temp_ae_09D_cdsl_2x.txt 
88843 lines read from ABmark/temp_ae_09D_cdsl_1.txt
23005 groups 11359 entries
77195 written to ABmark/temp_ae_09D_cdsl_2x.txt


----------------------------------------

python clean/fmt_1.py cdsl temp_ae_14x.txt temp_ae_15.txt

python clean/fmt_1.py ab ABmark/temp_ae_09D_cdsl_2x.txt ABmark/temp_ae_09D_cdsl_3.txt


---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
