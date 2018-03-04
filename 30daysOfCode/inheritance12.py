#https://www.hackerrank.com/challenges/30-inheritance/problem

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    def calculate(self):
        total = 0
        for x in self.scores:
            total += x
        average = total/len(self.scores)
        if 90<=average<=100:
            return "O"
        elif 80<=average<=90:
            return "E"
        elif 70<=average<=80:
            return "A"
        elif 55<=average<=70:
            return "P"
        elif 40<=average<=55:
            return "D"
        elif average<40:
            return "T"

#Test123
#test456