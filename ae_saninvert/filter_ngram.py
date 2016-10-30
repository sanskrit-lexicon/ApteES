"""filter_ngram.py
   Sep 25, 2016
   Search for Sanskrit words in a file like invert2.txt which
   have an ngram (of a given length) NOT present in the ngrams of hwnorm1
"""
import sys
sys.path.append('hwnorm1')
import hwnorm1
from ngram import get_ngrams
import re

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

def local_normalize(key):
 """ For our purposes, some further spelling changes before finding
    ngrams
 """
 key1 = re.sub(r'EH$','a',key)
 key1 = re.sub(r'iM','i',key1)
 key1 = re.sub(r'IM','I',key1)
 key1 = re.sub(r'AH$','A',key1)
 key1 = re.sub(r'osmi$','asmi',key1) # pracakitosmi -> pracakitaH asmi
 return key1

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
  key1 = local_normalize(key)
  key_ngrams = get_ngrams(key1,ngramlen)
  # allow for logic to change last ngram
  key_ngrams_adjusted = key_ngrams
  ngrams = ngrams + key_ngrams_adjusted
 # are all ngrams in the dictionary ngramsd ?
 unknown_ngrams=[]
 for ngram in ngrams:
  if ngram not in ngramsd:
   unknown_ngrams.append(ngram)
 rec.unknown_ngrams = unknown_ngrams
 rec.found = (len(unknown_ngrams) == 0)
 rec.sortkey = ''
 if not rec.found:
  #rec.sortkey = ','.join(rec.unknown_ngrams)
  temp = unknown_ngrams[0] # just first 1, if there are multiple
  rec.sortkey = temp[-2:]  # just last 2 characters

def filter(ngramlen,ngramsd,recs,fileout,fileout1):
 fout = open(fileout,"w")
 fout1 = open(fileout1,"w")
 for rec in recs:
  rec_ngrams(rec) # modify rec based on ngrams
 # generate output
 n = 0
 n1 = 0
 # sort records
 recs1 = sorted(recs,key=lambda rec: rec.sortkey)
 for rec in recs1:
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
 
