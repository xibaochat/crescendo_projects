import math
def cumu_pro(x, mean, sd):
    return 0.5 * (1 + math.erf((x - mean) / (sd *  2**0.5)))


mean, sd = list(map(float, input().split()))

time_a = float(input())

time_b, time_c = list(map(float, input().split()))

cumu_pro_1 = round(cumu_pro(time_a, mean, sd), 3)
cumu_pro_2 = round((cumu_pro(time_c, mean, sd) - cumu_pro(time_b, mean, sd)), 3)

print(cumu_pro_1, cumu_pro_2, sep = '\n')





    
