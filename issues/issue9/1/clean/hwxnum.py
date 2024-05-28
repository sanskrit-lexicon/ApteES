# coding=utf-8
""" hwxnum.py for ae
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

def get_diffs(a,b):
 # a, b are lists of strings
 import difflib
 # calculate the difference between the two texts
 #diffs = d.compare(a,b) # a generator of strings
 diffs = difflib.ndiff(a,b)
 #diffs1 = list(diffs)
 diffs1 = [x for x in diffs if (not x.startswith(' '))]
 diffs2 = [x for x in diffs1 if x != '']
 return diffs2


def get_data1(filein):
 lines = read_lines(filein)
 
 ans = []
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  line1 = lines[iline+1] # next line
  m = re.search(r'<L>(.*?)<',line)
  L = m.group(1)
  bb = re.sub(r'¦.*$','',line1)
  x = '%s %s' %(L,bb)
  ans.append(x)
 return ans

if __name__=="__main__":
 filein1 = sys.argv[1] # xxx.txt cdsl
 filein2 = sys.argv[2]
 fileout = sys.argv[3] # 

 data1 = get_data1(filein1) # cdsl
 data2 = get_data2(filein2) # AB
 diffs = get_diffs(data1,data2)
 write_lines(fileout,diffs)
