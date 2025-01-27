"""EX02 - One-Shot Wordle - LOOPS!!."""

__author__ = "730560669"

# declared variables 
secret_word: str = "python"
secret_word_length: int = (len(secret_word))
guess_word: str = input(f"What is your {secret_word_length}-letter word? ")
guess_word_length: int = len(guess_word)

guess_string = ""  # variable for emoji boxes 
# emoji boxes unicodes
WHITE: str = "\U00002B1C"
GREEN: str = "\U0001F7E9"
YELLOW: str = "\U0001F7E8"

# indexes for both while loops
i: int = 0 

j: int = 0

# boolean expression for yellow box 
yellow_character = False

# loop sequence to get guess
while guess_word_length != secret_word_length:
    guess_word = input(f"That was not {secret_word_length} letters! Try again:")
    guess_word_length = len(guess_word)

# main while loop that gives the emoji boxes 
while i < secret_word_length:
    if guess_word[i] == secret_word[i]:
        guess_string += GREEN
    i = i + 1
print(guess_string)

# tells reader if guess is correct
if guess_word != secret_word:
    print("Not quite. Play again soon! ")
if guess_word == secret_word:
    print("Woo! You got it!")