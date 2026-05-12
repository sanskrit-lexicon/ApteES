
https://github.com/sanskrit-lexicon/ApteES/issues/12

cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue12

----------
temp_ae_0.txt
cp csl-orig ae.txt at commit  ded7832c
cp /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt temp_ae_0.txt

-----------
These changes do not change ae.xml
Local copy of issue11 generated work:
/c/xampp/htdocs/cologne/ae-issue11
-----------
changes to ae.txt are coordinated with changes to make_xml.py
cp /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py temp_make_xml_0.py

----------------
changes of notation
python change_notation.py to temp_ae_0.txt temp_ae_1.txt
# invertibility check
python change_notation.py from temp_ae_1.txt temp_ae_0a.txt
diff temp_ae_0.txt temp_ae_0a.txt | wc -l
#0

# make changes to temp_make_xml_1.py to reflect new notation.
# copy temp_make_xml_1.py to csl-pywork
cp temp_make_xml_1.py /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py
cp temp_ae_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt
##  regenerate
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ae  ../../ae
sh xmlchk_xampp.sh ae
# ok

# ------------------
is ae.xml the same:
diff /c/xampp/htdocs/cologne/ae-issue11/pywork/ae.xml /c/xampp/htdocs/cologne/ae/pywork/ae.xml  | wc -l
# 0 Yes!  ae.xml is unchanged.

# ------------------
# generate the extended-ascii codes.
# These should be documented in ea_meta2.txt is csl-orig.
python check_ea1.py temp_ae_1.txt ea.txt
27 ea codes
====================================
install to github for repos csl-orig and csl-pywork
install to Cologne.

