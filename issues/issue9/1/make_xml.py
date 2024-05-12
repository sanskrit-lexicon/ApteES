# coding=utf-8
""" make_xml.py
 Reads/Writes utf-8
 11-14-2020. remove .encode('utf-8') .  For python3 coding
 12-21-2023. md: (a) 🞄 for line break, (b) <ab>X</ab> -> <i><ab>X</ab></i>
"""
from __future__ import print_function
import xml.etree.ElementTree as ET
import sys, re,codecs
from hwparse import init_hwrecs,HW
xmlroot = HW.dictcode

%if dictlo in ['skd','vcp','armh']:
def adjust_slp1(x):
 # in skd, all text is Devanagari.  But, the text is skd.txt does not use
 #  the {#..#} markup to denote Devanagari.
 # We want to add <s>..</s> markup.
 # This requires that we separate out other markup  (always in form
 # <...>)
 outarr = []
 import string
 regex = r'(<[^>]+>)|(\[Page.*?\])|([^%s])' %string.printable
 parts = re.split(regex,x)
 for part in parts:
  if not part: #why needed?
   pass
  elif part.startswith('<') and part.endswith('>'):
   outarr.append(part)
  elif part.startswith('[Page') and part.endswith(']'):
   outarr.append(part)
  elif part[0] not in string.printable:
   outarr.append(part)
  else: # assume text slp1
   # put it into <s></s>
   y = part
   outarr.append("<s>%s</s>" % y)
 ans = ''.join(outarr)
 return ans

%endif
%if dictlo == 'krm':
def close_divs_krm(newline):
 newline = newline.replace('</Poem> </div>','</div></Poem>')
 newline = newline.replace(u'<Poem><s>“grAsasya karmakartftve nizWAnatvaM Bavet ziYaH .</s> </div>',u'</div> <Poem><s>“grAsasya karmakartftve nizWAnatvaM Bavet ziYaH .</s>')
 newline = newline.replace(u'</Poem> <s>iti prakriyAsarvasvam .</s> </div>',
  u'</div></Poem> <s>iti prakriyAsarvasvam .</s> ')
 return newline

%endif
%if dictlo not in ['ap','skd','sch','md','shs','cae','wil','ap90','bur','acc','yat']:  # These have their own code
def dig_to_xml_specific(x):
%if dictlo in ['pw','pwg','ae','gst','ieg','mwe','pgn','pui','vei','mw72','snp','bor','mw','inm','bop','abch','acph','acsj']:
 """ no changes particular to digitization"""
 return x
%else:
 """ changes particular to digitization"""
%endif
%if dictlo == 'gra':
 # 06-29-2023
 x = x.replace('_{','{')
 x = x.replace('〔','')
 x = x.replace('〕','')
 x = x.replace('%%','')
%endif
%if dictlo == 'bhs':
 # 07-27-2023
 x = x.replace('〔',"<span class='ls'>")
 x = x.replace('〕','</span>')
%endif
%if dictlo == 'pd':
 x = re.sub(r' < ',' &lt; ',x)  # 6 cases
 return x
%endif
%if dictlo == 'krm':
 x = x.replace('</F>','')
 x = x.replace('<F>','<div n="F">');
 return x
%endif
%if dictlo not in ['vcp']:
 # There are a couple entries with an <H> element.
 # Just remove these lines
 if x.startswith('<H>'):
  print("REMOVING <H> LINE",x)
  return ''
%endif
%if dictlo in ['vcp']:
 x = re.sub(r'<>','<lb/>',x) # <lb/>
 x = re.sub(r'<HI>','<div n="HI">',x) # 3362 cases
%endif
%if dictlo in ['bhs','gra','krm']:
 #x = re.sub(r'<P>','<div n="P">',x) # 2322 cases
%else:
 x = re.sub(r'<P>','<div n="P">',x) # 2322 cases
%endif
%if dictlo not in ['vcp']:
 #if '<g></g>' in x: # once only. Already converted in stc.txt
 # x = x.replace('<g></g>','<lang n="greek"></lang>')
 #x = re.sub(r'<Picture>','<div n="Picture">',x) # 71 cases
%endif
%if dictlo in ['vcp']:
 if re.search(r'^<H>',x):
  x = re.sub(r'<H>','<div n="H">',x)  # 18 cases
  print("Unexpected <H>:",x)
 x = re.sub(r'<Picture>','<div n="Picture">',x) # 71 cases
%endif
 # markup like <C1>x1<C2>x2...  indicates tabular data in vcp.
%if dictlo not in ['vcp']:
 #x = re.sub(r'<C([0-9]+)>',r'<C n="\1"/>',x)
%else:
 x = re.sub(r'<C([0-9]+)>',r'<C n="\1"/>',x)
%endif
 # change '--' to mdash
%if dictlo in ['bhs','gra','ae','krm']:
 #x = x.replace('--',u'—')  #597 cases
%else:
 x = x.replace('--',u'—')  #597 cases
%endif
%if dictlo not in ['vcp']:
 #{^X^}  superscript
 x = re.sub(r'{\^(.*?)\^}',r'<sup>\1</sup>',x)
%endif
%if dictlo in ['vcp']:
 x = adjust_slp1(x) # add <s> markup to text
%endif
%if dictlo in ['armh']:
 x = re.sub(r'(.)$', '\g<1><br/>', x)
 x = adjust_slp1(x) # add <s> markup to text
%endif
 return x
