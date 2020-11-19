#!/usr/bin/python

# Reducer: Calculate the average for each movie considering that the movies are ordered by id

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
    
    sum += float( value )
    num += 1

print (previous + '\t' + str( sum/num ))