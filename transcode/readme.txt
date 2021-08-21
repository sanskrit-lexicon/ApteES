

Objective is to generate a Devanagari version. Require that the
original slp1 version (ae.txt) be retrievable from the Devangari version.

In ae.txt, Devanagari is represented with slp1 transliteration.
This appears in these spots:
1. In metalines in <k1> and <k2> fields
2. in markup {#X#}

Punctuation preparation:
The 'period' character in slp1 represents danda.  However, danda character
is believed to NOT occur in any of the Devanagari text of AE.  Thus, in
{#X#} text, we should remove periods; there are about 270 such X with period.
Revisions to ae.txt are made in the 'punctuation' subdirectory.


reconstruct ae_iast.txt
python ae_transcode.py slp1 roman ae.txt ae_iast.txt

confirm invertibility:
python ae_transcode.py roman slp1 ae_iast.txt temp_ae_slp1.txt
diff ae.txt temp_ae_slp1.txt  (no difference)
NOTE:  ae_transcode program changed to
  manually adjust three lines in the roman-slp1 transcoding.

-----------------------------------------------------------------------


Currently (Jan 3, 2021), ae.txt agrees with version in csl-orig at
commit# 67bfbda32328317ab45f69432f58204595227609).

Folder to create versions of the base digitization of ae  (ae.txt)
where the slp1 text is transcoded.
We also check for invertibility of this transcoding.

The current transcoding results are:
 ae_iast.txt and ae_deva.txt.

These are reconstructed by:

python ae_transcode.py slp1 roman ae.txt ae_iast.txt
and
python ae_transcode.py slp1 deva ae.txt ae_deva.txt

Discussion of ae_iast.txt
-------------------------

The transcoding details are contained in transcoder/slp1_roman.xml.

python ae_transcode.py slp1 roman ae.txt ae_iast.txt

We do the inverse transcoding, from iast back to slp1.
The inverse transcoding is governed by transcoder/roman_slp1.xml.

python ae_transcode.py roman slp1 ae_iast.txt temp_ae_slp1.txt
diff ae.txt temp_ae_slp1.txt > temp.txt

The diff shows that there are 3 cases where the transcoding is NOT invertible.
Note: temp_ae_slp1.txt should == ae.txt
  only differs in 3 words:
slp1  <L>116525.7<pc>588,2<k1>paramahaMsopanizadhfdaya<k2>parama/—haMsopanizad-hfdaya<e>4
iast  <L>116525.7<pc>588,2<k1>paramahaṃsopaniṣadhṛdaya<k2>paramá—haṃsopaniṣad-hṛdaya<e>4
slp1a <L>116525.7<pc>588,2<k1>paramahaMsopanizaDfdaya<k2>parama/—haMsopanizad-hfdaya<e>4

slp1  <L>139372<pc>704,3<k1>prAghAra<k2>prAg—hAra<e>3
iast  <L>139372<pc>704,3<k1>prāghāra<k2>prāg—hāra<e>3
<L>139372<pc>704,3<k1>prAGAra<k2>prAg—hAra<e>3

slp1  <L>139373<pc>704,3<k1>prAghoma<k2>prAg—homa<e>3
iast  <L>139373<pc>704,3<k1>prāghoma<k2>prāg—homa<e>3
slp1a <L>139373<pc>704,3<k1>prAGoma<k2>prAg—homa<e>3


Discussion of ae_deva.txt
-------------------------

This is how we can transcode ae.txt to Devanagari.

python ae_transcode.py slp1 deva ae.txt ae_deva.txt 

python ae_transcode.py deva slp1 ae_deva.txt temp_ae_slp1.txt

Now, ae.txt and temp_ae_slp1.txt should be the same
diff ae.txt temp_ae_slp1.txt 
The files are the same!
