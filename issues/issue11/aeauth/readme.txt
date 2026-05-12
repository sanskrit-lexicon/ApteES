
aeauth
Tooltips for literary source references.

temp_ae_new.txt markup for literary source is
〔X N〕
Only 1141 instances
Generate a file with all instances
python lsextract.py ../temp_ae_new.txt lsextract.txt
1141 lines written to lsextract.txt

Examine lsextract.txt, get
distinct abbreviations, and parameter type(s)
r = lower case roman numeral
n = digit sequence
30 distinct abbreviations
Bh.|r. n
D. K.|r. n
H.|n
K.|r. n
Ka.|None OR n
Kav.|None
Ki.|r. n
Li.|None OR n
M.|n
Mah.|r. n. n
Mal.|n
Mallinātha| None
Me.|n
Mr.|n
Mu.|n
N.|r. OR r. n
P.|n OR r. n
R.|r. n
Rat.|n
S.|None or n
S. B.|n OR n, n
S. K.|None
S. R.|n
Si.|r. n
U.|n
V.|n
V. M.|n
Ve.|n
Vi.|n
Y.|r. n


----------------
Counts, using abbreviations above
python lsextract1.py ../temp_ae_new.txt lsextract1.txt

check_ls: ntot= 1141
30 lines written to lsextract1.txt

----------------
prepare for ae ls-Abbreviation Tooltips
modify csl-pywork files

---------------------------------------------
INSTALL aeauth  (literary source abbreviations for 'ae')
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ae/pywork
cp -r ../../ap/pywork/apauth aeauth
# Manual edits in aeauth directory:
# manual edit of aeuth/tooltip.txt  
# format is X\tTOOLTIP
# aeuth/tooltip.txt  will be completed later

# manual edits in csl-pywork/v02 to get 'ae' ls abbreviations
# 1. inventory.txt
#    add auth for 'ae'
# 2. generate_ab_bib_ls.sh
#     add 'ae' everywhere there is 'ap90'
# 3. makotemplates/pywork/redo_postxml.sh
#    "literary source":
#    add 'ae' to list of applicable dictionaries 
# 4. makotemplates/pywork/sqlite/sqlite_txt.py
#    add 'aeauthtooltips'' to SCHEMA_MAP
#    (same map as 'apauth')
# --------------
# modify basicadjust
# at "authtooltips", add 'ae' to the list of dicts
#  /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
# then, in csl-websanlexicon/v02,
#  copy basicadjust.php to csl-apidev.
# sh apidev_copy.sh  
# regenerate local displays for ae, and check xml
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ae  ../../ae
sh xmlchk_xampp.sh ae
# ok

========================================
csl-pywork, csl-websanlexicon, csl-apidev pushed to github
========================================
# use ../lexab/temp_ae_footer.txt to fill in
# aeauth_tooltip_0.txt (start with lsextrac1.txt)
# aeauth_tooltip.txt   (IAST spelling in tooltips)

cp aeauth_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ae/pywork/aeauth/tooltip.txt
