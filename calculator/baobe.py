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

def do_operation(a, b, function_from_user):
    if function_from_user == 'add':
        result = a + b
    elif function_from_user == 'subtract':
        result = a - b
    elif function_from_user == 'multiply':
        result = a * b
    elif function_from_user == 'divid':
        result = a / b
    print(result)

    
a, b = ask_input_to_user()
operation = ask_function_to_user()


