"""Examples of importing Python."""


from lessons import helpers

# Import names defined globally specific 
from lessons.helpers import THE_ANSWER, powerful 


def main() -> None: 
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer{helpers.THE_ANSWER}")
    print(powerful(2,6))
    print(THE_ANSWER)
if __name__ == "__main__":
    main()