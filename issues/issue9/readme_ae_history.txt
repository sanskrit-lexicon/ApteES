
cd /c/xampp/htdocs/cologne/csl-orig

git log --follow --pretty=format:"%h %ad %s" --date=short -- v02/ae/ae.txt > temp_ae_history.txt

The history (newest to oldest) is shown below

3b990c8 2026-04-30 chh->ch. close #197
97ca509 2026-04-30 AE missing print change incorporated. Close https://github.com/sanskrit-lexicon/csl-corrections/issues/189
ab93968 2026-04-28 AE minor edit in Lnum
71b0710 2026-04-28 Corrections in AE which were noted in printchange file, but missing in the csl-orig file. See #87
e71b290 2026-04-27 AE ring above
3bb2826 2026-04-25 Terminal semicolon adjustments per https://github.com/sanskrit-lexicon/csl-corrections/issues/75
a0b406e 2026-04-25 AE changes per https://github.com/sanskrit-lexicon/csl-corrections/issues/75
3a45c5a 2026-04-25 DC 22 Apr 2026. See #168
17d36fc 2026-04-14 Daily corrections from 11 Apr 2026 to 13 Apr 2026
d6ce730 2026-02-04 close #2802
61b497f 2026-02-03 01/25/2026 18:33:40	ae			Help
555929d 2024-06-27 ae: user corrections
  NOTE: 405cab9 version of ae.txt is same as temp_ae_0_all.txt
40fcab9 2023-06-08 ae: User correction(s)
a8b57cd 2021-12-20 AE: User correction
4c74ae2 2021-12-17 ae: correct markup to expose a few headwords. Ref: https://github.com/sanskrit-lexicon/csl-devanagari/issues/26
5f3b1b2 2021-12-17 ae: remove <div n='lb'/> markup. Ref: https://github.com/sanskrit-lexicon/csl-devanagari/issues/26
17ad89c 2021-09-06 https://github.com/sanskrit-lexicon/CORRECTIONS/issues/92#issuecomment-913174476 corrections carried to csl-orig
f2734fb 2021-08-21 AE: adjust period character in {#X#} Devanagari
d43b57c 2021-03-20 AE: 34 #473, #474
34cdf28 2021-01-13 AE English word corrections. Ref: https://github.com/sanskrit-lexicon/csl-corrections/issues/42
504678a 2020-11-26 AE.  Correct line 84710
f5f3ed2 2020-11-26 AE English word corrections. Ref: https://github.com/sanskrit-lexicon/csl-corrections/issues/19#issuecomment-734530676
3d07067 2019-12-17 1 User correction for AE.
5e0f026 2019-11-04 reorganize so v00/csl-data/XXXScan/2020/orig/xxx.txt becomes v02/xxx/xxx.txt, and similarly for xxx_hwextra.txt
6f45dd5 2019-07-20 csl-orig initial commit
