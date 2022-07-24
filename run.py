"""
importing hangman stages from the hangman file
"""
from hangman import stage
import os
import random
import time

import requests


WORDLIST = []


def get_world_list():
    """
    Generating a word from the API
    """

    global WORDLIST
    WORDLIST = requests.get("https://random-word-api.herokuapp.com/all").json()


def get_random_word():
    """
    Taking a word from the
    get_world_ list function and randomizing the outcome.
    While loop for excluding - and empty spaces
    returning the variable word
    Printing out rules
    """

    print('The number of - equals to the letters')
    print('Wrong guesses will take a life')
    print('When you guess wrong a stage will be added')
    print('Anything but letters is not a valid input')
    print('Trying to choose several letters will take a life')
    print('The letters are generated from an entire dictionary')
    print('hence the name Hangman Deluxe')
    print('Good luck!\n')

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
    chosen_word = get_random_word()  # get_random_word()
    word_letters = list(chosen_word)  # letter in the word
    guessed_letters = list()  # what the user has guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(lives, 'lives left. these letters have been used: ',
              ' '.join(guessed_letters))

        # what current word is (ie W-R D)
        user_displayable_word = [
            letter if letter in guessed_letters else '-'
            for letter in chosen_word
        ]
        print('Current word: ', ''.join(user_displayable_word))

        user_letter = input('Guess a letter: ')
        user_letter = user_letter.lower()

        if user_letter.isnumeric() or user_letter in ['!', '@', ]:
            print('invalid character. Please try again')
            continue

        if user_letter in guessed_letters:
            print('you have already used this letter! Please try again!')
            continue

        if user_letter not in word_letters:
            lives = lives - 1  # takes away a life if wrong
            print('Sorry, Letter is not in the word, it cost a life!')

        if user_letter in word_letters:
            guessed_letters.append(user_letter)
            word_letters.remove(user_letter)

        print(stage(lives))
        time.sleep(5)
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
    # loads the word list before commencing the game
    get_world_list()

    # get user input
    # user_input = (input, 'Write a letter!:')
    # word = get_random_word()
    print("Welcome to Hangman Deluxe! Guess the word to win the game!\n")
    hangman()


if __name__ == '__main__':
    main()
