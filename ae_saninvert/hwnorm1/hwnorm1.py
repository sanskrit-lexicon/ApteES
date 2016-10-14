"""hwnorm1.py
   Sep 5, 2016
"""
import sys,re

class HWnorm1rec(object):
 d = {} # dictionary of normalized keys
 n = 0
 def __init__(self,line):
  line=line.rstrip('\r\n')
  m = re.search(r'^(.*?):(.*)$',line)
  self.normkey = m.group(1)
  rest = m.group(2)
  parts = rest.split(';')
  self.keys = []
  self.dictstrs = []
  for part in parts:
   (key,s) = part.split(':')
   self.keys.append(key)
   self.dictstrs.append(s)
  HWnorm1rec.d[self.normkey]=self
  HWnorm1rec.n = HWnorm1rec.n + 1

def init_hwnorm1(filein=None):
 if filein == None:
  import os
  dir_path = os.path.dirname(os.path.realpath(__file__))
  filein = os.path.join(dir_path,"hwnorm1c.txt")
 with open(filein,"r") as f:
  recs = [HWnorm1rec(line) for line in f]
 print len(recs),"read from",filein

"""
function slp_cmp1_helper1($m){
 $slp1_cmp1_helper_data = array(
 'k'=>'N','K'=>'N','g'=>'N','G'=>'N','N'=>'N',
 'c'=>'Y','C'=>'Y','j'=>'Y','J'=>'Y','Y'=>'Y',
 'w'=>'R','W'=>'R','q'=>'R','Q'=>'R','R'=>'R',
 't'=>'n','T'=>'n','d'=>'n','D'=>'n','n'=>'n',
 'p'=>'m','P'=>'m','b'=>'m','B'=>'m','m'=>'m');
 //n = m.group(1) // always M
 $c = $m[2];
 $nasal = $slp1_cmp1_helper_data[$c];
 return ($nasal. $c);
}
function normalize_key($a){
 //1. Use  homorganic nasal rather than anusvara
 $a = preg_replace_callback('/(M)([kKgGNcCjJYwWqQRtTdDnpPbBm])/',"slp_cmp1_helper1",$a);
 //2. normalize so that 'rxx' is 'rx' (similarly, fxx is fx)
 $a = preg_replace('/([rf])(.)\2/','\1\2',$a);
 //3. ending 'aM' is 'a' (Apte)
 $a = preg_replace('/aM$/','a',$a);
 //4. ending 'aH' is 'a' (Apte)
 $a = preg_replace('/aH$/','a',$a);
 //4a. ending 'uH' is 'u' (Apte)
 $a = preg_replace('/uH$/','u',$a);
 //4b. ending 'iH' is 'i' (Apte)
 $a = preg_replace('/iH$/','i',$a);
 //5. 'tt' is 't' (pattra v. patra)
 $a = preg_replace('/ttr/','tr',$a);
 //6. ending 'ant' is 'at'
 $a = preg_replace('/ant$/','at',$a);
 //7. 'cC' is 'C'
 $a = preg_replace('/cC/','C',$a);
 return $a;
}
"""
slp1_cmp1_helper_data = {
 'k':'N','K':'N','g':'N','G':'N','N':'N',
 'c':'Y','C':'Y','j':'Y','J':'Y','Y':'Y',
 'w':'R','W':'R','q':'R','Q':'R','R':'R',
 't':'n','T':'n','d':'n','D':'n','n':'n',
 'p':'m','P':'m','b':'m','B':'m','m':'m'}
def slp_cmp1_helper1(m):
 # n = m.group(1) # always M
 c = m.group(2)
 nasal = slp1_cmp1_helper_data[c]
 return nasal + c

def normalize_key(key):
 a = key
 #1. Use  homorganic nasal rather than anusvara
 a = re.sub('(M)([kKgGNcCjJYwWqQRtTdDnpPbBm])',slp_cmp1_helper1,a)
 #2. normalize so that 'rxx' is 'rx' (similarly, fxx is fx)
 a = re.sub(r'([rf])(.)\2',r'\1\2',a)
 #3. ending 'aM' is 'a' (Apte)
 a = re.sub('aM$','a',a)
 #4. ending 'aH' is 'a' (Apte)
 a = re.sub('aH$','a',a)
 #4a. ending 'uH' is 'u' (Apte)
 a = re.sub('uH$','u',a)
 #4b. ending 'iH' is 'i' (Apte)
 a = re.sub('iH$','i',a)
 #5. 'tt' is 't' (pattra v. patra)
 a = re.sub('ttr','tr',a)
 #6. ending 'ant' is 'at'
 a = re.sub('ant$','at',a)
 #7. 'cC' is 'C'
 a = re.sub('cC','C',a)
 return a


def find(key):
 if HWnorm1rec.n == 0:
  init_hwnorm1()
 normkey = normalize_key(key)
 #print key,normkey
 if normkey not in HWnorm1rec.d:
  return None
 return HWnorm1rec.d[normkey]

if __name__ == "__main__":
 key = sys.argv[1]
 rec = find(key)
 if not rec:
  print "key not found"
 else:
  print "key found:",rec.keys
