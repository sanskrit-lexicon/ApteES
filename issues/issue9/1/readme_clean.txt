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
