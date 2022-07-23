"""
importing an API
"""
import os
import random
import time

import requests
from hangman import stage

WORDLIST = []


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
    global WORDLIST
    word = random.choice(WORDLIST)
    while '-' in word or ' ' in word:
        word = random.choice(WORDLIST)
        print(word)
    return word


def hangman():
    """
    Generating messages and displaying the already guessed letters
    """
    global WORDLIST
    chosen_word = 'gamer'  # get_random_word()
    word_letters = list(chosen_word)  # letter in the word
    guessed_letters = list()  # what the user has guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(lives, 'lives left. these letters: ', ' '.join(guessed_letters))

        # what current word is (ie W-R D)
        user_displayable_word = [
            letter if letter in guessed_letters else '-'
            for letter in chosen_word
        ]
        print('Current word: ', ''.join(user_displayable_word))

        user_letter = input('Guess a letter: ')
        user_letter = user_letter.lower()

        if user_letter.isnumeric() or user_letter in ['!', '@', '#', '$', '%', '^', '&']:
            print('invalid character. Please try again')
            continue

        if user_letter in guessed_letters:
            print('you have already used this letter! Please try again!')
            continue

        if user_letter not in word_letters:
            lives = lives - 1  # takes away a life if wrong
            print('Sorry, Letter is not present in the word, it cost a life!')

        if user_letter in word_letters:
            guessed_letters.append(user_letter)
            word_letters.remove(user_letter)

        print(stage(lives))
        time.sleep(2)
        os.system('clear')

        if guessed_letters == word_letters:
            break

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'You have lost the game the word was {chosen_word}')
    else:
        print(f'You have guessed the word', {chosen_word}, 'well done!')


def select_word(word):
    """
    Finding the word
    """
    return random.choice(word)


def print_secret_word(secret_word):
    """
    Printing the secret word to guess
    """
    # print(" _ " * len(secret_word))


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


def main():
    """ 
    Printing the word from API
    """
    # load the word list before commencing the game
    get_world_list()

    # get user input
    # user_input = (input, 'Write a letter!:')
    # word = get_random_word()
    print("Welcome to Hangman Deluxe! guess the word to win the game\n")
    hangman()


if __name__ == '__main__':
    main()
