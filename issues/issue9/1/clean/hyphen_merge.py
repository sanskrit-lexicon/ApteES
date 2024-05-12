# coding=utf-8
""" hyphen_merge.py for ae
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

def compare_1(groups1,groups2,auths):
 regex = get_auth_nums_regex(auths)
 dbg = False
 changes = []
 notok = 0
 nok = 0
 entries1 = group_entries(groups1)
 entries2 = group_entries(groups2)
 assert len(entries1) == len(entries2)
 if dbg: print(len(entries1),"entries in 'compare'")
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  group1 = groups1[e1]
  group2 = groups2[e2]
  assert group1[0] == group2[0] # metaline
  metaline = group1[0]
  datalines1 = group1[1:-1]
  datalines2 = group2[1:-1]
  data1 = merge_lines(datalines1)
  data2 = merge_lines(datalines2)
  data1a = get_auth_nums(data1,regex)
  data2a = get_auth_nums(data2,regex)
  if data1a == data2a:
   nok = nok + 1
   continue
  # data differs
  notok = notok + 1
  change = Change2(metaline,data1a,data2a)
  changes.append(change)
 print(nok,'entries the same')
 print(notok,'entries differ')
 return changes

def get_auth_nums_regex_4(auths):
 # auths [A,B,...,Z]
 a = '|'.join(auths)  # A|B|...|Z
 b = r'\b(%s)' % a
 c = b + ' ([0-9 .IV]+\.)' # only diff from get_auth_nums_regex
 regex = c
 if True: # dbg
  print('auths=',auths)
  print('regex=',regex)
  #exit(1)
 return regex

def compare_4(groups1,groups2,auths):
 regex = get_auth_nums_regex_4(auths)
 dbg = False
 changes = []
 notok = 0
 nok = 0
 entries1 = group_entries(groups1)
 entries2 = group_entries(groups2)
 assert len(entries1) == len(entries2)
 if dbg: print(len(entries1),"entries in 'compare'")
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  group1 = groups1[e1]
  group2 = groups2[e2]
  assert group1[0] == group2[0] # metaline
  metaline = group1[0]
  datalines1 = group1[1:-1]
  datalines2 = group2[1:-1]
  data1 = merge_lines(datalines1)
  data2 = merge_lines(datalines2)
  data1a = get_auth_nums(data1,regex)
  data2a = get_auth_nums(data2,regex)
  if data1a == data2a:
   nok = nok + 1
   continue
  # data differs
  notok = notok + 1
  change = Change2(metaline,data1a,data2a)
  changes.append(change)
 print(nok,'entries the same')
 print(notok,'entries differ')
 return changes

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

def write_changes_1(fileout,changes):
 outarr=[]
 nauthdiff = 0
 for change in changes:
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  list1 = change.list1
  list2 = change.list2
  n1 = len(list1)
  n2 = len(list2)
  nmax = max(n1,n2)
  for i in range(nmax):
   if i < n1:
    auth1,nums1 = list1[i]
    a1 = '%s %s' % (auth1,nums1)    
   else:
    a1 = 'NA'
    auth1 = 'NA'
   if i < n2:
    auth2,nums2 = list2[i]
    a2 = '%s %s' % (auth2,nums2)    
   else:
    a2 = 'NA'
    auth2 = 'NA'
   if a1 == a2:
    flag = 'EQ'
   else:
    flag = 'NEQ'
   if auth1 != auth2:
    flag = flag + 'A'
   if False: # prior version
    out = '%s %s %s %s %s' %(i+1,metaline,a1,flag,a2)
    outarr.append(out)
   else:
    if i == 0:
     outarr.append('* ' + metaline)
    out = '%s %s %s %s' %(i+1,a1,flag,a2)
    outarr.append(out)
 write_lines(fileout,outarr)

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

def change_groups_01_helper(line1,line2):
 # first line ends with '-'
 # next lines starts with '-'
 dbg = False 
 words1 = line1.split(' ')
 words2 = line2.split(' ')
 word1 = words1.pop() # last word on line1
 word2 = words2[0]   # first word on line2
 assert word1.endswith('-')
 assert word2.startswith('-')
 word1a = word1[0:-1]  # all but the ending '-'
 word2a = word2[1:]    # all but the initial '-'
 word1_new = word1a + word2a
 
 words1_new = words1.append(word1_new)
 words2_new = words2[1:]  # all but first word
 line1_new = ' '.join(words1)
 line2_new = ' '.join(words2_new)
 return line1_new,line2_new

def change_groups_01(groups1):
 # revise groups1 in place
 dbg = False
 nchg = 0
 notok = 0
 nok = 0
 entries1 = group_entries(groups1)
 #print(len(entries1),"entries")
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  flag = False
  for i,line in enumerate(group1):
   line = group1[i]
   if not line.endswith('-'):
    continue
   flag = True
   i2 = i+1
   nextline = group1[i2]
   if not nextline.startswith('-'):
    if not nextline.startswith('[Page'):
     continue
    i2 = i + 2
    nextline = group1[i2]
    if not nextline.startswith('-'):
     continue
   line_new,nextline_new = change_groups_01_helper(line,nextline)
   group1[i] = line_new
   group1[i2] = nextline_new
  if flag:
   nchg = nchg + 1
 print(nchg,'entries changed')

def change_groups_02(groups1):
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
  newgroupline = re.sub(r'-#}\n{#-?(.*?)#}', r'-\1#}\n',groupline)
  if newgroupline != groupline:
   # remove initial space that our change may have introduced
   newgroupline1 = re.sub(r'\n +','\n',newgroupline)
   # if one of the lines starts with '. ', put the period on prev line
   newgroupline2 = re.sub(r'\n\. +', '.\n',newgroupline1)
   newgroup = newgroupline2.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('change_groups_02: %s entries changed' % nchg)
 
def change_groups_02a(groups1):
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
  newgroupline = re.sub(r'-#}\n(\[Page.*?\])\n{#-?(.*?)#}',
                        r'-\2#}\n\1\n',groupline)
  if newgroupline != groupline:
   # remove initial space that our change may have introduced
   newgroupline1 = re.sub(r'\n +','\n',newgroupline)
   # if one of the lines starts with '. ', put the period on prev line
   newgroupline2 = re.sub(r'\n\. +', '.\n',newgroupline1)
   newgroup = newgroupline2.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('change_groups_02a: %s entries changed' % nchg)
 
def change_groups_02b(groups1):
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
  newgroupline = re.sub(r'-#}\n\n{#-?(.*?)#}',
                        r'-\1#}\n\n',groupline)
  if newgroupline != groupline:
   # remove initial space that our change may have introduced
   newgroupline1 = re.sub(r'\n +','\n',newgroupline)
   # if one of the lines starts with '. ', put the period on prev line
   newgroupline2 = re.sub(r'\n\. +', '.\n',newgroupline1)
   newgroup = newgroupline2.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('change_groups_02b: %s entries changed' % nchg)

def change_groups_02c(groups1):
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
  newgroupline = re.sub(r'-#}\n{@',
                        r'#}.\n{@',groupline)
  if newgroupline != groupline:
   # remove initial space that our change may have introduced
   newgroupline1 = re.sub(r'\n +','\n',newgroupline)
   # if one of the lines starts with '. ', put the period on prev line
   newgroupline2 = re.sub(r'\n\. +', '.\n',newgroupline1)
   newgroup = newgroupline2.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('change_groups_02c: %s entries changed' % nchg)

def change_groups_02d(groups1):
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
  newgroupline = re.sub(r'-#}\n{%',
                        r'#}\n{%',groupline)
  if newgroupline != groupline:
   # remove initial space that our change may have introduced
   newgroupline1 = re.sub(r'\n +','\n',newgroupline)
   # if one of the lines starts with '. ', put the period on prev line
   newgroupline2 = re.sub(r'\n\. +', '.\n',newgroupline1)
   newgroup = newgroupline2.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('change_groups_02d: %s entries changed' % nchg)

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
 elif option == '02':
  change_groups_02(groups)
  change_groups_02a(groups)
  change_groups_02b(groups)
  change_groups_02c(groups)
  change_groups_02d(groups)

 lines2 = groups_to_lines(groups)
 changes = make_changes(lines,lines2)
 write_changes(fileout,changes)