%endif # dictionaries other than ap,skd
%if dictlo == 'ap':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 # There is one instance of a 'Poem' tag, under hw=akzOhiRI
 #  <Poem>...
 #  ...
 #   ... </Poem>
 # change this to <div n="Poem">...</div>
 if re.search('Poem>',x):
  x = x.replace('<Poem>','<div n="Poem">')
  # Because of the the 'close_div' logic, we just remove </Poem>.
  # The close-div logic will add the </div>
  #x = x.replace('</Poem>','</div>')
  x = x.replace('</Poem>','')
  return x
 # in AP, ‡ is used in Devanagari text to indicate a line-break hyphen
 # This is different from the usage of this symbol in AP90.
 # Replace with '-'
 x = re.sub(u'‡','-',x)
 # in ap.txt, the Currency symbol € is markup indicating a root. It has no
 # correspondent in the printed text. About 3000+ instances.
 # For now, replace it with an empty '<root/>' element, and do not display
 # it in 'disp.php'
 x = x.replace(u'€','<root/>')
 # Divisions are indicated by lines starting with a period.
 # Three types are seen:
 # .{#-BaH#}
 # .²1 Absence  ...
 # .³({%a%})
 # 07-03-2021.  Drop restriction that the line STARTS with .² or .³
 #if re.search(u'^[.][²]',x):
 if re.search(u'[.][²]',x):
 # there may be nothing else on the line (300+ cases), in particular no space
 # do same thing anyway, not requiring the trailing space.
  x = re.sub(u'[.][²]([^ ]*) ',r'<div n="2" name="\1">\1 ',x)
  x = re.sub(u'[.][²]([^ ]*)',r'<div n="2" name="\1">\1 ',x)
 #elif re.search(u'^[.][³]',x):
 elif re.search(u'[.][³]',x):
  m = re.search('[.][³]([^ ]*) ',x)
  if not m:
   m = re.search('[.][³]([^ ]*)',x)
  assert m ,"adjust_xml. PROBLEM 1:x=\n%s"%x
  data = m.group(1)
  # data = ({%x%})
  m = re.search(r'\(<i>(.)</i>\)',data)
  assert m ,"adjust_xml. PROBLEM 2:x=\n%s"%x
  name=m.group(1)
  x = re.sub(u'[.][³]([^ ]*) ',r'<div n="3" name="%s">\1 '%name,x)
  x = re.sub(u'[.][³]([^ ]*)',r'<div n="3" name="%s">\1 '%name,x)

 # introduce line-break (call it a plain div) at any line starting with
 # a period.  This was the convention used by Thomas to designate
 # divisions. This is the /{#-BaH#} type case
 if x.startswith('.'):
  #print("extra div:",x)
  x = re.sub(r'^[.]','<div n="Q">',x)
 return x
%endif # ap dictionary
%if dictlo == 'skd':
def dig_to_xml_specific(x):
 """ changes particular to skd digitization
  Use empty <mark n="..."/> tags instead of divs for H and P
  EXCEPT for "F" (footnote), which is coded as a div
  and <C n="..."/>
 """
 x = re.sub(r'<>','<lb/>',x) # <lb/>
 # <P> seems to indicate that the line is indented.
 x = re.sub(r'<P>','<mark n="P"/>',x) #
 x = re.sub(r'<Picture>','<mark n="Picture"/>',x)
 if re.search(r'^<H>',x):
  # There are many case.
  # In the preparation of meta-line version, some (noticeably letter-breaks)
  # have been put OUTSIDE of the <L>...<LEND> scope which we are parsing
  # here.  The other <H> indicate intermediate titles. But it seems safer
  # to view them now as EMPTY tags, rather than divs. That is the
  # purpose of the <mark n="..."/> tag.
  x = re.sub(r'<H>','<mark n="H"/>',x)

  #print("Unexpected <H>:",x)
 # text has <F>...</F> five cases
 # This is the only 'div' markup used.
 # We close the div HERE, and do NOT call close_divs function
 x = re.sub(r'<F>','<div n="F">',x) # 5 cases in skd: Footnote
 x = re.sub(r'</F>','</div>',x)
 # markup like <C1>x1<C2>x2...  indicates tabular data in skd.
 x = re.sub(r'<C([0-9]+)>',r'<C n="\1"/>',x)
 # change '--' to mdash
 x = x.replace('--',u'—')  # many cases
 x = adjust_slp1(x) # add <s> markup to text
 return x
%endif
%if dictlo == 'sch':
def dig_to_xml_specific(x):
 """ changes particular to sch digitization"""
 # 04-24-2017.  Several changes
 # {!x!}  a pw homonym number
 x = re.sub(r'{!(.%?)!}',r'<hom n="pwk">\1</hom>',x)
 # {part=,seq=6766,type=,n=5}
 m = re.search(r'{part=(.*?),seq=(.*?),type=(.*?),n=(.*?)}',x)
 if m:
  temp = m.group(0)
  part = m.group(1)
  seq = m.group(2)
  t = m.group(3) # type
  n = m.group(4)
  if t != '':
   telt = '<type>%s</type>'% t
  else:
   telt = ''
  attribs=[]
  attribs.append('seq="%s"'%seq)
  attribs.append('n="%s"' %n)
  if part != '':
   attribs.append('part="%s"' % part)
  attribstr = ' '.join(attribs)
  infoelt = '<info %s/>' %attribstr
  new = '%s%s' %(telt,infoelt)
  #new = '<info part="%s" seq="%s" n="%s"/><type>%s</type>'%(part,seq,n,t)
  x = x.replace(temp,new)
 # introduce '<div>' before each EM DASH
 x = x.replace(u'—',u'<div>—')
 return x
