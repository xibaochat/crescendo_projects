i = 4
d = 4.0
s = 'HackerRank '

try:
    given_int = int(input())
    given_double = float(input())
    given_string = str(input())
except:
    print('check the data type')

print(given_int+i,given_double+d,s+given_string, sep = '\n')
