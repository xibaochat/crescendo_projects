n = int(input())
array = list(map(int, input().split()))
if n < 5 or n > 50:
    print('out of range')
for i in array:
    if i <= 0 or i > 100:
        print('not in the range')
array = sorted(array)
l = len(array)

from statistics import median
Q2 = int(median(array))
if l % 2 ==0:
    array1 = array[0:int(l/2)]
    array2 = array[int(l/2):]
else:
    array1 = array[0:int((l-1)/2)]
    array2 = array[int((l-1)/2)+1:]
Q1 = int(median(array1))
Q3 = int(median(array2))
print(Q1,Q2,Q3, sep = '\n')














                                            
