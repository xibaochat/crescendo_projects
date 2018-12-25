def calculate_possible(p, t):
    return ((1 - p)**(t -1))*p


if __name__ in '__main__':
    m, n = list(map(int, input().split()))
    p = m / n
    t = int(input())
    machine_defect_possiboloty = round(calculate_possible(p,t), 3)
    print(machine_defect_possiboloty)
