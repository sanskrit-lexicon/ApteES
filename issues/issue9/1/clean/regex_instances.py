# coding=utf-8
""" regex_instances.py
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

def instances(groups,regex):
 d = {} # returned
 ntot = 0
 entries1 = group_entries(groups)
 for ientry,e1 in enumerate(entries1):
  group1 = groups[e1]
  metaline = group1[0]
  groupline = '\n'.join(group1)
  all = re.findall(regex,groupline)
  for x in all:
   if x not in d:
    d[x] = 0
   d[x] = d[x] + 1
   ntot = ntot + 1
 n = len(d.keys())
 print(n,'distinct instances found of regex=',regex)
 print(ntot,'total instances')
 return d

def write_instances_1(fileout,d):
 keys = sorted(d.keys())
 outarr = []
 ntot = 0
 for key in keys:
  n = d[key]
  ntot = ntot + n
  #outarr.append('%05d %s' %(n,key))
  outarr.append('%05d\t%s\t%s' %(n,key,key))
 write_lines(fileout,outarr)
 
def write_instances_2(fileout,d):
 keys = sorted(d.keys())
 outarr = []
 ntot = 0
 for key in keys:
  n = d[key]
  ntot = ntot + n
  outarr.append('%05d %s' %(n,key))
 write_lines(fileout,outarr)

if __name__=="__main__":
 option = sys.argv[1]
 regex = sys.argv[2]
 print('regex=',regex)
 filein = sys.argv[3] # xxx.txt cdsl
 fileout = sys.argv[4] # xxx.txt
 lines = read_lines(filein)
 groups = init_groups_simple(lines)
 d = instances(groups,regex)
 if option == '1':
  write_instances_1(fileout,d)
 elif option == '2':
  write_instances_2(fileout,d)
 else:
  print('unknown option',option)
