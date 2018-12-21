from statistics import median

def manage_input():
    try:
        n = int(input())
    except:
        exit('not an int')
    if n < 5 or n > 50:
        exit('not in the range')
    
    array = input().split()
    each_element_frequency = list(map(int, input().split()))

    return n, array, each_element_frequency

def total_set(n,array,frequency):
    s = {}
    for i in range(n):
        s += array[i]*each_element_frequency[i]
    s = sorted(list(s))
    
    return s

def length_array(frequency):
    length_array = sum(frequency)
    
    return length_set

def get_first_and_third_quartiles(frequency, data_set):
                                                                                        if length_array(frequency) % 2 == 0:
                                                                                            array1 = array[0:int(length_array/2)]
                                                                                            array2 = array[int(length_array/2):]
                                                                                        else:
                                                                                            array1 = array[0:int((length_array-1)/2)]
                                                                                            array2 = array[int((length_array-1)/2)+1:]
                                                                                            
                                                                                            return round((int(median(array2)) - int(median(array1))),1)



                                                                                    if __name__ in '__main__':
                                                                                        number, array, frequency = manage_input()
                                                                                        data_set = total_set(n,array,frequency)
                                                                                        length_set = length_array(frequency)
                                                                                        q3 = get_first_and_third_quartiles(frequency, data_set)
    print(q3)                                                                                    
