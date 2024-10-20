# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Aim of project: the aim of this project is to build a working hangman game in python using everything that has been taught and learnt so far from AIcore's coding bootcamp. 

What has been learnt:

Contents: 

Milestone 1:
1. firstly the random package from python's inbuilt packages was imported. This allowed me to randomly chose and object from a data structure. I.e a list.
2. Then a list with 5 string objects, that represented 5 different fruits, was created.
3. This was then applied to the the 'random()' function to generate a random one of said string objects.
4. a varible 'guess' was created with an input, prompting the user to enter a letter. This input was then used for a condtional 'for' loop to ascertain if the input was correct i.e. a 1 chracter long alphabetic letter.

5. guess = len(1) was used, changed corrently to len(guess) ==1
6. both the required conditions ascertaining the char length and type, were formatted as two 'if' statments one nested under the other.

   if guess.isalpha() == True:
     if len(guess) == 1:
     print(message)
   
 This lead to each being verfied serprately, leading to the condtion message not being printed as wanted. Was changed to include the operaton 'and' 
