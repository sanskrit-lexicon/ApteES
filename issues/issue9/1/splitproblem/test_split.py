# coding=utf-8
""" test_split --  investigate an oddity in re.split
"""
from __future__ import print_function
import sys, re,codecs


def get_data_1():
 groupline = """<L>9357<pc>419<k1>set<k2>set
{@Set@}¦, {%s.%} {#astamayaH, astamanaM, astaH#}. {@2@} {#jAtaM#},
{#jAti#} {%f.%}, {#gaRaH, saMGaH, SreRI, paMkti#} {%f.%}, {#samUhaH#},
{#saMyogaH#}; ‘s. s of ornaments fitting all parts of the body’
{#sarvAMgikA ABaraRasaM-yogAH#}
(Mal. 6). {@3@} (Of persons) {#vargaH#},
{#gaRaH, saMGaH#}. - {%v. t.%} {#A-ni-DA#} 3 U, {#vi-, nyas#}
4 P, {#sTA#} c.; ({#sTApayati#}), {#niviS#} c., {#a-varuh#}
c.; oft. by {#kf#} 8 U, {#dA#} 3 U, {#f#} c.
({#arpayati#}); (in the ground) {#ruh#} c.,
{#niKan#} 1 P. {@2@} {#pra-pari-kxp#} c., {#vyava-sTA#} c.
{@3@} {#praRi-DA, pratibaMD#} 9 P, ({#yadimaRistrapuRi#} {#pratibaDyate#} P. 1. 1),
{#ut-, Kac#} 10 ({#Kaca-yati#}),
{#anu-vyaD#} 4 P; ‘s. with jewels’
{#ratnAnuvidDa#}. {@4@} {#ni-, So#} 4 P, {#ut-, tij#} c.,
{#tIkzRIkf#}. {@5@} {#yuj#} 7 U, 10, {#saM-A-°, samA-DA, saM-, vi-DA#}.
(limb &c.); ‘s. one's foot in’
{#padaM kf#} (lit. and fig.), {#kari-zyasi padaM punarASramesmin#}
(S. 4), {#kftaM me#}
{#vapuzi navayOvanena padaM#} (Ka. 137); ‘s. a trap’
{#pASaM yuj#}; ‘s. in motion’ {#cal#}
c., {#saMcar#} c., {#Ir#} 10.; ‘s. the heart on’
{#manaH-DiyaM-cittaM#}, &c. ({@Mind@}, q. v.)
{#baMD#} or {#A-DA#} or {#saMni-viS#} c. or {#yuj#},
{#Asakta#} - {%v.%} {#BU#} 1 P (with loc.); ‘s. your heart on religious duties’
{#ADIyatAM#}
{#Darme DIH#} (Ka. 63); ‘s. not your heart on transient objects’
{#vinASaDarmasu viza-yezu mano mA saMniveSaya, vinASivizayAsakto#}

{#mA BUH#}; ‘s. the teeth on edge’ {#daMtaharzaM#}
{#jan#} c.; ‘s. right’, ‘s. in order’ {#sa-mIkf, vyava-sTA#}
c.; {#vinyas, virac#} 10; ‘s. to rights’
{#prati-, samA-DA, susTIkf; prati-yuj#},
({#pratiyojayitavyavallakI#} R. VIII. 41);
‘s. free’ {#muc#} 6 P or c.; {%See%} {@Free@}; ‘s. at naught’
{#tfRAya-tfRavat-man#} 4 A, {#tf-RIkf#};
ex. also by {#kA mAtrA-gaRanA#}; ‘s. to music’
{#svara-tAla-badDa#} {%a.%} {#kf#}. - {%v. i.%} {#astaM#}
{#gam-vraj#} 1 P or {#yA-i#} 2 P, {#astAcalaM-astaSiKaraM-avalaMb#}
1 A or {#prAp#} 5 P, {#sAgare#}
{#masj#} 6 P. {@2@} {#saMhan-baMD#} -pass. Ⓝ{@[Set] about@},➔
{#AraB#} 1 A, {#pra-vft#} 1 A. Ⓝ{@[Set] against@},➔ {#viruD#}
7 U, {#pratyava-sTA#} c., {#pratiyuD#} c.; {%See%} {@Oppose@}. Ⓝ{@[Set] apart@},➔
{#pfTak rakz#} 1 P or {#sTA#}
c., {#pfTak kf#}. Ⓝ{@[Set] aside@},➔ {#avakzip#} 6 P, {#muc#},
{#tyaj#} 1 P, oft. by {#As#} 2 A, {#sTA#} 1 P; ‘s. aside that point’
{#AstAM-tizWatu-tAvaddUre#}
{#sa vizayaH#}; {%See%} {@Reject@}, {@Omit@}. Ⓝ{@[Set] before@},➔
{#upa-sTA#} c., {#upAnI#} 1 P, {#upAhf#} 1 P; ‘s. food before a person’
{#pariviz#} c.
Ⓝ{@[Set] down@} ⒈,➔ {#nyas, BUmO nyas#} or {#ni-DA#}. {@2@} {#A-aDi-kzip, Barts#}
10 A, {#apakfz#} 1 P,
{#avaman#} c., {#ava-jYA#} 9 U. {@3@} {#gaR#} 10, {#man#}
4 A. {@4@} (In writing) {#liK#} 6 P, {#nirdiS#}
6 P. Ⓝ{@[Set] forth@},➔ {#upani-vini-as, varR#} 10,
{#upakzip, nirdiS, aBi-DA#}. Ⓝ{@[Set] forward@},➔
{#prayA, pragam, prasf#} ({%v. t.%}) {#puraskf, unnam#} c.,
{#vfD#} c. Ⓝ{@[Set] in@},➔ {#samupA-gam, upa-sTA, pravft#},
{#avatF#} 1 P; ‘summer which has just s. in’
{#acirapravfttaM grIzmasamayaM#} (S. 1),
{#vasaMtAvatArasamaye#} &c.; ({%v. t.%}) {#aMtar grah#} 9 U.
Ⓝ{@[Set] off@} ⒈,➔ {@Set out@}, q. v.; ({%v. t.%}) {#SuB#} c., {#prakAS#}
c; {#SoBAM puz#} 4, 9 P {#lakzmIM tan#} 8 U, ({#malinamapi#} {#himAMSorlakzma lakzmIM tanoti#} S. 1.);
oft. by
{#SuB#} 1 A, {#guRA vinayena SoBaMte#} ‘are s. off by modesty’;
‘s. off against’ {#tul#} 10
({#tulayati#}), {#pratigaR#}. Ⓝ{@[Set] on@},➔ {#pravft#} c., {#prayuj#},
({#aTAvamAnena pituH prayuktA#} K. I. 21), {#prer#},
{#protsah#} c.; {%See%} {@Prompt@}; ‘s. on foot’
{#prati-zWA#} c., {#pravft#}; c., {#AraB#}; ‘s. on fire’
{#dah#} c., {#jvalanAya f#} c. or {#visfj#} 6 P; ‘s. on guard’
{#avahita#} {%a.%} {#kf#}. Ⓝ{@[Set] out@},➔ {#pra-sTA#}
1 A, {#pra-yA, pragam, pracal, nirgam#}. Ⓝ{@[Set] over@},➔
{#niyuj, aDikf, aDi-zWA#} c. Ⓝ{@[Set] to@},➔ {#manaH baMD#} or
{#yuj#} or {#niviS#} c., {#Asakta#} - {%a.%} {#BU#}; ‘they s. to their work’
{#kAryavyApftA baBUvuH#} &c.,
Ⓝ{@[Set] up@},➔ {#baMD, utTA#} c.; {#saM-ava-prati-sTA#} c.; {%See%} {@Raise@},
‘the people s. up a howl’ {#badDa-kolAhalA janAH; utTito ninAdaH#}
‘a scream was s. up’;
({%v. i.%}) {#vfttiM-vyava-hAraM-AraB#}
or {#pravft#} c.; ‘s. up for’ {#aBi-man#}
4 A: {%See%} {@Pretend@}, {@Profess@}. Ⓝ{@[Set] upon@},➔.
{#Akram, A-ava-skaMd#} 1 P, {#sahasA grah#}. - {%a.%}
{#niyata, parikalpita, ekarUpa; vinyasta, suvi-racita#}.
{@2@} {#sTApita, nyasta, nihita, niveSita#},
[Page420]
&c. {@3@} {#Kacita, Curita, anuvidDa, praRihita#},
{#pratibadDa, pratyupta, karaMba, karaMbita#}. Ⓝ{@[Set]ter@},➔ {%s.%}
{#yojayitf#} {%m.%}, {#pratizWApakaH#}, &c. {@2@} {#mfgayAkukkuraH#},
{#viSvakadruH#}. Ⓝ{@[Set]ting@},➔ {%s.%} {#yojanA, sanniveSaH#},
{#sTApanaM-nA, arpaRaM, ropaRaM#}, &c. {@2@} {#astamanaM#},
{#astaM#}. Ⓝ{@Set-down@} ⒉,➔ {%s.%} {#apakarzaRaM, aBiBavaH#},
{#mAnaKaMqanaM#}. Ⓝ{@Set-off@} ⒉,➔ {%s.%} {#parivartaH, tulyamUlyaM#}
{#vastu#}.
<LEND>"""
 return groupline

