"""
importing an API
"""
import random
import string
import requests

WORDLIST = []


def get_world_list():
    global WORDLIST
    WORDLIST = requests.get("https://random-word-api.herokuapp.com/all").json()


def get_random_word():
    global WORDLIST
    word = random.choice(WORDLIST)
    while '-' in WORDLIST or ' ' in WORDLIST:
        word = random.choice(WORDLIST)

    return word


def hangman(words_list):
    word = get_random_word()

    word_letter = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
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

        user_letter = input('Guess a letter: ').upper()
        if guessed_letters in alphabet - guessed_letters:
            used_letters.add(guessed_letters)
            if used_letters in word_letters:
                word_letter.remove(guessed_letters)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Letter is not in the word, try again!')

        elif user_letter in used_letters:
            print('you have already used this letter! Please try again')
        else:
            print('invalid character. Please try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'You have lost the game the word was {words_list}')
    else:
        print('You have guessed the word', words_list, 'well done!')


def main():
    """something
    """
    # user_input = input('write something')
    # print(user_input)
    words_list = get_world_list()
    hangman(words_list)

    return(words_list)


if __name__ == '__main__':
    main()
