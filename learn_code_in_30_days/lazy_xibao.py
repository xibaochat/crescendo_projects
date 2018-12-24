class Person(object):
    def __init__(self, given_age):
        self.age = self.check_given_age_value(given_age)
        
    def check_given_age_value(self, age):
        if age < 0:
            print('Age is not valid, setting age to 0.')
            return 0
        return age

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
            

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
