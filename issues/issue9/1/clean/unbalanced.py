# coding=utf-8
""" unbalanced.py 
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

def merge_lines(lines,joinchar=' '):
 out = joinchar.join(lines)
 return out

def group_entries(groups):
 entries = []
 for igroup,group in enumerate(groups):
  if group[0].startswith('<L>'):
   entries.append(igroup)
 return entries


def init_groups_simple(lines):
 groups = []
 inentry = False
 nentry = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   inentry = True
   group = [line]
  elif line.startswith('<LEND>'):
   group.append(line)
   groups.append(group)
   nentry = nentry + 1
   inentry = False
  elif not inentry:
   group = [line]
   groups.append(group)
  else: # inentry == True
   group.append(line)
 print(len(groups),"groups",nentry,"entries")
 return groups

def mark_unbalanced(groups1,xopen,xclose):
 dbg = False
 nchg = 0
 entries1 = group_entries(groups1)
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  groupline = '\n'.join(group1)
  xopena = re.findall(xopen,groupline)
  xclosea = re.findall(xclose,groupline)
  nopena = len(xopena)
  nclosea = len(xclosea)
  if nopena == nclosea:
   continue
  if dbg:
   print(metaline,nopena,nclosea)
   print(xopen,xclose)
   exit(1)
  # add an asterisk for metaline
  nchg = nchg + 1
  metaline1 = '* ' + metaline
  group1[0] = metaline1
 print(nchg,'entries marked as unbalanced')
 
def write_groups(fileout,groups):
 outarr = []
 for group in groups:
  for x in group:
   outarr.append(x)
 write_lines(fileout,outarr)

def groups_to_lines(groups):
 outarr = []
 for group in groups:
  for x in group:
   outarr.append(x)
 return outarr

def make_changes(lines1,lines2):
 n = len(lines1)
 if n != len(lines2):
  print('ERROR: files have different number of lines')
  exit(1)
 changes = []
 metaline1 = None
 metaline2 = None
 for iline,line1 in enumerate(lines1):
  line2 = lines2[iline]
  if line1.startswith('<L>'):
   metaline1 = line1
   
  if line1 == line2:
   continue
  changes.append(Change(iline,line1,line2,metaline1))
 return changes

def write_changes(fileout,changes):
 outarr = []
 for change in changes:
  for x in change.changeout:
   outarr.append(x)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

if __name__=="__main__":
 xopen = sys.argv[1]
 xclose = sys.argv[2]
 filein = sys.argv[3] # xxx.txt cdsl
 fileout = sys.argv[4] # revised xxx.txt
 lines = read_lines(filein)
 groups = init_groups_simple(lines)
 # revise groups
 mark_unbalanced(groups,xopen,xclose)
 write_groups(fileout,groups) 
