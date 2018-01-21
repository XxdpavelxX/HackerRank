#https://www.hackerrank.com/challenges/30-arrays/problem

arr= [1,2,3,4]

reverseArr = []
while len(arr)>0:
    reverseArr.append(arr[-1])
    arr.pop()
arrayString = map(str, reverseArr)
answer = " ".join(arrayString)
print answer


#or
print(" ".join(map(str, arr[::-1])))