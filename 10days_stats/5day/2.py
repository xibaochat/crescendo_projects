
import math
def cumulative_possibility(x):

    return (1/2 * (1 + math.erf(x - normal_distribution_mean)) / (standard_deviation *  (2**1/2)))


normal_distribution_mean, standard_deviation = list(map(float, input().split()))

assemble_time_a = float(input())

assemble_time_b, assemble_time_c = list(map(float, input().split()))

cumulative_possibility_a = round(cumulative_possibility(assemble_time_b), 3)
cumulative_possibility_b = round((cumulative_possibility(assemble_time_c) - cumulative_possibility(assemble_time_b)), 3)

print(cumulative_possibility_a, cumulative_possibility_b)
    
















































