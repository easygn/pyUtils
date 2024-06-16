##############################
# Batch Renamer  v3 : June 16, 2F
# remade by Easygn , June 14, 2F
# prototype code by stackoverflow  
#####

import os
import sys

F_EXT1 = '.jpg'
F_EXT2 = '.png'

repC = 1
dupC = 0

# PATHforPI = '/home/pi/ramdisk'


for fNm in os.listdir(): ##(PfP)
  if F_EXT1 in fNm or F_EXT2 in fNm:
    if len(sys.argv) > 2:
      if '-r1' in sys.argv[2]:  nNm = sys.argv[1]+str(repC)+fNm[fNm.rindex('.'):]
      elif '-r3' in sys.argv[2]:  nNm = sys.argv[1]+'_{:03}'.format(repC)+fNm[fNm.rindex('.'):]
      elif '-r' in sys.argv[2] or '-r2' in sys.argv[2]:  nNm = sys.argv[1]+'_{:02}'.format(repC)+fNm[fNm.rindex('.'):]
      elif '-b' in sys.argv[2]:  nNm = fNm[0:fNm.rindex('.')]+sys.argv[1]+fNm[fNm.rindex('.'):]
      else:  nNm = sys.argv[1]+fNm
      repC+=1
    else:  nNm = sys.argv[1]+fNm
    if nNm in os.listdir():
      dupC+=1
      nNm = nNm[0:nNm.rindex('.')]+'_' + str(dupC)+fNm[nNm.rindex('.'):]
    os.rename(fNm, nNm)