def get_data_2():
 groupline = """{#masj#} 6 P. {@2@} {#saMhan-baMD#} -pass. Ⓝ{@[Set] about@},➔
{#AraB#} 1 A, {#pra-vft#} 1 A. Ⓝ{@[Set] against@},➔ {#viruD#}
7 U, {#pratyava-sTA#} c., {#pratiyuD#} c.; {%See%} {@Oppose@}. Ⓝ{@[Set] apart@},➔
c., {#pfTak kf#}. Ⓝ{@[Set] aside@},➔ {#avakzip#} 6 P, {#muc#},
{#sa vizayaH#}; {%See%} {@Reject@}, {@Omit@}. Ⓝ{@[Set] before@},➔
Ⓝ{@[Set] down@} ⒈,➔ {#nyas, BUmO nyas#} or {#ni-DA#}. {@2@} {#A-aDi-kzip, Barts#}
6 P. Ⓝ{@[Set] forth@},➔ {#upani-vini-as, varR#} 10,
{#upakzip, nirdiS, aBi-DA#}. Ⓝ{@[Set] forward@},➔ 
{#vfD#} c. Ⓝ{@[Set] in@},➔ {#samupA-gam, upa-sTA, pravft#},
Ⓝ{@[Set] off@} ⒈,➔ {@Set out@}, q. v.; ({%v. t.%}) {#SuB#} c., {#prakAS#}
({#tulayati#}), {#pratigaR#}. Ⓝ{@[Set] on@},➔ {#pravft#} c., {#prayuj#},
{#avahita#} {%a.%} {#kf#}. Ⓝ{@[Set] out@},➔ {#pra-sTA#}
1 A, {#pra-yA, pragam, pracal, nirgam#}. Ⓝ{@[Set] over@},➔
{#niyuj, aDikf, aDi-zWA#} c. Ⓝ{@[Set] to@},➔ {#manaH baMD#} or
Ⓝ{@[Set] up@},➔ {#baMD, utTA#} c.; {#saM-ava-prati-sTA#} c.; {%See%} {@Raise@},
4 A: {%See%} {@Pretend@}, {@Profess@}. Ⓝ{@[Set] upon@},➔.
{#pratibadDa, pratyupta, karaMba, karaMbita#}. Ⓝ{@[Set]ter@},➔ {%s.%}
{#viSvakadruH#}. Ⓝ{@[Set]ting@},➔ {%s.%} {#yojanA, sanniveSaH#},
{#astaM#}. Ⓝ{@Set-down@} ⒉,➔ {%s.%} {#apakarzaRaM, aBiBavaH#},
{#mAnaKaMqanaM#}. Ⓝ{@Set-off@} ⒉,➔ {%s.%} {#parivartaH, tulyamUlyaM#}
"""
 return groupline

