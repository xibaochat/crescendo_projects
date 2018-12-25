# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def binomial_calculation(n):
    f = factorial(m) / (factorial(m - n) * factorial(n))
    return f

def calculate_possibility(f, m, n):
    return f * (p**n) * ((1 - p)**(m - n))

if __name__ in '__main__':
    p, m = list(map(int, input().split()))
    p = p/100
    s1 = 0
    s2 = 0
    for n in range(0, 3):
        f = binomial_calculation(n)
        s1 += calculate_possibility(f, m, n)
    print(round(s1, 3))
    
    for n in range(2, m+1):
        f = binomial_calculation(n)
        s2 += calculate_possibility(f, m, n)
    print(round(s2, 3))


                                                                                        
