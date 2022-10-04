"""EX04 - utils <3!"""

__author__ = "730560669"


def all(list_x: list[int], single_int: int) -> bool:
    """Function to find one integer to match all in a list."""
    i: int = 0
    if list_x == list():
        return False 
    while i < len(list_x):
        if single_int != list_x[i]:
            return False 
        elif list_x[i] == single_int:
            i = i + 1 
    return True 

    
def max(list_y: list[int]) -> int:
    """Function that when given a list of integers it returns the largest number in the list."""
    if len(list_y) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_number: int = -9999999999
    while i < len(list_y): 
        if max_number < list_y[i]:
            max_number = list_y[i]
        i = i + 1 
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Function when given two lists of integers it will return True if every element in each list is the same."""
    if len(list_1) != len(list_2):
        return False 
    i: int = 0 
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i = i + 1 
    return True 

