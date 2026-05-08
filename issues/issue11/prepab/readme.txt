
prepab/readme.txt

-------------------------------
# change from Devanagari to slp1
python transcode.py deva slp1 temp_ae_10A_deva.txt temp_ae_10A_slp1.txt
# check
python transcode.py slp1 deva temp_ae_10A_slp1.txt temp_ae_10A_deva1.txt 
diff temp_ae_10A_deva.txt temp_ae_10A_deva1.txt | wc -l
# 0 ok
rm temp_ae_10A_deva1.txt
----------
python transcode.py deva slp1 temp_ae_newf_deva.txt temp_ae_newf_slp1.txt
# check
python transcode.py slp1 deva temp_ae_newf_slp1.txt temp_ae_newf_deva1.txt 
diff temp_ae_newf_deva.txt temp_ae_newf_deva1.txt | wc -l
#0 ok
rm temp_ae_newf_deva1.txt

---------------------------------
AB uses several Unicode characters that don't display properly in Emacs.
Change these to visually similar characters that DO display properly in Emacs

python check_ea1.py temp_ae_10A_slp1.txt ea_ae_10A_slp1.txt
python check_ea1.py  temp_ae_newf_slp1.txt ea_ae_newf_slp1.txt

Characters that display poorly:
⧫  (\u29eb)  BLACK LOZENGE
  "◊" (U+25CA) LOZENGE
  ◆ U+25C6 BLACK DIAMOND
  Other possibilities
  ◈ U+25C8 WHITE DIAMOND CONTAINING BLACK SMALL DIAMOND
  ✦  (\u2726) 32695 := BLACK FOUR POINTED STAR
  
🞄  (\u1f784)  BLACK SLIGHTLY SMALL CIRCLE
  ● U+25CF BLACK CIRCLE
  another possibility
  • U+2022 BULLET  
  
🠚  (\u1f81a)  HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD
  ➜ U+279C HEAVY ROUND‑TIPPED RIGHTWARDS ARROW


python ea_change.py temp_ae_10A_slp1.txt temp_abv1.txt
# 88844 lines written to temp_abv1.txt

python ea_change.py temp_ae_newf_slp1.txt temp_abv2.txt
# 66804 lines written to temp_abv2.txt

---------------------------------------
# check ea for revised versions
python check_ea1.py temp_abv1.txt ea_abv1.txt
python check_ea1.py temp_abv2.txt ea_abv2.txt
