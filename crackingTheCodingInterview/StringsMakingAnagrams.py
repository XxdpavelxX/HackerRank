# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def number_needed(a, b):
    a, b = list(a), list(b)
    a_vals = list(a)
    for i in a_vals:
        if i in b:
            a.remove(i)
            b.remove(i)
    return len(a) + len(b)

print number_needed('abc', 'cde')


# def number_needed(a, b):
#     count = 0
#     for i in range(97, 123):
#         ia = sum(letter == chr(i) for letter in a)
#         ib = sum(letter == chr(i) for letter in b)
#         count += abs(ia-ib)
#     return count
#
# print number_needed('abc', 'cde')
#
#
from math import fabs


# def number_needed(a, b):
#     letterArray = [0] * 26
#     for c in a:
#         index = ord(c) - ord('a');
#         letterArray[index] += 1
#     for c in b:
#         index = ord(c) - ord('a')
#         letterArray[index] -= 1
#     result = 0
#     for i in letterArray:
#         result += fabs(i)
#     return int(result)
#
#
# a = raw_input().strip()
# b = raw_input().strip()
#
# print number_needed(a, b)