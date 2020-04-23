import pytest

from hw5.issue import Advert
from hw5.issue import ColorizedAdvert

iphone_advert = {
    "title": "iPhone X",
    "price": 100,
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"],
    },
}

dog_advert = {
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    },
}


def test_bad_init_data():
    bad_types = [list, tuple, int, str, float]
    for bad_type in bad_types:
        with pytest.raises(ValueError) as e:
            Advert(bad_type())
        assert str(e.value) == "data must be instance of dict"


def test_without_title():
    advert_dict = {
        "something": 1,
    }
    with pytest.raises(ValueError) as e:
        Advert(advert_dict)
    assert str(e.value) == "Can't find key 'title'"


def test_default_price():
    advert_dict = {
        "something": 1,
        "title": "test title",
    }
    advert = Advert(advert_dict)
    assert advert.price == 0


def test_bad_attribute():
    advert_dict = {"something": 1, "title": "test title", "price": 200}
    with pytest.raises(AttributeError):
        advert = Advert(advert_dict)
        advert.bad_attr


def test_bad_price_type():
    bad_types = [list, tuple, dict, str]
    advert_dict = {
        "something": 1,
        "title": "test title",
    }
    for bad_type in bad_types:
        advert_dict["price"] = bad_type()
        with pytest.raises(ValueError) as e:
            Advert(advert_dict)
        assert str(e.value) == "price must be instance of float or int"


def test_good_price_type():
    good_types = [int, float]
    advert_dict = {
        "something": 1,
        "title": "test title",
    }
    for good_type in good_types:
        advert_dict["price"] = good_type()
        Advert(advert_dict)


def test_negative_price():
    bad_values = [-5, -5.5]
    advert_dict = {
        "something": 1,
        "title": "test title",
    }
    for bad_value in bad_values:
        advert_dict["price"] = bad_value
        with pytest.raises(ValueError) as e:
            Advert(advert_dict)
        assert str(e.value) == "price can't be less than 0"


def test_iphone_advert():
    advert = Advert(iphone_advert)
    assert advert.title == "iPhone X"
    assert advert.price == 100
    assert advert.location.address == "город Самара, улица Мориса Тореза, 50"
    assert advert.location.metro_stations == ["Спортивная", "Гагаринская"]


def test_data_with_keyword():
    advert = Advert(dog_advert)
    assert advert.class_ == "dogs"
    assert getattr(advert, "class") == "dogs"
    assert getattr(advert, "class_") == "dogs"


def test_set_price():
    advert = Advert(iphone_advert)
    assert advert.title == "iPhone X"
    assert advert.price == 100
    advert.price = 200
    assert advert.price == 200


def test_colorized_advert():
    advert = ColorizedAdvert(iphone_advert)
    DEFAULT_COLOR_TEMPLATE = "\033[1;30;41m"
    NORMILIZE_COLOR_TEMPLATE = "\033[0;0;0m"

    assert (
        repr(advert)
        == DEFAULT_COLOR_TEMPLATE + "iPhone X | 100 ₽" + NORMILIZE_COLOR_TEMPLATE
    )
