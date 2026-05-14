"""
make_change0.py

"""
import re,sys
import codecs

fieldsep = ':'  

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} lines from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

class Group:
 def __init__(self,iline,metaline):
  self.iline = iline
  self.meta = metaline
  m = re.search(r'^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',metaline)
  self.L = m.group(1)
  self.k1 = m.group(3)
  self.pc = m.group(2)
  self.lines = [] # all lines in entry
  self.lines.append(metaline)
  #self.dbrecs = []  # list of {{X->Y}} 

def init_groups(lines): 
 #regexpc = '{{.*?}}'
 
 groups = []
 group = None
 n = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   group = Group(iline,line)
  if group == None:  # line outside of entry
   continue
  if line.startswith('<LEND>'):
   group.lines.append(line)
   groups.append(group)
   group = None
   continue
  group.lines.append(line)

 print(f'# groups={len(groups)}')
 return groups

class Arrow:
 def __init__(self,prtchg):
  # {{tpUMrvaM->tpUrvaM||20161211|||}},
  self.prtchg = prtchg
  m = re.search(r'^{{(.*?)->(.*?)\|\|(.*?)\|\|\|(.*)}}$',prtchg)
  if m == None:
   print(f'Arrow problem: {prtchg}')
   exit(1)
  self.old = m.group(1)
  self.new = m.group(2)
  self.date = m.group(3)
  self.comment = m.group(4)
  #print(f'{self.prtchg}, "{self.old}", "{self.new}", "{self.date}", "{self.comment}"')
  #exit(1)
  
class Xtract:
 def __init__(self,line):
  parts = line.split('\t')
  self.L = parts[0]
  self.k1 = parts[1]
  self.arrows = []
  for prtchg in parts[2:]:
   arrow = Arrow(prtchg)
   # print(f'DBG: {prtchg}, "{arrow.new}"')
   self.arrows.append(arrow)
  self.used = False

 
def init_extracts(lines):
 recs = [Xtract(line) for line in lines]
 d = {} # dictionary on L
 for rec in recs:
  L = rec.L
  assert L not in d
  d[L] = rec
 return recs,d

def findarrow(newstr,lines):
 ans = {}
 for i,line in enumerate(lines):
  if newstr in line:
   ans[i] = line
 return ans
class Change:
 def __init__(self,group,arrow):
  iline0 = group.iline  # index of metaline in ae.txt
  newstr = arrow.new
  prtchg = arrow.prtchg
  changelines = findarrow(newstr,group.lines)
  a = []
  a.append(f'; {group.meta}')
  a.append(f'; {arrow.prtchg}')
  changekeys = list(changelines.keys())
  self.nochange = False
  if len(changekeys) == 1:
   i = changekeys[0]
   # lnum = iline0 + i + 1
   lnum = iline0 + i # ?why
   oldline = group.lines[i]
   newline = oldline.replace(newstr,prtchg)
   a.append(f'{lnum} old {oldline}')
   a.append(';')
   a.append(f'{lnum} new {newline}')
  else:
   # show old/new ALL lines, commented out
   a.append(f'; {newstr}  NOT CHANGED')
   self.nochange = True
   nglines = len(group.lines)
   for i in range(nglines):
    if i in (0,nglines-1):
     continue
    # lnum = iline0 + i + 1
    lnum = iline0 + i
    oldline = group.lines[i]
    newline = oldline.replace(newstr,prtchg)
    a.append(f'; {lnum} old {oldline}')
    a.append(';')
    a.append(f'; {lnum} new {newline}')
    a.append(';')
  self.changelines = a
  
def make_changes(groups,xrecsd):
 changes = []
 nochange = 0 # number of changes not made
 for group in groups:
  L = group.L
  if L not in xrecsd:
   #print(f'{L} not in xrecsd')
   continue
  xrec = xrecsd[L]
  arrows = xrec.arrows
  for arrow in arrows:
   change = Change(group,arrow)
   changes.append(change)
   if change.nochange:
    nochange = nochange + 1
 print(f'{nochange} NOT CHANGED')
 return changes
#-----------------------------------------------------
def get_outlines(groups):
 outarr = []
 for group in groups:
  if  group.dbrecs == []:
   continue
  a = []
  a.append(f'{group.L}')
  a.append(f'{group.k1}')
  for prtchg in group.dbrecs:
   a.append(f'{prtchg}')
  out = '\t'.join(a)
  outarr.append(out)
 return outarr

def get_changes_outarr(changes):
 a = []
 for change in changes:
  for line in change.changelines:
   a.append(line)
 return a

if __name__=="__main__":
 filein = sys.argv[1]
 filein1 = sys.argv[2] # extract_change1.txt
 fileout = sys.argv[3]  
 lines = read_lines(filein)  ## ae.txt
 groups = init_groups(lines)

 lines1 = read_lines(filein1)
 xrecs,xrecsd = init_extracts(lines1)
 print(f'{len(xrecs)} xrecs')
 changes = make_changes(groups,xrecsd)
 print(f'{len(changes)} changes') 
 outlines = get_changes_outarr(changes)

 write_lines(fileout,outlines)
 
