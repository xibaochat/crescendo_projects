from statistics import median


def manage_input():
    n = int(input())
    if n < 5 or n > 50:
        exit('out of range')

    array = list(map(int, input().split()))
    for i in array:
        if i <= 0 or i > 100:
            exit('not in the range')
    array = sorted(array)
    return n, array

def get_first_and_last_quartile(length_array, array):
    if length_array % 2 == 0:
        array1 = array[0:int(length_array/2)]
        array2 = array[int(length_array/2):]
    else:
        array1 = array[0:int((length_array-1)/2)]
        array2 = array[int((length_array-1)/2)+1:]

    return int(median(array1)), int(median(array2))


if __name__ in '__main__':
    length_array, array = manage_input()
    q1, q3 = get_first_and_last_quartile(length_array, array)
    q2 = int(median(array))

    print(q1, q2, q3, sep='\n')
