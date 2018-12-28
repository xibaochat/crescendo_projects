try:
    n = int(input())
except:
    exit('not a int')
    if n < 1 or n > 10**5:
        exit('not in the range')

phone_book = {}
for i in range(n):
    name, number = input().split()
    if len(number) != 8:
        exit('should be 8-digit number')
    else:
        phone_book[name] = number

while True:
    try:
        query_name = input()
        if query_name in phone_book:
            print('{0}={1}'.format(query_name, phone_book[query_name]))
        else:
            print('Not found')
    except:
        break
