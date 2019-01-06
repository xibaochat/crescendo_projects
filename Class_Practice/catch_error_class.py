class Calculator:
    def power(self, n , p):
        if n|p < 0:
            raise Exception ('n and p should be non-negative')
        return n ** p

myCalculator = Calculator()
number_input = int(input())
for i in range(number_input):
    n,p = map(int, input().split())
    try:
        answer = myCalculator.power(n,p)
        print(answer)
    except Exception as e:
        print(e)
