#!/usr/bin/python

# Reducer: For each range we will print all the movie ids that are in that range

import sys

previous = None

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        previous = key
        print("\n", "Range ", key, end=": ")
    
    print(value, end="  ")