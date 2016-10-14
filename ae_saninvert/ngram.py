"""ngram.py
   Sep 25, 2016
   Generate n-grams from hwnorm1
   python ngram.py 
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

if __name__ == "__main__":
 ngramlen = int(sys.argv[1])  # 2,3, etc.
 assert ngramlen>=1,"ngramlen must be >=1"
 fileout = "hwnorm1/%sgram.txt"%ngramlen
 hwnorm1.init_hwnorm1()
 ngramsd = {}
 for key in hwnorm1.HWnorm1rec.d: # normalized headword spelling
  ngrams = get_ngrams(key,ngramlen)
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

