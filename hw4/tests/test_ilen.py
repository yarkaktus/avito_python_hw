from hw4.hw import ilen


def test_list():
    assert ilen([]) == 0
    assert ilen([1, 2, 3]) == 3


def test_range():
    assert ilen(range(0)) == 0
    assert ilen(range(3)) == 3


def test_tuple():
    assert ilen(tuple()) == 0
    assert ilen((1, 2, 3)) == 3


def test_set():
    assert ilen({}) == 0
    assert ilen({1, 2, 3}) == 3


def test_str():
    assert ilen("") == 0
    assert ilen("123") == 3


def test_dict():
    assert ilen(dict()) == 0
    assert ilen(dict({"1": 1, "2": 2, "3": 3})) == 3
