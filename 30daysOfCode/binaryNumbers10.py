#https://www.hackerrank.com/challenges/30-binary-numbers/problem

import sys

n = int(raw_input().strip())

binary = bin(n).strip('0b')
highestTotal = 0
currentTotal = 0
for char in binary:
    if char == "1":
        currentTotal += 1
    elif char == "0":
        if currentTotal > highestTotal:
            highestTotal = currentTotal
        currentTotal = 0
if currentTotal > highestTotal:
    highestTotal = currentTotal

print highestTotal