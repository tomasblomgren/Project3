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

    #getting user input
    user_letter = input('Gissa en bokstav: ').upper()
    if used_letter in alphabet - used_letters:
        used_letters.add(used_letter)
        if used_letters in word_letters:
            word_letter.remove(used_letter)
    elif user_letter in used_letters:
        print('you have already used this letter! Please try again')
    else:
        ('invalid character. Please try again')

user_input = input('skriv något')
print(user_input)