from hw4.hw import distinct


def test_blank_list():
    assert distinct([]) == []


def test_simple_list():
    assert distinct([1, 2, 3]) == [1, 2, 3]


def test_list_with_many_same_one_elem():
    assert distinct([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]


def test_list_with_many_elem():
    assert distinct([1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
