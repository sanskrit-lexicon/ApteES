

Generate a Devanagari version ae_deva.txt. Require that the
original slp1 version (ae.txt) be retrievable from the Devanagari version.

In ae.txt, Devanagari is represented with slp1 transliteration.
This appears in  markup {#X#}.

Punctuation preparation:
The 'period' character in slp1 represents danda.  However, danda character
is believed to NOT occur in any of the Devanagari text of AE.  Thus, in
{#X#} text, we should remove periods; there are about 270 such X with period.
Revisions to ae.txt are made in the 'punctuation' subdirectory.

Use ae.txt from repository csl-orig, file v02/ae/ae.txt
  at commit f2734fb8ac5ae662cc9fa62c6053a80078df8677

-----------------------------------------------------------------------
construct ae_deva.txt
python ae_transcode.py slp1 deva ae.txt ae_deva.txt

check invertibility
python ae_transcode.py deva slp1 ae_deva.txt temp_ae_deva_slp1.txt

diff ae.txt temp_ae_deva_slp1.txt
<NO DIFFERENCE EXPECTED>
-----------------------------------------------------------------------
We probably could do same for an iast version.
