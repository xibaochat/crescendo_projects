import re
if __name__ == '__main__':
    name_array = []
    try:
        N = int(input())
    except:
        exit('not an int')
    if N < 2 or N > 30:
        exit('not in the range')

    for i in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if len(firstName) > 20:
            exit('first name is too long')
        if len(emailID) > 50:
            exit('email address is too long')

        if re.findall(r'^.+@gmail.com$', emailID) != []:
            name_array.append(firstName)

    name_array = sorted(name_array)
    print(('\n').join(name_array))
