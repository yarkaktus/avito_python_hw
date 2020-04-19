import pytest

from hw3.one_hot_encoder import fit_transform


def test_empty_args():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty_list():
    assert fit_transform([]) == []


def test_nontstr_args():
    with pytest.raises(TypeError):
        fit_transform(1, 2, 3)


def test_simple_case():
    cities = ["Moscow", "New York", "Moscow", "London"]
    exp_transformed_cities = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_one_city():
    cities = ["Moscow"]
    exp_transformed_cities = [
        ("Moscow", [1]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_many_one_city():
    cities = ["Moscow", "Moscow", "Moscow", "Moscow", "Moscow"]
    exp_transformed_cities = [
        ("Moscow", [1]),
        ("Moscow", [1]),
        ("Moscow", [1]),
        ("Moscow", [1]),
        ("Moscow", [1]),
    ]
    assert fit_transform(cities) == exp_transformed_cities
