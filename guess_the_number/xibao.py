#!/usr/bin/python3


import random


def ask_input_to_user(msg):
    try:
        number = int(input(msg))
    except:
        return ask_input_to_user('Please enter an integer: ')
    return number

def guess_the_number():
    random_num = random.randint (0, 10000) 

    number_given_by_user = ask_input_to_user("Give me a number: ")
    
    while(random_num != number_given_by_user):
        if random_num < number_given_by_user:
            number_given_by_user = ask_input_to_user('Too high, try again: ')
        elif random_num > number_given_by_user:
            number_given_by_user = ask_input_to_user('Too low, try again: ')
    print('Felicitation!')

guess_the_number()