%endif
%if dictlo == 'md':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 # we maintain line breaks and don't put in divs.
 #  the pattern <b>-   is a promising pattern for a div
 #  but there are two many variations for which this does not
 #  render properly. Thus we postpone this enhancement for now.
 # and retain line-breaks.
 divflag = False
 # for experimenting.  When divflag is True, remove '<>' and introduce <div>
 # Remove 12-15-2021. See later for introduction of <lb/>
 #if divflag:
 # x =  re.sub(r'<>','',x)  # main
 #else:
 # x =  re.sub(r'<>','<lb/>',x)  # main
 # change -- to mdash
 x = re.sub(r'--',u'—',x)
 # change ‡ to _  (two vowels that will be combined via sandhi)
 # x = re.sub(u'‡','_',x)
 x = re.sub(u'‡','‿',x) # 09-13-2023.  u+203f Undertie
 # remove the ¤ symbol. It brackets some numbers (e.g. ¤2¤) but there
 # is no obvious typographical feature.
 x = re.sub(u'¤','',x)
 # change <g>X</g> to <lang n="greek">x</lang> # 09-14-2023 comment out
 # x = re.sub(r'<g>(.*?)</g>',r'<lang n="greek">\1</lang>',x)
 if divflag:
  # add divs for <b>-
  x = re.sub(r'<b>-','<div n="1" ><b>-',x)
 """
 # add divs for other bold
 x = re.sub(r'<b>([^-])',r'<div n="2" ><b>\1',x)
 """
 # Add italic markup to '<ab>', lex, bot, zoo
 # There are both local and global <ab> instances (local: <ab n="T">X</ab>
 x = re.sub(r'(<ab.*?</ab>)',  r'<i>\1</i>',x)
 # Add italic markup to '<lex>'  currently only global
 x = re.sub(r'(<lex.*?</lex>)',  r'<i>\1</i>',x)
 # for bot and zoo : this is done at another spot for 'md'
 return x
%endif
%if dictlo == 'shs':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 x = re.sub('<>','<lb/>',x)
 x = re.sub(r' E[.]','<div n="E"> E.',x)
 x = re.sub(r' ([mfn]+[.] *\(<s>.*?</s>\))',r' <div n="1">\1',x)
 x = re.sub(r' ([mfn]+[.] *)$',r' <div n="1">\1',x)
 x = re.sub(r' ([0-9]+[.])',r' <div n="2"> \1',x)
 x = re.sub(r'<Poem>','<div n="Poem">',x)
 x = re.sub(r'</Poem>','',x)  # the 'Poem' div will be closed in closed_divs
 # divs for roots
 x = re.sub(r' (r[.] [1-9])',r'<div n="1">\1',x)
 x = re.sub(r' ([wW]ith *<s>.*?</s>)',r'<div n="1">\1',x)
 return x
%endif
%if dictlo == 'cae':
def dig_to_xml_specific(x):
 """ no changes particular to digitization"""
 return x
%endif
%if dictlo == 'wil':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 if x.startswith('<H>'):
  # Start of section beginning with a particular letter. Drop this line
  x = ''
 elif re.search(u'^[.]²[0-9]+',x):
  # a division coded by Thomas
  # drop the initial '.²'
  # and start <div n="1">
  x = '<div n="1">' + x[2:]
 elif re.search(r'^[.]E[.]',x):
  # an Etymology division
  # drop the initial '.'
  # and start <div n="E">
  x = '<div n="E">' + x[1:]
 elif re.search(r'^[.]',x):
  # unknown division
  print("UNKNOWN DIVISION: ",x)
  x =  " " + x
 else:
  # assume a simple continuation line
  x = " " + x
 # In a currently small number of cases (as with root 'RI'), sub-meanings
 # are coded with superscript letters, as '^a'. We'll code these as
 # <div n="2">
 x = re.sub(r'[\^]','<div n="2">',x)
 return x
%endif
%if dictlo == 'ap90':
def dig_to_xml_specific(x):
 """ changes particular to ap90 digitization"""
 # introduce '<div>' before each EM DASH
 #x = x.replace(u'—',u'<div>—')
 # 05-24-2021. commented out
 ##x = re.sub(r'^<>--([0-9])',r'<div n="1"/>— \1',x)
 ##x = x.replace('<>','<lb/>')
 # x = x.replace('<>','') # 05-24-2021.  not needed as of 12-15-2021
 ##x = re.sub(r' --([0-9][.])',r' <div n="1"/>— \1',x)
 x = x.replace('<P>','<P/>')
 if '<H>' in x:  # this has been removed (20170701)
  print("Skipping",x)
  x = ''
 x = x.replace('<NI>','<P/>') # under kAlidAsa in Appendix II
 # 04-21-2021.  Code formerly in basicadjust.php (— is mdash = &#x2014;
 x = x.replace('<P/>','<div n="P"/>')
 ## x = x.replace('<b>--','<div n="1"/><b>— ') removed 05-24-2021
 x = x.replace('<b>','<div n="1"/><b>') # 05-24-2021
 x = x.replace('<s>--','<div n="1"/><b>—</b> <s>')
 x = x.replace('<i>--','<div n="1"/><i>— ')
 x = re.sub(r'--([IV]+[.])',r'<div n="1"/>— \1',x)
 # 05-24-2021.
 # {cNc} -> N
 x = re.sub(r'{c(.*?)c}',r'\1',x)
 # {vXv}
 x = re.sub(r'{v(.*?)v}', r'<br/> <span style="font-size:larger;font-weight:bold;">\1</span>',x)
 # {1} -> <div n="1"/>—
 x = re.sub(r'{([0-9]+)}', r'<div n="1"/> \1',x)
 #remaining -- to mdash
 # x = x.replace('--',u'— ') remove 05-24-2021
 # x = x.replace('--',u' ') # 05-24-2021
 # 09-14-2022. Ref https://github.com/sanskrit-lexicon/csl-orig/issues/892
 #x = re.sub(r'<b>--([0-9])',r'<b>\1',x) # remove -- before numbers in bold
 x = x.replace('<b>--','<b>')
 #x = re.sub(r'<b>--',r'<b>',x) # remove -- before numbers in bold
 x = x.replace('--',u'-') # replace remaining -- by -.
 # 05-24-2021. # remove double mdashes.  This is awkward.
 #x = x.replace('— —','— ')
 # 05-24-2021  Change way [Page] handled
 #x = re.sub(r'\[Page(.*?)[+].*?\]',r'(<ab n="Page \1">pb</ab>) ',x)
 # 09-14-2022  Here is another way to handle [Pagexx]: add '<br/>
 x = re.sub(r'\[Page(.*?)[+].*?\]',r'<br/>(<ab n="Page \1">pb</ab>) ',x)
 
 return x
