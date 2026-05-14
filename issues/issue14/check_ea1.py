""" check_ea1.py Assumes input is utf8-unicode, and similarly writes.
    03-24-2017. 
    01-23-2018.  Handles combining codes
    06-30-2023.  Revise for python3
"""

import re,sys
import codecs, unicodedata

def make_combining_chars():
 chars = [
  r'\u0300', # combining grave accent
  r'\u0301', # combining acute accent
  r'\u0302', # combining circumflex accent
  r'\u0303', # combining tilde
  r'\u0304', # combining macron
 ]
 ans = []
 for x in chars:
  # ref: //stackoverflow.com/questions/2828284/conversion-of-strings-like-uxxxx-in-python
  # y = x.decode('unicode-escape')
  # AttributeError: 'str' object has no attribute 'decode'
  y = bytes(x,"ascii").decode('unicode-escape')
  ans.append(y)
 if False:
  for key in ans:
   ords = [r"\u%04x" % ord(c) for c in key]
   ordstr = '.'.join(ords)
   names = [unicodedata.name(c) for c in key]
   namestr = ' + '.join(names)
   out = "%s  (%s)  := %s" %(key,ordstr,namestr)
   print(out.encode('utf-8'))
  exit(0)
 return ans

combining_chars = make_combining_chars() # a list 




def update_asdict(line,asdict):
 if line == '':
  return
 parts = []
 prev = None
 for ic,c in enumerate(line):
  if ic == 0:
   prev = c
  elif c in combining_chars:
   prev = prev + c
  else:
   # not a combining character and not the first character
   parts.append(prev)
   prev = c
  if ord(c) == 8206: # \u200e left-to-right mark:
   print('left-to-right-mark at character position',ic+1,'in line\n' ,line)
   print(len(line))
   atemp =[]
   for jc in range(ic-5,ic+5):
    xc = line[jc]
    if jc == ic:
     atemp.append('**'+xc+'**')
    else:
     atemp.append(xc)
   atempx = ' '.join(atemp)
   print(atempx)
   print()
 parts.append(prev)
 #print 'line=',line.encode('utf-8')
 for ic,c in enumerate(parts):
  #print ic,c
  if (len(c) == 1) and (ord(c) <= 127):
   # skip ascii character character
   continue
  if c not in asdict:
   asdict[c] = 0
  asdict[c] = asdict[c] + 1
 #exit(0)

def check_ea(filein,fileout):
# set up regex callback 'repl' with access to dictionary asdict
 asdict = {}
 # read the lines of the file
 f = codecs.open(filein,encoding='utf-8',mode='r')
 n = 0
 for line in f:
  line = line.rstrip()
  n = n + 1
  update_asdict(line,asdict)
  
 f.close()
 keys = asdict.keys()
 print(n,"lines in",filein)
 print(len(keys),"extended ascii codes found in",filein)

 keys = sorted(keys)
 print( len(keys))
 outlines = []
 for key in keys:
  asobj = asdict[key]
  #key1=convert(key)
  # key is a string
  # ords = ["\u%04x" % ord(c) for c in key]
  ords = []
  for c in key:
   try:
    uval = r"\u%04x" % ord(c)
   except:
    print('WARNING: Cannot convert: c=%s, ord(c)=%s' % (c,ord(c)))
    uval = "???"
   ords.append(uval)
  ordstr = ''.join(ords)
  names = [unicodedata.name(c) for c in key]
  namestr = ' + '.join(names)
  #out = "%s  (\\u%04x) %5d := %s" %(key,ord(key),asobj,namestr)
  out = "%s  (%s) %5d := %s" %(key,ordstr,asobj,namestr)
  outlines.append(out)
 fout = codecs.open(fileout,'w','utf-8')
 for out in outlines:
  fout.write("%s\n" % out)
 fout.close()
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 check_ea(filein,fileout)
