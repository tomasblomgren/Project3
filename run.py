"""
importing an API
"""
import random
import sys
import requests
WORDLIST = [None]


def get_world_list():
    """
    Generating a word from the API
    """
    print('Running get_world_list')
    global WORDLIST
    WORDLIST = requests.get("https://random-word-api.herokuapp.com/all").json()


def get_random_word():
    """
    Taking a word from the
    get_world_ list function and randomizing the outcome.
    While loop for excluding - and empty spaces and returning the variable word
    """
    print('Running get_random_word')
    # global WORDLIST
    word = random.choice(WORDLIST)
    while '-' in WORDLIST or ' ' in WORDLIST:
        word = random.choice(WORDLIST)
        print(word)
    return word


def hangman(words_list):
    """
    Generating messages and displaying the already guessed letters
    """
    global WORDLIST
    word = random.choice(WORDLIST)
    word_letter = list(WORDLIST)  # letter in the word
    guessed_letters = list()  # what the user has guessed
    word_letters = ''

    lives = 6
    guessed_letters = []

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(lives, 'lives left. these letters: ', ' ' .join(guessed_letters))

        # what current word is (ie W-R D)
        word_list = [letter if letter in guessed_letters else '-'
                     for letter in words_list]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Guess a letter: ')
        if guessed_letters in word - guessed_letters:
            if guessed_letters in word_letters:
                word_letter.remove(guessed_letters)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Letter is not in the word, try again!')

        elif user_letter in guessed_letters:
            print('you have already used this letter! Please try again')
        else:
            print('invalid character. Please try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'You have lost the game the word was {words_list}')
    else:
        print('You have guessed the word', words_list, 'well done!')


def main():
    """ Printing the word from API
    """
    user_input = (input, 'Write a letter!:')
    word = get_random_word
    hangman(WORDLIST)

    return word


if __name__ == '__main__':
    main()


def select_word(word):
    """
    Finding the word
    """
    return random.choice(word)


def print_secret_word(secret_word):
    """Printing the secret word to guess
    """
    print(" _ " * len(secret_word))


print("hello world!")
word = WORDLIST
secret_word = select_word(word)
print_secret_word(secret_word)


def get_hangman_stage(lives):
    """
    Adding stages in combination with lives
    as the game progresses you add a stage or you add a letter
    """
    max_attempts = 6
    stages = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]
    return stages[max_attempts - lives]


def is_guess_in_secret_word(guess, secret_word):
    guess = input("guess a letter!: ")
    if len(guess) > 1 or not guess.isalpha():
        print("only single letters are allowed, try again")
        SystemExit()
    else:
        if guess in secret_word:
            return True
        else:
            return False


print("Welcome to Hangman Deluxe! guess the word to win the game")
secret_word = select_word(word)
lives = 6
guessed_letters = []
guess = input("Guess a letter!: ")
guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

if guess_in_secret_word:
    if guess in word:
        print("you have already guessed that letter{}" .format(guess))
    else:
        print("Correct! {} is in the secret word".format(guess))
        guessed_letters += lives
else:
    print("No {} is not part of the word" .format(guess))
    guessed_letters -= lives

data_str = ("Enter your data here!: ")

print(word)

is_guess_in_secret_word(guess, secret_word)
