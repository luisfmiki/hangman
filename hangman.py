# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    secret = list(secret_word)
    size = len(secret_word)
    num = 0
    for letter in secret:
      for x in letters_guessed:
        if x == letter:
          num += 1
    if num == size:
      return True
    else:
      return False 


def get_guessed_word(secret_word, letters_guessed):
    secret = list(secret_word)
    underscored = ""
    for x in range(len(secret_word)):
      underscored = underscored + "_ #"
    b = underscored.split("#")  
    num = 0
    for letter in secret:
        for x in letters_guessed:
            if x == letter:
                b[num] = x
        num += 1
    g = "".join(b)
    return g


def get_available_letters(letters_guessed):
    alfabeto = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in alfabeto:
            alfabeto.remove(letter)
    return "".join(alfabeto)

def hangman(secret_word):
    print("Welcome to the the hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("----------")
    guesses = 6
    letters_guessed = []
    secret = "".join(secret_word)
    warnings = 3    
    while guesses > 0:
        print("You have", guesses, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if letter.isalpha():
            if letter.lower() not in letters_guessed:
                letters_guessed.append(letter.lower())
                if letter.lower() not in secret:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
                elif is_word_guessed(secret_word, letters_guessed):
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    print('---------')
                    print('Congratulations, you won!')
                    print('Your total score for this game is:', guesses*len(secret_word))
                    p = input("Play again?: ")
                    if p == "y":
                        print("----------")
                        hangman(choose_word(wordlist))
                    else:
                        sys.exit()
                else:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
            if warnings == 0:
                guesses -= 1
                print("You run out of warnings, so you lose a guess!", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("----------")
    print("Sorry, you ran out of guesses. The world was", secret)
    p = input("Play again?:")
    if p == "y":
        print("----------")
        hangman(choose_word((wordlist)))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    check = 0
    my = my_word.replace(" ", "")
    if len(my) != len(other_word):
        return False
    for x in range(len(other_word)):
        if my[x] == other_word[x] or my[x] == '_':
            check += 1
        else:
            return False
    if check == len(other_word):
        return True 
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def show_possible_matches(my_word):
    x = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            x += 1
            print(word, end=" ")
    if x == 0:
        print("No matches found")
    print("\n")
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def hangman_with_hints(secret_word):
    print("Welcome to the the hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("----------")
    guesses = 6
    letters_guessed = []
    secret = "".join(secret_word)
    warnings = 3    
    while guesses > 0:
        print("You have", guesses, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if letter.isalpha():
            if letter.lower() not in letters_guessed:
                letters_guessed.append(letter.lower())
                if letter.lower() not in secret:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
                elif is_word_guessed(secret_word, letters_guessed):
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    print('---------')
                    print('Congratulations, you won!')
                    print('Your total score for this game is:', guesses*len(secret_word))
                    p = input("Play again?: ")
                    if p == "y":
                        print("----------")
                        hangman(choose_word(wordlist))
                    else:
                        sys.exit()
                else:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        elif letter == "*":
          print("Possible matches are:")
          show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            if warnings == 0:
                guesses -= 1
                print("You run out of warnings, so you lose a guess!", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("----------")
    print("Sorry, you ran out of guesses. The world was", secret)
    p = input("Play again?:")
    if p == "y":
        print("----------")
        hangman(choose_word((wordlist)))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
