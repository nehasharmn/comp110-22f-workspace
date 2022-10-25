"""EX05 - list Utility Functions <3!"""

__author__ = "730560669"

from exercises.ex05.utils import only_evens, concat, sub 


def test_only_evens_empty() -> None:
    """Tests the conditions when list is empty: edge case."""
    x_list: list[int] = []
    assert only_evens(x_list) == []


# use case
def test_only_evens_all_odds() -> None:
    """Tests the function when all elements in list are odd."""
    x_list: list[int] = [1, 1, 1]
    assert only_evens(x_list) == []


# use case 
def test_only_evens_only_one_even() -> None:
    """Tests the function when only one element is even."""
    x_list: list[int] = [1, 2, 3]
    assert only_evens(x_list) == [2]


# edge case 
def test_concat_empty() -> None:
    """Tests function when both lists are empty."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


# use case
def test_concat_one_list_longer() -> None:
    """Tests function when one list is longer than the other."""
    a: list[int] = [1, 2, 3, 4]
    b: list[int] = [2, 1]
    assert concat(a, b) == [1, 2, 3, 4, 2, 1]


# use case
def test_concat_one_list_empty() -> None:
    """Tests function when one list is empty."""
    a: list[int] = []
    b: list[int] = [2, 1]
    assert concat(a, b) == [2, 1]


# use case 
def test_concat_two_list_same() -> None:
    """Tests function when two lists are the same."""
    a: list[int] = [2, 1]
    b: list[int] = [2, 1]
    assert concat(a, b) == [2, 1, 2, 1]


def test_concat_two_list_same_length() -> None:
    """Tests function when two lists are the same length."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]


# edge case
def test_sub_empty() -> None: 
    """Tests function when the list is empty and indexes are 0."""
    a_list: list[int] = []
    assert sub(a_list, 0, 0) == []


# use case 
def test_sub_start_index_negative() -> None:
    """Tests the function when the start index is negative."""
    a_list: list[int] = [10, 20, 30, 40, 50]
    assert sub(a_list, -1, 4) == [10, 20, 30, 40]


# use case
def test_sub_end_index_greater() -> None:
    """Tests the function when the end index is greater then the length of the list."""
    a_list: list[int] = [10, 20, 30]
    assert sub(a_list, 1, 3) == [20, 30]