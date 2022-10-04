

from exercises.ex05.utils import only_evens

# edge case
def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


# use case
def test_only_evens_all_odds() -> None:
    xs: list[int] = [1,1,1]
    assert only_evens(xs) == []


# use case 
def test_only_evens_only_one_even() -> None:
    xs: list[int] = [1,2,3]
    assert only_evens(xs) == [2]

from exercises.ex05.utils import concat
# edge case 
def test_concat_empty()-> None:
    xs: list [int] = []
    bs: list [int] = []
    assert concat(xs,bs) == []

# use case
def test_concat_one_list_longer() -> None:
    xs: list [int] = [1,2,3,4]
    bs: list [int] = [2,1]
    assert concat(xs,bs) == [1,2,3,4,2,1]

# use case
def test_concat_one_list_empty() -> None:
    xs: list [int] = []
    bs: list [int] = [2,1]
    assert concat(xs,bs) == [2,1]

from lessons.help_pt3 import sub 

def test_sub_empty() -> None: 
    a_list: list[int] = []
    assert sub(a_list, 0, 0) == []

def test_sub_start_index_negative() -> None:
    a_list: list [int] = [10,20,30,40,50]
    assert sub(a_list, -1, 4) == [10,20,30,40]

def test_sub_end_index_greater() -> None:
    a_list: list[int] = [10,20,30]
    assert sub(a_list, 1, 3) == [20,30]