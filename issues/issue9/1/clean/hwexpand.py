# coding=utf-8
""" hwsexpand.py for ae
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

 
def get_hwrecs1(groups):
 hwrecs = []
 nchg = 0
 entries = group_entries(groups)
 for ientry,e in enumerate(entries):
  group = groups[e]
  metaline = group[0]
  # first line primary entry headwords
  firstline = group[1]
  assert '¦' in firstline
  headpart,tailpart = firstline.split('¦')
  a = '\n'.join(group[2:-1])
  groupline = '%s\n%s' %(tailpart,a)
  subhws = re.findall(r'{@-.*?@}',groupline)
  hwrec = HWrec_01(metaline,headpart,subhws)
  hwrecs.append(hwrec)
 return hwrecs

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

def get_hwrecs1a(groups):
 hwrecs = []
 nchg = 0
 entries = group_entries(groups)
 for ientry,e in enumerate(entries):
  group = groups[e]
  metaline = group[0]
  # first line primary entry headwords
  firstline = group[1]
  assert '¦' in firstline
  headpart,tailpart = firstline.split('¦')
  a = '\n'.join(group[2:-1])
  groupline = '%s\n%s' %(tailpart,a)
  subhws = re.findall(r'{@-[^@]*?@},\n{@-[^@]*?@}, ',groupline)
  hwrec = HWrec_01(metaline,headpart,subhws)
  hwrecs.append(hwrec)
 return hwrecs

def get_hwrecs2a(groups):
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
   a = re.findall('{@[^@]*?@}, {@[^@]*?@},',subhw0)
   for subhw in a:
    subhws.append(subhw)
  hwrec = HWrec_01(metaline,headpart,subhws)
  hwrecs.append(hwrec)
 return hwrecs

class HWrec_03:
 def __init__(self,metaline,matches):
  self.metaline = metaline
  self.matches = matches

def get_hwrecs3(groups,regex):
 hwrecs = []
 nchg = 0
 entries = group_entries(groups)
 for ientry,e in enumerate(entries):
  group = groups[e]
  metaline = group[0]
  groupline = '\n'.join(group)
  matches = re.findall(regex,groupline)
  hwrec = HWrec_03(metaline,matches)
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

def write_diffs_3(fileout,recs1,recs2):
 outarr = []
 assert len(recs1) == len(recs2)
 #dbg_metaline = '<L>574<pc>021<k1>aspire<k2>aspire'
 ndiff = 0
 for idx,rec1 in enumerate(recs1):
  rec2 = recs2[idx]
  #dbg = True and (rec1.metaline == dbg_metaline)
  if rec1.matches == rec2.matches:
   continue
  n1 = len(rec1.matches)
  n2 = len(rec2.matches)
  ndiff = ndiff + 1
  metaline = rec1.metaline
  assert metaline == rec2.metaline
  meta = re.sub(r'<k2>.*$','',metaline)
  outarr.append('* '+meta)  # * for emacs org mode
  n = max(n1,n2)
  for i in range(n):
   if i < n1:
    a1 = rec1.matches[i]
   else:
    a1 = '--'
   if i < n2:
    a2 = rec2.matches[i]
   else:
    a2 = '--'
   if a1 == a2:
    flag = 'EQ'
   else:
    flag = 'NE'
   #out = '%02d %s %s %s' %(i+1,a1,flag,a2)
   b1 = a1.replace('\n','<LB>')
   b2 = a2.replace('\n','<LB>')
   out = '%02d %s %s %s' %(i+1,b1,flag,b2)
   outarr.append(out)
  outarr.append('')

 print(ndiff,"ndifferences in write_diffs_3")
 write_lines(fileout,outarr)

def write_diffs_4(fileout,recs1,recs2):
 outarr = []
 assert len(recs1) == len(recs2)
 ndiff = 0
 for idx,rec1 in enumerate(recs1):
  rec2 = recs2[idx]
  if rec1.matches == rec2.matches:
   continue
  n1 = len(rec1.matches)
  n2 = len(rec2.matches)
  if n1 == n2:  # only difference from write_diffs_3
   continue
  
  ndiff = ndiff + 1
  metaline = rec1.metaline
  assert metaline == rec2.metaline
  meta = re.sub(r'<k2>.*$','',metaline)
  outarr.append('* '+meta)  # * for emacs org mode
  n = max(n1,n2)
  for i in range(n):
   if i < n1:
    a1 = rec1.matches[i]
   else:
    a1 = '--'
   if i < n2:
    a2 = rec2.matches[i]
   else:
    a2 = '--'
   if a1 == a2:
    flag = 'EQ'
   else:
    flag = 'NE'
   #out = '%02d %s %s %s' %(i+1,a1,flag,a2)
   b1 = a1.replace('\n','<LB>')
   b2 = a2.replace('\n','<LB>')
   out = '%02d %s %s %s' %(i+1,b1,flag,b2)
   outarr.append(out)
  outarr.append('')

 print(ndiff,"ndifferences ")
 write_lines(fileout,outarr)

class HWrec_05:
 def __init__(self,metaline,data):
  self.metaline = metaline
  self.data = data

def get_hwrecs5(groups):
 hwrecs = []
 nchg = 0
 regex1 = r'Ⓝ.*?➔'
 regex2 = r'{@[^@]*@}'
 entries = group_entries(groups)
 for ientry,e in enumerate(entries):
  group = groups[e]
  metaline = group[0]
  groupline = '\n'.join(group)
  matches1 = re.findall(regex1,groupline)
  data = []
  for match in matches1:
   matches2 = re.findall(regex2,match)
   data.append([match,matches2])
  hwrec = HWrec_05(metaline,data)
  hwrecs.append(hwrec)
 return hwrecs

def write_diffs_5(fileout,recs1,recs2):
 outarr = []
 assert len(recs1) == len(recs2)
 ndiff = 0
 for idx,rec1 in enumerate(recs1):
  rec2 = recs2[idx]
  ndata1 = len(rec1.data)
  ndata2 = len(rec2.data)
  assert ndata1 == ndata2
 
  for idx,data1 in enumerate(rec1.data):
   data1_n,data1_hws = data1
   data2 = rec2.data[idx]
   data2_n,data2_hws = data2
   if len(data1_hws) == len(data2_hws):
    continue
   metaline = rec1.metaline
   assert metaline == rec2.metaline
   meta = re.sub(r'<k2>.*$','',metaline)
   outarr.append('* '+meta)  # * for emacs org mode
   out1 = data1_n
   out2 = data2_n
   outarr.append('cdsl: ' + out1)
   outarr.append('  ab: ' + out2)
   outarr.append('')
   # first difference only
   ndiff = ndiff + 1
   break

 print(ndiff,"ndifferences ")
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

def replacehws_main(groups1,d2):
 newgroups = []
 ndiff = 0
 for group1 in groups1:
  if not group1[0].startswith('<L>'):
   newgroups.append(group1)
   continue
  metaline = group1[0]
  if not metaline in d2:
   print('metaline not found:',metaline)
   exit(1)
  group2 = d2[metaline]
  #
  firstline1 = group1[1]
  assert '¦' in firstline1
  headpart1,tailpart1 = firstline1.split('¦')
  hws1 = re.findall(r'{@[^@]*@}',headpart1)

  firstline2 = group2[1]
  assert '¦' in firstline2
  headpart2,tailpart2 = firstline2.split('¦')
  hws2 = re.findall(r'{@[^@]*@}',headpart2)

  n1 = len(hws1)
  n2 = len(hws2)
  if n1 != n2:
   print('replacehws_main # headwords different',metaline)
   exit(1)
  # 
  newfirstline1 = headpart2 + '¦' + tailpart1
  # newgroup1 is same as group1 except for the bbline (group[1])
  newgroup1 = []
  for i,line1 in enumerate(group1):
   if i == 1:
    newgroup1.append(newfirstline1)
   else:
    newgroup1.append(group1[i])
  newgroups.append(newgroup1)
  if newgroup1 != group1:
   ndiff = ndiff + 1
 print('replacehws_main:',ndiff,'groups changed')
 return newgroups

def replacehws_sub(groups1,d2):
 newgroups = []
 ndiff = 0
 for group1 in groups1:
  if not group1[0].startswith('<L>'):
   newgroups.append(group1)
   continue
  metaline = group1[0]
  if not metaline in d2:
   print('metaline not found:',metaline)
   exit(1)
  group2 = d2[metaline]
  groupline1 = '\n'.join(group1)
  groupline2 = '\n'.join(group2)
  hws1 = re.findall(r'Ⓝ[^➔]*➔',groupline1,re.DOTALL)
  hws2 = re.findall(r'Ⓝ[^➔]*➔',groupline2,re.DOTALL)
  assert len(hws1) == len(hws2)
  # now replace hws1[i] with hws2[i]
  newgroupline1 = groupline1
  for i,hw1 in enumerate(hws1):
   hw2 = hws2[i]
   newgroupline1 = newgroupline1.replace(hw1,hw2)
  #
  newgroup1 = newgroupline1.split('\n')
  newgroups.append(newgroup1)
  if newgroup1 != group1:
   ndiff = ndiff + 1
 print('replacehws_sub:',ndiff,'groups changed')
 return newgroups

def metaline_dict(groups):
 d = {}
 for group in groups:
  if group[0].startswith('<L>'):
   metaline = group[0]
   if metaline in d:
    print('metaline_dict duplicate:',metaline)
    exit(1)
   d[metaline] = group
 return d

if __name__=="__main__":
 filein1 = sys.argv[1] # xxx.txt cdsl
 filein2 = sys.argv[2] # AB version
 fileout = sys.argv[3] # 
 lines1 = read_lines(filein1)
 groups1 = init_groups_simple(lines1)
 lines2 = read_lines(filein2)
 groups2 = init_groups_simple(lines2)

 # correlate groups1 and groups2 with metaline
 d2 = metaline_dict(groups2)

 
 newgroups1a = replacehws_main(groups1,d2)
 newgroups = replacehws_sub(newgroups1a,d2)
 write_groups(fileout,newgroups)
 exit(1)
 
 if outopt == '1':
  hwrecs1= get_hwrecs1(groups1)
  hwrecs2= get_hwrecs2(groups2)
  write_diffs_1(fileout,hwrecs1,hwrecs2)
 elif outopt == '2':
  hwrecs1= get_hwrecs1a(groups1)
  hwrecs2= get_hwrecs2a(groups2)
  write_diffs_1(fileout,hwrecs1,hwrecs2)
 elif outopt == '3':
  regex1 = re.compile(r'Ⓝ[^•]*?➔',re.DOTALL)
  hwrecs1= get_hwrecs3(groups1,regex1)
  regex2 = re.compile(r'Ⓝ.*?➔',re.DOTALL)
  hwrecs2= get_hwrecs3(groups2,regex2)
  write_diffs_3(fileout,hwrecs1,hwrecs2)
 elif outopt == '4':
  regex = re.compile(r'Ⓝ.*?➔')
  get_hwrecs4 = get_hwrecs3
  hwrecs1= get_hwrecs4(groups1,regex)
  hwrecs2= get_hwrecs4(groups2,regex)
  write_diffs_4(fileout,hwrecs1,hwrecs2)
 elif outopt == '5':
  #regex = re.compile(r'Ⓝ.*?➔')
  #get_hwrecs4 = get_hwrecs3
  hwrecs1= get_hwrecs5(groups1)
  hwrecs2= get_hwrecs5(groups2)
  write_diffs_5(fileout,hwrecs1,hwrecs2)


 else:
  print('ERROR. Unknown option',outopt)
  exit(1)
