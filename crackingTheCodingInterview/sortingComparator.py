# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "%s %s" % (self.name, self.score)

    def comparator(a, b):
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0


player = Player("David",100)
print player
cmp = Player.comparator
print cmp