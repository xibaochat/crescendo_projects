import sys
try:
    n = int(input().strip())
except:
    exit('not an int')
if n < 2 or n > 600:
    exit('not in the range')

a = list(map(int, input().strip().split(' ')))
for elem in a:
    if elem < 1 or elem > 2 * (10**6):
        exit('elem not in the range')
num_swap = 0

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j + 1]:
            c = a[j +1]
            a[j + 1] = a[j]
            a[j] = c
            num_swap += 1
print('Array is sorted in {0} swaps.\nFirst Element: {1}\nLast Element: {2}'.format(num_swap, a[0], a[-1]))
