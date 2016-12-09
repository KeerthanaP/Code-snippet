__author__ = "Keerthana Prabhakaran"
__version__ = "1.0.1"
__maintainer__ = "Keerthana Prabhakaran"
__email__ = "keerthi.pkrn@gmail.com"
__status__ = "Accepted"

"""
python detectingCycle.py

Given a sequence, write a program to detect cycles within it
Input(Contents of inFile.py):
2 0 6 3 1 6 3 1 6 3 1
Output:
6 3 1
"""

import itertools
import sys
with open(sys.argv[1],'r') as f:
        for l in f:
                a,b = l[:-1].split(';')
                a = a.split(',')
                b=int(b)
                c = list(itertools.chain.from_iterable([i[::-1] for i in zip(*(iter(a),) * b)]))
                print ','.join(itertools.chain.from_iterable(c+a[len(c):]))

