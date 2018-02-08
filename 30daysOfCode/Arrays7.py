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
<<<<<<< 0f4725c1a17031c69394374a1a2f4538c8cf5fc1
#test901
=======
#test456
>>>>>>> Abstract classes 13
