import random
list_of_fruits = ['Apple', 'Orange', 'Banana' , 'Rasberry', 'Strawberry' ]

print(list_of_fruits)

random_fruit = random.choice(list_of_fruits)

print(random_fruit)

while True:

  guess = input('Please choose a letter: ')

  if guess.isalpha()  and len(guess) == 1:
     break
  else:
     print("Invalid letter. Please, enter a single alphabetical character.")

if guess in random_fruit
 