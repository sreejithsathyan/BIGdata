import sys
max_val = 0
for line in sys.stdin:
	(val,key) = line.strip().split("\t")
        if (val>max_val):
		max_val = val
print (max_val)
