try:
    number_str = int(input())
except:
    exit('not an int')
    
    
for i in range(number_str):
    arr_1 = []
    arr_2 = []
    s = input()
    for j in range(len(s)):
        if j % 2 ==0:
            arr_1.append(s[j])
        else:
            arr_2.append(s[j])
        str1 = ''.join(arr_1)
        str2 = ''.join(arr_2)
    print (str1, str2)


                                                            