%endif
%if dictlo == 'bur':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 if re.search(r'^<P>',x):
  x = re.sub(r'<P>','<div n="P">',x)
 elif re.search(r'^<H>',x):
  x = re.sub(r'<H>','<H/>',x)
  print("Unexpected <H>:",x)
 # -- div takes precedence over || div
 # change '||' to a div, type = 3
 #  do NOT Retain the '||' , an aesthetic choice
 x = x.replace('||','<div n="3">')
 # We want most mdashes to start a div. but not all.
 # Restricting to the desired group is tricky. Here is a try.
 x = re.sub(u'(-- *[A-ZÀ])',r'<div n="2">\1',x)
 x = re.sub(u'(-- *<ab>[SMFN][.])',r'<div n="2">\1',x)
 # additional abbreviations before ANY abbreviation (only about 100 cases left)
 x = re.sub(u'(-- *<ab>)',r'<div n="2">\1',x)
 # {%X%} has already been changed to <i>X</i>
 x = re.sub(u'(-- *<i>)',r'<div n="2">\1',x)
 x = re.sub(u'(-- *\()',r'<div n="2">\1',x)
 # 05-03-2020. Somehow, there are empty <div n="2"> instances
 # try to get rid of these
 x = re.sub(r'<div n="2"><div n="2">','<div n="2">',x)
 # change '--' to mdash
 x = x.replace('--',u'—')
 return x
%endif
%if dictlo == 'acc':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 if re.search(r'^<>',x):
  x = re.sub(r'<>','<br/>',x)
 elif re.search(r'^<P>',x):
  x = re.sub(r'<P>','<div n="P">',x)
 elif re.search(r'^<HI1>',x):
  x = re.sub(r'<HI1>','<div n="2">',x)  # add closing div later.
 elif re.search(r'^<HI>',x):
  x = re.sub(r'<HI>','<div n="3">',x)
 elif re.search(r'^<H>',x):
  x = re.sub(r'<H>','<H/>',x)
 return x
%endif
%if dictlo == 'yat':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 if re.search(r'^<>',x):
  x = re.sub(r'<>','<br/>',x)
 return x
%endif

%if dictlo == 'pwkvn':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 x = re.sub(r'<althws>.*?</althws>','',x)
 x = re.sub(r'</?hw>','',x)
 x = re.sub(r'-?<lb/>','',x)
 x = re.sub(r'<as1>([^<]*?)</as1>',r'\1',x) # temporary markup
 return x
%endif

def dig_to_xml_general(x):
%if dictlo in ['abch', 'acph', 'acsj']:
 return x
%endif
 """ These changes likely apply to ALL digitizations"""
 # xml requires that an ampersand be represented by &amp; entity
 x = x.replace('&','&amp;')
 # remove broken bar.  In xxx.txt, this usu. indicates a headword end
 x = x.replace(u'¦',' ')
 # bold, italic, and Sanskrit markup converted to xml forms.
%if dictlo in ['ben','ccs','mci','stc','bhs','gra','pe','gst','ieg','mwe','pgn','pui','vei','pd','mw72','snp','bor','krm','inm','skd','bop','vcp']:
 # These are not applicable to vcp, but do no harm
%endif
%if dictlo == 'mw':
 # These are not applicable to mw, skip for efficiency
 #x = re.sub(r'{@','<b>',x)
 #x = re.sub(r'@}','</b>',x)
 #x = re.sub(r'{%','<i>',x)
 #x = re.sub(r'%}','</i>',x)
 #x = re.sub(r'{#','<s>',x)
 #x = re.sub(r'#}','</s>',x)
%elif dictlo == 'krm':
 x = re.sub(r'{@','<b>',x)
 x = re.sub(r'@}','</b>',x)
 x = re.sub(r'{%','<i>',x)
 x = re.sub(r'%}','</i>',x)
 #x = re.sub(r'{#','<s>',x)
 #x = re.sub(r'#}','</s>',x)
%elif dictlo == 'cae':
 # No bold in cae.txt
 #x = re.sub(r'{@','<b>',x)
 #x = re.sub(r'@}','</b>',x)
 x = re.sub(r'{%','<i>',x)
 x = re.sub(r'%}','</i>',x)
 x = re.sub(r'{#','<s>',x)
 x = re.sub(r'#}','</s>',x)
%else:
 x = re.sub(r'{@','<b>',x)
 x = re.sub(r'@}','</b>',x)
 x = re.sub(r'{%','<i>',x)
 x = re.sub(r'%}','</i>',x)
 x = re.sub(r'{#','<s>',x)
 x = re.sub(r'#}','</s>',x)
%endif
 return x

def dig_to_xml(xin):
 x = xin
 x = dig_to_xml_general(x)
 x = dig_to_xml_specific(x)
 return x

def dbgout(dbg,s):
 if not dbg:
  return
 filedbg = "make_xml_dbg.txt"
 fout = codecs.open(filedbhg,"a","utf-8")
 fout.write(s + '\n')
 fout.close()

