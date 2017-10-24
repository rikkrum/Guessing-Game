# this is a guess the number game

import random

guessesTaken = 0 # number of guesses begin at 0

print('Hello! What is your name? ')
myName = input() # lets me input my name

number = random.randint(1,20) # generates random numbers between range of 1-20, can be changed to whatever
print('Well,' + myName + ', I am thinking of a number between 1 and 20. ')
for guessesTaken in range(6): # range here limits how many guesses before game over. for loop 6 times begins
    print('Take a guess.') # four spaces in front of print

    guess = input() # allows me to enter my guess
    guess = int(guess) # takes my input and make it into an integer

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break # breaks the for loop

if guess == number:
    guessesTaken = str(guessesTaken + 1) # range always begins at 0, so 6 tries is 0-5, plus 1 to make 6. the 6 is turned into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope! The number I was thinking of was ' + number + '.')
              
    
