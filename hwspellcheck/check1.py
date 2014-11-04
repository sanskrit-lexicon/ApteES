# coding=utf-8
""" check1.py
 Read hw2 file for AE.  Use en_GB and en_US dictionaries to check
 spelling.  Write lines line hw2, with a 'status' field.

 python check1.py <input>  <output> 
 <input> = filename of 'extracted' file.

 Requires virtualenv with enchant installed. See readme.org.
"""
import sys, re,codecs
import enchant
import collections # requires Python 2.7+

class Aword(object): # analylzed word from hwchk2
 def __init__(self,line):
  try:
   (self.page,self.word,self.line12)= re.split(r':',line)
   self.status = 'X' # means not found yet, possible spelling error
   self.line = line
  except:
   out = "Aword ERROR: line=%s" % line
   print out.encode('utf-8')
   exit(1)

def check1(filein,fileout):
 dictnames = ['en_GB','en_US']
 dictrefs = [enchant.Dict(d) for d in dictnames]
 n=0
 fout = codecs.open(fileout,'w','utf-8')
 f =  codecs.open(filein,encoding='utf-8',mode='r')
 # counters key on mtype
 c = collections.Counter() 
 for line in f:
  line = line.rstrip('\r\n')
  n=n+1
  a = Aword(line)
  c.update(['ALL'])
  for idict in xrange(0,len(dictnames)):
   if dictrefs[idict].check(a.word):
    a.status='OK=%s' % dictnames[idict]
    break
  c.update([a.status])
  newline = "%s:%s\n" %(a.line,a.status)
  fout.write(newline)
 f.close()
 fout.close()

 for status in sorted(c.keys()):
  print status,c[status]

if __name__=="__main__":
 filein = sys.argv[1] # extract
 #dictname = sys.argv[3] # german_words dictionary prefix for enchant
 fileout = sys.argv[2] # ok
 check1(filein,fileout)

