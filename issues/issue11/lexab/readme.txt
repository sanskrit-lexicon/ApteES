
lexab/readme.txt

Get counts of distinct
  <lex>X</lex>  lexical classification abbreviation
  ⁅X⁆ general abbreviation
  
python check_lexab.py ../prepab/temp_abv1.txt lexab_abv1.txt
# 110 lines written to lexab_abv1.txt

python check_lexab.py ../prepab/temp_abv2.txt lexab_abv2.txt
110 lines written to lexab_abv2.txt

diff lexab_abv1.txt  lexab_abv2.txt | wc -l
# 0   The two versions are identical in this respect.
--------------------------------------------
Prepare aeab_input.txt for use in csl-pywork
Format is X\t<id>X</id> <disp>Y</disp>
Use the 110 lines in lexab_abv2.txt for the X
Also,  some of the Y are from  ae_footer.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae_footer.txt temp_ae_footer.txt

Also used apab_input.txt

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apab/apab_input.txt temp_apab_input.txt

---------------------------------------------
INSTALL aeab  (common abbreviations for 'ae')
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ae/pywork
cp -r ../../ap/pywork/apab aeab
# Manual edits in aeab directory:
cd aeab
rm apab_input.txt
cd /c/xampp/htdocs/sanskrit-lexicon/ApteES/issues/issue11
cp lexab/aeab_input.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ae/pywork/aeab/

# manual edits in csl-pywork/v02 to get 'ae' abbreviations
# 1. inventory.txt
#    add abbreviations for 'ae'
# 2. generate_ab_bib_ls.sh
#     add 'ae' everywhere there is 'ap90'
# 3. makotemplates/pywork/redo_postxml.sh
#    "abbreviations":
#    add 'ae' to list of applicable dictionaries 
# 4. makotemplates/pywork/sqlite/sqlite_txt.py
#    add 'aeab' to SCHEMA_MAP (same map as 'apab')
# --------------
# regenerate local displays for ae, and check xml
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ae  ../../ae
sh xmlchk_xampp.sh ae
# ok



