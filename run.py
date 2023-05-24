#coding=utf-8
import os, sys, platform
os.system('rm -rf RNDM.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf RNDM.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RNDM.so'):
        os.system('curl -L https://github.com/MALS-69/Random/blob/main/RNDM.cpython-311.so?raw=true -o RNDM.so') 
        print("\1b[1;92mWELCOME TO MY NEW TOOLS ")
        import RNDM
    else:
        import RNDM
        
 
elif bit == '32bit':
    print(" SORRY 32 BIT NOT WORKING ")
