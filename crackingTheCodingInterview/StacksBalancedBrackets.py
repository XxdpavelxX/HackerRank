#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
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


# def is_matched(expression): #doesnt work times out for some
#     dicty = {"{" : "}", "[" : "]", "(" : ")"}
#     listy = []
#     for i in expression:
#         if i in dicty.keys():
#             listy.append(dicty[i])
#         elif len(listy) > 0 and i != listy[-1]:
#             return False
#         else:
#             listy.pop()
#     return len(listy) == 0

def is_matched(expression):
    t = expression
    while t == expression and len(expression) > 0:
        t = t.replace("()", "")
        t = t.replace("[]", "")
        t = t.replace("{}", "")
        if t == expression:
            return False
        else:
            expression = t
    return True


print is_matched("{[()]}")