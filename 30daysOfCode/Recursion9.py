#https://www.hackerrank.com/challenges/30-recursion/problem

#!/bin/python

import sys

def factorial(n):
    fact = 1
    while n > 1:
        fact = n * fact
        n = n-1
    return fact

if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result