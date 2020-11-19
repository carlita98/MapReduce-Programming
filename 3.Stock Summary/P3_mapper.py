#!/usr/bin/python

# Summarization pattern: We want to calculate an aggregate over
# our data. The average of daily stock price at close per year.

# Mapper: will print the year and the end_price

#The structure of the file: Date,Open,High,Low,Close,Adj Close,Volume
import sys
import re
import csv

csv_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
for line in csv_reader:
    date = re.split(r"-", line[0])
    print(date[0] + "\t" + line[4])
