##############################
# Batch Renamer  v2 : June 16, 2F
# remade by Easygn , June 14, 2F
# prototype code by stackoverflow  
#####

import os
import sys

F_EXT1 = '.jpg'
F_EXT2 = '.png'

# PATHforPI = '/home/pi/ramdisk'

def O1(): os.rename(fNm, sys.argv[1]+fNm)

for fNm in os.listdir(): ##(PfP)
  if F_EXT1 in fNm or F_EXT2 in fNm:
     if len(sys.argv) > 2:
       if '-b' in sys.argv[2]:  os.rename(fNm, fNm[0:fNm.rindex('.')]+sys.argv[1]+fNm[fNm.rindex('.'):])
       else:  O1()
     else:  O1()
