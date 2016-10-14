"""invert1.py
   Sep 4, 2016
   Use ae.xml
"""
import sys,re,codecs
from lxml import etree

def san_adjust1(x):
 """ x is a sanskrit word or phrase.
    Remove some characters
 """
 # replace punctuation
 #x = re.sub(r'[:,.!?;()]',' ',x)
 x = re.sub(r'[^a-zA-Z-]',' ',x)
 x = x.strip() # remove white space at ends
 x = re.sub(r' +',' ',x) # replace multiple spaces with a single space
 x = re.sub(r'- *-','-',x) # See Abandon example vi-ut- -sfj => vi-ut-sfj
 return x

def main(filein,fileout):
 fout = codecs.open(fileout,"w","utf-8")
 n=0
 for _, element in etree.iterparse(filein, tag='H1'):
  n = n + 1
  key1elt = element.find('.//' + 'key1')
  key1 = key1elt.text
  Lelt = element.find('.//' + 'L')
  L = Lelt.text
  pcelt=element.find('.//' + 'pc')
  pc = pcelt.text
  sanelts = element.findall('.//' + 's')
  # Since there may be markup (notably '<lb/>' within the s-elements
  # To get ALL the text, we can't just  use sanelt.text
  #sanlist0=[sanelt.text for sanelt in sanelts]
  #print "   ",sanlist0
  #sanlist = [sanelt.text for sanelt in sanelts if sanelt.text ]
  sanlist=[sanelt.xpath("string()") for sanelt in sanelts]
  #print "   ",sanlist1
  sanlist = map(san_adjust1,sanlist)
  sanlist = [s for s in sanlist if s != '']
  sanliststr = ','.join(sanlist)
  out = "%s:%s:%s:%s" %(key1,L,pc,sanliststr)
  fout.write(out + '\n')
  if n  == 10:
   #break
   pass
  if key1 == 'abrogate':
   print out
 fout.close()
 print n,"H1 elements in",filein
 print n,"records written to",fileout

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout=sys.argv[2]
 main(filein,fileout)

