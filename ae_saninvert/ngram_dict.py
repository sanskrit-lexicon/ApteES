"""ngram_dict.py
   Sep 25, 2016
   Generate n-grams from hwnorm1
   python ngram_dict.py len dictcode pos fileout
   pos = any or beg
   Jun 5, 2017.  Choose ngrams for a particular dictionary 
"""
import sys
sys.path.append('hwnorm1')
import hwnorm1
from sansort import slp_cmp

def get_ngrams(x,n):
 ans=[]
 for i in xrange(0,len(x)-n+1):
  ans.append(x[i:i+n])
 return ans

def keyindict(keynorm,dictup):
 rec = hwnorm1.HWnorm1rec.d[keynorm]
 for ikey,key in enumerate(rec.keys):
  dictcodes = rec.dictstrs[ikey].split(',')
  if dictup in dictcodes:
   return key
 return None  # this record not found in dictup

if __name__ == "__main__":
 ngramlen = int(sys.argv[1])  # 2,3, etc.
 dictup = sys.argv[2].upper()
 poscode = sys.argv[3].lower()
 poscodes = ['any','beg']
 assert poscode in poscodes,"ERROR poscode (%s) must be in %s" %(poscode,poscodes)
 fileout = sys.argv[4]
 assert ngramlen>=1,"ngramlen must be >=1"
 #fileout = "hwnorm1/%sgram.txt"%ngramlen
 hwnorm1.init_hwnorm1()
 ngramsd = {}
 for keynorm in hwnorm1.HWnorm1rec.d: # normalized headword spelling
  key = keyindict(keynorm,dictup)
  if key == None:
   # dictup not a dictionary for keynorm
   continue
  ngrams = get_ngrams(key,ngramlen)
  if poscode == 'beg':
   # only beginning ngram
   if len(ngrams)>0:
    ngrams = [ngrams[0]] 
  for ngram in ngrams:
   if ngram not in ngramsd:
    ngramsd[ngram]=0
   ngramsd[ngram] = ngramsd[ngram] + 1
  
 keys = ngramsd.keys()
 keys.sort(cmp=slp_cmp)
 with open(fileout,"w") as f:
  for key in keys:
   out = "%s:%s"%(key,ngramsd[key])
   f.write(out + "\n")
 print len(keys),"ngrams written to",fileout

