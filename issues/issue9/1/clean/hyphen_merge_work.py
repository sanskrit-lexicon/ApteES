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
 def __init__(self,metaline,lnum,line,newline):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline

class Change1:
 def __init__(self,metaline,line,newline):
  self.metaline = metaline
  self.line = line
  self.newline = newline

class Change2:
 def __init__(self,metaline,list1,list2):
  self.metaline = metaline
  self.list1 = list1
  self.list2 = list2
 
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

def init_groups(lines):
 groups1 = init_groups_simple(lines)
 # join all the groups before the first 'entry'
 groups2 = []
 g0 = [] #
 flag = True
 for igroup,group in enumerate(groups1):
  isentry = group[0].startswith('<L>') 
  if (not isentry) and flag:
   g0 = g0 + group
  elif isentry and flag:
   flag = False
   # print('g0=',g0)
   groups2.append(g0)
   groups2.append(group)
  else:
   groups2.append(group)
 print(len(groups2),"groups merging introduction")
 return groups2

def change_groups_1_helper(line1,line2):
 dbg = False 
 words1 = line1.split(' ')
 words2 = line2.split(' ')
 word1 = words1.pop() # last word on line1
 word2 = words2[0]   # first word on line2
 assert word1.endswith('-')
 word1a = word1[0:-1]  # all but the ending '-'
 word1_new = word1a + word2
 
 words1_new = words1.append(word1_new)
 words2_new = words2[1:]  # all but first word
 if dbg:
  print('line1=',line1)
  print('line2=',line2)
  print('words1=',words1)
  print('words2=',words2)
  print('word1=',word1)
  print('words1(R)=',words1)
  print('words2(R)=',words2_new)
 line1_new = ' '.join(words1)
 line2_new = ' '.join(words2_new)
 if dbg:
  print('old1=',line1)
  print('old2=',line2)
  print()
  print('new1=',line1_new)
  print('new2=',line2_new)
 return line1_new,line2_new

def make_changes(lines):
 changes = []
 dbg = False
 nchg = 0
 notok = 0
 nok = 0
 #entries1 = group_entries(groups1)
 #print(len(entries1),"entries")
 metaline = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   # new entry begins
   metaline = line
  if line.startswith('<LEND>'):
   metaline = None
   continue
  if metaline == None:
   # only change lines that are within an entry
   continue
  metaline = group1[0]
  # begin to compute change records
  if not line.endswith('-'):
   continue
   flag = True
   nextline = group1[i+1]
   line_new,nextline_new = change_groups_1_helper(line,nextline)
   group1[i] = line_new
   group1[i+1] = nextline_new
  if flag:
   nchg = nchg + 1
 print(nchg,'entries changed')

def change_groups_2_helper(line1,line2):
 dbg = False
 words1 = line1.split(' ')
 words2 = line2.split(' ')
 if dbg:
  print('line1=',line1)
  print('line2=',line2)
  print('words1=',words1)
  print('words2=',words2)
 word1 = words1.pop() # last word on line1
 word2 = words2.pop(0) # first word on line2, 
 assert word1.endswith('-#}') and word2.startswith('{#')
 word1a = word1[0:-3]  # all but the ending '-#}'
 word2a = word2[2:]    # all but the beginning '{#'
 word1_new = word1a + word2a
 
 words1.append(word1_new)
 if dbg:
  print('words1(R)=',words1)
  print('words2(R)=',words2)
 line1_new = ' '.join(words1)
 line2_new = ' '.join(words2)
 if dbg:
  print('old1=',line1)
  print('old2=',line2)
  print()
  print('new1=',line1_new)
  print('new2=',line2_new)
  exit(1)
 return line1_new,line2_new

def change_groups_2(groups1):
 # revise groups1 in place
 dbg = False
 nchg = 0
 notok = 0
 nok = 0
 entries1 = group_entries(groups1)
 print(len(entries1),"entries")
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  flag = False
  inext = None
  for i,line in enumerate(group1):
   line = group1[i]
   if not line.endswith('-#}'):
    continue
   if group1[i+1].startswith('{#'):
    inext = i+1
   elif group1[i+2].startswith('{#'):
    inext = i+2
   else:
    # no luck
    continue
   nextline = group1[inext]
   flag = True
   line_new,nextline_new = change_groups_2_helper(line,nextline)
   group1[i] = line_new
   group1[inext] = nextline_new
  if flag:
   nchg = nchg + 1
 print(nchg,'entries changed')

