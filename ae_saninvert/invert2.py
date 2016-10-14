"""invert2.py
   Sep 4, 2016
"""
import sys,re,codecs
from sansort import slp_cmp

class Invert1(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.key1,self.L,self.pc,s) = line.split(':')
  self.phrases = s.split(',')
  x = []
  for phrase in self.phrases:
   if phrase == '':
    # for cases like 'abrogate', that have no sanskrit words.
    continue
   words = phrase.split(' ')
   for w in words:
    if w == '-': # exmple bring, cabin, ...
     continue
    if w.startswith('-'):
     w = w[1:]
    if w.endswith('-'):
     w = w[0:-1]
    if w == '':
     continue
    if w not in x:
     x.append(w)
  self.words = x
  #if self.key1 == 'abrogate':
  # print self.key1,self.words

def main(filein,fileout):
 # parse input, and construct array of Invert1 objects
 f = codecs.open(filein,"r")
 recs = []
 for line in f:
  rec = Invert1(line) 
  recs.append(rec)
 f.close()
 print len(recs),"records parse"
 # construct dictionary of words
 d = {}
 nrecwords=0
 for rec in recs:
  nrecwords = nrecwords + len(rec.words)
  for w in rec.words:
   # we assune rec.words has no duplicates
   if w not in d:
    d[w] = []
   d[w].append(rec)
 allwords = d.keys()
 print nrecwords,"words including duplicates"
 print len(allwords),"words found, excluding duplicates"
 # sort allwords
 allwords.sort(cmp=slp_cmp)
 # generate output (an inverted index)
 fout = codecs.open(fileout,"w")
 for w in allwords:
  wrecs = d[w]
  recids=[]
  for rec in wrecs: # rec is Invert1 object
   recid = "%s,%s,%s"%(rec.key1,rec.L,rec.pc)
   recids.append(recid)
  recids.sort()
  recidstr = ';'.join(recids)
  nids = len(recids)
  if nids > 999:
   print w,"appears in",nids,"entries"
  out = "%s:%03d:%s" % (w,nids,recidstr)
  fout.write(out + "\n")
 print len(allwords),"records written to",fileout
 fout.close()

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout=sys.argv[2]
 main(filein,fileout)

