from hw4.hw import last


def test_list():
    assert last([]) is None
    assert last([1, 2, 3]) == 3


def test_range():
    assert last(range(0)) is None
    assert last(range(3)) == 2


def test_tuple():
    assert last(tuple()) is None
    assert last((1, 2, 3)) == 3


def test_set():
    assert last({}) is None
    assert last({1, 2, 3}) == 3


def test_str():
    assert last("") is None
    assert last("123") == "3"


def test_dict():
    assert last(dict()) is None
    assert last(dict({"1": 1, "2": 2, "3": 3})) == "3"
