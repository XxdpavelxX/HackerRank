#https://www.hackerrank.com/challenges/30-review-loop/problem

#for N in range(input()):
#    S = raw_input()
#    print S[::2], S[1::2]

def splitter(number, word):
    for N in range(number):
        S = word
        return S[::2], S[1::2]

print splitter(3, "Hacker")
