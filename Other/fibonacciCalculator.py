# def fibonacci(number):
#     counter = 0
#     fibList = [0,1]
#     while number>len(fibList)-1:
#         oldNumber = fibList[-2]
#         fibList.append(oldNumber + fibList[-1])
#         counter += 1
#     return fibList[-1]
#
#
# def findClosestFib(number):
#     x = 0
#     difference = 1
#     new_difference = 0
#     firstChange = 0
#     while (difference <= new_difference or firstChange < 1) or x == 0:
#         fib_number = fibonacci(x)
#         difference = new_difference
#         new_difference = abs(number - fib_number)
#         if new_difference > difference:
#             firstChange += 1
#         x = x+1
#         print "dif: ",difference, "new diff: ",new_difference, "fib number: ", fib_number
#
# findClosestFib(13)


def fib(number):
    counter = 0
    a, b = 0, 1
    print "hi"
    while number>counter:            # First iteration:
        a, b = b, a + b
        counter += 1
    print b

[0,1,1,2,3]
fib(5)
