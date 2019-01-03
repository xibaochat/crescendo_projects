class Person(object):
    def __init__(self, firstname, lastname, idnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.idnumber = idnumber
    def printPerson(self):
        print('Name:'+ self.lastname + ',' + self.firstname)
        print('ID:' + self.idnumber)

class Student(Person):
    def __init__(self,firstname, lastname, idnumber, scores):
        Person.__init__(self, firstname, lastname, idnumber)
        self.scores = scores
    def calculate(self):
        ave = sum(self.scores)/len(self.scores)
        if ave >= 90 and ave <=100:
            return 'O'
        elif ave >= 80 and ave < 90:
            return 'E'
        elif ave >= 70 and ave < 80:
            return 'A'
        elif ave >= 55 and ave < 70:
            return 'P'
        elif ave >= 40 and ave < 55:
            return 'D'
        else:
            return 'T'
line = input().split()
firstname = line[0]
lastname = line[1]
idnumber = line[2]
numscores = int(input())
scores = list(map(int, input().split()))
s = Student(firstname, lastname, idnumber, scores)
s.printPerson()
print('Grade:', s.calculate())
