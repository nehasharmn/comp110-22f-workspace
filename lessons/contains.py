"""an example of a list utility algorithim"""

# name: contains
# function wih 2 parameters:
# needle - what we're searching for 
# haystack - what we're searching through 
# return type: bool 
# start from first index
# loop through each index of list 
#       test if equal to needle 
            # Yes! Return True
#           return false 
def contains (needle: str, haystack: list[str]) -> bool:
    i: int = 0 
    while i < len(haystack):
       if haystack[i] == needle:
        return True   
    i += 1 