def close_divs(line):
 """ line is the full xml record, but the <div> elements have not been
  closed.  Don't close empty div tags.
 """
%if dictlo in ['bor']:
 # we assume this closure already done
 return line
%endif
%if dictlo == 'sch':
 divregex = r'<div>' # sch has '<div>' with no attributes.
%else:
 divregex = r'<div[^>]*?[^/]>'
%endif
 if not re.search(divregex,line):
  # no divs to close
  return line
 ans = [] # strings parts of data
 idx0 = 0
 # div can have attribute
 for m in re.finditer(divregex,line):
   idx1=m.start()
   idx2 = m.end()
   line1 = line[idx0:idx1] # text preceding this div
   ans.append(line1)
   if idx0 != 0:
    # close the previous div
    ans.append('</div>')
   # include this div
   linediv = line[idx1:idx2]
   ans.append(linediv)
   idx0 = idx2 # reset for next iteration
 # construct string for all text in line upto position idx0
 new = ''.join(ans)
 # The last div will not be closed
 rest = line[idx0:]
 # We can assume that rest contains
 # <type>*</type></body> -> </div><type>*</type></body>
 # (no type)</body> -> </div></body>
 if re.search(r'(<type>.*?</type>)</body>',rest):
  newrest = re.sub(r'<type>',r'</div><type>',rest)
 elif re.search(r'</body>',rest):
  newrest = re.sub(r'</body>','</div></body>',rest)
 else:
  raise ValueError("close_divs_error: %s"%line)
 newline = new + newrest
%if dictlo == 'krm':
 newline = close_divs_krm(newline)
%endif
 return newline

def construct_xmlhead(hwrec):
 key2 = hwrec.k2
 key1 = hwrec.k1
 hom = hwrec.h
 if hom == None:
  # no homonym
  h = "<key1>%s</key1><key2>%s</key2>" % (key1,key2)
 else:
  h = "<key1>%s</key1><key2>%s</key2><hom>%s</hom>" % (key1,key2,hom)
 return h

def construct_xmltail(hwrec):
 L = hwrec.L
 pagecol = hwrec.pc
 tail = "<L>%s</L><pc>%s</pc>" % (L,pagecol)
 if hwrec.type == None:
  # normal
  return tail
 # otherwise, also <hwtype n="type" ref="LP"
 hwtype = '<hwtype n="%s" ref="%s"/>' %(hwrec.type,hwrec.LP)
 tail = tail + hwtype
 return tail

def body_alt(bodylines,hwrec):
 """
  insert an extra body line at the top.
 """
 hwtype = hwrec.type
 assert hwtype in ['alt','sub', 'fem', 'neu'],"body_alt error: %s"%hwtype
 LP = hwrec.LP  # L-number of parent
 hwrecP = HW.Ldict[LP]
 key1P = hwrecP.k1
 key1 = hwrec.k1
 templates = {
  'alt':'<alt>%s is an alternate of %s.</alt>',
  'sub':'<alt>%s is a sub-headword of %s.</alt>',
  'fem':'<alt>%s is feminine form of %s.</alt>',
  'neu':'<alt>%s is neuter form of %s.</alt>',
 }
 if HW.Sanskrit:
  # prepare for conversion from slp1 to user choice
  key1P = '<s>%s</s>' %key1P
  key1 = '<s>%s</s>' %key1
 template = templates[hwtype]
 extraline = template %(key1,key1P)
 # insert extraline at the front
 return [extraline]+bodylines

%if dictlo == 'inm':
def body_inm(lines):
 ans0 = []
 # phase 0: 12-13-2021 insert <div n="lb"> into most lines
 nodivstarts = ('<div n="P">', '<div n="HI">', '[Page', '<F>',
                #'<C n="4"/>(4) Jahnu','<C n="6"/>(6) Ṛcīka'  # why these 2?
               )
 newlines = []
 for idx,line in enumerate(lines):
  if idx == 0:
   # first of 'datalines'
   newline = line
  elif line.startswith(nodivstarts):
   newline = line
  else:
   newline = '<div n="lb">' + line
  newlines.append(newline)
 # phase 1: append <sup> lines to previous line
 nsup=0
 for idx,line in enumerate(newlines):
  if line.startswith('<sup>'): # footnote marker
   idx0 = len(ans0) - 1
   ans0[idx0] = ans0[idx0] + line
  else:
   ans0.append(line) 
 # phase 2: close each line beginning with <div
 for idx,line in enumerate(ans0):
  if line.startswith('<div'):
   if line.endswith('</F>'):
    ans0[idx] = re.sub('</F>','</div></F>',line)
   else:
    ans0[idx] = line + '</div>'
 return ans0

%endif
%if dictlo == 'bop':
def body_bop(lines):
 ans0 = []
 # phase 1: append <sup> lines to previous line
 nsup=0
 for idx,line in enumerate(lines):
  if line.startswith('<sup>'): # footnote marker
   idx0 = len(ans0) - 1
   ans0[idx0] = ans0[idx0] + line
  else:
   ans0.append(line)
 # phase 2: close each line beginning with <div
 for idx,line in enumerate(ans0):
  if line.startswith('<div'):
   if line.endswith('</F>'):
    ans0[idx] = re.sub('</F>','</div></F>',line)
   else:
    ans0[idx] = line + '</div>'
 return ans0

%endif

