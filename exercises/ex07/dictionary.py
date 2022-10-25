"""Dictionaries!"""


def invert(x: dict[str, str]) -> dict[str, str]:
    """This function takes in a dictionary and inverts it."""
    new_dict = {}
    for key in x:
        if x[key] in new_dict:
            raise KeyError("Repeated KEYS")
        new_dict_value = key 
        new_dict_key = x[key] 
        new_dict[new_dict_key] = new_dict_value
    return new_dict


def favorite_color(x: dict[str, str]) -> str:
    """This function picks out the most reoccuring value in the dictionary and outputs it as a string."""
    empty_dict: dict[str, str] = {}
    empty_strr: str = ""
    i: int = 0 
    max: int = 0 
    for key in x:
        if x[key] in empty_dict:
            empty_dict[x[key]] += 1
        else:
            empty_dict[x[key]] = 1
    for key in empty_dict:
        i = empty_dict[key]
        if i > max:
            max = i 
            empty_strr = key 
    return empty_strr


def count(x: list[str]) -> dict[str, int]:
    """This function counts the number of of a certain value in the last and outputs the number of it in a dictionary."""
    counter: dict[str, int] = {}
    for item in x:
        if item not in counter:
            counter[item] = 0 
        counter[item] += 1 
    return counter
