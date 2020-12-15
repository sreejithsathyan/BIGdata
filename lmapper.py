#!/usr/bin/env python
import sys

# get lies from stdin
for line in sys.stdin:
    # remove unwanted whitespace using strip
    line = line.strip()
    # split lines into list of integers
    integers = line.split()
    # Output with delimited format(integer,1)
    for integer in integers:
        # printing final output
        print('%s\t%s' % (integer, 1))
