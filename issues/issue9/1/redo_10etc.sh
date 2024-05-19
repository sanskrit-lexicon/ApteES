echo "-------------------------"
python diff_to_changes_dict.py temp_ae_09.txt temp_ae_10.txt changes_10.txt

echo "-------------------------"
python clean/see_merge.py 01 temp_ae_10.txt changes_11.txt
python updateByLine.py temp_ae_10.txt changes_11.txt temp_ae_11.txt

echo "-------------------------"
python clean/bold.py 01 temp_ae_11.txt changes_12.txt
python updateByLine.py temp_ae_11.txt changes_12.txt temp_ae_12.txt

echo "-------------------------"

echo "-------------------------"

echo "-------------------------"

echo "-------------------------"



