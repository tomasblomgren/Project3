"""
importing an API
"""
import random
import string
import requests


def get_world_list():
    return requests.get("https://random-word-api.herokuapp.com/all").json()


def get_valid_word():
    word = random.choice(words_list)
    while '-' in words_list or ' ' in words_list:
        word = random.choice(words_list)

    return word


def hangman(words_list):
    word = get_valid_word()
    word_letter = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    word_letters = ''

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '
              .join(used_letters))

        # what current word is (ie W-R D)
        word_list = [letter if letter in used_letters else '-'
                     for letter in words_list]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letters in word_letters:
                word_letter.remove(used_letter)

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


if __name__ == '__main__':
    main()
