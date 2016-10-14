"""invert2_filter1.py
   Sep 5, 2016
   Search for Sanskrit words (of invert2.txt) in hwnorm1.
"""
import sys
sys.path.append('hwnorm1')
import hwnorm1

class Invert2(object):
 def __init__(self,line):
  # line like BAkti:002:devote,2832,105;devout,2834,106
  line = line.rstrip('\r\n')
  self.line = line
  # n is the number of instances
  # This equals the length of the occurrences array
  (self.word,self.n,s) = line.split(':')
  self.occurrences = []
  for s1 in s.split(';'):
   (hw,L,page) = s1.split(',')
   self.occurrences.append((hw,L,page))
  assert int(self.n) == len(self.occurrences),"Invert2 ERROR:%s"%line
  self.found=False

def init_invert2recs(filein=None):
 if filein == None:
  filein = "invert2.txt"
 with open(filein,"r") as f:
  recs = [Invert2(line) for line in f]
 print len(recs),"records read from",filein
 return recs

def filter1_find(word):
 word1 = word.replace('-','')
 hwnorm1rec = hwnorm1.find(word1)
 if hwnorm1rec:
  return hwnorm1rec.normkey
 if word1.endswith(('ena','eRa')):
  # instrumental singular of a word ending in 'a'
  word2 = word1[0:-3]+'a'
  hwnorm1rec = hwnorm1.find(word2)
  if hwnorm1rec:
   return hwnorm1rec.normkey

 return False

def filter2_find(word):
 # take the parts separately
 wordparts = word.split('-')
 found = True
 parts=[]
 for w in wordparts:
  form = filter1_find(w)
  if not form:
   found = False
  else:
   parts.append(form)
 if found:
  return '+'.join(parts)
 return False

def filter3_find(word):
 # generate 2-word parts, each of length 3+
 #
 word = word.replace('-','') # remove '-'
 nword = len(word)
 minlen = 3
 subwords = []  # list of 2-tuples
 for i in xrange(minlen,nword-minlen):
  subword = (word[0:i],word[i:])
  subwords.append(subword)
 # try each
 for wordparts in subwords:
  found = True
  parts=[]
  for w in wordparts:
   hwnorm1rec = hwnorm1.find(w)
   if not hwnorm1rec:
    found = False
    break
   else:
    parts.append(hwnorm1rec.normkey)
  if found:
   return '+'.join(parts)
 return False

def filter(option,recs,fileout,fileout1):
 fout = open(fileout,"w")
 fout1 = open(fileout1,"w")
 for rec in recs:
  if option == '1':
   rec.found = filter1_find(rec.word)
  elif option == '2':
   rec.found = filter2_find(rec.word)
  elif option == '3':
   rec.found = filter3_find(rec.word)
  else:
   print "filter option unknown:'%s'"%option
   exit(1)
 # generate output
 n = 0
 n1 = 0
 for rec in recs:
 
  if rec.found:
   out = "%s##%s" %(rec.line,rec.found)
   fout.write(out + "\n")
   n = n + 1
  else:
   fout1.write(rec.line + "\n")
   n1 = n1 + 1
 fout.close()
 fout1.close()
 print n,"records written to",fileout
 print n1,"records written to",fileout1

if __name__ == "__main__":
 option = sys.argv[1]
 filein = sys.argv[2]
 fileout = sys.argv[3]
 fileout1 = sys.argv[4]
 recs = init_invert2recs(filein)
 filter(option,recs,fileout,fileout1)
 
