#-*- coding:utf-8 -*-
"""ea_convert.py
 
"""
import sys,re,codecs
import unicodedata
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def get_replacements(option):
 a = [
  (u'\u29eb', u'\u2666'), # BLACK LOZENGE  ->  BLACK DIAMOND SUIT
  #(u'\u0001f784', u'\u2022'),  # BLACK SLIGHTLY SMALL CIRCLE -> BULLET 
  #(u'\u0001f81a', u'\u2794'), # HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD -> HEAVY RIGHTWARDS ARROW
  (u'🞄',u'\u2022'),
  (u'🠚',u'\u2794'),
  ]
 ax = [
  ('&#x29EB;', ' HELLO '), # BLACK LOZENGE  ->  BLACK DIAMOND SUIT
  ('\\U0001f784', '\\U2022'),  # BLACK SLIGHTLY SMALL CIRCLE -> BULLET 
  ('\\U0001f81a', '\\U2794'), # HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD -> HEAVY RIGHTWARDS ARROW
  ]
 
 if option == 'AB,CDSL':
  return a
 if option == 'CDSL,AB':
  b = []
  for x,y in a:
   b.append((y,x))
  return b
 print('UNKNOWN OPTION',option)
 exit(1)
 
def convert_lines(lines,option):
 replacements = get_replacements(option)
 print(replacements)
 
 newlines = []
 for oldline in lines:
  line = oldline
  for old,new in replacements:
   line = line.replace(old,new)
  newlines.append(line)
 return newlines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')

def read_lines(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def test():
#   ('\u01f81a', '\u2794'), # HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD -> HEAVY RIGHTWARDS ARROW
#  ('🠚','\u2794'),
 s = '{@A@}, {@An@}¦,🠚✦🠚♦(As an article)'
 s = ',🠚 cd🠚 (As an article)'
 # test1
 s = '🠚'  # unicode 01f81a
 t = '\u1f81a'
 print('test1:',s,t,s == t)
 # test2
 s = '🞄'  # unicode 01f784
 t = '\u17f84'
 print('test2:',s,t,s == t)

 # test3
 s = '🠚'  # unicode 01f81a
 t = '\u0001\uf81a'
 print('test3:',s,t,s == t)
 # test4
 s = '🞄'  # unicode 01f784
 t = '\u0001u7f84'
 print('test4:',s,t,s == t)

 s = 'Your original string with 🞄 character'
 t = s.replace(u"\U0001F784", "XXX")
 print('s=',s)
 print('t=',t)
 exit(1)
 sa = s.replace(u'\u1f81a','HELLO')
 print('s =',s)
 print('sa=',sa)
 print('s == sa is',s==sa)
 sb = s.replace('🠚',' HELLO ')
 print('sb=',sb)
 #exit(1)
#test()

if __name__=="__main__":
 
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # extended ascii

 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 newlines = convert_lines(lines,option)
 write_lines(fileout,newlines)
 print(len(newlines),"lines written to",fileout)
 
 
 
