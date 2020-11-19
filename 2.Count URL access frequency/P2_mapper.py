#!/usr/bin/python

# Summarization pattern: We want to calculate an aggregate over
# our data. The number of ocurrences of each URL.
# In particular this is the Word Count example.

# Mapper: will generate a line for each URL followed by a 1

# The URL starts with "/" and ends with " "
import sys
import re

for line in sys.stdin:
    httpPetition = re.findall(r'".+"', line)
    httpSections = re.split(r'\s', httpPetition[0])

    try: 
        print(httpSections[1], "\t1")
    except IndexError: 
        print("ERROR: Invalid format" + "\t1")
