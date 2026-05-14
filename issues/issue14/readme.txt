
Update ae-meta2.txt

cd /c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue11/temp_meta2 # home

cp /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae-meta2.txt prev_ae-meta2.txt

cp prev_ae-meta2.txt ae-meta2.txt

# extended ascii codes with frequency
python check_ea1.py /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt ae_ea.txt
27 extended ascii codes

# xml tags in ae.txt
python xmltag.py /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt ae_xmltag.txt

python xmltag.py /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt temp_ap_xmltag.txt
python xmltag.py /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_xmltag.txt


॰  (\u0970)     1 := DEVANAGARI ABBREVIATION SIGN
Error -- remove under hw strike  Dash॰

Made this change to ae.txt in csl-orig
-----
install ae-meta2.txt
cp ae-meta2.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae-meta2.txt
push csl-orig to github
