import random

list_of_fruits = ['apple', 'orange', 'banana' , 'rasberry', 'strawberry' ]

class Hangman:
    def __init__(self, list_of_fruits, num_lives):
        random_fruit = random.choice(list_of_fruits)
        self.random_fruit = random_fruit
        r_fruit_chars = list(random_fruit)
        self.r_fruit_chars = r_fruit_chars
        rfc_len =  len(r_fruit_chars)
        rfc_hangmanlist_small = ["_"]
        rfc_hangmanlist = rfc_hangmanlist_small * rfc_len
        self.rfc_hangmanlist = rfc_hangmanlist
        set_rfc = set(r_fruit_chars)
        rfc_num_ulet = len(set_rfc)   
        self.rfc_num_ulet = rfc_num_ulet
        self.num_lives = num_lives 
        self.list_of_fruits = list_of_fruits
        list_of_guesses = []
        self.list_of_guesses = list_of_guesses


def check_guess(self, guess):
    guess.lower()
    if guess in self.random_fruit:
        print(f"Good guess! {guess} is in the word.")
        for let in self.random_fruit:
            if let == guess:
                guess_index_num = self.r_fruit_chars.index(guess)
                self.rfc_hangmanlist[guess_index_num] = guess
                self.rfc_num_ulet -= 1
                return
    elif guess not in self.random_fruit:   
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word. Try again.")
        print(f"You have {self.num_lives} lives left.")
        return 
        
def ask_for_input(self):
    guess = input('Please choose a letter: ')
    while True:
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            break
        elif guess in self.list_of_guesses:
            print("you already tried that letter!")
            break
        else:
            if guess.isalpha() and len(guess) == 1:
                check_guess(self, guess)
                self.list_of_guesses.append(guess)
                break
                
        

def play_hangman():
    num_lives = 5
    game = Hangman(list_of_fruits, num_lives)
    while True:
        if game.num_lives == 0:
          print("Too bad you lost, LoosSsSssssser, please try again, unless you too chicken... Nerd!")
          return
        elif game.rfc_num_ulet > 0:
              ask_for_input(game)
        elif game.num_lives != 0 and game.rfc_num_ulet == 0:
          print("Congraulations, you have won! A million, billion, fluxtillionwillon blessings upon you and your family. Namste grasshopper!")
          return 
        
play_hangman() 