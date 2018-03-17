import sys
from Hangman import Hangman
import os
#from hangman import Hangman

#Declarations
done_playing = False
wrong_input = True

#start up
print('Hello! Would you like to play hangman?')
response = input('y/n?')

if response == 'n':
    print('Goodbye!')
    sys.exit()

#prompt user for a word
word = input('What word or phrase would you like to use?')
while len(word) > 25:
    print('Your word/phrase is too long. The maximum number of characters is 25.')
    word = input('Please type in a new word.')

#main game loop
os.system('cls')
print("Let's play hangman!")
hangman = Hangman(word)
while (hangman.get_life != 0):
    print()
    print()
    print()
    guess = input('Guess a letter:')
    hangman.find_letter(guess)
    if hangman.check_gameover() == True:
        sys.exit()
    if hangman.check_win() == True:
        sys.exit()
    hangman.print_word()
    hangman.print_hangman()