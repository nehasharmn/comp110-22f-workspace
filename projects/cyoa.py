"""Welcome to buzzfeed quiz <3"""

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
# FUNCTION DEFINITIONS
def greet() -> None:
    global player 
    print("-------------------------------------------------------------------------------------------------------")
    player = input(f"|{EYES} Build an acai bowl {BOWL} and I'll tell you what freshman dorm you would most likely live in at UNC {EYES}|\n-------------------------------------------------------------------------------------------------------\n What is your name?: ")


def one_question() -> str:
    global points 
    # Q1 
    v = True 
    answer_q1 = input("Pick your base:\n A: Classic Acai\n B: Pitaya\n C: Green\n D: Blue Magic\n")
    while v is True:
        import random 
        if answer_q1 == "a":
            points = random.randint(1,4)
            v = False 
        if answer_q1 == "b":
            points = random.randint(1,4)
            v = False 
        if  answer_q1 == "c":
            points = random.randint(1,4)
            v = False 
        if  answer_q1 == "d":
            points = random.randint(1,4)
            v = False 
        if answer_q1 != "a" != answer_q1 != "b" != answer_q1 != "c" != answer_q1 != "d":
            answer_q1 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 

            
def question_1() -> str:
    global points 
    # Q1 
    v = True 
    answer_q1 = input("Pick your base:\n A: Classic Acai\n B: Pitaya\n C: Green\n D: Blue Magic\n")
    while v is True:
        if answer_q1 == "a":
            points = 1
            v = False 
        if answer_q1 == "b":
            points = 2
            v = False 
        if  answer_q1 == "c":
            points = 3
            v = False 
        if  answer_q1 == "d":
            points = 4
            v = False 
        if answer_q1 != "a" != answer_q1 != "b" != answer_q1 != "c" != answer_q1 != "d":
            answer_q1 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
    prompt = "Next question!"
    return prompt


def question_2(x: int) -> int:
    # Q2 
    v = True 
    answer_q2 = input(f"Granola?{WHEAT}\n A: YES\n B: noo\n")
    while v is True:
        if answer_q2 == "a":
            x = x + 1
            v = False 
        if answer_q2 == "b":
            x = x + 2
            V = False 
        if answer_q2 != "a" != answer_q2 != "b":
            answer_q2 = input(f"{RED_FLAG} invalid input! try again: ")
            v = True 
        print(f"Nice! {player}")
        return x


def question_3() -> str:
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
    global points 
    # Q5
    v = True 
    answer_q5 = input(f"Choose a nut butter:\n A: Nutella{CHOCOLATE}\n B: Peanut Butter{PEANUT}\n C: Almond Butter\n D: Cashew Butter\n")
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
    global points 
    # Q7 
    v = True
    answer_q7 = input("Pick one fun add-on?\n A: Coconut Flakes\n B: Flax Seeds\n C: Pumpkin Seeds\n D: Hemp Hearts\n")
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
    global player 
    global points
    i = 0
    if i < 1:
        print(greet())
    i += 1
    starting_the_experience = True 
    v = True 
    while starting_the_experience is True:
        print(f"{player} to answer the questions, type your response in lowercase letters when asked!")
        three_options = input("You have 3 options. Choose one:\n A: Leave the quiz\n B: Start the quiz\n C: Do the one question quiz instead!\n")
        while v is True:
            if three_options == "a":
                v = False
                starting_the_experience = False
                print(f"Goodbye, {player}!")
                print(f"You had {points} points.") 
                quit()
            if three_options == "c": 
                print("Mini QUIZ TIME!!")
                one_question()
                if points == 1:
                        print("You love a basic acai bowl...Granville")
                if points == 2:
                        print ("You keep it simple and classy...a scampus(south campus) dweller")
                if points == 3:
                        print("You're complicated...North Campus")
                if points == 4:
                        print("You like to juggle a lot at once...Cobb")    
            if three_options == "b":
                print("Lets Start!")
                v = False 
                i = 0 
                if i < 1:
                    question_1()
                i += 1 
                i = 0 
                if i < 1:
                    (question_2(points))
                i += 1 
                i = 0 
                if i < 1:
                    question_3()
                i = 0 
                if i < 1:
                    question_4()
                i += 1
                i = 0 
                if i < 1:
                    question_5()
                i += 1
                i = 0 
                if i < 1:
                    question_6()
                i += 1
                i = 0 
                if i < 1:
                    question_7()
                i += 1
                if 6 <= points < 10:
                    print("You love a basic acai bowl...Granville")
                if 10 <= points < 14:
                    print ("You keep it simple and classy...a scampus(south campus) dweller")
                if 14 <= points < 18:
                    print("You're complicated...North Campus")
                if 18 <= points < 25:
                    print("You like to juggle a lot at once...Cobb")
            x = input("Do you want to play again?: ")
            if x == "yes":
                v = False
                print(f"You had {points} points throughout the game which determined your campus!")
                main()
            else:
                print(f"You had {points} points throughout the game which determined your campus!")
            v = False 
            starting_the_experience = False
    

if __name__ == "__main__":
    main()