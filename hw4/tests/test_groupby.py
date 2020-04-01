from hw4.hw import groupby


def test_groupby_gender():
    users = [
        {'gender': 'female', 'age': 23},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21}
    ]
    result = {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    assert groupby('gender', users) == result


def test_groupby_male():
    users = [
        {'gender': 'female', 'age': 23},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21}
    ]
    result = {
        23: [{'gender': 'female', 'age': 23}],
        20: [{'gender': 'male', 'age': 20}],
        21: [{'gender': 'female', 'age': 21}]
    }
    assert groupby('age', users) == result
