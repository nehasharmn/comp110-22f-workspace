"""EX03 - Structured Wordle <3"""

__author__ = "730560669"

# contains_char function definition
def contains_char(search_2nd: str, single_character: str)-> bool:
    """this while loop takes a string of any length and matches a single character string to it's indicies using a declaration"""
    assert len(single_character) == 1 
    i: int = 0
    j: int = 0
    single_character_1 = False
    while i < len(search_2nd):
        if search_2nd[i] == single_character[i]:
            return True 
        else:
            while single_character_1 is False and j < len(search_2nd):
                if single_character [i] == search_2nd[j]:
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
def emojified(guess: str, secret: str)-> str:
    assert len(guess) == len(secret)
    WHITE: str = "\U00002B1C"
    GREEN: str = "\U0001F7E9"
    YELLOW: str = "\U0001F7E8"
    guess_string = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            guess_string = guess_string + GREEN
            return guess_string
    


