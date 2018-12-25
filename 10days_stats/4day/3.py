def possibility_find_defect(p):
    possibility = 0
    for i in range(t):
        possibility += ((1 - p)**i)*p
    return round(possibility, 3)

if __name__ in '__main__':
    m, n = list(map(int, input().split()))
    p =  m / n
    t = int(input())
    print(possibility_find_defect(p))
