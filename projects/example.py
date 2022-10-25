"""Welcome to buzzfeed quiz <3!"""

__author__ = "730560669"

# global variables
player: str = ""
points: int = 0 
# NAMED_CONSTANTS
EYES: str = "\U0001F440"
BOWL: str = "\U0001F963"
RED_FLAG: str = "\U0001F6A9"
KIWI: str = "\U0001F95D"
BANANA: str = "\U0001F34C"
STRAWBERRY: str = "\U0001F353"
BLUEBERRY: str = "\U0001FAD0"
WHEAT: str = "\U0001F33E"
HONEY: str = "\U0001F36F"
CHOCOLATE: str = "\U0001F36B"
PEANUT: str = "\U0001F95C"
PEACE: str = "\U0000270C"
HANG_LOOSE: str = "\U0001F919"
PRINCESS: str = "\U0001F478"
MONKEY: str = "\U0001F649"
JUGGLE: str = "\U0001F939"
STAR: str = "\U00002B50"
MEMO: str = "\U0001F4DD"
TONGUE: str = "\U0001F61B"
CART: str = "\U0001F938"
# FUNCTION DEFINITIONS


def greet() -> None:
    """Greets the Player and prompts them for their name."""
    global player 
    print("-------------------------------------------------------------------------------------------------------")
    player = input(f"|{EYES} Build an acai bowl {BOWL} and I'll tell you what freshman dorm you would most likely live in at UNC {EYES}|\n-------------------------------------------------------------------------------------------------------\n What is your name?: ")


def one_question() -> str:
    """A mini quiz that prompts the user to pick their favorite acai base."""
    global points 
    # Q1 
    v = True 
    answer_q1 = input(f"Pick your base:{CART}\n A: Classic Acai\n B: Pitaya\n C: Green\n D: Blue Magic\n")
    while v is True:
        import random 
        if answer_q1 == "a":
            points = random.randint(1, 4)
            v = False 
        if answer_q1 == "b":
            points = random.randint(1, 4)
            v = False 
        if answer_q1 == "c":
            points = random.randint(1, 4)
            v = False 
        if answer_q1 == "d":
            points = random.randint(1, 4)
            v = False 
        if answer_q1 != "a" != answer_q1 != "b" != answer_q1 != "c" != answer_q1 != "d":
            answer_q1 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 

            
def question_1() -> str:
    """Question one of the quiz...ask user to pick their favorite base."""
    global points 
    # Q1 
    v = True 
    answer_q1 = input(f"Pick your base:{TONGUE}\n A: Classic Acai\n B: Pitaya\n C: Green\n D: Blue Magic\n")
    while v is True:
        if answer_q1 == "a":
            points = 1
            v = False 
        if answer_q1 == "b":
            points = 2
            v = False 
        if answer_q1 == "c":
            points = 3
            v = False 
        if answer_q1 == "d":
            points = 4
            v = False 
        if answer_q1 != "a" != answer_q1 != "b" != answer_q1 != "c" != answer_q1 != "d":
            answer_q1 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "Next question!"
    return prompt


def question_2(x: int) -> int:
    """Question 2 of the quiz...asks user if they want granola."""
    # Q2 
    v = True 
    answer_q2 = input(f"Granola?{WHEAT}\n A: YES\n B: noo\n")
    while v is True:
        if answer_q2 == "a":
            x = x + 1
            v = False 
        if answer_q2 == "b":
            x = x + 2
            v = False 
        if answer_q2 != "a" != answer_q2 != "b":
            answer_q2 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
        print(f"Nice! {player}")
        return x


def question_3() -> str:
    """Question 3 of the quiz...asks user their first fruit topping."""
    global points 
    # Q3 
    v = True 
    answer_q3 = input(f"What is your first fruit topping?\n A: Bananas{BANANA}\n B: Blueberries{BLUEBERRY}\n C: Strawberries{STRAWBERRY}\n D: Kiwi{KIWI}\n")
    while v is True:
        if answer_q3 == "a":
            points = points + 1
            v = False
        if answer_q3 == "b":
            points = points + 2
            v = False
        if answer_q3 == "c":
            points = points + 3
            v = False
        if answer_q3 == "d":
            points = points + 4
            v = False
        if answer_q3 != "a" != answer_q3 != "b" != answer_q3 != "c" != answer_q3 != "d":
            answer_q3 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "Cool!"
    return prompt


