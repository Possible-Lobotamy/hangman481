import random

import random
word_list = ['Apple', 'Orange', 'Banana' , 'Rasberry', 'Strawberry' ]

print(word_list) 

word = random.choice(word_list)

print(word)

guess = input('Please choose a letter: ')

if guess.isalpha() == True and len(guess) == 1:
     print('Good guess!')
else: 
   print("Oops! That is not a valid input")