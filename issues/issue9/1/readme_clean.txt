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

-------------------------------------------------------------
05 ? ...START
cp temp_ae_04.txt temp_ae_05.txt
---
8587 matches in 7997 lines for ";#" in buffer: temp_ae_04.txt
11 matches for "#};" in buffer: temp_ae_04.txt
change all ';#}' to '#};' 

-------------------------------------------------------------

*************************************************************
-------------------------------------------------------------
10887 matches in 10105 lines for "‘" in buffer: temp_ae_1.txt
10943 matches in 10161 lines for "’" in buffer: temp_ae_1.txt

These should be the same.

------------------------------------------
in buffer: temp_ae_1.txt:

544 matches for "-$" 
541 matches for "^-" 
432 matches for "-<LB>-" 


8749 matches for "-#}$" 
8597 matches for "^{#-" 
37 matches for "^-{#"
40 matches for "#}-$"

7284 matches for "-#}<LB>{#-" 
4008 matches in 3507 lines for "\.,%"
8590 matches in 8126 lines for ";#}"

9697 matches in 9562 lines for ",#}"
20888 matches in 20112 lines for ",@}"
8121 matches in 7981 lines for "@} {%

1507 matches in 1501 lines for "{@-[A-Z]"
4728 matches in 3600 lines for "#} c\."    c. = "Causal"

257 matches for "-@}$"
1952 matches for "^{@-"

11271 matches for ",@}¦"
89 matches for "[^,]@}¦"
 (+ 11271 89) = 11360
  Last L is 11359

29 matches for "\.@}¦"  appear to be typos
