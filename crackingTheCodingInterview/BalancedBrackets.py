#my attempt
# def is_matched(expression):
#     length = len(expression)
#     x = 0
#     opposites = {"{" : "}", "[" : "]", "(" : ")"}
#     status = {"open":0}
#     bracketsPassed = []
#     while x < length:
#         currentBracket = expression[x]
#         if opposites[currentBracket] not in bracketsPassed:
#             status[open] += 1
#
#
#         x=x+1


#Online Solutions:
# def is_matched(expression):
#     dic = {'{':'}','[':']','(':')'}
#     lst =[]
#     for i in expression:
#         if i in dic.keys():
#             lst.append(dic[i])
#         elif len(lst)>0 and i==lst[-1]:
#             lst.pop()
#         else:
#             return False
#     return len(lst) == 0
#
#
#
#
# def is_matched(expression):
#     pairs = {'{' : '}', '[' : ']', '(' : ')'}
#     sk = []
#     for c in expression:
#         if c in pairs:
#             sk.append(pairs[c])
#         elif not sk or c != sk.pop():
#             return False
#     return not sk
#
#
#
# def is_matched(e):
#     while (len(e) > 0):
#         t = e
#         e = e.replace('()', '')
#         e = e.replace('{}', '')
#         e = e.replace('[]', '')
#         if t == e:
#             return False
#
#     return True



# t = int(raw_input().strip())
# for a0 in xrange(t):
#     expression = raw_input().strip()
#     if is_matched(expression) == True:
#         print "YES"
#     else:
#         print "NO"

print is_matched('{[()]}')