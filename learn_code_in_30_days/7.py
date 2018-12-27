if __name__ == '__main__':
    try:
        n = int(input())
    except:
        exit('not an int')

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
