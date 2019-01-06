class calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        return n ** p

if __name__ in '__main__':
    my_calculator = calculator()
    nb_input = int(input())
    for i in range(nb_input):
        n, p = map(int, input().split())
        try:
            answer = my_calculator.power(n, p)
            print(answer)
        except Exception as err:
            print(err)
