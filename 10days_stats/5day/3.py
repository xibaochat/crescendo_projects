import math
def cumu_pro(mean, sd, x):
    return 0.5 * (1 + math.erf ((x - mean) / ((2**0.5)*sd)))

mean, sd = list(map(float, input().split()))
num_1 = float(input())
num_2 = float(input())
value_1 = round((1 - cumu_pro(mean, sd, num_1))*100, 2)
value_2 = round((1 - cumu_pro(mean, sd, num_2))*100, 2)
value_3 = round((cumu_pro(mean, sd, num_2))*100, 2)
print(value_1, value_2, value_3, sep = '\n')

    
