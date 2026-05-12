# coding=utf-8
""" change_notation.py
 
"""
import sys, re,codecs

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

# see readme.txt 
replacements = [
 ('\t ➜✦\t ⇨◆' , 'Ⓐ'),
 ('\t ⇨✦\t ⇨◆' , 'Ⓑ'),
 ('\t ➜✦' , 'Ⓒ'),
 ('\t ➜◆' , 'Ⓓ'),
 ('\t ⇨✦━' , 'Ⓔ'),
 ('〔' , '<ls>'),
 ('〕' , '</ls>'), 
 ]
def get_newline(line,option):
 newline = line
 for old,new in replacements:
  if option == 'to':
   newline = newline.replace(old,new)
  elif option == 'from':
   newline = newline.replace(new,old)
  else:
   print('option error:',option)
   exit(1)
 return newline

def get_newline1(line,option):
 # to avoid a few 'local' abbreviations 
 if option == 'to':
  newline = re.sub('⁅(.*?)⁆',r'<ab>\1</ab>',line)
 elif option == 'from':
  newline = re.sub(r'<ab>(.*?)</ab>',r'⁅\1⁆',line)
 else:
  print('get_newline1 option error',option)
  exit(1)
 return newline
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # boesp_utf8.txt
 fileout = sys.argv[3] # stats on transcoded characters
 lines = read_lines(filein)
 newlines = []
 for line in lines:
  newline = get_newline(line,option)
  newline = get_newline1(newline,option)
  newlines.append(newline)
 write_lines(fileout,newlines)
 
