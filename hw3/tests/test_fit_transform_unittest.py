import unittest

from hw3.one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_empty_args(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_empty_list(self):
        self.assertEqual(fit_transform([]), [])

    def test_nontstr_args(self):
        with self.assertRaises(TypeError):
            fit_transform(1, 2, 3)

    def test_simple_case(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        exp_transformed_cities = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_one_city(self):
        cities = ["Moscow"]
        exp_transformed_cities = [
            ("Moscow", [1]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_many_one_city(self):
        cities = ["Moscow", "Moscow", "Moscow", "Moscow", "Moscow"]
        exp_transformed_cities = [
            ("Moscow", [1]),
            ("Moscow", [1]),
            ("Moscow", [1]),
            ("Moscow", [1]),
            ("Moscow", [1]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)
