def ask_input_to_user():
    try:
        num1 = int(input('give me first number:\n'))
        num2 = int(input('give me second number:\n'))
    except:
        print('integer,shabi\n')
        return ask_input_to_user()
    return num1, num2

def ask_function_to_user():
    user_input = input('choose one from add, subtract, multiply or divid:\n')
    if user_input not in ['add', 'subtract', 'multiply','divid']:
        print('please choose a good one\n')
        return ask_function_to_user()
    return user_input

def do_operation(a,b,operation):
    if operation  == 'add':
        print( a + b)
    elif operation == 'subtract':
        print( a - b)
    elif operation == 'multiply':
        print( a * b)
    else:
        print(a / b)


if __name__ in '__main__':
    a, b = ask_input_to_user()
    operation = ask_function_to_user()
    do_operation(a, b, operation)

