
if __name__ == '__main__':
    try:
        n = int(input())
    except:
        exit('not an int')
    if n < 1 or n > 10**6:
        exit('not in the range')
    arr = bin(n)[2:]
    arr = arr.split('0')
    max_len = len(max(arr, key = lambda x : len(x)))
    print(max_len)
