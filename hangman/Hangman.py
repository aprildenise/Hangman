class Hangman:

    #global variables
    """
    global word
    word = ""
    global word_length
    word_length = 0
    global list
    list = []
    """
    global life
    life = 6

    #constructor?
    def __init__(self, given_word):
        global word
        word = given_word
        self.index_word()

    #index the given word into the list
    def index_word(self):
        word_length = len(word)
        global list
        list = [[] for i in range(word_length)] #create a list with length = length of the word
        global guessed_letters 
        guessed_letters = []

        #iterate through the word and add the letter,false pair to the list
        counter = 0
        for letter in word:
            list[counter] = False
            counter = counter + 1
        #print(list) 

    #checks if a word/phrase contains the letter
    def find_letter(self, guess):
        counter = 0
        num = 0;
        global guessed_letters
        guessed_letters.extend(guess)
        for letter in word:
            if guess.lower() == letter.lower():
                list[counter] = True;
                num+= 1
            counter+= 1
        if num > 0:
            print('Your guess was CORRECT!')
            #print(list)
        else:
            print('Your guess was WRONG!')
            global life
            life-=1

    #get the life of the player/hangman
    def get_life(self):
        return life

    #check if you've lost!
    def check_gameover(self):
        if life == 0:
            print('Your hangman has been hung! Game over!')
            print('Your word was: ' + word)
            return True
        else:
            return False

    def check_win(self):
        global list
        for value in list:
            if value == False:
                return False
        print("Congrats! You've guessed the word!")
        return True

    #print out the word
    def print_word(self):
        counter = 0
        printout = ""
        print('You have:')
        for letter in list:
            #print(list[counter])
            if list[counter] is False:
                printout+= " _ "
            else:
                character = word[counter]
                printout = printout + " " + character + " "
            counter+=1
        print(printout)
        print('You already guessed:')
        print(guessed_letters)

    #chose which hangman to print out
    def print_hangman(self):
        if life == 6:
            self.print_full_man()
        elif life == 5:
            self.print_five_man()
        elif life == 4:
            self.print_four_man()
        elif life == 3:
            self.print_three_man()
        elif life == 2:
            self.print_two_man()
        elif life == 1:
            self.print_one_man()
        else:
            self.print_dead_man()

    #print out the full hang man
    def print_full_man(self):
        print('   T------+')
        print('   O      |')
        print('  /|\     |')
        print('  / \     |')

    #print out the 5 man
    def print_five_man(self):
        print('   T------+')
        print('   O      |')
        print('  /|\     |')
        print('  /       |')

    def print_four_man(self):
        print('   T------+')
        print('   O      |')
        print('  /|\     |')
        print('          |')

    def print_three_man(self):
        print('   T------+')
        print('   O      |')
        print('  /|      |')
        print('          |')

    def print_two_man(self):
        print('   T------+')
        print('   O      |')
        print('   |      |')
        print('          |')
        
    def print_one_man(self):
        print('   T------+')
        print('   O      |')
        print('          |')
        print('          |')

    def print_dead_man(self):
        print('   T------+')
        print('          |')
        print('          |')
        print('          |')