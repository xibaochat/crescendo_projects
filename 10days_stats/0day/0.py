def manage_input():
    try:
        number_of_element = int(input())
    except:
        print('not an integer')
    given_array = input().split()
    try:
        given_array = list(map(int, given_array))
    except:
        print('not a int')
    return number_of_element, given_array
        
def find_average(number, array):
    average = sum(array)/number
    return round(average,1)

def find_median(number,array):
    if len(array) < 1:
        return None
    elif len(array) % 2 == 0 :
        return (array[int(len(array)/2)-1] +  array[int(len(array)/2)])/2.0
    else:
        return array[int((len(array)-1)/2)]
    
def find_mode(array):
    from collections import Counter
    max_occurence = []
    counted_array = Counter(array).most_common(number)
    return counted_array[0][1]

if __name__ in '__main__':
    number, array = manage_input()
    print(find_average(number, array))
    print(find_median(number, array))
    print(find_mode(array))
