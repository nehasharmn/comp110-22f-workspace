"""EX03 - Structured Wordle <3"""

__author__ = "730560669"

def contains_char(search_2nd: str, single_character: str)-> bool:
    """this while loop takes a string of any length and matches a character to it's indicies using a declaration"""
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