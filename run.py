import random
import string
import requests
from requests import request
response_API = requests.get("https://random-word-api.herokuapp.com/all")

def get_valid_word(response_API):
    word = random.choice(response_API)

    return word

def hangman():
    word = get_valid_word(response_API=)
    word_letter = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have',live,'lives left and you have used these letters: ' ' ' .join(used_letters))

        #What current word is (ie W-R D)
        word_list = [letter if letter in used_letters else - for letter in response_API]
        print('Current word: ', ''.join(word_list))
        user_letter = input('Gissa en bokstav: ').upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
                if used_letters in word_letters:
                word_letter.remove(used_letter)

                else:
                    lives = lives - 1 # takes away a life if wrong
                    print('Letter is not in the word, try again!')

        elif user_letter in used_letters:
        print('you have already used this letter! Please try again')
        else:
        print('invalid character. Please try again')
    
    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You have lost the game','the word was' response_API)
    print('You have guessed the word', response_API, ' well done!')

user_input = input('skriv något')
print(user_input)