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
