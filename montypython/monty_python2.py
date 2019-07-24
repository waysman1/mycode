#!/usr/bin/env python3

round = 0   #integer round initiated to 0

while(True):  # sets up an infinite loop condition
    round = round + 1   # increases the round counter
    print('Finsh the movie title, "Monty Python\'s The Life of _____"')  
    answer = input()    # string anser collected from user
    if (answer == 'Brian'):    # logic to check if user gave correct answer
        print('Correct')
        break  # break statement escape the while loop
    elif (round==3):   # logic to ensure round has not yet been reached 3
        print('Sorry, the answer was Brian.')
        break  # break statement escapes the while loop
    else:    #if answer was wrong, and round is ot yet equal to 3
        print('Sorry! Try again!')

