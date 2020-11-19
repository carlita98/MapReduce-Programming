#!/usr/bin/python

# Reducer: trivial, just print the input value
import sys

for line in sys.stdin:
    key, value = line.split( '\t' )
    print (value)

