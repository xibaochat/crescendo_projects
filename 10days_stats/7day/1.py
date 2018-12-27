def manage_input():
    x = []
    y = []
    try:
        n = int(input())
    except:
        exit('not a int')
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    for i in x:
        if x.count(i) > 1:
            exit('should be a unique value')
        elif i < 1 or i > 500:
            exit('not in the range')
        else:
            continue
    for j in y:
        if y.count(j) > 1:
            exit('should be a umique value')
        elif j < 1 or j > 500:
            exit('not in the range')
        else:
            continue
    return x, y, n

def query_square(n, x, y):
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    s = 0
    for i in range(n):
        s += (sorted_x.index(x[i]) - sorted_y.index(y[i]))**2
    return round(1 - 6*s /(n*(n**2 - 1)), 3)



x, y, n = manage_input()
spearman_rank_correlation_coefficient = query_square(n, x, y)
print(spearman_rank_correlation_coefficient)
