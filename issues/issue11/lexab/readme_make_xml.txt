def dig_to_xml_specific(x)

# https://github.com/sanskrit-lexicon/ApteES/issues/9#issuecomment-2135901199

 x = re.sub('⁅(.*?)⁆',r'<ab>\1</ab>',x)
 x = re.sub('〔(.*?)〕',r'<ls>\1</ls>',x)
 x = re.sub('<lex>(.*?)</lex>', r'<i><ab>\1</ab></i>',x)
 x = x.replace('\t ➜✦\t ⇨◆',' ')
 x = x.replace('\t ⇨✦━','<div n="lb"/>')
 x = x.replace('\t ⇨✦\t ⇨◆','<div n="lb"/>')
 x = x.replace('\t ➜✦',' ')
 x = x.replace('\t ➜◆',' ')
 x = x.replace('Ⓝ','<div n="lb"/>')
 x = re.sub('\[Page.*?\]',' ',x)
 x = re.sub(r'[⒈⒉]', '', x)  # 22 pairs of 'homonyms'.

Also, '[PageN]' is removed from xml
