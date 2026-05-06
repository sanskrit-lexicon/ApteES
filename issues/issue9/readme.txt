#05-08-2024

This directory in local installation:
cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue9
------------------------------------------
temp_ae_0.txt  cdsl-orig version as of 05-08-2024
  commit 8f8a0cb4a89dfb9e5d8897bc3c03a4be594fd2b1
cd /c/xampp/htdocs/cologne/csl-orig
git show 4fde1c49:v02/ae/ae.txt > /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue9/temp_ae_0_all.txt

89611 temp_ae_0_all.txt 

------------------------------------------

------------------------------------------
mkdir 0

cd 0
It is convenient to remove the material before the first entry and after
the last entry.
python extract_entries.py ../temp_ae_0_all.txt temp_ae_0_header.txt temp_ae_0.txt temp_ae_0_footer.txt

sh redolocal.sh
 uses temp_ae_0.txt to generate apps/0
 display url:
 http://localhost/sanskrit-lexicon/ApteES/issues/issue9/apps/0/web/

------------------------------------------
# we will also modify some files, e.g. make_xml.py
# this is a very preliminary version, changing only the markup of 'last'

mkdir 0a
cp 0/temp_ae_0.txt 0/temp_ae_0a.txt

cp /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py 0a/
# revise make_xml.py  See 05-06-2024 comments therein
# don't break on each line.
#

Revise temp_ae_0a.txt
Just within L=6066 (hw='last')
- Add {@1@}
- {@ -> <br/> {@  (but not before broken bar)
- '‘' -> '<br/>‘'
- '-adv.' -> '<br/>-adv.</br>  also before '-v.i.'
- br before 'oft. b
- ' te jI-#}\n{#vi' -> 'te'\njIvi'

------------------------------------------
 We need to do a lot of 'cleanup' work before display improvements.
 We'll call this version 1
mkdir 1

cp 0a/make_xml.py 1/  
cp 0/redolocal.sh 1/ # and change to version=1

For cleanup work details, see see readme_cleanup.txt

------------------------------------------
2026-05-06
  temp_ae_0_all.txt is same as that of ae.txt at commit 405cab9
  See readme_ae_history.txt

----------------
# get current ae_all.txt (at commit 3b990c8) and separate into 3 parts:
  ae_header.txt
  ae.txt  (all the entries)
  ae_footer.txt
mkdir temp_ae_20260506
cd temp_ae_20260506
cp /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt ae_all.txt
python ../0/extract_entries.py ae_all.txt ae_header.txt ae.txt ae_footer.txt
550 written to ae_header.txt
88835 written to ae.txt
226 written to ae_footer.txt
-----------------
# copy the 3 parts to csl-orig
cp ae.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt
cp ae_header.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae_header.txt
cp ae_footer.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae_footer.txt

------------------
push csl-orig to github.
cd /c/xampp/htdocs/cologne/csl-orig/v02
git add .
git commit -m "AE: remove header and footer #9"
git push
