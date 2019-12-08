#Guess the number game

import random

num = random.randrange(1, 101)

chance = 10

while chance > 0:
    guess = input('Guess the number between 1-100 : ')
    guess = int(guess)
    
    if num == guess:
        print('You guessed the right number!!!!!')
        break
    else:
        print('You are wrong :( \nHere take another chance')
        chance -= 1
        print('Choices left =', chance)
        if guess < num:
            print('Heaven')
        else:
            print('Hell')