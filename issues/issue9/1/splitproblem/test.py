import sys, re,codecs

def runtest(nlines):
 lines = []
 for i in range(nlines):
  line = ' B %02d E = %s' %(i,i+1)
  lines.append(line)
 groupline = '\n'.join(lines)
 regex = r'(B.*?E)'
 bparts = re.split(regex,groupline,re.DOTALL)
 print('bparts:',len(bparts))
 # b = [part for part in bparts if part.startswith(firstc)]
 for i,bpart in enumerate(bparts):
  bpart1 = bparts[i].replace('\n','') 
  print('part[%s] = "%s"' % (i,bpart1))

if __name__=="__main__":  
 nlines = int(sys.argv[1])
 runtest(nlines)
