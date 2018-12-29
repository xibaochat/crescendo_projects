def manage_input():
    mark = []
    x = []
    y = []
    for i in range(5):
        mark.append(list(map(float, input().split())))
    for elem in mark:
        x.append(elem[0])
        y.append(elem[1])
    return x, y

def calculate_mean_and_sd(x, y):
    from statistics import mean
    from statistics import pstdev
    miu_x = mean(x)
    miu_y = mean(y)
    sd_x = pstdev(x)
    sd_y = pstdev(y)
    return miu_x, miu_y, sd_x, sd_y

def calculate_person_correlation_coeffient(x, y, miu_x, miu_y, sd_x, sd_y):
    s = 0
    for i in range(5):
        s += (x[i] - miu_x) * (y[i] - miu_y)
    return s / (5 * sd_x * sd_y)

def calculate_y(person_correlation_coeffient, sd_x, sd_y, miu_x, miu_y):
    b = person_correlation_coeffient * (sd_y / sd_x)
    a = miu_y - (b * miu_x)
    return round(a + b * 80, 3)


x, y = manage_input()
miu_x, miu_y, sd_x, sd_y = calculate_mean_and_sd(x, y)
person_correlation_coeffient = calculate_person_correlation_coeffient(x, y, miu_x, miu_y, sd_x, sd_y)
y_ = calculate_y(person_correlation_coeffient, sd_x, sd_y, miu_x, miu_y)

print(y_)
