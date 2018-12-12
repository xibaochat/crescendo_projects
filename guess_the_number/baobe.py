def compare_num():
    import random
    random_num = random.randint (0, 10000) 
    try:
        user_give_number = int (input ('please enter a number:'))
    except:
        print ('please enter an integer!') 
        
    
    while(random_num != user_give_number):
        if random_num < user_give_number:
            print ('too high, try again')
            user_give_number = int(input('please enter a number:'))
        elif random_num > user_give_number:
            print ('too low, try again')
            user_give_number = int(input('please enter a number:'))
        else:
            print('felicitation!')
            break
        
compare_num()
