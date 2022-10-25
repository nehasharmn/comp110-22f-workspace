"""EX03 - Structured Wordle <3!"""

__author__ = "730560669"

print("hello")
def contains_char(search_2nd: str, single_character: str) -> bool: 
    """This while loop takes a string of any length and matches a single character string to it's indicies using a declaration."""
    assert len(single_character) == 1 
    i: int = 0
    j: int = 0
    single_character_1 = False
    while i < len(search_2nd):
        if search_2nd[i] == single_character[i]:
            return True 
        else:
            while single_character_1 is False and j < len(search_2nd):
                if single_character[i] == search_2nd[j]:
                    single_character_1 = True 
                j = j + 1
            if single_character_1 is True:
                return True 
            else:
                single_character_1 = False
                i = 1 + i
                j = 0  
                return False
                
print() 


# emojified function definition 
def emojified(guess: str, secret: str) -> str:
    """Codifies the guess word to compare the correct indicies of the secret word... asks user for a guess and secret -> outputs emojis based on matching indicies."""
    assert len(guess) == len(secret)
    WHITE: str = "\U00002B1C"
    GREEN: str = "\U0001F7E9"
    YELLOW: str = "\U0001F7E8"
    guess_string = ""
    i = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            guess_string += GREEN
        elif contains_char(secret, guess[i]) is True:
            guess_string += YELLOW
        else:
            guess_string += WHITE
        i = i + 1
    return guess_string


print()


def input_guess(expected_length: int) -> str: 
    """This function def uses an integer and calls the user to enter a word the length of that integer and keeps calling the user until they do."""
    guess_word: str = input(f"Enter a {expected_length} character word:")
    while len(guess_word) != expected_length:
        guess_word = input(f"That was not {expected_length} chars! Try again:")
    return guess_word


print()

 
def main() -> None: 
    """The enterypoint of the program and main game loop."""
    secret = "codes"
    turn: int = 1  
    while turn <= 6:
        print(f"===Turn {turn}/6===")
        guess = input_guess(len(secret)) 
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 7
        else:
            turn = turn + 1 
    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()