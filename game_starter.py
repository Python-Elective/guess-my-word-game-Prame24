
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for c in letters_guessed:
      if c not in secret_word:
        return False
    return True
    
    
    # FILL IN YOUR CODE HERE...


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])) # output = False
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])) #output = False
# print(is_word_guessed('pineapple', ['p', 'i', 'n','e','a', 'l'])) #output = True
# print(is_word_guessed ('carrot', ['b', 'g', 'd', 'z', 'w', 'y', 'v', 'm', 'i', 'k'])) #output = False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    output_string = ''
    for c in secret_word:
       if c in letters_guessed:
         output_string += c
       else:
         output_string += '_ '
    return output_string
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
# print(get_guessed_word('durian', []))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    # alphabet = string.ascii_lowercase
    
    # for c in letters_guessed:
    #   alphabet = alphabet.replace(c,'')
      
    # return alphabet

    alphabet = list(string.ascii_lowercase)
    
    # for c in letters_guessed:
    #   if c in letters_guessed:
    #     alphabet.remove(c)
        
    # return ' '.join([c for c in alphabet if c not in letters_guessed])
    
    output_string = ''
    for c in alphabet:
      if c not in letters_guessed:
        output_string = output_string + c + ' '
    return output_string

#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
# print( get_available_letters([]))
# print( get_available_letters(['r', 'y', 'd', 'u', 't']))
# print( get_available_letters(['p', 'r', 'f', 'd', 'k', 'h', 'c', 'a', 'i', 'y', 'w', 'b']))
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guess_attempt = 8
    letters_guessed = []
    guess = ''
    guessInLower = ''
    
    print('let the game begin!')
    print(f'I am thinking of a word with {len(secret_word)} letters')
    
    while guess_attempt > 0 and '_ ' in get_guessed_word(secret_word, letters_guessed):
      print(f'you have {guess_attempt} guesses remaining')
      print(f'Letters available: {get_available_letters(letters_guessed)}')
      guess = input('guess a letter: ')
      guessInLower = guess.lower()
      
      if guessInLower in letters_guessed:
        print(f'YOU FOOL, you already guessed this: {get_guessed_word(secret_word, letters_guessed)}\n')
      elif guessInLower in secret_word:
        letters_guessed.append(guessInLower)
        print(f'correct: {get_guessed_word(secret_word ,letters_guessed)}\n')
      else:
        print(f'incorrect!: {get_guessed_word(secret_word ,letters_guessed)}\n')
        letters_guessed.append(guessInLower)
        guess_attempt -= 1
        
        
    if is_word_guessed(secret_word, letters_guessed) == False:
      return print(f'YOU LOSE, secret word is: {secret_word}')
    else:
      return print(f'YOU WIN!')



def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()