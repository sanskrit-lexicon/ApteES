# coding=utf-8
""" fmt_1.py
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

class Entry:
 def __init__(self,metaline,head,body):
  self.metaline = metaline
  self.head = head
  self.body = body
  
def reformat_cdsl(groups):
 ans = []
 nchg = 0
 newgroups = []
 for group in groups:
  if not group[0].startswith('<L>'):
   continue
  metaline = group[0]
  entries = []  # (sub)-entries of this group
  # first line primary entry headwords
  firstline = group[1]
  assert '¦' in firstline
  m = re.search(r'^(.*?¦,) *(.*)$',firstline)

  headpart,tailpart = m.group(1),m.group(2)
  
  a = '\n'.join(group[2:-1])
  groupline = '%s\n%s' %(tailpart,a)
  parts = re.split(r'({@-.*?@})',groupline)
  assert not parts[0].startswith('{@-')
  bodypart = parts[0]
  entry = Entry(metaline,headpart,bodypart)
  entries.append(entry)
  nparts = len(parts)
  for ipart,part in enumerate(parts):
   if not part.startswith('{@-'):
    continue
   if ipart == nparts:
    print('fmt_1 ERROR 1',metaline)
    exit(1)
   headpart = part
   bodypart = parts[ipart+1]
   entry = Entry(metaline,headpart,bodypart)
   entries.append(entry)
  newgroup = []
  newgroup.append(metaline)
  for entry in entries:
   head = entry.head
   body = entry.body
   newgroup.append('<e><head>%s</head>' % head)
   newgroup.append('<body>')
   body_lines = body.split('\n')
   for body_line in body_lines:
    if body_line.strip() != '':
     newgroup.append(body_line)
   newgroup.append('</body>')
   newgroup.append('</e>')
  newgroup.append('<LEND>')
  newgroups.append(newgroup)
 print(len(newgroups),"cdsl groups")
 return newgroups

def get_hwrecs2(groups):
 hwrecs = []
 nchg = 0
 entries = group_entries(groups)
 for ientry,e in enumerate(entries):
  group = groups[e]
  metaline = group[0]
  # first line primary entry headwords
  firstline = group[1]
  if not ('¦' in firstline):
   print('get_hwrecs2: Error 1',metaline)
   exit(1)
  headpart,tailpart = firstline.split('¦')
  a = ' '.join(group[2:-1])
  groupline = '%s %s' %(tailpart,a)
  
  subhws0 = re.findall(r'Ⓝ.*?➔',groupline)
  subhws = []
  for subhw0 in subhws0:
   a = re.findall('{@.*?@}',subhw0)
   for subhw in a:
    subhws.append(subhw)
  hwrec = HWrec_01(metaline,headpart,subhws)
  hwrecs.append(hwrec)
 return hwrecs


def write_diffs_1(fileout,recs1,recs2):
 outarr = []
 assert len(recs1) == len(recs2)
 ndiff = 0
 for idx,rec1 in enumerate(recs1):
  rec2 = recs2[idx]
  n1 = len(rec1.subhws)
  n2 = len(rec2.subhws)
  if n1 == n2:
   continue
  ndiff = ndiff + 1
  metaline = rec1.metaline
  assert metaline == rec2.metaline
  #m = re.search('<L>(.*?)<',metaline) 
  #L = m.group(1)
  headpart1 = rec1.headpart
  subhws1 = rec1.subhws
  numsubhws1 = len(subhws1)
  meta = re.sub(r'<k2>.*$','',metaline)
  outarr.append('* '+meta)  # * for emacs org mode
  n = max(n1,n2)
  for i in range(n):
   if i < n1:
    a1 = rec1.subhws[i]
   else:
    a1 = '--'
   if i < n2:
    a2 = rec2.subhws[i]
   else:
    a2 = '--'
   out = '%02d %s %s' %(i+1,a1,a2)
   outarr.append(out)
  #outarr.append('cdsl: %s' % ' :: '.join(rec1.subhws))
  #outarr.append('ab  : %s' % ' :: '.join(rec2.subhws))
  outarr.append('')

 print(ndiff,"ndifferences in write_diffs_1")
 write_lines(fileout,outarr)

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

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # 
 fileout = sys.argv[3] # 
 lines = read_lines(filein)
 groups = init_groups_simple(lines)

 if option == 'cdsl':
  newgroups = reformat_cdsl(groups)
  write_groups(fileout,newgroups)
 elif option == 'ab':
  newgroups = reformat_ab(groups)
  write_groups(fileout,newgroups)
 else:
  print('ERROR. Unknown option',option)
  exit(1)
