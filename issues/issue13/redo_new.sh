sfx=$1 
cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue13/ # home

cp temp_ae_${sfx}.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt


cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ae  ../../ae
sh xmlchk_xampp.sh ae

cd /c/xampp/htdocs/cologne/csl-orig
git restore .

cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue13/ # home


