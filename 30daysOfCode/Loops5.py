#https://www.hackerrank.com/challenges/30-loops/problem

import sys

n = int(raw_input().strip())

i = 1
while i <= 10:
    print "%s x %s = %s"%(n, i, i*n)
    i += 1
