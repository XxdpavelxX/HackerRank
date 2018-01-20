#https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Sample Input:
# 6 4
# give me one grand today night
# give one grand today
#Sample Output: Yes

#Slow answer (times out sometimes)
def ransom_note(magazine, ransom):
    for word in magazine:
        if word in ransom:
            ransom.remove(word)
    print len(ransom)
    if len(ransom) == 0:
        return True
    return False

#Fast Answer
def ransom_note(magazine, ransom):
    dicty = {}
    if len(ransom) > len(magazine):
        return False
    for word in magazine:
        if word not in dicty:
            dicty[word] = 1
        else:
            dicty[word] += 1
    for word in ransom:
        try:
            dicty[word] -= 1
            if dicty[word]<0:
                return False
        except KeyError:
            return False
    return True


print ransom_note(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today'])
print ransom_note(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four'])