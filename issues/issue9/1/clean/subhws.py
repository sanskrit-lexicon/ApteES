# coding=utf-8
""" hwcount1.py
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

class Subhw:
 def __init__(self,L0,pc,head,tail,isubhw,nsubhws):
  self.dbg = False #(L0 == '9357')
  if self.dbg:
   print(L0,pc,head,isubhw,nsubhws,'\n  ',tail)
  self.L0 = L0
  self.pc = pc
  self.head = head
  self.tail = tail
  self.isubhw = isubhw
  self.nsubhws = nsubhws
  self.init_L()
  self.init_k1_k2()
  self.e = '2' # like H2 for MW
  self.init_metaline()  
  self.init_group()
  
 def init_L(self):
  L0 = float(self.L0)
  if self.nsubhws < 10:
   incr = 0.1
  else:
   # max # subgroups = 20
   incr = 0.04
  L1 = float(L0) + (float(self.isubhw)*incr)
  L2 = '%.2f' % L1
  # trim 0s
  L = re.sub('0+$','',L2)
  self.L = L

 def init_k1_k2(self):
  h = self.head
  parts = re.findall(r'{@[^@]*@}',h)
  k2s = []
  for part in parts:
   # we don't want ',' to be in part
   # if there is such a comma, change it to *
   part = part.replace(',' , '*')
   
   x = part[2:-2] # remove {@ and @}
   x = x.lower()  # lower case
   x = x.replace('[','')  # [ and ] used by AB
   x = x.replace(']','')
   k2s.append(x)
  k2 = ','.join(k2s)
  # for k1, use the first k2
  x = k2s[0]
  # this may change later
  x = x.replace(' ','_')
  k1 = x
  # attach to object
  self.k1 = k1
  self.k2 = k2

 def init_metaline(self):
  L = self.L
  pc = self.pc
  k1 = self.k1
  k2 = self.k2
  e = self.e
  self.metaline = '<L>%s<pc>%s<k1>%s<k2>%s<e>%s' %(L,pc,k1,k2,e)

 def init_group(self):
  metaline = self.metaline
  head = self.head
  # remove square-brackets
  head = head.replace('[', '')
  head = head.replace(']', '')
  tail = self.tail
  lend = '<LEND>'
  #groupline = '%s\n%s¦%s\n%s' % (metaline,head,tail,lend)
  groupline = '%s\n%s¦, %s\n%s' % (metaline,head,tail,lend)
  # for the AB version
  groupline = groupline.replace('¦,➔','¦, ')
  group = groupline.split('\n')
  self.group = group

def split1(pattern,input_string):
 # a robust replacement for re.split(regex,pattern,re.DOTALL)
 matches = re.finditer(pattern, input_string, re.DOTALL)
 prev_end = 0  # Keep track of the end position of the previous match
 parts = []
 for match in matches:
  start, end = match.span()
  # intervening_text
  parts.append(input_string[prev_end:start])
  parts.append(match.group(0))
  prev_end = end
 # the remaining text after the last match
 remaining_text = input_string[prev_end:]
 parts.append(remaining_text)
 return parts

def get_subhws(groups):
 newgroups = []
 dbg = True
 regex = r'(Ⓝ[^➔]*➔)'
 for group in groups:
  if not group[0].startswith('<L>'):
   print('get_subhws: unexpected group at %s' % group[0])
   exit(1)
  metaline = group[0]
  assert group[-1].startswith('<LEND>')
  m = re.search(r'<L>(.*)<pc>(.*)<k1>(.*)<k2>(.*)$',metaline)
  (L0,pc0,k10,k20) = (m.group(1),m.group(2),m.group(3),m.group(4))
  # first line primary entry headwords
  firstline = group[1]
  assert '¦' in firstline
  headpart,tailpart = firstline.split('¦')
  a = '\n'.join(group[2:-1])  
  groupline = '%s\n%s' %(tailpart,a)
  # add '<e>1' to metaline
  newmetaline = metaline + '<e>1' # 
  # new groups 
  #parts = re.split(regex,groupline,re.DOTALL)
  parts = split1(regex,groupline)
  if len(parts) == 1:
   # no subhws
   newgroup = []
   for i,line in enumerate(group):
    if i == 0:
     newline = newmetaline #
    elif i == 1:
     # for the AB version
     newline = line.replace('¦,➔','¦, ')
    else:
     newline = line
    newgroup.append(newline)
   #newgroup = [newmetaline] + group[1:]
   newgroups.append(newgroup)
   continue
  # first 'subgroup'
  line1 = '%s\n%s¦%s\n<LEND>' % (newmetaline,headpart,parts[0])
  # for ab version
  line1 = line1.replace('¦,➔','¦, ')
  g0 = line1.split('\n')  # 'parent' of subheadwords
  # remaining subgroups
  subhws = []
  parts1 = parts[1:]
  nparts1 = len(parts1)
  assert (nparts1 % 2) == 0
  nsubhws = nparts1 // 2
  
  isubhw = 0
  for ipart,part in enumerate(parts1):
   if (ipart % 2) == 1:
    continue
   h = part  # Ⓝ[^➔]*➔
   tail = parts1[ipart + 1]
   m = re.search(r'^Ⓝ([^➔]*)➔$',h)
   head = m.group(1)
   if head.endswith(','):
    head = head[0:-1] # remove trailing comma, if present
   isubhw = isubhw + 1
   subhw = Subhw(L0,pc0,head,tail,isubhw,nsubhws)
   subhws.append(subhw)
  # update newgroups
  newgroups.append(g0)
  for subhw in subhws:
   newgroups.append(subhw.group)
 return newgroups

def write_groups_1(fileout,groups):
 outarr = []
 for group in groups:
  # group in a list of lines
  for x in group:
   # remove blank lines
   if x.strip() != '':
    outarr.append(x)
  # add a blank line at end of group
  outarr.append('')
 write_lines(fileout,outarr)

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt 
 fileout = sys.argv[2] # 
 lines = read_lines(filein)
 groupsall = init_groups_simple(lines)
 # ignore material 'between' entries.
 groups = [group for group in groupsall if group[0].startswith('<L>')]
 newgroups = get_subhws(groups)
 write_groups_1(fileout,newgroups)

