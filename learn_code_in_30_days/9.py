def manage_input():
    try:
        n = int(input())
    except:
        exit('not a integer!')
    if n < 2 or n > 12:
        exit('not in the range')
        return n

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = manage_input()
recursion_value = factorial(n)
print(recursion_value)
