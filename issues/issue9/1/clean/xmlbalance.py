# coding=utf-8
""" xmlbalance.py 
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

def mark_groups(groups1,replacements):
 dbg = False
 nchg = 0
 entries1 = group_entries(groups1)
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  groupline = '\n'.join(group1)
  newgroupline = groupline
  for old,new in replacements:
   newgroupline = newgroupline.replace(old,new)
  if newgroupline == groupline:
   continue
  nchg = nchg + 1
  newgroup = newgroupline.split('\n')
  groups1[e1] = newgroup

 print(nchg,'entries changed')
 
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

def init_replacements(s):
 """ Example
 s = 'A,a;B,b'
 return [('A','a'),('B','b')]
"""
 ans = []
 parts1 = s.split(';')
 for part1 in parts1:
  (old,new) = part1.split(',')
  ans.append((old,new))
 return ans

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # xxx.txt cdsl
 fileout = sys.argv[3] # revised xxx.txt
 replacements = init_replacements(option)
 lines = read_lines(filein)
 groups = init_groups_simple(lines)
 # revise groups
 mark_groups(groups,replacements)
 write_groups(fileout,groups) 