def change_groups_3_helper(line1,line2):
 dbg = False
 words1 = line1.split(' ')
 words2 = line2.split(' ')
 if dbg:
  print('line1=',line1)
  print('line2=',line2)
  print('words1=',words1)
  print('words2=',words2)
 word1 = words1.pop() # last word on line1
 word2 = words2.pop(0) # first word on line2, 
 assert word1.endswith('-%}') and word2.startswith('{%')
 word1a = word1[0:-3]  # all but the ending '-%}'
 word2a = word2[2:]    # all but the beginning '{%'
 word1_new = word1a + word2a
 
 words1.append(word1_new)
 if dbg:
  print('words1(R)=',words1)
  print('words2(R)=',words2)
 line1_new = ' '.join(words1)
 line2_new = ' '.join(words2)
 if dbg:
  print('old1=',line1)
  print('old2=',line2)
  print()
  print('new1=',line1_new)
  print('new2=',line2_new)
  exit(1)
 return line1_new,line2_new

def change_groups_3(groups1):
 # revise groups1 in place
 dbg = False
 nchg = 0
 notok = 0
 nok = 0
 entries1 = group_entries(groups1)
 print(len(entries1),"entries")
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  flag = False
  inext = None
  for i,line in enumerate(group1):
   line = group1[i]
   if not line.endswith('-%}'):
    continue
   if group1[i+1].startswith('{%'):
    inext = i+1
   elif group1[i+2].startswith('{%'):
    inext = i+2
   else:
    # no luck
    continue
   nextline = group1[inext]
   flag = True
   line_new,nextline_new = change_groups_3_helper(line,nextline)
   group1[i] = line_new
   group1[inext] = nextline_new
  if flag:
   nchg = nchg + 1
 print(nchg,'entries changed')

def revise_auth_nums_2(data1,data1a,data2a):
 dbg = True
 ans = []
 newdata1 = data1
 for i,ls1 in enumerate(data1a):
  ls2 = data2a[i]
  auth1,nums1 = ls1
  auth2,nums2 = ls2
  if auth1 != auth2:
   print('revise_auth_nums_2: auths differ',ls1,ls2)
   continue
  if nums1.replace(' ','') != nums2.replace(' ',''):
   print('revise_auth_nums_2: nums differ',ls1,ls2)
   continue
  old = '%s %s' %(auth1,nums1)
  new = '%s %s' %(auth2,nums2)
  # newdata1 = newdata1.replace(old,new)
  newdata1 = re.sub('\b' + old,new,newdata1)
 return newdata1


def write_groups(fileout,groups):
 outarr = []
 for group in groups:
  for x in group:
   outarr.append(x)
 write_lines(fileout,outarr)

def groups_2_lines(groups):
 outarr = []
 for group in groups:
  for x in group:
   outarr.append(x)
 return outarr

def write_line_changes(fileout,lines1,lines2):
 assert len(lines1) == len(lines2)
 outarr = []
 inentry = False
 for iline1,line1 in enumerate(lines1):
  line2 = lines2[iline1]
  if line1.startswith('<L>'):
   metaline1 = line1
   inentry = True
   assert line2.startswith('<L>')
   metaline2 = line2
  if not inentry:
   # don't change lines outside of entries
   continue
  if line1.startswith('<LEND>'):
   inentry = False
   assert line2.startswith('<LEND>')
   continue
  if line1 == line2:
   continue
  # write change
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # xxx.txt cdsl
 fileout = sys.argv[3] # xxx.txt
  
 lines = read_lines(filein)
 if option == '1':
  changes = make_changes_1(lines)
  write_changes(fileout,changes)
  exit(1)
 groups_new = init_groups(lines)
 # revise groups_new
 if option == '1':
  change_groups_1(groups_new)
 elif option == '2':
  change_groups_2(groups_new)  
 elif option == '3':
  change_groups_3(groups_new)  
 # write_groups(fileout,groups)
 lines2 = groups_2_lines(groups_new)
 write_line_changes(fileout,lines,lines2)
 changes = make_changes(groups_old,groups_new)
 
 write_groups_changes(fileout,groups_old,groups_new)
 
