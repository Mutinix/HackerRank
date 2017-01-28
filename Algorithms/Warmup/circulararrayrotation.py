#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]

# Reduce the number of rotations required
# If k equals n, then we're back to where we started
# and we don't need to rotate at all.
# So, all we're doing is calculating how many complete rotations
# are performed, and then just rotating the remaining elements.
k = k%n
a = map(int,raw_input().strip().split(' '))
ar = a[n-k:] + a[:n-k]
for a0 in xrange(q):
    m = int(raw_input().strip())
    print ar[m]