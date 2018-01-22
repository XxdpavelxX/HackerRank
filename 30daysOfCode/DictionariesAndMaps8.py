#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
number = input()
dicty = {}
x = 0
while x < number:
    newInp = raw_input()
    key, val = newInp.split(" ")
    dicty[key] = val
    x += 1

y = 0
while y < number:
    try:
        findInp = raw_input()
        print "%s=%s" % (findInp, dicty[findInp])
    except KeyError:
        print "Not found"
    y += 1