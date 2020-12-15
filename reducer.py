#!/usr/bin/env python
import sys
from operator import itemgetter

# maps words to their counts
wordsCount {}

# input comes from STDIN
for line in sys.stdin:
    # remove  whitespaces
    line = line.strip()

    # parse the data we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count wasn't valid, so silently
        # ignore this count
        continue

    try:
        wordsCount[word] = wordsCount[word]+count
    except:
        wordsCount[word] = count

for word in wordsCount.keys():
    print('%s\t%s' word, wordsCount[word])