class Person:
    def __init__(self,age):
        self.age = self.check_given_age(age)

    def check_given_age(self, age):
        if age < 0:
            print('Age is not valid, setting age to 0.')
            return 0
        return age

    def amIold(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearpass(self):
        self.age += 1

number_person = int(input())
for i in range(number_person):
    age = int(input())
    p = Person(age)
    p.amIold()
    for j in range(3):
        p.yearpass()
    p.amIold()
