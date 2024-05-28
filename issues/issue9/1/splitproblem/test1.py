import re, sys

def process_parts(input_string):
 pattern = r'(B.*?E)'
 matches = re.finditer(pattern, input_string, re.DOTALL)
 prev_end = 0  # Keep track of the end position of the previous match
 for match in matches:
  start, end = match.span()
  intervening_text = input_string[prev_end:start]
  print(f"Intervening Text: {intervening_text.strip()}")
  print(f"Match: {match.group(0)}")
  prev_end = end
 # Print the remaining text after the last match
 remaining_text = input_string[prev_end:]
 print(f"Remaining Text: {remaining_text.strip()}")

def split1(pattern,input_string):
 # a robust replacement for re.split(regex,pattern,re.DOTALL)
 matches = re.finditer(pattern, input_string, re.DOTALL)
 prev_end = 0  # Keep track of the end position of the previous match
 parts = []
 for match in matches:
  start, end = match.span()
  # intervening_text
  parts.append(input_string[prev_end:start])
  parts.append(match.group(0))
  prev_end = end
 # the remaining text after the last match
 remaining_text = input_string[prev_end:]
 parts.append(remaining_text)
 return parts

def print_compare(a,b):
 # a, b are lists of strings
 na = len(a)
 nb = len(b)
 n = max(na,nb)
 for i in range(n):
  a1 = '--' # not present
  b1 = '--'
  if i < na:
   a1 = a[i].replace('\n','')
  if i < nb:
   b1 = b[i].replace('\n','')
  if a1 == b1:
   flag = 'SAME'
   print('%02d "%s" %s' %(i+1,a1,flag))
  else:
   flag = 'DIFF'
   print('%02d "%s" %s "%s"' %(i+1,a1,flag,b1))
 
if __name__ == "__main__":
 nlines = int(sys.argv[1])
 regex = r'(B.*?E)'
 lines = [f' B {i:02d} E = {i+1}' for i in range(nlines)]
 groupline = '\n'.join(lines)
 parts1 = split1(regex,groupline)
 parts2 = re.split(regex,groupline,re.DOTALL)
 flag = parts1 == parts2
 if flag:
  print('both methods give same result')
 else:
  print('the two methods give different results')
  print_compare(parts1,parts2)