%if dictlo in ['anhk']:
def construct_xmlstring_1(datalines,hwrec):
 # for koshas like anhk
 dbg = False
 datalines1 = []
 # 1. h (head)
 h = construct_xmlhead(hwrec)
 dbgout(dbg,"head: %s" % h)
 #2. construct tail
 tail = construct_xmltail(hwrec)
 dbgout(dbg,"tail: %s" % tail)
 #3. construct body
 """ sample of datalines
<k1>kawaka-klI<meanings>kaRWaka,sEnya,parvatanitamba
<k1>kaRwaka-klI<meanings>romaharza,sUcyagra,kzudravErin
kawakaM kaRWake sEnye nitambe parvatasya ca .
kaRwakaM romaharze syAt sUcyagre kzudravEriRi .. 3 ..

<H1><h><key1>kawaka</key1><key2>kawaka</key2></h>
 <body>
<lb/><s>kawaka-klI</s> meanings <s>kaRWaka,sEnya,parvatanitamba</s> 
<lb/><s>kaRwaka-klI</s> meanings <s>romaharza,sUcyagra,kzudravErin</s> 
<lb/><s>kawakaM kaRWake sEnye nitambe parvatasya ca .</s> 
<lb/><s>kaRwakaM romaharze syAt sUcyagre kzudravEriRi .. 3 ..</s>
</body>
<tail><L>3</L><pc>140</pc></tail></H1>
 """
 # paratition datalines into hwdetails and entrydetails
 hwdetails = []
 entrydetails = []
 for i,x in enumerate(datalines):
  if x.startswith('<'):
   hwdetails.append(x)
  else:
   entrydetails.append(x)
 # add formatting to entrydetails
 entrydetails1 = []
 for i,x in enumerate(entrydetails):
  y = '<s>%s</s>' % x
  z = '<entrydetail>%s</entrydetail>' % y
  entrydetails1.append(z)
 entrydetails_str = ''.join(entrydetails1)
                                 
 # add formatting to hwdetails
 hwdetails1 = []
 for i,x in enumerate(hwdetails):
  yerr = '<div> %s -->' % x
  m = re.search(r'<k1>(.*?)<meanings>(.*?)$',x)
  if m == None:  # error condition
   y = '<!-- ERROR wrong form: %s -->' %x
   hwdetails1.append(y)
  else:
   hw = m.group(1)
   meaning = m.group(2)
   y1 = '<hw><s>%s</s></hw>' % hw
   y2 = '<meaning><s>%s</s></meaning>' % meaning
   y = '%s%s' % (y1,y2)
   z = '<hwdetail>%s</hwdetail>' % y
   hwdetails1.append(z)
 # string form
 hwdetails_str = ''.join(hwdetails1)
 # construct body0, by combining hwdetails and entrydetails
 bodya = '<hwdetails>' + hwdetails_str + '</hwdetails>'
 bodyb = '<entrydetails>' + entrydetails_str +'</entrydetails>'
 body = bodya + bodyb
 dbgout(dbg,"body: %s" % body)
 #4. construct result
 data = "<H1><h>%s</h><body>%s</body><tail>%s</tail></H1>" % (h,body,tail)
 #5. Close the <div> elements
 # data = close_divs(data)
 return data
%elif dictlo in ['abch', 'acph', 'acsj']:
def construct_xmlstring_2_helper(syns):
 # syns = a,b,c ...
 # each syn is either k1 or k1-gender
 # return list of k1s.
 parts = syns.split(',')
 synk1s = []
 for part in parts:
  # part is either x-y or x
  subparts = part.split('-')
  k1 = subparts[0]
  synk1s.append(k1)
 return synk1s

def construct_xmlstring_2(datalines,hwrec):
 # for koshas like abch
 dbg = False
 datalines1 = []
 # 1. h (head)
 h = construct_xmlhead(hwrec)
 dbgout(dbg,"head: %s" % h)
 #2. construct tail
 tail = construct_xmltail(hwrec)
 dbgout(dbg,"tail: %s" % tail)
 #3. construct body
 """ 
Sample entr
<L>1233<pc>39
<info kvvv="<s>tiryakkARqaH</s>, <s>pfTvIkAyaH</s>"/>
<eid>3076<syns><s>SilA-strI,aDodAru-klI</s>
<eid>3077<syns><s>nAsA-strI,urDvadAru-klI</s>
<s>stamBAdeH syAdaDodArO SilA nAsorDvadAruRi .. 1008 ..</s>
<LEND>
constructed html
 """
 # partition datalines into infos hwdetails and entrydetails
 infos = []
 hwdetails = []
 entrydetails = []
 for i,x0 in enumerate(datalines):
  # remove <s> markup
  x = re.sub(r'</?s>','',x0)
  if x.startswith('<info'):
   infos.append(x)
  elif x.startswith('<'):
   hwdetails.append(x)
  else:
   entrydetails.append(x)
 # add formatting to entrydetails
 entrydetails1 = []
 for i,x in enumerate(entrydetails):
  y = '<s>%s</s>' % x
  z = '<entrydetail>%s</entrydetail>' % y
  entrydetails1.append(z)
 entrydetails_str = ''.join(entrydetails1)
                                 
 # add formatting to hwdetails
 hwdetails1 = []
 for i,x in enumerate(hwdetails):
  yerr = '<div> %s -->' % x
  m = re.search(r'<eid>(.*?)<syns>(.*?)$',x)
  if m == None:  # error condition
   y = '<!-- ERROR wrong form: %s -->' %x
   hwdetails1.append(y)
   continue
  eid = m.group(1)
  syns = m.group(2)
  k1 = hwrec.k1
  if k1 not in construct_xmlstring_2_helper(syns):
   continue
  y1 = '<eid>%s</eid>' % eid
  y2 = '<syns><s>%s</s></syns>' % syns
  y = '%s%s' % (y1,y2)
  z = '<hwdetail>%s</hwdetail>' % y
  hwdetails1.append(z)
 # add formatting to info(s)
 # Assume exactly 1 info line
 info = infos[0]
 m = re.search(r'<info kvvv="(.*?)"/>',info)
 if m != None:
  kvvv_val = m.group(1) # value of kvvv
  info_str = "<s>%s</s>" % kvvv_val
 # string form
 hwdetails_str = ''.join(hwdetails1)
 # construct body0, by combining hwdetails and entrydetails
 bodya = '<hwdetails>' + hwdetails_str + '</hwdetails>'
 bodyb = '<entrydetails>' + entrydetails_str +'</entrydetails>'
 bodyc = '<div>%s</div>' % info_str  # put it into a div
 body = bodyc + bodya + bodyb
 
 dbgout(dbg,"body: %s" % body)
 #4. construct result
 data = "<H1><h>%s</h><body>%s</body><tail>%s</tail></H1>" % (h,body,tail)
 #5. Close the <div> elements
 # data = close_divs(data)
 return data
