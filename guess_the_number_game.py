

import random


range_1 = int(input('Choose the start number : '))
range_2 = int(input('Choose the end number : '))

chances = 3




random_num = random.randint(range_1, range_2)
print('Random number generated : ', random_num)

guess = 1

while(guess <= chances):

    user_input = int(input('Enter the number :'))
    if(user_input > random_num):
        print('Your guess is too high')
        guess +=1
        
    elif(user_input < random_num):
        print('Your guess is too low..')
        guess +=1
       

    elif(user_input == random_num):
        print('Great! You got it right')
        break

if(guess > chances):
    print('You ran out if chances..')

        
