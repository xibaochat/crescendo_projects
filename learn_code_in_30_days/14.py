class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.__elements = sorted(set(self.__elements))
        self.maximumDifference = self.__elements[len(self.__elements) - 1] - self.__elements[0]
        if self.maximumDifference < 0:
            self.maximumDifference = -1 * self.maximumDifference



_ = input()
a = [int(e) for e in input().split()]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
