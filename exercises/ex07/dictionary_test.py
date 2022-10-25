"""Dictionary Tests."""

__author__ = "730560669"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests the conditions when dictionary is empty: edge case."""
    x_dict: dict[str, str] = {}
    assert invert(x_dict) == {}


def test_invert_mutiple_keys_values() -> None:
    """Tests the conditions when dictionary is mutiple keys and values: use case."""
    x_dict: dict[str, str] = {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert(x_dict) == {'a': 'z', 'b': 'y', 'c': 'x'}


def test_invert_one_key_value() -> None:
    """Tests the conditions when dictionary is one key and value: edge case."""
    x_dict: dict[str, str] = {'neha': 'sharma'}
    assert invert(x_dict) == {'sharma': 'neha'}


def test_favorite_color_empty() -> None:
    """Tests the conditions when dictionary is one key and value: edge case."""
    x_dict: dict[str, str] = {}
    assert favorite_color(x_dict) == "" 


def test_favorite_color_two_similar_values() -> None:
    """Tests the conditions when dictionary has two same values: use case."""
    x_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(x_dict) == "blue"


def test_favorite_color_tie() -> None:
    """Tests the conditions when dictionary is has a tie in values: use case."""
    x_dict: dict[str, str] = {"Marc": "yellow", "Neha": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(x_dict) == "yellow"

    
def test_count_empty() -> None:
    """Tests the conditions when list is empty: edge case."""
    x_list: list[str] = []
    assert count(x_list) == {}


def test_count_mulitple_values() -> None:
    """Tests the conditions when list has mutiple values: use case."""
    x_list: list[str] = ['a', 'b', 'c', 'c']
    assert count(x_list) == {'a': 1, 'b': 1, 'c': 2}


def test_count_mulitple_values_same() -> None:
    """Tests the conditions when list has the same amount of values: use case."""
    x_list: list[str] = ['a', 'b', 'c', 'c', 'a', 'b']
    assert count(x_list) == {'a': 2, 'b': 2, 'c': 2}