def get_data_3():
 groupline = """{#mA BUH#}; ‘s. the teeth on edge’ {#daMtaharzaM#} {#jan#} c.; ‘s. right’, ‘s. in order’ {#sa-mIkf, vyava-sTA#} c.; {#vinyas, virac#} 10; ‘s. to rights’ {#prati-, samA-DA, susTIkf; prati-yuj#}, ({#pratiyojayitavyavallakI#} R. VIII. 41); ‘s. free’ {#muc#} 6 P or c.; {%See%} {@Free@}; ‘s. at naught’ {#tfRAya-tfRavat-man#} 4 A, {#tf-RIkf#}; ex. also by {#kA mAtrA-gaRanA#}; ‘s. to music’ {#svara-tAla-badDa#} {%a.%} {#kf#}. - {%v. i.%} {#astaM#} {#gam-vraj#} 1 P or {#yA-i#} 2 P, {#astAcalaM-astaSiKaraM-avalaMb#} 1 A or {#prAp#} 5 P, {#sAgare#} {#masj#} 6 P. {@2@} {#saMhan-baMD#} -pass. Ⓝ{@[Set] about@},➔ {#AraB#} 1 A, {#pra-vft#} 1 A. Ⓝ{@[Set] against@},➔ {#viruD#} 7 U, {#pratyava-sTA#} c., {#pratiyuD#} c.; {%See%} {@Oppose@}. Ⓝ{@[Set] apart@},➔ {#pfTak rakz#} 1 P or {#sTA#} c., {#pfTak kf#}. Ⓝ{@[Set] aside@},➔ {#avakzip#} 6 P, {#muc#},{#tyaj#} 1 P, oft. by {#As#} 2 A, {#sTA#} 1 P; ‘s. aside that point’{#AstAM-tizWatu-tAvaddUre#} {#sa vizayaH#}; {%See%} {@Reject@}, {@Omit@}. Ⓝ{@[Set] before@},➔ {#upa-sTA#} c., {#upAnI#} 1 P, {#upAhf#} 1 P; ‘s. food before a person’ {#pariviz#} c. Ⓝ{@[Set] down@} ⒈,➔ {#nyas, BUmO nyas#} or {#ni-DA#}. {@2@} {#A-aDi-kzip, Barts#} 10 A, {#apakfz#} 1 P, {#avaman#} c., {#ava-jYA#} 9 U. {@3@} {#gaR#} 10, {#man#} 4 A. {@4@} (In writing) {#liK#} 6 P, {#nirdiS#} 6 P. Ⓝ{@[Set] forth@},➔ {#upani-vini-as, varR#} 10, {#upakzip, nirdiS, aBi-DA#}. Ⓝ{@[Set] forward@},➔  {#prayA, pragam, prasf#} ({%v. t.%}) {#puraskf, unnam#} c., {#vfD#} c. Ⓝ{@[Set] in@},➔ {#samupA-gam, upa-sTA, pravft#}, {#avatF#} 1 P; ‘summer which has just s. in’ {#acirapravfttaM grIzmasamayaM#} (S. 1), {#vasaMtAvatArasamaye#} &c.; ({%v. t.%}) {#aMtar grah#} 9 U. Ⓝ{@[Set] off@} ⒈,➔ {@Set out@}, q. v.; ({%v. t.%}) {#SuB#} c., {#prakAS#} c; {#SoBAM puz#} 4, 9 P {#lakzmIM tan#} 8 U, ({#malinamapi#} {#himAMSorlakzma lakzmIM tanoti#} S. 1.); oft. by {#SuB#} 1 A, {#guRA vinayena SoBaMte#} ‘are s. off by modesty’; ‘s. off against’ {#tul#} 10 ({#tulayati#}), {#pratigaR#}. Ⓝ{@[Set] on@},➔ {#pravft#} c., {#prayuj#}, ({#aTAvamAnena pituH prayuktA#} K. I. 21), {#prer#}, {#protsah#} c.; {%See%} {@Prompt@}; ‘s. on foot’ {#prati-zWA#} c., {#pravft#}; c., {#AraB#}; ‘s. on fire’ {#dah#} c., {#jvalanAya f#} c. or {#visfj#} 6 P; ‘s. on guard’ {#avahita#} {%a.%} {#kf#}. Ⓝ{@[Set] out@},➔ {#pra-sTA#} 1 A, {#pra-yA, pragam, pracal, nirgam#}. Ⓝ{@[Set] over@},➔ {#niyuj, aDikf, aDi-zWA#} c. Ⓝ{@[Set] to@},➔ {#manaH baMD#} or {#yuj#} or {#niviS#} c., {#Asakta#} - {%a.%} {#BU#}; ‘they s. to their work’ {#kAryavyApftA baBUvuH#} &c., Ⓝ{@[Set] up@},➔ {#baMD, utTA#} c.; {#saM-ava-prati-sTA#} c.; {%See%} {@Raise@},‘the people s. up a howl’ {#badDa-kolAhalA janAH; utTito ninAdaH#} ‘a scream was s. up’; ({%v. i.%}) {#vfttiM-vyava-hAraM-AraB#} or {#pravft#} c.; ‘s. up for’ {#aBi-man#} 4 A: {%See%} {@Pretend@}, {@Profess@}. Ⓝ{@[Set] upon@},➔. {#Akram, A-ava-skaMd#} 1 P, {#sahasA grah#}. - {%a.%} {#niyata, parikalpita, ekarUpa; vinyasta, suvi-racita#}. {@2@} {#sTApita, nyasta, nihita, niveSita#}, [Page420] &c. {@3@} {#Kacita, Curita, anuvidDa, praRihita#}, {#pratibadDa, pratyupta, karaMba, karaMbita#}. Ⓝ{@[Set]ter@},➔ {%s.%} {#yojayitf#} {%m.%}, {#pratizWApakaH#}, &c. {@2@} {#mfgayAkukkuraH#}, {#viSvakadruH#}. Ⓝ{@[Set]ting@},➔ {%s.%} {#yojanA, sanniveSaH#}, {#sTApanaM-nA, arpaRaM, ropaRaM#}, &c. {@2@} {#astamanaM#}, {#astaM#}. Ⓝ{@Set-down@} ⒉,➔ {%s.%} {#apakarzaRaM, aBiBavaH#}, {#mAnaKaMqanaM#}. Ⓝ{@Set-off@} ⒉,➔ {%s.%} {#parivartaH, tulyamUlyaM#} {#vastu#}. <LEND>
"""
 return groupline

