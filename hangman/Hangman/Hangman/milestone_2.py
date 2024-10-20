import random

import random
list_of_fruits = ['Apple', 'Orange', 'Banana' , 'Rasberry', 'Strawberry' ]

print(list_of_fruits)

random_fruit = random.choice(word_list)

print(random_fruit)

guess_a_letter = input('Please choose a letter: ')

if guess_a_letter.isalpha() == True and len(guess) == 1:
     print('Good guess!')
else: 
   print("Oops! That is not a valid input")