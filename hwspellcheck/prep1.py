"""  prep1.py 

"""

import sys,re,codecs

def init_dig(filedig):
 f = codecs.open(filedig,encoding='utf-8',mode='r')
 recs = [line.rstrip('\r\n') for line in f]
 f.close()
 print "%s dig records read from %s" % (len(recs),filedig)
 return recs

def prep1(filein,filedig,fileout):
 digrecs = init_dig(filedig)
 fout = codecs.open(fileout,'w','utf-8')
 f = codecs.open(filein,encoding='utf-8',mode='r')
 nout = 0 # number of lines written to fileout
 nin = 0 # number of lines read
 nprob = 0
 for linein in f:
  nin = nin+1
  line = linein.rstrip()
  (page,hw,line12,status0) = re.split(':',line)
  m = re.search('^E=([a-z]*)',status0)
  if not m:
   print "Error parsing line#%s: %s" %(nin,line)
   exit(0)
  hw1 = m.group(1) # corrected spelling
  (lnumstr1,lnumstr2) = re.split(',',line12)
  lnum = int(lnumstr1)
  old = digrecs[lnum - 1] # dig line before correction
  # ae has capitalized headwords (first letter capitalized)
  hwcap = hw.capitalize()
  hw1cap = hw1.capitalize()
  new = re.sub(hwcap,hw1cap,old)
  if old == new:
   out = ";X spellchk: %s -> %s" % (hw,hw1)
   nprob = nprob + 1
  else:
   out = "; spellchk: %s -> %s" % (hw,hw1)
  fout.write("%s\n" % out)
  lnumstr1 = "%06d" % lnum
  out = "%s old %s" %(lnumstr1,old)
  fout.write("%s\n" % out)  
  out = "%s new %s" %(lnumstr1,new)
  fout.write("%s\n" % out)
  nout = nout+1
 f.close()
 fout.close() 
 print "%s lines read from %s" %(nin,filein)
 print "%s lines written to %s" %(nout,fileout)
 print "%s change problems" % nprob
 
if __name__=="__main__":
 filename = sys.argv[1]
 filenamedig = sys.argv[2]
 fileout = sys.argv[3]
 prep1(filename,filenamedig,fileout)
