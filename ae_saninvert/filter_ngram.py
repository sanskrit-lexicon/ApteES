"""filter_ngram.py
   Sep 25, 2016
   Search for Sanskrit words in a file like invert2.txt which
   have an ngram (of a given length) NOT present in the ngrams of hwnorm1
"""
import sys
sys.path.append('hwnorm1')
import hwnorm1
from ngram import get_ngrams

class Invert2(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  (self.word,self.n,s) = line.split(':')
  self.occurrences = []
  for s1 in s.split(';'):
   (hw,L,page) = s1.split(',')
   self.occurrences.append((hw,L,page))
  self.found=False

def init_invert2recs(filein=None):
 if filein == None:
  filein = "invert2.txt"
 with open(filein,"r") as f:
  recs = [Invert2(line) for line in f]
 print len(recs),"records read from",filein
 return recs

def rec_ngrams(rec):
 word = rec.word
 # if word is hyphenated, do NOT look for ngrams that
 # straddle a hyphen
 parts = rec.word.split('-')
 # get ngrams for all parts
 ngrams = []
 for word in parts:
  # normalize in the hwnorm1 way
  key = hwnorm1.normalize_key(word)
  ngrams = ngrams + get_ngrams(key,ngramlen)
 # are all ngrams in the dictionary ngramsd ?
 unknown_ngrams=[]
 for ngram in ngrams:
  if ngram not in ngramsd:
   unknown_ngrams.append(ngram)
 rec.unknown_ngrams = unknown_ngrams
 rec.found = (len(unknown_ngrams) == 0)

def filter(ngramlen,ngramsd,recs,fileout,fileout1):
 fout = open(fileout,"w")
 fout1 = open(fileout1,"w")
 for rec in recs:
  rec_ngrams(rec) # modify rec based on ngrams
 # generate output
 n = 0
 n1 = 0
 for rec in recs:
  if rec.found:
   out = "%s" %(rec.line)
   fout.write(out + "\n")
   n = n + 1
  else:
   ngramstr = ','.join(rec.unknown_ngrams)
   s = "unknowns=%s" % ngramstr
   out = "%s##%s"%(rec.line,s)
   fout1.write(out + "\n")
   n1 = n1 + 1
 fout.close()
 fout1.close()
 print n,"records written to",fileout
 print n1,"records written to",fileout1

class Ngram(object):
 d = {}
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.ngram,self.count) = line.split(':')
  Ngram.d[self.ngram] = self

def init_ngrams(filein):
 with open(filein,"r") as f:
  for line in f:
   rec = Ngram(line)
 return Ngram.d


if __name__ == "__main__":
 ngramlen = int(sys.argv[1])
 assert ngramlen>=1,"ngramlen must be >=1"

 filengram = sys.argv[2]
 filein = sys.argv[3]
 fileout = sys.argv[4]
 fileout1 = sys.argv[5]
 recs = init_invert2recs(filein)
 ngramsd = init_ngrams(filengram)
 filter(ngramlen,ngramsd,recs,fileout,fileout1)
 
