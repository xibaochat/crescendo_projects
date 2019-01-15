def manage_input():
    actual_data = list(map(int, input().split()))
    expected_data = list(map(int, input().split()))
    if actual_data[0] < 1 or expected_data[0] < 1 or actual_data[0] > 31 or expected_data[0] > 31:
        exit('day not in the range')
    if actual_data[1]< 1 or expected_data[1] < 1 or actual_data[1] > 12 or expected_data[1] > 12:
        exit('month not in the range')
    if actual_data[2] < 1 or expected_data[1] < 1 or actual_data[2] > 3000 or expected_data[2] > 3000:
        exit('month not in the range')
    return actual_data, expected_data

def calculate_fine(actual_data, expected_data):
    if actual_data[2] ==  expected_data[2] and actual_data[1] > expected_data[1] :
        print((actual_data[1] - expected_data[1]) * 500)

    elif actual_data[2] ==  expected_data[2] and actual_data[1] == actual_data[1] and actual_data[0] > expected_data[0]:
        print((actual_data[0] - expected_data[0]) * 15)

    elif actual_data[2] > expected_data[2]:
        print(10000)
    else:
        print(0)


actual_data, expected_data = manage_input()
calculate_fine(actual_data, expected_data)
