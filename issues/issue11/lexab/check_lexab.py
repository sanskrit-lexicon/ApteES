""" check_lexab.py
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

def update_asdict(line,asdict):
 # modifies dictionary asdict
 if line == '':
  return
 if line.startswith('<L>'):
  return
 if line.startswith('<LEND>'):
  return
 for m in re.finditer('<lex>(.*?)</lex>',line):
  x = m.group(0)
  if x not in asdict:
   asdict[x] = 0
  asdict[x] = asdict[x] + 1
 for m in re.finditer('⁅(.*?)⁆',line):
  x = m.group(0)
  if x not in asdict:
   asdict[x] = 0
  asdict[x] = asdict[x] + 1

def check_lexab(lines):
 asdict = {}
 # read the lines of the file and update asdict
 for line in lines:
  update_asdict(line,asdict)
 # generate summary lines from asdict
 keys = asdict.keys()
 print(len(keys),"codes found")

 keys = sorted(keys)
 #print( len(keys))
 outlines = []
 for key in keys:
  n = asdict[key]
  out = f'{n:05d} {key}'
  outlines.append(out)
 return outlines
 
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 outarr = check_lexab(lines)
 write_lines(fileout,outarr)
 
