#!/usr/bin/python

# Summarization pattern: We want to calculate an aggregate over
# our data. The average rating for each movie.

# Mapper: will print the movie_id and rating 

# The structure of the file: userId,movieId,rating,timestamp
import sys
import re
import csv

csv_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
for line in csv_reader:
    print(line[1] + "\t" + line[2])
