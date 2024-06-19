################################
# Webpage txt URL mining and exporter v2 : June 20, 2F 
# remade by Easygn , April 22 2F
# prototype gen by Claude3 Ai sonnet
#####

import os
import sys

##FND_KW = 'articles/'
##F_TRG = 'a.html'
##F_EXT = 'out.txt'


file = open(sys.argv[1], 'r', encoding='utf-8')

txt = file.read()
KwdTrues = 0
maxTrues = len(sys.argv) - 3

if sys.argv[2] in os.listdir() :  wrFile = open(sys.argv[2], 'a', encoding='utf-8')
else :  wrFile = open(sys.argv[2], 'w', encoding='utf-8')

for line in txt.split('\n'):
  for aL in range (3, len(sys.argv)):
    if sys.argv[aL] in line:  KwdTrues += 1
  if '">' in line: KwdTrues += 1
  if KwdTrues > maxTrues:
    wrFile.write(line[line.find('http'):line.find('">')] + '\n')
  KwdTrues = 0

print('Done')
