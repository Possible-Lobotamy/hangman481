import random
list_of_fruits = ['apple', 'orange', 'banana' , 'rasberry', 'strawberry' ]
random_fruit = random.choice(list_of_fruits)

def check_guess(guess):
  guess.lower()
  if guess in random_fruit:
       print(f"Good guess! {guess} is in the word.")
  else: 
       print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    check_guess(guess)
    while True:
      guess = input('Please choose a letter: ')
      if guess.isalpha()  and len(guess) == 1:
        break
      else:
         print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()