def get_data_4():
 a = get_data_1()
 a1 = a.replace('\r','')
 assert a1 == a
 a2 = a.replace('\n', ' ')
 return a2


def test(title,groupline,regex,firstc):
 print(title,'begin',regex)
 a = re.findall(regex,groupline,re.DOTALL)
 print('findall:',len(a))
 if title == 'data_3':
  bparts = re.split(regex,groupline)
 else:
  bparts = re.split(regex,groupline,re.DOTALL)
  
 print('bparts:',len(bparts))
 b = [part for part in bparts if part.startswith(firstc)]
 print('b:',len(b))
 na = len(a)
 nb = len(b)
 nmax = max(na,nb)
 for i in range(nmax):
  a1 = '--'
  b1 = '--'
  if i < na:
   a1 = a[i]
  if i < nb:
   b1 = b[i]
  print(i+1,'a=',a1,'b=',b1)
 print()
 print(title,'end')

def test1():
 groupline = get_data_1()
 n = len(groupline)
 print(n,'length groupline')
 regex = r'(Ⓝ[^➔]*➔)'
 firstc = 'Ⓝ'
 for i in range(n):
  g = groupline[i:]
  c = groupline[i]
  a = re.findall(regex,g,re.DOTALL)
  bparts = re.split(regex,g,re.DOTALL)
  b = [part for part in bparts if part.startswith(firstc)]
  na = len(a)
  nb = len(b)
  if na == nb:
   print('success at i=%s, c=%s, g = %s' % (i,c,groupline[i-10:i] + '_' +groupline[i] + '_' + groupline[i+1:i+20]))
   exit(1)

