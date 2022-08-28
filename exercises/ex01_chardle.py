"""EX01 - Chardle - A cute step toward Wordle."""

__author__= "730560669"

word_name: str = input("Enter a 5-character word: ")

single_character: str = input("Enter a single character: ")


if len(word_name) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
    
print("Searching for " + single_character + " in "+ word_name)

instances: int = 0

if single_character == word_name[0]:
    print(single_character + " found at index 0")
    instances= instances+1

if single_character == word_name[1]:
    print(single_character + " found at index 1")
    instances= instances+1
if single_character == word_name[2]:
    print(single_character + " found at index 2")
    instances= instances+1

if single_character == word_name[3]:
    print(single_character + " found at index 3")
    instances= instances+1

if single_character == word_name[4]:
    print(single_character + " found at index 4")
    instances= instances+1

# Counting Matching Indices
if instances == 0:
    print("No instances of " + single_character + " found in" + word_name)
if instances == 1:
    print("1 instance of " + single_character + " found in" + word_name)
if instances == 2:
    print("2 instances of " + single_character + " found in " + word_name)
if instances == 3:
    print("3 instances of " + single_character + " found in " + word_name)
if instances == 4:
    print("4 instances of " + single_character + " found in " + word_name)
if instances == 5:
    print("5 instances of " + single_character + " found in " + word_name)
    