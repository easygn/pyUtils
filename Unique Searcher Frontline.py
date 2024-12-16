##############################
# Unique txt Opcode Searcher
# remade by Easygn, Dec 16 2F
# prototype gen by Claude3 Ai Haiku
#####

import os
import sys
import time

file = open(sys.argv[1], 'r', encoding='utf-8')
txt = file.read()

opcSize = 12 # Default
if (len(sys.argv) > 2):
  argI = int(sys.argv[2])
  if (argI >= 8):  opcSize = argI

mostCount = 3  # " "
if (len(sys.argv) > 3):
  argI = int(sys.argv[3])
  if (argI >= 1):  mostCount = argI

line_list = []
line_count = []

beginT = time.time()

for line in txt.split('\n'):
  key = line[:opcSize].strip()

  if key in line_list:
    line_count[line_list.index(key)] = line_count[line_list.index(key)] + 1
  else:
    line_list.append(key)
    line_count.append(1)

#unique_lines = [ lines[0] for lines in line_starts.values() if len(lines) == 1 ]

for line in line_list:
  if line_count[line_list.index(line)] <= mostCount:
    print(line, 'find', line_count[line_list.index(line)], "nums")

print( "Process time :",  round (time.time() - beginT, 2),  "sec" )