%else:
def construct_xmlstring(datalines,hwrec):
 # non-kosha dictionaries
 dbg = False
 datalines1 = []
 # 1. h (head)
 h = construct_xmlhead(hwrec)
 dbgout(dbg,"head: %s" % h)
 #2. construct tail
 tail = construct_xmltail(hwrec)
 dbgout(dbg,"tail: %s" % tail)
 #3. construct body
#%if dictlo in ['sch','ap90']:
%if dictlo in ['sch']:
 # To mimic current display of Sch, we remove the 'head' from first line:
 # Sept. 2021.  Head has two parts {#X#} N? {%Y%} : (N optional).
 # Remove only {#X#}
 for i,x in enumerate(datalines):
  if i == 0:
   m = re.search(u'^(.*?¦)(.*)$' ,x)
   if not m:
    print("xml_string ERROR at =",x)
    exit(1)
   head = m.group(1)
   rest = m.group(2)
   head1 = re.sub(r'{#.*?#} ','',head)
   head1 = head1.replace('¦',' ')
   x = head1 + rest
   #x = rest
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['acc']:
 for i,x in enumerate(datalines):
  if (i != 0) and not x.startswith('<'):
   x = '<br/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['shs','skd','vcp']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith('<Picture>'):
   # skd,vcp only
   x = '<lb/>' + x
  elif x.startswith(('<','[Page')):
   pass
  else:
   x = '<lb/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['mdxxx']:
 # Since dictlo never is mdxxx, this coded not executed.
 # code retained in this file for information out 12-21-2023
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith('[Page'):
   pass
  else:
   x = '<lb/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['md']:
 # revision of 12-21-2023.
 # 🞄 01F784  (Black Slightly Small Circle) gets turned into new lines
 circle = '🞄'
 for i,x in enumerate(datalines):
  # add italic markup for bot, zoo
  x = re.sub(r'(<bot.*?</bot>)',  r'<i>\1</i>',x)
  x = re.sub(r'(<zoo.*?</zoo>)',  r'<i>\1</i>',x)
  parts = x.split(circle)
  for ipart,part in enumerate(parts):
   if (ipart == 0) and (i == 0):
    newpart = part
   else:
    newpart = '<lb/>' + part #
   datalines1.append(newpart)
 datalines = datalines1
%endif
%if dictlo in ['pe','pgn','pui','vei']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith('<C '):
   # occurs in pe, vei
   x = '<div n="lb"/>' + x
  elif x.startswith(('<','[Page')):
   pass
  else:
   x = '<div n="lb"/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['snp']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith('<bot>'):
   x = '<div n="lb"/>' + x
  elif x.startswith(('<','[Page')):
   pass
  else:
   x = '<div n="lb"/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif

%if dictlo in ['mw72']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('<div n="P"/>','[Page')):
   pass
  else:
   x = '<div n="lb"/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['yat']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('[Page')):
   pass
  else:
   x = '<br/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['ben','bhs']: 
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('[Page')):
   pass
  else:
   x = '<div n="lb">' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['bop']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('[Page')):
   pass
  elif x.startswith(('<F>','<div n="pfx">')):
   pass
  else:
   #x = '<div n="lb">' + x # 05-06-2024
   x = '<br/>' + x # 05-06-2024
   pass
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['gst','ieg','mci']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('[Page')):
   pass
  elif x.startswith(('<div n="P">')):
   pass
  else:
   x = '<div n="lb">' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['krm']:
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('<s>','<note')):
   x = '<div n="lb">' + x   
  elif x.startswith(('[Page')):
   pass
  elif x.startswith(('<')):
   pass
  else:
   x = '<div n="lb">' + x
  datalines1.append(x)
 datalines = datalines1
%endif
%if dictlo in ['bor','mwe']: # 05-08-2024 not for ae
 for i,x in enumerate(datalines):
  if i == 0:
   pass
  elif x.strip() == '':
   pass
  elif x.startswith(('[Page')):
   pass
  else:
   x = '<div n="lb"/>' + x
  datalines1.append(x)
 datalines = datalines1
%endif
 bodylines = [dig_to_xml(x) for x in datalines]
 if hwrec.type != None:
  bodylines = body_alt(bodylines,hwrec)
%if dictlo == 'inm':
 bodylines = body_inm(bodylines)
%endif
%if dictlo == 'bop':
 # bop closing divs is awkward in presence of <F>X</F>
 # bodylines = body_bop(bodylines) # 05-06-2024
 pass # 05-06-2024
%endif
 body0 = ' '.join(bodylines)
 dbgout(dbg,"chk4: %s" % body0)
 body = body0
 dbgout(dbg,"body0: %s" % body0)
 ##3a. Remove <LEND>. datalines does not include <LEND>. See get_datalines
 #body = body.replace('<LEND>','') # Line ending mark needs to be removed.
 #4. construct result
