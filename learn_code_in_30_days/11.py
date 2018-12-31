def manage_input():
    arr = []
    for i in range(6):
        row = list(map(int, input().split()))
        if len(row) != 6:
            exit('should be 6 units')
        else:
            arr.append(row)
    return arr

def get_pattern(arr):
    a1 = []
    a2 = []
    a3 = []
    for elem in arr[0:4]:
        for i in range(4):
            a1.append(elem[i : i + 3])
        for elem in arr[1:5]:
            for i in range(1,5):
                a2.append(elem[i])
        for elem in arr[2:6]:
            for i in range(4):
                a3.append(elem[i : i + 3])
    return a1, a2, a3
def calculate_max(a1, a2, a3):
    s = []
    for i in range(16):
        s.append(sum(a1[i]) + a2[i] + sum(a3[i]))
    return max(s)

if __name__ == '__main__':
    arr = manage_input()
    a1, a2, a3 = get_pattern(arr)
    max_value = calculate_max(a1,a2,a3)
    print(max_value)
