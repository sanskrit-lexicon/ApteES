#-*- coding:utf-8 -*-
"""changes_1.py 
 
"""
import sys,re,codecs

def notify_out(metaline,lnum,line):
 outarr = []
 outarr.append('; %s'%metaline)
 outarr.append('%s old %s' %(lnum,line))
 outarr.append(';')
 return outarr

def change_out(metaline,lnum,line,new):
 outarr = []
 outarr.append('; %s'%metaline)
 outarr.append('%s old %s' %(lnum,line))
 outarr.append('%s new %s' %(lnum,new))
 outarr.append(';')
 return outarr

def change_out_prev(metaline,lnum,line,new,lnumprev,lineprev):
 outarr = []
 outarr.append('; %s'%metaline)
 outarr.append('%s old %s' %(lnumprev,lineprev))
 outarr.append('%s new %s' %(lnumprev,lineprev))
 outarr.append(';')
 outarr.append('%s old %s' %(lnum,line))
 outarr.append('%s new %s' %(lnum,new))
 outarr.append(';')
 outarr.append(';')
 return outarr


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # changes file
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip('\r\n') for line in f]
 with codecs.open(fileout,"w","utf-8") as fout:
  metaline = None
  for iline,line in enumerate(lines):
   line = line.rstrip('\r\n')
   if line.startswith('<L>'):
    metaline = line
    continue
   if line == '<LEND>':
    metaline = None
    continue
   if metaline == None:
    continue
   new = line.replace('.#}','#}.')
   if new == line:
    continue
   #m = re.search(regex1,line)
   #if m == None:
   # continue
   n = n + 1
   # generate change transaction
   #new = re.sub(regexraw1,r'\1<ab>\2</ab>',line)
   outarr = change_out(metaline,iline+1,line, new)
   for out in outarr:
    fout.write(out+'\n')
 print(n,'cases written to',fileout)
 

