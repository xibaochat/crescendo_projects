import math

def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)

def calculate_value(m, n):
    value =  (math.exp(-1 * m) * (m**n)) / factorial(n)
    return round(value, 3)
m = float(input())
n = float(input())          


print(calculate_value(m, n))
            
