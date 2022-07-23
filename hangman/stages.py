
def get_hangman_stages(lives):
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



# print("Welcome to Hangman Deluxe! guess the word to win the game\n")
# secret_word = select_word(word)
#
# guessed_letters = []
# guess = input("Guess a letter!: ")
# guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)
#
# if guess_in_secret_word:
#     if guess in word:
#         print(
#             f"you have already guessed that letter{guessed_letters}" .format(guess))
#     else:
#         print("Correct! {} is in the secret word".format(guess))
#         guessed_letters += lives
# else:
#     print("No {} is not part of the word" .format(guess))
#     guessed_letters -= lives
#
# data_str = ("Enter your data here!: ")
#
# print(word)
#
#
# print(get_hangman_stage(lives))
