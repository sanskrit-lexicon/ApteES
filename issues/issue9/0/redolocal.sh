version='0'
home="/c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue9/${version}"
cd ${home}
cp temp_ae_${version}.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
appdir=${home}/apps
sh generate_dict.sh ae  $appdir
validate="/c/xampp/htdocs/cologne/xmlvalidate.py"
python3 $validate $appdir/pywork/ae.xml $appdir/pywork/ae.dtd
cd /c/xampp/htdocs/cologne/csl-orig/v02/ae/
git restore ae.txt
cd ${home}


