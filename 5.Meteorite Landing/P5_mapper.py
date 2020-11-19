#!/usr/bin/python

# Summarization pattern: We want to calculate an aggregate over
# our data. The average mass for each class.

# Mapper: will print the recclass and mass 

# The structure of the file: name, id, nametype, recclass, mass, fall, year, reclat, reciong, GeoLocation
import sys
import csv

csv_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
for line in csv_reader:
    if (line[4]!= '' and line[4]!= "0"):
        print(line[3] + "\t" + line[4])