from hw4.hw import first


def test_list():
    assert first([]) is None
    assert first([1, 2, 3]) == 1


def test_range():
    assert first(range(0)) is None
    assert first(range(3)) == 0


def test_tuple():
    assert first(tuple()) is None
    assert first((1, 2, 3)) == 1


def test_set():
    assert first({}) is None
    assert first({1, 2, 3}) == 1


def test_str():
    assert first("") is None
    assert first("123") == "1"


def test_dict():
    assert first(dict()) is None
    assert first(dict({"1": 1, "2": 2, "3": 3})) == "1"
