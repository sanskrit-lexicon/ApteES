# coding=utf-8
""" see_merge.py for ae
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

class Change(object):
 def __init__(self,iline,line1,line2,metaline1):
  self.iline = iline
  self.line1 = line1
  self.line2 = line2
  self.lnum = iline+1
  self.metaline1 = metaline1 
  a = []
  a.append('; %s' %metaline1)
  a.append('%s old %s' %(self.lnum,self.line1))
  a.append(';')
  a.append('%s new %s' %(self.lnum,self.line2))
  a.append(';---------------------------------------------------')
  self.changeout = a

def merge_lines(lines,joinchar=' '):
 out = joinchar.join(lines)
 return out

def group_entries(groups):
 entries = []
 for igroup,group in enumerate(groups):
  if group[0].startswith('<L>'):
   entries.append(igroup)
 return entries


def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)

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
 # print('group0 = ',group[0])
 return groups

def change_groups_01(groups1):
 dbg = False
 nchg = 0
 notok = 0
 nok = 0
 entries1 = group_entries(groups1)
 #print(len(entries1),"entries")
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  groupline = '\n'.join(group1)
  newgroupline = re.sub(r'({%See%})\n({@[^@]*@})([;,.]*) *',
                        r'\1 \2\3\n',
                        groupline)
  """                 
  newgroupline = re.sub(r'‘([^’]+)\n([^’]+)’\n',
                        r'‘\1 \2’\n\n',
                        newgroupline)
  newgroupline = re.sub(r'‘([^’]+)\n([^’]+)’([;,.])',
                        r'‘\1 \2’\3\n',
                        newgroupline)
  """                    
  if newgroupline != groupline:
   # remove initial space that our change may have introduced
   newgroupline1 = re.sub(r'\n +','\n',newgroupline)
   # if one of the lines starts with '. ', put the period on prev line
   newgroupline2 = re.sub(r'\n\. +', '.\n',newgroupline1)
   newgroup = newgroupline2.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('change_groups_01: %s entries changed' % nchg)
 

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
 option = sys.argv[1]
 filein = sys.argv[2] # xxx.txt cdsl
 fileout = sys.argv[3] # xxx.txt
 lines = read_lines(filein)
 groups = init_groups_simple(lines)
 # revise groups
 if option == '01':
  change_groups_01(groups)
 else:
  print('unknown option',option)
  exit(1)

 lines2 = groups_to_lines(groups)
 changes = make_changes(lines,lines2)
 write_changes(fileout,changes)
