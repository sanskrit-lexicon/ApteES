"""
extract_change.py

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
 print(f'{len(lines)} read from {filein}')
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
  self.dbrecs = []  # list of {{X->Y}} 

def init_groups(lines): 
 regexpc = '{{.*?}}'
 
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
  for m in re.finditer(regexpc,line):
   group.dbrecs.append(m.group(0))

 print(f'# groups={len(groups)}')
 #print(f'ncomp={ncomp}')
 return groups


#-----------------------------------------------------
def old_get_outlines(groups):
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

def get_outlines_all(groups):
 outarr = []
 maxi = 0
 for group in groups:
  if  group.dbrecs == []:
   continue
  for i,prtchg in enumerate(group.dbrecs):
   a = []
   maxi = max(maxi,i)
   # a.append(i)
   a.append(f'{group.L}')
   a.append(f'{group.k1}')
   a.append(f'{prtchg}')
   out = '\t'.join(a)
   outarr.append((i,out))
 print(f'maxi = {maxi}')
 return outarr,maxi


if __name__=="__main__":
 filein = sys.argv[1]
 fileoutpfx = sys.argv[2]  # compounds.txt
 lines = read_lines(filein)
 groups = init_groups(lines)

 print(f'{len(groups)} entries from {filein}')
 outlines_all,maxi = get_outlines_all(groups)

 
 for i in range(maxi+1):
  outarr = [x[1] for x in outlines_all if x[0] == i]
  fileout = f'{fileoutpfx}_{i}.txt'
  write_lines(fileout,outarr)
 # all cases
 outarr = [x[1] for x in outlines_all]
 fileout = f'{fileoutpfx}_all.txt'
 write_lines(fileout,outarr)
