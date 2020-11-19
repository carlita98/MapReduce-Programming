#!/usr/bin/python

# Filtering parttern: It evaluates each line separately and decides, 
# based on whether or not it contains a given word if it should stay or go.
# In particular this is the Distributed Grep example.

# Mapper: print a line only if it contains a given word

import sys
import re

searchedWord = sys.argv[1]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r'\s' , line)
    words = [item.lower() for item in words]
    
    if searchedWord.lower() in words:
        print( "" + '\t' + line )