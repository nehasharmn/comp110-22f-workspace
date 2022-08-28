"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I am thinking of a number between 1-5, what is it?")
guess: int = int(input( "What is your guess?"))

if guess == SECRET:
    print("you guessed correctly!!!")
    print("have a wonderful day :)")
else:
        print("sorry, you guessed incorrectly :(")
        print( "try running the program again")
if guess > SECRET:
            print("you guessed too high!")
else:
    print("you guessed too low")
print ("Game over.")