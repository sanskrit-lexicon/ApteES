cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue11/ # home
#cp basicadjust_new.php /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
#cp basicadjust_new.php /c/xampp/htdocs/cologne/csl-apidev/basicadjust.php

cp temp_ae_new.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt

cp make_xml_new.py /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py
cp aeauth/aeauth_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ae/pywork/aeauth/tooltip.txt

cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ae  ../../ae
sh xmlchk_xampp.sh ae
cd /c/xampp/htdocs/cologne/csl-orig
git restore .
cd /c/xampp/htdocs/cologne/csl-pywork
git status
# git restore .
cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue11/ # home