def question_4() -> str:
    """Question 4 of the quiz...asks user for their second fruit topping."""
    global points 
    # Q4 
    v = True
    answer_q4 = input(f"What is your second fruit topping?\n A: Bananas{BANANA}\n B: Blueberries{BLUEBERRY}\n C: Strawberries{STRAWBERRY}\n D: Kiwi{KIWI}\n")
    while v is True:
        if answer_q4 == "a":
            points = points + 1
            v = False
        if answer_q4 == "b":
            points = points + 2
            v = False
        if answer_q4 == "c":
            points = points + 3
            v = False
        if answer_q4 == "d":
            points = points + 4
            v = False
        if answer_q4 != "a" != answer_q4 != "b" != answer_q4 != "c" != answer_q4 != "d":
            answer_q4 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "Awesome!"
    return prompt


def question_5() -> str:
    """Question 5 of the quiz...asks user to choose a nutbutter."""
    global points 
    # Q5
    v = True 
    answer_q5 = input(f"Choose a nut butter:{TONGUE}\n A: Nutella{CHOCOLATE}\n B: Peanut Butter{PEANUT}\n C: Almond Butter\n D: Cashew Butter\n")
    while v is True:
        if answer_q5 == "a":
            points = points + 1
            v = False 
        if answer_q5 == "b":
            points = points + 2
            v = False
        if answer_q5 == "c":
            points = points + 3
            v = False
        if answer_q5 == "d":
            points = points + 4
            v = False
        if answer_q5 != "a" != answer_q5 != "b" != answer_q5 != "c" != answer_q5 != "d":
            answer_q5 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "YUM!"
    return prompt


def question_6() -> str:
    """Question 6 of the quiz...asks user if they want honey."""
    global points 
    # Q6 
    v = True 
    answer_q6 = input(f"Honey on top?{HONEY}\n A: yes\n B: no\n")
    while v is True:
        if answer_q6 == "a":
            points = points + 1
            v = False 
        if answer_q6 == "b":
            points = points + 2
            v = False 
        if answer_q6 != "a" != answer_q6 != "b":
            answer_q6 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "One more question!"
    return prompt


def question_7() -> str:
    """Last question of quiz...asks user for a fun add on..."""
    global points 
    # Q7 
    v = True
    answer_q7 = input(f"Pick one fun add-on?{TONGUE}{CART}\n A: Coconut Flakes\n B: Flax Seeds\n C: Pumpkin Seeds\n D: Hemp Hearts\n")
    while v is True:
        if answer_q7 == "a":
            points = points + 1
            v = False
        if answer_q7 == "b":
            points = points + 2
            v = False
        if answer_q7 == "c":
            points = points + 3
            v = False
        if answer_q7 == "d":
            points = points + 4
            v = False
        if answer_q7 != "a" != answer_q7 != "b" != answer_q7 != "c" != answer_q7 != "d":
            answer_q7 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "On to the reveal!"
    return prompt


def main() -> None:
    """Entrypoint of game and game loop."""
    global player 
    global points
    greet()
    starting_the_experience = True 
    v = True 
    while starting_the_experience is True:
        print(f"{player} to answer the questions, type your response in lowercase letters when asked!")
        three_options = input(f"You have 3 options. Choose one:\n A: Leave the quiz{STAR}\n B: Start the quiz {STAR}\n C: Do the one question quiz instead!{STAR}\n")
        while v is True:
            if three_options == "a":
                v = False
                starting_the_experience = False
                print(f"Goodbye, {player}! {PEACE}")
                print(f"You had {points} points.") 
                quit()
            if three_options == "c": 
                print(f"Mini QUIZ TIME!!{MEMO}")
                one_question()
            if points == 1:
                print(f"You love a basic acai bowl...Granville {PRINCESS}")
            if points == 2:
                print(F"You keep it simple and classy...a scampus(south campus) dweller {HANG_LOOSE}")
            if points == 3:
                print(F"You're complicated...North Campus {MONKEY}")
            if points == 4:
                print(f"You like to juggle a lot at once...Cobb {JUGGLE}")    
            if three_options == "b":
                print("Lets Start!")
                v = False 
                question_1()
                question_2(points)
                question_3()
                question_4()
                question_5()
                question_6()
                question_7()
                if 6 <= points < 10:
                    print(f"You love a basic acai bowl...Granville {PRINCESS}")
                if 10 <= points < 14:
                    print(f"You keep it simple and classy...a scampus(south campus) dweller {HANG_LOOSE}")
                if 14 <= points < 18:
                    print(f"You're complicated...North Campus {MONKEY}")
                if 18 <= points < 25:
                    print(f"You like to juggle a lot at once...Cobb {JUGGLE}")
            x = input("Do you want to play again?: ")
            if x == "yes":
                v = False
                print(f"You had {points} points throughout the game which determined your campus!")
                main()
            else:
                print(f"You had {points} points throughout the game which determined your campus! Bye {PEACE}")
            v = False 
            starting_the_experience = False
    

if __name__ == "__main__":
    main()