# coding=utf-8
""" ea_change.py
 
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

# see readme.txt 
replacements = [
 ('⧫' , '◆' ),
 ('🞄' , '●' ),
 ('🠚' , '➜' ),
 ]
def get_newline(line):
 newline = line
 for old,new in replacements:
  newline = newline.replace(old,new)
 return newline

if __name__=="__main__":
 filein = sys.argv[1] # boesp_utf8.txt
 fileout = sys.argv[2] # stats on transcoded characters
 lines = read_lines(filein)
 newlines = []
 for line in lines:
  newline = get_newline(line)
  newlines.append(newline)
 write_lines(fileout,newlines)
 
