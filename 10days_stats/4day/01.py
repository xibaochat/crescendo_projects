def factorial(x):
    if x == 0:
       return 1		
    return x * factorial(x-1)

def caculate_factorial(x):
    return factorial(6) / (factorial(x) * factorial(6-x))

def caculate_possibility(x):
    return caculate_factorial(x) * (p**x) * ((1-p)**(6-x))


if __name__ in '__main__':
    ration_boy, ration_girl = list(map(float, input().split()))
    p = ration_boy / (ration_girl + ration_boy)
    n = 6
    s = 0 
    for x in range(3,7):
        s += caculate_possibility(x)

    print(round(s, 3))
