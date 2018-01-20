# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def array_left_rotation(a, n, k):
    listy = a[-k:] +a[:k]
    extra = len(listy) - n
    return listy[extra:]


print array_left_rotation([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 20, 10)
print array_left_rotation([1, 2, 3, 4, 5], 5, 4)
# 5 1 2 3 4

# 77 97 58 1 86 58 26 10 86 51 41 73 89 7 10 1 59 58 84 77
#
# 20, 10