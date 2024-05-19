# coding=utf-8
""" marklnum.py
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
 return groups

def change_groups_01_helper(groups1,case,regex1,regex2):
 dbg = False
 nchg = 0
 entries1 = group_entries(groups1)
 for ientry,e1 in enumerate(entries1):
  group1 = groups1[e1]
  metaline = group1[0]
  groupline = '\n'.join(group1)
  newgroupline = re.sub(regex1, regex2,groupline)
  if newgroupline != groupline:
   newgroup = newgroupline.split('\n')
   groups1[e1] = newgroup
   nchg = nchg + 1
 print('Case %s, %s entries changed: "%s" -> "%s" ' %
       (case,nchg,regex1,regex2))

def change_groups_01(groups):
 change_groups_01_helper(groups,'01a',  r'\. ([0-9]+)@}', r'@}. {@\1@}')
 change_groups_01_helper(groups,'01b',  r'{@([^-][^@]+) -', r'{@\1@} {@-')
 change_groups_01_helper(groups,'01c',
                         r'{@(-[A-Z][a-z]+), (-[A-Z][a-z]+)@}',
                         r'{@\1@}, {@\2@}')

 change_groups_01_helper(groups,'01d',  r'\.@}', r'@}.')
 change_groups_01_helper(groups,'01e',  r',@}', r'@},')
 change_groups_01_helper(groups,'01f',
                         r'{@([A-Z][a-z]*), ([A-Z][a-z]*)@}¦',
                         r'{@\1@}, {@\2@}¦')
 change_groups_01_helper(groups,'01g',
                         r'{@-([A-Z][a-z]*), ?([A-Z][a-z]*)@}',
                         r'{@-\1@}, {@-\2@}')
 change_groups_01_helper(groups,'01h',
                         r'{@-([a-z]*), ?-([a-z]*)@}',
                         r'{@-\1@}, {@-\2@}')
 change_groups_01_helper(groups,'01i',
                         r'{%See%} {@([A-Z][a-z]*), ?([A-Z][a-z]*)@}',
                         r'{%See%} {@\1@}, {@\2@}')
 change_groups_01_helper(groups,'01j',
                         r'{@(-[a-z]*), ?(-[A-Z][a-z]*)@}',
                         r'{@\1@}, {@\2@}')
 change_groups_01_helper(groups,'01k',
                         r'{@(-[A-Z][a-z]*), ?(-[a-z]*)@}',
                         r'{@\1@}, {@\2@}')
 change_groups_01_helper(groups,'01l',
                         r'{@([0-9]+) ([A-Z][a-z]*)@}',
                         r'{@\1@} {@\2@}')
 change_groups_01_helper(groups,'01m',
                         r'{@(-[a-z]+), ([A-Z][a-z]+)@}',
                         r'{@\1@}, {@-\2@}')
 #change_groups_01_helper(groups,'01x',  r'', r'')
 #change_groups_01_helper(groups,'01x',  r'', r'')
 #change_groups_01_helper(groups,'01x',  r'', r'')
 #change_groups_01_helper(groups,'01x',  r'', r'')


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

def init_replacements(filein):
 lines = read_lines(filein)
 ans = []
 for line in lines:
  count,old,new = line.split('\t')
  replacement = (old,new)
  ans.append(replacement)
 return ans

def change_groups_02(groups,replacements):
 nchg = 0
 entries = group_entries(groups)
 for ientry,e1 in enumerate(entries):
  group1 = groups[e1]
  metaline = group1[0]
  groupline = '\n'.join(group1)
  newgroupline = groupline
  for replacement in replacements:
   old,new = replacement
   newgroupline = newgroupline.replace(old,new)
  if newgroupline != groupline:
   newgroup = newgroupline.split('\n')
   groups[e1] = newgroup
   nchg = nchg + 1
 print("change_groups_02:",nchg,"entries changed")

def get_lnums(option):
 if option == '01':
  lnums = [ 5713,  6077,  8004,  9124, 10459, 10768, 11135, 12440, 12904, 12910, 12925, 12926, 14982, 15860, 16503, 16637, 18315, 21603, 22353, 23649, 24205, 25457, 25827, 26463, 27014, 27302, 27408, 28307, 31075, 32935, 33992, 36359, 36958, 36964, 38215, 38381, 38509, 38732, 39802, 41636, 45089, 45212, 49200, 49295, 54590, 55676, 57467, 60279, 61046, 62141, 64896, 65101, 66080, 68192, 70869, 71297, 71363, 71861, 72196, 72232, 73895, 77078, 77160, 78049, 78194, 79530, 79909, 81072, 81177, 83663, 84236, 84715, 85341, 86499, 87267, 88432, 
   ]
 elif option == '02':
  lnums = [
    595,    627,   1678,   2140,   2348,   2379,   3157,   4630,   4657,   6077,   7022,   7306,   9456,   9861,   9982,  10843,  11051,  11135,  11140,  11338,  11657,  11909,  12241,  12247,  12251,  12255,  12357,  12378,  12382,  12427,  12440,  12446,  12453,  12507,  12601,  13021,  13137,  13712,  13857,  15410,  15419,  17438,  17600,  17717,  18315,  18872,  18877,  20570,  21603,  22353,  23649,  24205,  24384,  24405,  25457,  25827,  26463,  26502,  27014,  27341,  27408,  27841,  27845,  27849,  27908,  28150,  29707,  30956,  31019,  31029,  31053,  31058,  31063,  31075,  31087,  31581,  32512,  33992,  34957,  35167,  35954,  36458,  36705,  36871,  36958,  37079,  37181,  37204,  37432,  37456,  37734,  37972,  38058,  38114,  38215,  38538,  38712,  39474,  39747,  39802,  39830,  41636,  41959,  43077,  43099,  43467,  43733,  43888,  43892,  44626,  44937,  45085,  45148,  45175,  45179,  45521,  46052,  46344,  47402,  47917,  48046,  49089,  49200,  49295,  51437,  51927,  52295,  52301,  52307,  52351,  52355,  52441,  53044,  53982,  55164,  55464,  55670,  55676,  55875,  56332,  56497,  56501,  56505,  56719,  57467,  57524,  57528,  57532,  57857,  57908,  58001,  58639,  59282,  59586,  59956,  60054,  60279,  62141,  62895,  62899,  62924,  62929,  62933,  62937,  62947,  63146,  63534,  63538,  63543,  63626,  63745,  63790,  65648,  65652,  66080,  66433,  67400,  70020,  70397,  70488,  70869,  71861,  72058,  72254,  73201,  73268,  73401,  73667,  73895,  74060,  74411,  75305,  75570,  75578,  76393,  76580,  76748,  78756,  80006,  80071,  81177,  81858,  82878,  84507,  84629,  85502,  85786,  85884,  86179,  86203,  86299,  86594,  86866,  87175,  87322,  87325,  87392,  87734,  87967,
  ]   
 else:
  lnums = []
 return lnums

def mark_lnums(lines,lnums):
 ans = []
 for line in lines:
  ans.append(line)
 for lnum in lnums:
  iline = lnum - 1
  old = ans[iline]
  new = '** ' + old
  ans[iline] = new
 return ans

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # xxx.txt cdsl
 fileout = sys.argv[3] # xxx.txt
 lines = read_lines(filein)
 lnums = get_lnums(option)
 newlines = mark_lnums(lines,lnums)
 write_lines(fileout,newlines)
 exit(1)
 groups = init_groups_simple(lines)
 # revise groups
 if option == '01':
  change_groups_01(groups)
 elif option == '02':
  filein1 = sys.argv[4]
  replacements = init_replacements(filein1)
  change_groups_02(groups,replacements)
 lines2 = groups_to_lines(groups)
 changes = make_changes(lines,lines2)
 write_changes(fileout,changes)
