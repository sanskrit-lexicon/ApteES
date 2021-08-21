
changes to ae.txt re punctuation.

start with temp_ae.txt, a copy of file csl-orig/v02/ae/ae.txt,
 cls-orig commit is 84262537f4686a539b1e3f543ede586ed40f7f29.

changes.txt is made manually, in  several steps.

1. period at end of Deva
It seems safe to move ENDING periods out;
 i.e., .#} -> #}.
python changes_1.py temp_ae.txt changes_1.txt
199 cases
2. period internal to Deva.
These may need to change to comma. Examine individually.
python changes_2.py temp_ae_1.txt changes_2.txt
 70 cases, examine each manually vs. scanned images.

3. String ',-#}'
python changes_3.py temp_ae_1.txt changes_3.txt
7 cases. Various

python updateByLine.py temp_ae.txt changes.txt temp_ae_1.txt

cp temp_ae_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/ae/ae.txt
