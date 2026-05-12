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

def update_lslist(line,lslist):
 # modifies list lslist
 for m in re.finditer('〔(.*?)〕',line):
  x = m.group(1)
  lslist.append(x)

def check_ls(lines):
 lslist = []
 # read the lines of the file and update lslist
 for line in lines:
  update_lslist(line,lslist)
 # generate summary lines from lslist
 outarr = sorted(lslist)
 print(len(outarr),"ls refs found")
 return outarr

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 outarr = check_ls(lines)
 write_lines(fileout,outarr)
 
