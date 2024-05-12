# coding=utf-8
""" extract_entries
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)


def separate(lines):
 # index of line before first <L>
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   iline1 = iline - 1
   break
 # index of line after last <LEND>
 for iline,line in reversed(list(enumerate(lines))):
  if line.startswith('<LEND>'):
   iline2 = iline + 1
   break
 print(iline1,iline2)
 return iline1,iline2
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 fileout1 = sys.argv[2] # before first <L>
 fileout2 = sys.argv[3] # xxx.txt from first <L> through last <LEND>
 fileout3 = sys.argv[4] # after last <LEND>
 
 lines = read_lines(filein)
 iline1,iline2 = separate(lines)
 write_lines(fileout1,lines[0:iline1])
 write_lines(fileout2,lines[iline1:iline2])
 write_lines(fileout3,lines[iline2:])
 
# (- 89611 89385)
