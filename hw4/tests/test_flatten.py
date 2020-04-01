from hw4.hw import flatten


def test_blank_list():
    assert flatten([]) == []


def test_simple_list():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_nested_list():
    assert flatten([1, 2, 3, [4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, 2, 3, [4, [5, [6]]]]) == [1, 2, 3, 4, 5, 6]
