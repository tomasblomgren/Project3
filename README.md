## Hangman Deluxe
This hangman game is run through a terminal in Heroku. 
This game is made for someone who wants to pass some spare time
The elementary school classic written in python and displayed in the terminal is a well known game, Also surprisingly useful for learning new words and increasing your vocabulary. The word generated is taken from an entire dictionary of 170000 words so the room for learning is immense.  

## How to play
The user will try to guess the secret word before their 6 lives/attempts run out. Each faulty guess will take one life and add to the hangman structure. The objective is to guess the word before your lives run out. Your word will be hidden but the amount of letters will correspond with a - sign for each letter in the word. The words are generated through an API connected to an entire dictionary, hence the name Hangman Deluxe. 

## Features

- Randomly generated words from a dictionary API
- Hidden letters which will reveal as the game progresses 
- Display of the hangman structure correlated to the players lives
- Messages displayed such as "sorry the letter was not in the word. it costs a life"
- You cannot guess numbers or other symbols such as @ and !

## Feature ideas

- Adding a difficulty setting to increase or decrease lives
- Adding a hint function
- Adding a explanation when guessing the word right(this word means ...)
- Allow player versus player mode to challenge another person
- Allow your score to be added to a universal scoreboard

## Technologies used

- Python version 3.8.11
- Heroku.com for deployment

## Testing

### PEP 8 validator testing

- PEP8 python validator was used for this project
- There are no errors returned from PEP8 validator!

## Further Testing 

- The functions where all called separately to ensure that they are working as intended
- The game was tested by friends and family who are not familiar with coding to get a geniune user experience. The feedback was that it will be improved with the ideas featured in the Feature ideas section but that it was fun due to the fact that there are alot of words
- 

## First time visitor goals

- As a first time visitor the goal is to be able to figure out hangman if you've never played it before. It should be crystal clear to the user what to do and how to win without having to do research on another platform. 
- The user should also be able to learn some new words based on the vast source given through the dictionary


## Unfixed bugs

- There are not unfixed bugs in this project!

## Deployment

### Heroku

- I have deployed this project through Heroku
-
-
-

The live link can be found here: 

## Credits

### Content

- The project has been inspired by: https://www.youtube.com/watch?v=cJJTnI22IF8 and code snippets has been taken and implemented in the finished project under line 35 (def hangman)
- The rules has been inspired by: https://codefather.tech/blog/hangman-game-python/
- ideas for creating the game inspired by: https://www.youtube.com/watch?v=m4nEnsavl6w
- W3Schools used for updating and learning methods in python
- 

## Acknowledgements 

- My mentor at code institute
- The tutoring support at Code institute

