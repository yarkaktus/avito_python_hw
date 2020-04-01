from hw4.hw import chunks


def test_size_eq_len():
    assert chunks(4, [1, 2, 3, 4]) == [(1, 2, 3, 4)]


def test_size_gt_len():
    assert chunks(5, [1, 2, 3, 4]) == [(1, 2, 3, 4)]


def test_size_eq_one():
    assert chunks(1, [1, 2, 3, 4]) == [(1,), (2,), (3,), (4,)]


def test_many_chunks():
    assert chunks(2, [1, 2, 3, 4, 5]) == [(1, 2), (3, 4), (5,)]
