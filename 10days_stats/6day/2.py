def manage_input():
    try:
        number_sample = int(input())
    except:
        exit('not a int')
    try:
        mean = float(input())
    except:
        exit('not a number')
    try:
        sd = float(input())
    except:
        exit('not a number')
    try:
        p = float(input())
    except:
        exit('not a float')
    try:
        z_score = float(input())
    except:
        exit('not a float')
    return number_sample, mean, sd, p, z_score

def calculate_interval(mean, z_score, sd, number_sample):
    a = mean - (z_score*sd) / (number_sample**0.5)
    b = mean + (z_score*sd) / (number_sample**0.5)
    return round(a, 2), round(b, 2)



number_sample, mean, sd, p, z_score = manage_input()
interval_a, interval_b = calculate_interval(mean, z_score, sd, number_sample)
print(interval_a, interval_b, sep = '\n')
