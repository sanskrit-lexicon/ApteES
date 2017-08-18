
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
10-30-2016: After corrections, 2 cases found

python filter_ngram.py 3 hwnorm1/3gram.txt invert2_notfound3.txt invert2_notfound3_ngram3ok.txt  invert2_notfound3_ngram3prob.txt

10-30-2016: 961 cases found
Note:  There be false positives, for instance
maraRavyavasAya-budDiM:001:relax,8776,387##unknowns=DiM
muktagAtrEH:001:languid,6035,250##unknowns=rEH
mAnuzIM:001:human,5036,209##unknowns=zIM

These false positives are cases of inflected form endings.
For purpose of finding odd n-grams, change spellings so that
 ending 
  EH -> a  (instr.pl. of nouns ending in 'a')
  AH -> A  (f. nom. pl.)
  iM -> i  (m. acc. sg.)
  IM -> I  (f. acc. sg.)
  osmi -> asmi  (pracakitosmi -> pracakitaH asmi)  
Removing these false positives reduces the number of 
NOT FOUND 3-gram instances to 781 cases

invert2_notfound3_ngram3prob.txt now used in


ngram_dict

python ngram_dict.py 2 mw beg ngram_2_beg_mw.txt
python ngram_dict.py 3 mw beg ngram_3_beg_mw.txt

python ngram_dict.py 2 mw any ngram_2_mw.txt
python ngram_dict.py 3 mw any ngram_3_mw.txt
