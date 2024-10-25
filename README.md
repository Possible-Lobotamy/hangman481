# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Aim of project: the aim of this project is to build a working hangman game in python using everything that has been taught and learnt so far from AIcore's coding bootcamp. 

What has been learnt:
- how to properly refer to class attributes
- how better to use local vairiables
- how to properly break out of while loops
- what a infinite loop does to your computer
- the importance of proper indentation
- how to better use nested functions
- how more effeciently use if else iterations
- not to fall behind on deadlines

Contents: 
line 21: Milestone 1 
line 28 Milestone 2
line 45 Milestone 3
line 61 Milestone 4
line 79 Milestone 5 


Milestone 1, steps:
1. github acount was accessed 
2. Hangman repo was made on github
3. files on VS code were made, with the intent of being able to push changed as well as clone repos where needed

Milestone 2, steps:
1. Firstly the random package from python's inbuilt packages was imported. This allowed for objects to be randomly chosen from a data structure. I.e a list.
2. Then a word list with 5 string objects, that represented 5 different fruits, was created.
3. This was then applied to the the random() function to choose a random object from the word list.
4. A variable 'guess' was then created with an input, prompting the user to enter a letter. This input was then used for a condtional 'for' loop to ascertain if the input was correct i.e. a 1 chracter long alphabetic letter.

Milestone 2, code issues and fixes:
 - guess = len(1) was used, changed corrently to len(guess) ==1
 - both the required conditions ascertaining the char length and type, were formatted as two 'if' statments one nested under the other.

   if guess.isalpha() == True:
     if len(guess) == 1:
     print(message)
   
 This lead to each being verfied serprately, leading to the condtion message not being printed as wanted. Was changed to include the operaton 'and' 

Milestone 3, steps:
1. Two functions were aimed to be set up: ask_for_input, to ask for the users guess input and check_guess to check said guess input and take the appropiate actions. 
2.1 A 'while loop' with the conditons set to true was created.
2.2 The user was prompted to enter a guess, which was then assigned to the 'guess' variable.
3.3 The 'guess' was checked using the len() and the isalpha() functions, to ascertain if it is a 1 digit alaphabetical letter, if it is a message asking to try again is printed and loop is broken, taking the user back to the input. 
4.1 seperately, an 'if else' statement block was created that checks if the 'guess' letter is or isn't in the randomly chosen word.
4.2 This 'if else' block is set to trigger either a messsage confriming or rufuting the letters presence in the word.
7. Both blocks of code, 3 and 4  are applied to their respective, functions with 3 going into the ask_for_input()  and 4 going to the check_guess()
8. If the ask_input() passes the while true condtions, the check_guess_function is called within the ask_for_input function, and the 'guess' is put through the guess_letter checks, before breaking the loop and returning. 
 
Milestone 3, code issues and fixes: 
- isalpha function used incorrectly untill realised
- check_guess() not nested at the right place using the right indentation at first. Fixed to be actually in an elif statement of the while loop. 
  

Milestone 4, steps:
1. a class of object called 'Hangman' is created for the game, with the parameters of the list of words, and the number of lives
2. using those two parametres, and verious created formulas class attributes are defined these are:
- word (word to be guessed, from the word list)
- letters guessed list (blank list of chracters from the word, to be filled in with the rightly guessed letters)
- number of unique letters (the number of letters in the word that haven't been guessed yet, not including duplicate letters)
- number of lives (the number of lives the player starts with)
- list of guesses (a list of all the guesess tried by the player)
  note that the names here do not refer to the directly to the names of the class arributes, just the concepts
3. the guess made in the check_guess function is set to appened to list of guesses. 

Milestone 4, code issues and fixes:
- problem, that each time a guess is right and a letter in the list, will replace the "_" placeholder with the letter as the index method stops at the first istance of the letter. Therefore, a word like 'Banana' with an 'n' guess would lead to '_ _ n _ _ _'. can't solve with set() as it disorders the list. Solved using a for loop to iterate every letter in the word.
- the guess.append(list_of_guesses) doesn't work as list of guesses isn't defined. this was part of a bigger problem and solved in the next milestone
- using a list fo the number of letters, presents a problem, as it allows duplicates, meaning for mulitples the letters would have to be guesses multiple times, which would invalidate the code logic. Fixed by making the list[] a set([]), duplicates not allowed. 


  Milestone 5, Steps:
  1. Firstly a play_hangman() defining function was created.
  2. The num_lives varible was set as local varible, within the function, with a value of (num_lives = 5)
  3. An instance of the Hangman class named 'game' was intiated, with the list_of_fruits, and num_lives as the list of words, and number of lives as parameters
  4. A While true loop was created to ascertain a few values:
  - if the number of lives is above 0 (num_lives == 0), a message indicating that the player has lost is 
      printed.
  - If the number of unique letters is greater than 0 (rfc_num_ulet > 0) the ask for input_function is called.
  - If number of lives is greater than 0 and the number of unique letters is 0 (game.num_lives > 0 and rfc_num_ulet == 0 ) then a message congratulating the player on 
      winning the game is printed.
  5. The check_guess function was then expanded upon
    - the guess input was converted to lowercase using lower()
    - if the guess is in the word, a message is printed, telling the player that it is.
    - using a for iteration for every letter in the in the word, if the letter == word then the index of the guess in the word is ascertained and then the letter is added to the equvilent index character of the letter guessed list.
    - if the guess is not in the word, the number of lives is reduced by 1 and two messges are printed informing that the letter is not in the word, and stating how many lives are left.
   6. This is then returned to the end of ask_for_input function, which appends the guess to the list of guesses.
   7. The game continues untill all the lives are used, or the number of unique letters are guessed i.e. won or lost. 
  
  Milestone 5, code issues and fixes:
  -  stopped the printed message printing several times if the letter is present more than once, achevied by taking it out of the for loop in check_guess and having it print just if the guess is in the word list i.e. "if guess in random_fruit"
  - when defining the play_game function to intilise the game, the varible number of lives is defined before calling the instant of the hangman class. However "number_letters" > the number of unique letters, in the random word generated, is not defined, and when used to set the conditions for game state, (L, cont, W), throws a Name error, and is not defined. this is in fact the same error as the list_of_guesses varible not being found. Essentially the class attributes were not being called in the the right way in the called for functions using self. prrefix to relate to the class, and in the play_game functiion. not using the game. prefix for the instance of the class. this was solved.
  - created an infinte loop, not using the break statements at the right points, that crashed my VSC. break statments moved to appropiate points.
  - the chracters of the word turned into a class attribute r_fruit_chars, as this helped make it easier to define other class attirbutes / function varibles etc. 

















 
