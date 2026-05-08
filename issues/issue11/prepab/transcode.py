# coding=utf-8
""" transcode.py
 
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')

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

if __name__=="__main__":
 tranin = sys.argv[1]
 tranout = sys.argv[2]
 filein = sys.argv[3] # boesp_utf8.txt
 fileout = sys.argv[4] # stats on transcoded characters
 lines = read_lines(filein)
 newentries = []
 def transcode_sub(m):
  x = m.group(1)
  y = transcoder.transcoder_processString(x,tranin,tranout)
  return '<s>%s</s>' % y
 newlines = []
 for line in lines:
  newline = re.sub(r'<s>(.*?)</s>',transcode_sub,line)
  newlines.append(newline)
 write_lines(fileout,newlines)
 
