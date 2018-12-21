# Enter your code here. Read input from STDIN. Print output to STDOUT
def manage_input():
    try:
        num = int(input())
    except:
        print('not an integer')
    x = []
    w = []
    try:
        x = list(map(int, input().split()))
        w = list(map(int, input().split()))
        
    except:
        print('not an int')
    return num, x, w

def caculate_weighted_mean(number, array_x, array_w):
    i = 0
    s = 0
    while(i < number):
        s += array_x[i]*array_w[i]
        i += 1
    weighted_mean = s/sum(array_w)
    return weighted_mean

if __name__ in '__main__':
    number, array_x, array_w = manage_input()
    print(caculate_weighted_mean(number, array_x, array_w))


                                                                                                