%if dictlo != 'mw':
 data = "<H1><h>%s</h><body>%s</body><tail>%s</tail></H1>" % (h,body,tail)
%endif
%if dictlo == 'mw':
 #data = "<H1><h>%s</h><body>%s</body><tail>%s</tail></H1>" % (h,body,tail)
 data = "<h>%s</h><body>%s</body><tail>%s</tail>" % (h,body,tail)
 tag = 'H%s' %hwrec.e
 data = '<%s>%s</%s>' %(tag,data,tag)
%endif
%if dictlo in ['sch','ap90']:
 #4a. For sch: Put the <info> element into the tail
 data = re.sub('(<info.*?>) *</body><tail>',r'</body><tail>\1',data)
 #4b. For comparison to previous version, remove a space after <body>
 data = re.sub(r'<body> ','<body>',data)
%endif
 #5. Close the <div> elements
#%if dictlo not in ['inm','skd','bop']:
%if dictlo not in ['inm','skd']:  # 05-06-2024
 data = close_divs(data)
%endif
 return data
%endif  # close construct_xmlstring variants
def xml_header(xmlroot):
 # write header lines
 text = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE %s SYSTEM "%s.dtd">
<!-- Copyright Universitat Koln 2013 -->
<%s>
""" % (xmlroot,xmlroot,xmlroot)
 lines = text.splitlines()
 lines = [x.strip() for x in lines if x.strip()!='']
 return lines

%if dictlo in ['abch', 'acph', 'acsj']:
def get_datalines1(hw,datalines):
 # used for abch
 ans= []
 for line in datalines:
  m = re.search(r'<k1>(.*?)<meanings>(.*?)$',line)
  if m == None: # keep verselines
   ans.append(line)
   continue
  # keep line only when hw matches one of the headwords of line
  k1 = get_k1(m.group(1))
  meanings_str = m.group(2)
  meaning_items = meanings_str.split(',')
  meanings_k1 = [get_k1(item) for item in meaning_items]
  allhws = [k1] + meanings_k1
  if hw in allhws:
   ans.append(line)
  # otherwise, the line is not kept.
 return ans
%endif

def get_datalines(hwrec,inlines):
 # for structure of hwrec, refer to hwparse.py
 n1 = int(hwrec.ln1)
 n2 = int(hwrec.ln2)
 # By construction, n1 is the meta line, and n2 is the <lend> line of
 # this entry in xxx.txt.
 # For our purposes, we do not need this first and last line
 n1 = n1 + 1
 n2 = n2 - 1
 # Next, we make indexes into the inlines array, which are 0-based
 # whereas n1 and n2 are 1-based
 idx1 = n1 - 1
 idx2 = n2 - 1
 datalines = inlines[idx1:idx2+1]
%if dictlo in ['abch', 'acph', 'acsj']:
 # restrict further to the hwdetails that mention this hw
 hw = hwrec.k1
 datalines = get_datalines1(hw,datalines)
%endif
 return datalines

def make_xml(filedig,filehw,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = [line.rstrip('\r\n') for line in f]
 # parse xxxhw.txt
 hwrecs = init_hwrecs(filehw)
 # open output xml file
 fout = codecs.open(fileout,'w','utf-8')
 nout = 0  # count of lines written to fout
 # generate xml header lines
 lines = xml_header(xmlroot)
 for line in lines:
  fout.write(line + '\n')
  nout = nout + 1
 # process hwrecs records one at a time and generate output
 nerr = 0
 for ihwrec,hwrec in enumerate(hwrecs):
  if ihwrec > 1000000: # 12
   print("debug stopping")
   break
  datalines = get_datalines(hwrec,inlines)
  # construct output
%if dictlo in ['anhk']:
  xmlstring = construct_xmlstring_1(datalines,hwrec)
%elif dictlo in ['abch', 'acph', 'acsj']:
  # using abch form
  xmlstring = construct_xmlstring_2(datalines,hwrec)
%else:
  # non-kosha dictionaries
  xmlstring = construct_xmlstring(datalines,hwrec)
%endif  
  # data is a string, which should be well-formed xml
  # try parsing this string to verify well-formed.
  try:
   root = ET.fromstring(xmlstring)
  except:
   # 01-09-2021. Remove conditional err messaging
   # since some Python versions (e.g. 2.7.5) give false occasions
   nerr = nerr + 1
   # For debugging, change False to True
   if False:
    outarr = []
    out = "<!-- xml error #%s: L = %s, hw = %s-->" %(nerr,hwrec.L,hwrec.k1)
    outarr.append(out)
    outarr.append("datalines = ")
    outarr = outarr + datalines
    outarr.append("xmlstring=")
    outarr.append(xmlstring)
    outarr.append('')
    for out in outarr:
     print(out)
    #exit(1) continue
  # write output
  fout.write(xmlstring + '\n')
  nout = nout + 1

 # write closing line for xml file.
 out = "</%s>\n" % xmlroot
 fout.write(out)
 fout.close()
 if (nerr == 0):
  print("All records parsed by ET")
 else:
  print("WARNING: make_xml.py:",nerr,"records records not parsed by ET")
if __name__=="__main__":
 print('make_xml.py BEGINS !!!!!')
 filein = sys.argv[1] # xxx.txt
 # filein1 = xxxhw.txt for dictlo = mw; for other dictlo, filein1 = xxxhw2.txt
 filein1 = sys.argv[2]
 fileout = sys.argv[3] # xxx.xml
 make_xml(filein,filein1,fileout)
 print('make_xml.py ENDS !!!!!')
 
