from statistics import median

def manage_input():
    try:
        n = int(input())
    except:
        exit('not an int')
    if n < 5 or n > 50:
        exit('not in the range')
    
    array = list(map(int, input().split()))
    each_element_frequency = list(map(int, input().split()))
    
    return n, array, each_element_frequency

def total_set(number,array,frequency):
    s = []
    for i in range(number):
        for j in range(frequency[i]):
            s.append(array[i])
    s = sorted(list(s))

    return s

def get_first_and_third_quartiles(frequency, data_set):
    length_set = sum(frequency)
    if length_set % 2 == 0:
        array1 = data_set[0:int(length_set / 2)]
        array2 = data_set[int(length_set / 2):]
    else:
        array1 = data_set[0:int((length_set - 1 ) / 2)]
        array2 = data_set[int((length_set - 1) / 2) + 1:]
        
        return float(round(median(array2) - median(array1), 1))
    
    
    
if __name__ in '__main__':
    number, array, frequency = manage_input()
    data_set = total_set(number,array,frequency)
    q3 = get_first_and_third_quartiles(frequency, data_set)
    print(q3)
