import json
from random import randint
import urllib.request

# From https://stackoverflow.com/a/45808300


def index_of(a_list, value):
    try:
        return a_list.index(value)
    except ValueError:
        return -1

# Built-in functions
# https://docs.python.org/3/library/functions.html

# Robot Map Game
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


def get_dictionary():
    source = "https://raw.githubusercontent.com/words/an-array-of-english-words/master/index.json"
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read())
        return data


# http://hangman.ascii.uk/
def header():
    return f'''
      WELCOME TO 
           _                                  
          | |                                           
          | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
          | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
          | | | | (_| | | | | (_| | | | | | | (_| | | | |
          |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                              __/ |                      
                            |___/  
                            
                                                     GAME!'''

# TODO: Complete function: find_letter_word_position = index_of(word, guess) - it's just returning
# the first item. eg: banana -> find 'a' => [1]

def draw_hangman(errors, current_scoreboard):
    lost = f'''
          ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _ \\
        | |          ||  `/,|
        | |          (\\`_.'
        | |         .-`--'.
        | |        /Y . . Y\\\\
        | |       // |   | \\\\
        | |      //  | . |  \\\\
        | |     ')   |   |   (`
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \
        """"""""""|_`-' `-' |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
. .          `'       . .
  '''

    no_errors = f'''
          ___________.._______
        | .__________))______|
        | | / / 
        | |/ /  
        | | /   
        | |/    
        | |     
        | |     
        | |     
        | |     
        | |     
        | |     
        | |     
        | |          
        | |          
        | |          
        | |          
        | |         
        """"""""""|_        |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
        . .          `'       . .
  '''

    one_error = f'''
          ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _ \\
        | |          ||  `/,|
        | |          (\\`_.'
        | |         
        | |        
        | |       
        | |      
        | |     
        | |     
        | |     
        | |     
        | |     
        | |     
        """"""""""|_        |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
        . .          `'       . .
  '''

    two_errors = f'''
          ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \
        | |          ||  `/,|
        | |          (\\`_.'
        | |         .-`--'.
        | |           . . 
        | |          |   |
        | |          | . |
        | |          |   |
        | |          
        | |          
        | |          
        | |          
        | |         
        """"""""""|_        |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
        . .          `'       . .
  '''

    three_errors = f'''
          ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\`_.'
        | |         .-`--'.
        | |        /Y . . 
        | |       // |   |
        | |      //  | . |
        | |     ')   |   |
        | |          
        | |          
        | |          
        | |          
        | |         
        """"""""""|_        |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
        . .          `'       . .
  '''

    four_errors = f'''
          ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\`_.'
        | |         .-`--'.
        | |        /Y . . Y\\\\
        | |       // |   |  \\\\
        | |      //  | . |   \\\\
        | |     ')   |   |   (`
        | |          
        | |          
        | |          
        | |          
        | |         
        """"""""""|_        |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
        . .          `'       . .
  '''

    five_errors = f'''
          ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \
        | |          ||  `/,|
        | |          (\\`_.'
        | |         .-`--'.
        | |        /Y . . Y\\\\
        | |       // |   |  \\\\
        | |      //  | . |   \\\\
        | |     ')   |   |   (`
        | |          ||'
        | |          || 
        | |          || 
        | |          || 
        | |         / | 
        """"""""""|_`-'     |"""|
        |"|"""""""\ \       '"|"|
        | |        \ \        | |
        : :         \ \       : :
        . .          `'       . .
  '''

    arts = [no_errors, one_error, two_errors,
            three_errors, four_errors, five_errors, lost]

    return f'''
      {arts[errors]}
      {current_scoreboard}'''


def scoreboard(formatted_word, guess, misses):
    return f'''
  - - - - - - - - - - - - - - - - - - - - - - - - 
  Word: {' '.join(formatted_word)}
  Guess: {guess.upper()}
  Misses: {', '.join(misses)}
  '''

def init_game():
    print(header())

    try:
        # dictionary = get_dictionary()
        dictionary = ["banana", "apples"]
    except:
        print('Error: failed to get data from dictionary.')

    random_word_index = randint(0, len(dictionary) - 1)
    word = dictionary[random_word_index]
    errors = 0
    max_errors = 5
    attempted_letters = []
    misses = []
    formatted_word = []

    for _ in range(0, len(word)):
      formatted_word.append("_")

    def handle_choose(guess):
        if guess not in attempted_letters:
            attempted_letters.append(guess)
            find_letter_word_position = index_of(word, guess)
            print(f'FIND: {find_letter_word_position}')
            if find_letter_word_position > -1:
                formatted_word[find_letter_word_position] = guess
            else:
                errors += 1
                misses.append(guess)

        return formatted_word

    while errors < max_errors:
        guess = input("Choose a letter: ")

        formatted_word = handle_choose(guess)

        print(draw_hangman(errors, scoreboard(
            formatted_word, guess, misses)))


init_game()
