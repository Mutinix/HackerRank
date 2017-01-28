#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

# Calculate the initial sum
elements = [a,b,c,d,e]
s = sum(elements)

# Set initial max and min values
maxs = -1
mins = float("inf")

# Check the new sum by subtracting each of the elements
for e in elements:
    if s - e > maxs:
        maxs = s - e
    if s - e < mins:
        mins = s - e
        
print mins, maxs