def check_ea(line):
 asdict = {}
 for c in line:
   #if ord(c) > 127:
   if (ord(c) > 127) or (ord(c) < 14):
    if c not in asdict:
     asdict[c] = 0
    asdict[c] = asdict[c] + 1
 return asdict

def write_ea(fileout,eadict):
 import unicodedata
 keys = eadict.keys()
 keys = sorted(keys)
 
 with codecs.open(fileout,"w","utf-8") as f:
   for key in keys:
    try:
     name = unicodedata.name(key)
    except:
     name = 'NONAME'
    out = "%s  (\\u%04x) %5d := %s" %(key,ord(key),eadict[key],name)
    f.write(out+'\n')
 print(len(keys),"extended ascii counts written to",fileout)

def test2(fileout,groupline,dotall = True):
 asdict = check_ea(groupline)
 write_ea(fileout,asdict)
 g = groupline
 regex = r'(Ⓝ[^➔]*➔)'
 firstc = 'Ⓝ'
 if dotall:
  a = re.findall(regex,g,re.DOTALL)
  bparts = re.split(regex,g,re.DOTALL)
 else:
  a = re.findall(regex,g)
  bparts = re.split(regex,g)
 b = [part for part in bparts if part.startswith(firstc)]
 na = len(a)
 nb = len(b)
 print(na,nb)

