#!/usr/bin/python

# Reducer: Calculate the average for each year

import sys

previous = None
sum = 0
num = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print (previous + '\t' + str( sum/num ))
        previous = key
        sum = 0
        num = 0
    
    sum = sum + float( value )
    num += 1

print (previous + '\t' + str( sum/num ))