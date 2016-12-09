
__author__ = "Keerthana Prabhakaran"
__version__ = "1.0.1"
__maintainer__ = "Keerthana Prabhakaran"
__email__ = "keerthi.pkrn@gmail.com"
__status__ = "Accepted"
#python reverseAndAdd.py inFile.txt
"""contents of inFile.txt
195
"""
import sys
with open(sys.argv[1],'r') as f:
        for l in f:
                i=0
                l=l[:-1]
                while 1:
                        i=i+1
                        a=int(l)
                        b=int(l[::-1])
                        c = str(a+b)
                        if c==c[::-1]:
                                print i,c
                                break
                        else:
                                l=c
                                
