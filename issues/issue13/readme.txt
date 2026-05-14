
# apply print changes
# this directory
/c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue13/ # home


# csl-orig history of ae
cd /c/xampp/htdocs/cologne/csl-orig
git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/ae/ae.txt > /c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue13/temp_ae_history.txt
# this is the commit with print changes (using previous format of ae.txt)

2026-05-10 a09f4a3 Dr. Dhaval Patel AE printchange incorporated in ae.txt

# temp_ae_pc.txt
cd /c/xampp/htdocs/cologne/csl-orig
git show a09f4a3:v02/ae/ae.txt > /c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue13/temp_ae_pc.txt
cd /c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue13/ # home

# temp_ae_0.txt  # latest version of ae.txt

cd /c/xampp/htdocs/cologne/csl-orig
git show ef0424a:v02/ae/ae.txt > /c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue13/temp_ae_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/ApteEs/issues/issue13/ # home

# ------------------
163 matches in 159 lines for "->" in buffer: temp_ae_pc.txt


# ------------------
# temp_ae_pc1.txt
see readme_hw.txt

# -------------------------

python extract_change.py temp_ae_pc1.txt extract_change
141 lines written to extract_change_0.txt
16 lines written to extract_change_1.txt
4 lines written to extract_change_2.txt
1 lines written to extract_change_3.txt

(+ 141 16 4 1) = 162
#--------------------------------------
# Batch 1  temp_ae_1.txt
python make_change0.py temp_ae_0.txt extract_change_0.txt  change_0.txt
# 20 NOT CHANGED
cp change_0.txt change_0_edit.txt
# manually fix the NOT CHANGED
python updateByLine.py temp_ae_0.txt change_0_edit.txt temp_ae_1.txt
145 change transactions from change_0_edit.txt

# check display generation fo temp_ae_1.txt
sh redo_new.sh 1
# ok
# ---------------------------------
# batch 2  temp_ae_2.txt
python make_change0.py temp_ae_1.txt extract_change_1.txt  change_1.txt
16 xrecs
6 NOT CHANGED
cp change_1.txt change_1_edit.txt
# manually fix the NOT CHANGED
python updateByLine.py temp_ae_1.txt change_1_edit.txt temp_ae_2.txt
14 change transactions from change_1_edit.txt
# check display generation fo temp_ae_2.txt
sh redo_new.sh 2
# ok

# ---------------------------------
# batch 3  temp_ae_3.txt
python make_change0.py temp_ae_2.txt extract_change_2.txt  change_2.txt
4 xrecs
2 NOT CHANGED
cp change_2.txt change_2_edit.txt
# manually fix the NOT CHANGE
python updateByLine.py temp_ae_2.txt change_2_edit.txt temp_ae_3.txt
2 change transactions from change_2_edit.txt
# check display generation for temp_ae_3.txt
sh redo_new.sh 3
# ok

# ---------------------------------
# batch 4  temp_ae_4.txt
python make_change0.py temp_ae_3.txt extract_change_3.txt  change_3.txt
1 xrecs
0 NOT CHANGED
cp change_3.txt change_3_edit.txt
# No changes made to change_3_edit.txt
python updateByLine.py temp_ae_3.txt change_3_edit.txt temp_ae_4.txt
1 change transactions from change_3_edit.txt
# check display generation for temp_ae_4.txt
sh redo_new.sh 4
# ok

# ----------------------------------------------
python extract_change.py temp_ae_4.txt extract_change4
2diff extract_change4_all.txt extract_change4_all.txt > diff_extract_change.txt

# ----------------------------------------------
Ready to install temp_ea_4.sh
Start with git pull csl-orig
... etc.
cp temp_ae_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt
