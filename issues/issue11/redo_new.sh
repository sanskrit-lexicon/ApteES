cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue11/ # home
#cp basicadjust_new.php /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
#cp basicadjust_new.php /c/xampp/htdocs/cologne/csl-apidev/basicadjust.php


cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
git restore .
echo "WARNING: /c/xampp/htdocs/cologne/csl-apidev basicadjust.php is revised"
#cd /c/xampp/htdocs/cologne/csl-apidev
#git restore .
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue19 #home