def test3():
 data1 = get_data_1()
 test2('temp_test2_data1.txt',data1,dotall = True)
 data1list = data1.splitlines()
 data3 = ' '.join(data1list)
 test2('temp_test2_data3.txt',data3,dotall = False)
 data4 = '\n'.join(data1list)
 test2('temp_test2_data4.txt',data4,dotall = True)
 print('data1 == data4:',data1 == data4)
 print('len(data1)=',len(data1),'len(data4)=',len(data4))
 # only diff is that c1
 n1 = len(data1)
 n4 = len(data4)
 nmax = max(n1,n4)
 for i in range(nmax):
  c1 = '--'
  c4 = '--'
  if i < n1:
   c1 = data1[i]
  if i < n4:
   c4 = data4[i]
  if c1 != c4:
   print('At indx %s, c1=%s, c4=%s' %(i,c1,c4))

def test4(nlines):
 lines = []
 for i in range(nlines):
  #line = 'X B %02d E = %s' %(i,i+1)
  line = 'B %02d E = %s' %(i,i+1)
  lines.append(line)
 groupline = '\n'.join(lines)
 #regex = r'(B[^E]*E)'
 regex = r'(B.*?E)'
 test('test4',groupline,regex,'B')
 #
 bparts = re.split(regex,groupline,re.DOTALL)
 print('bparts:',len(bparts))
 # b = [part for part in bparts if part.startswith(firstc)]
 for i,bpart in enumerate(bparts):
  bpart1 = bparts[i].replace('\n','') 
  print('part[%s] = "%s"' % (i,bpart1))
 
def test5(nlines):
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
 
