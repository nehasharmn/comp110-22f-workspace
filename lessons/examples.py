def main():
    who: str = get_the_user()
    print(welcome_message(who))

def get_the_user() -> str:
    name: str = input("who are you?")
    return name
def welcome_message(name: str)-> str:
    return "Hi " + name


def area_of_rectangle(length,width):
    answer = length * width
    return answer