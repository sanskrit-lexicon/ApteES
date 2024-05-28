
version 09D contains extended ascii characters that are not displayed in
Emacs using mono-spaced fonts.

python ea.py temp_ae_09D.txt temp_ae_09D_ea.txt
30 extended ascii counts written to temp_ae_09D_ea.txt

python ea1.py issue_9_guide.txt  issue_9_guide_ea.txt

7 extended ascii counts written to issue_9_guide_ea.txt

⧫  (\u29eb)     2 := BLACK LOZENGE
or the hexadecimal representation &#x29EB; to display it. If you’re typing it directly, on Windows, hold Alt and type 2 9 E B, and on Mac, hold Alt ⌥ and type 2 9 E B. Preview fonts like Times New Roman, Helvetica, and Courier also support this symbol

♦ U+2666 ♦ BLACK DIAMOND SUIT ( &diamondsuit;, ♦)
-----------------------------
(\u1f784)     2 := BLACK SLIGHTLY SMALL CIRCLE
U+2022 BULLET (•)
-----------------------------
(\u1f81a)     2 := HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD
HEAVY RIGHTWARDS ARROW (U+2794): ➔

-----------------------------
python ae_convert_ea.py AB,CDSL  temp_ae_09D.txt temp_ae_09D_cdsl.txt
# check invertibility
python ae_convert_ea.py CDSL,AB  temp_ae_09D_cdsl.txt temp_ae_09D_cdsl_ab.txt
#
diff -w temp_ae_09D.txt temp_ae_09D_cdsl_ab.txt | wc -l
# 0 # files are the same. invertibility confirmed.
# remove unneeded file
rm temp_ae_09D_cdsl_ab.txt


python ea.py temp_ae_09D_cdsl.txt temp_ae_09D_cdsl_ea.txt
