""" lsextract.py
"""
import re,sys
import codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = []
  for iline,line in enumerate(f):
   line = line.rstrip('\r\n')
   lines.append(line)
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')
 print(len(lines),"lines written to",fileout)

def update_lsdict(line,lsdict,lsabbrevs):
 # modifies lsdict
 for m in re.finditer('〔(.*?)〕',line):
  x = m.group(1)
  found = False
  for ls in lsabbrevs:
   if x.startswith(ls):
    lsdict[ls] = lsdict[ls] + 1
    found = True
    break
  if not found:
   print(f'ERROR: Abbreviation {x} not found')
   exit(1)

def check_ls(lines,lsabbrevs):
 lsdict = {}
 for ls in lsabbrevs:
  lsdict[ls] = 0
 # read the lines of the file and update lsdict
 for line in lines:
  update_lsdict(line,lsdict,lsabbrevs)
 # generate summary lines from lsdict
 outarr0 = [f'{ls}:{lsdict[ls]}:' for ls in lsabbrevs]
 outarr = sorted(outarr0) # normal alphabetic sort.
 print(len(outarr),"ls refs found")
 # get total using lsdict
 ntot = sum(lsdict[ls] for ls in lsabbrevs)
 print('check_ls: ntot=',ntot)
 return outarr

lsabbrevs_raw = """
Bh.|r. n
D. K.|r. n
H.|n
K.|r. n
Ka.|None OR n
Kav.|None
Ki.|r. n
Li.|None OR n
M.|n
Mah.|r. n. n
Mal.|n
Mallinātha| None
Me.|n
Mr.|n
Mu.|n
N.|r. OR r. n
P.|n OR r. n
R.|r. n
Rat.|n
S.|None or n
S. B.|n OR n, n
S. K.|None
S. R.|n
Si.|r. n
U.|n
V.|n
V. M.|n
Ve.|n
Vi.|n
Y.|r. n
"""
def get_lsabbrevs():
 lines = lsabbrevs_raw.splitlines()
 ans = []
 for line in lines:
  if '|' not in line:
   continue
  parts = line.split('|')
  abbrev = parts[0]
  ans.append(abbrev)
 print(f'{len(ans)} abbreviations')
 ans1 = sorted(ans, key = lambda x: len(x), reverse = True)
 if False:
  for x in ans1:
   print(x)
  exit(1)
 return ans1


#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lsabbrevs = get_lsabbrevs()
 lines = read_lines(filein)
 outarr = check_ls(lines,lsabbrevs)
 write_lines(fileout,outarr)

 
