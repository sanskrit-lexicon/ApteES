
work to make an inverted index for the sanskrit words appearing in AE.

python invert1.py ../../ae.xml invert1.txt

python invert2.py invert1.txt invert2.txt


invert_filter1: option 1
full word, with '-' removed, is found in hwnorm1
python invert2_filter1.py 1 invert2.txt invert2_found1.txt invert2_notfound1.txt

invert_filter1: option 2
Some words are given as separated by '-'.
Search for all word parts in hwnorm1
python invert2_filter1.py 2 invert2_notfound1.txt invert2_found2.txt invert2_notfound2.txt


invert_filter1: option 3
Remove '-'.  Search for compounds with exactly 2 parts.
python invert2_filter1.py 3 invert2_notfound2.txt invert2_found3.txt invert2_notfound3.txt

a-kiMcitkrara:001:trifle,10586,476
a-tarjAta:001:nature,7032,303
BAkti:002:devote,2832,105;devout,2834,106
BAktiH:001:enthusiasm,3565,138
BAktipuraHptara:001:devout,2834,106


ngram.py
 computes ngrams in hwnorm1 list.
 python ngram.py 2  (hwnorm1/2gram.txt)
 python ngram.py 3  (hwnorm1/3gram.txt)

filter_ngram.py
Reads an invert2.txt type file, and generates list of words with
  ngrams not found in ngram.txt for hwnorm1.
python filter_ngram.py 2 hwnorm1/2gram.txt invert2_notfound3.txt invert2_notfound3_ngram2ok.txt invert2_notfound3_ngram2prob.txt
 155 cases found.  They look promising as mis-spelled.

python filter_ngram.py 3 hwnorm1/3gram.txt invert2_notfound3.txt invert2_notfound3_ngram3ok.txt  invert2_notfound3_ngram3prob.txt

