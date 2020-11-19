#!/usr/bin/python

#Mapper: print the range (in which the movie rate is) and movie id

#Ranges are. Range 1 (1 or lower). Range 2 (between 1 and 2). Range 3 (between 2 and 3).
#Range 4 (between 3 and 4). Range 5 (between 4 and 5)

import sys
import re

isFirstLine = True

for line in sys.stdin:
    data = re.split (r"\t", line)
    
    if (float(data[1]) <= 1):
        range = 1
    elif (float(data[1]) <= 2):
        range = 2
    elif (float(data[1]) <= 3):
        range = 3
    elif (float(data[1]) <= 4):
        range = 4
    else: range = 5
 
    print(str(range) + "\t" + data[0])
