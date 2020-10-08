# This is a guess the number game.
import random
import time

print('Hello friend! What is your name?')
name = input()

print(' ')

namelen = len(name)
print(str(namelen) + ' Letter, Nice ' + name + '.')
print(' ')
print('Lets get to it shall we...')
time.sleep(5)
print(' ')
print('Well, ' + name + ' I am thinking of a number between 1 and 20 ')
secretNumber = random.randint(1, 20)
print(' ')
for guessesTaken in range(1, 7):
    print('take a guess ' + name + '!')
    guess = int(input())
    print(' ')
    if guess < secretNumber:
        print('Too low ' + name + '.')
    elif guess > secretNumber:
        print(' Too high, are you toying with me ' + name + '...')
    else:
        break   # This condition is for the correct guess.


if guess == secretNumber:
    print('Good job, ' + name + ' ! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('The number I was think of was ' + str(secretNumber))