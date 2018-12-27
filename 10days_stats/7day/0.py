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
def calculate_mean_and_sd(x, y):
    from statistics import mean
    from statistics import pstdev
    miu_x = mean(x)
    miu_y = mean(y)
    sd_x = pstdev(x)
    sd_y = pstdev(y)
    return miu_x, miu_y, sd_x, sd_y

def calculate_person_correlation_coeffient(n, x, y, miu_x, miu_y, sd_x, sd_y):
    s = 0
    for i in range(n):
        s += (x[i] - miu_x) * (y[i] - miu_y)
    return round(s / (n * sd_x * sd_y), 3)

x, y, n = manage_input()
miu_x, miu_y, sd_x, sd_y = calculate_mean_and_sd(x, y)
person_correlation_coeffient = calculate_person_correlation_coeffient(n, x, y, miu_x, miu_y, sd_x, sd_y)
print(person_correlation_coeffient)
