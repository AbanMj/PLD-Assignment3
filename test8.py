#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

import random
find= random.randint(0,100)

def guessing():
    guess= float(input('Guess the number:   '))
    while guess 

guess= guessing()