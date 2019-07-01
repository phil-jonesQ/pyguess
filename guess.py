# Ultra simple guess the number game. Using a module import to keep the code as minimal as possible.

import random
from processguess import *

won = False
guessCount = 0
number = random.randint(1,100)


while not won:
    print("Please guess the number I'm thinking of: " + " You have made " + str(guessCount) + " guesses")
    guess = input()
    try:
        val = int(guess)
    except ValueError:
        print("Error I need a Number!!")
        continue
    guessCount += 1
    guess = int(guess)
    if processguess(guess, number):
        won = False
    else:
        won = True

exit(0)














