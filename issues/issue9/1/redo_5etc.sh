python diff_to_changes_dict.py temp_ae_04.txt temp_ae_05.txt changes_05.txt
echo "-------------------------"
python clean/punct.py 01 temp_ae_05.txt changes_06.txt
echo "-------------------------"

python updateByLine.py temp_ae_05.txt changes_06.txt temp_ae_06.txt
echo "-------------------------"

python clean/punct.py 02 temp_ae_06.txt changes_07.txt replacements_06.txt
echo "-------------------------"

python updateByLine.py temp_ae_06.txt changes_07.txt temp_ae_07.txt
echo "-------------------------"

python clean/quote_merge.py 01 temp_ae_07.txt changes_08.txt
echo "-------------------------"

python updateByLine.py temp_ae_07.txt changes_08.txt temp_ae_08.txt
echo "-------------------------"

#echo "checking parens"
#python clean/xmlbalance.py '(,<F>;),</F>' temp_ae_08.txt temp_ae_08work.txt

#python clean/unbalanced.py '<F>' '</F>' temp_ae_08work.txt temp_ae_08worka.txt

#sh redolocal.sh 08worka

python clean/paren_merge.py 01 temp_ae_08.txt changes_09.txt

python updateByLine.py temp_ae_08.txt changes_09.txt temp_ae_09.txt
