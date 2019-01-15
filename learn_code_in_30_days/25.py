def manage_input():
    try:
        T = int(input())
    except:
        exit('not an int')
    if T < 1 or T > 30:
        exit('not in the range')
    queue = []
    for i in range(T):
        try:
            input_number = int(input())
        except:
            exit('not an int')
        if input_number < 1 or input_number > 2 * 10**9:
            exit('input not in the range')
        queue.append(input_number)

    return queue

def check_input_is_a_prime(queue):

    for elem in queue:
        if elem > 1 and elem < 4:
            print('Prime')
        elif elem == 1:
            print('Not prime')
        else:
            for i in range(2, int(elem**0.5) + 1):
                if elem % i == 0:
                    print('Not prime')
                    break
            else:
                print('Prime')



queue = manage_input()
check_input_is_a_prime(queue)
