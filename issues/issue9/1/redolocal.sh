subversion=$1
version='1'
home="/c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue9/${version}"
pywork="/c/xampp/htdocs/cologne/csl-pywork/v02"
cd ${home}
cp temp_ae_${subversion}.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt
cp make_xml.py ${pywork}/makotemplates/pywork/
cd ${pywork}
appdir=${home}/apps${subversion}
sh generate_dict.sh ae  $appdir
validate="/c/xampp/htdocs/cologne/xmlvalidate.py"
python3 $validate $appdir/pywork/ae.xml $appdir/pywork/ae.dtd
# remove files unused by displays
rm -r ${appdir}/downloads
rm -r ${appdir}/orig
# restore pywork
git restore .
cd /c/xampp/htdocs/cologne/csl-orig/v02/ae/
git restore ae.txt

cd ${home}


