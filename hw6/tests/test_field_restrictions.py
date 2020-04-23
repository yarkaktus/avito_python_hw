import pytest

from hw6.fields import CharField
from hw6.fields import IntegerField
from hw6.main import BaseModel
from hw6.main import db


def setup():
    db.connect()


def test_max_lenght_charfield():
    class Advert(BaseModel):
        title = CharField(max_length=1)
        price = IntegerField(min_value=0)

    with pytest.raises(ValueError) as e:
        Advert.create(title="very long title", price=10)
    assert str(e.value) == "length title must be less or equal 1"


def test_invalid_type_charfield():
    class Advert(BaseModel):
        title = CharField(max_length=100)
        price = IntegerField(min_value=100)

    with pytest.raises(ValueError) as e:
        Advert.create(title=100, price=10)
    assert str(e.value) == "title value must be str"


def test_min_value_integerfield():
    class Advert(BaseModel):
        title = CharField(max_length=100)
        price = IntegerField(min_value=100)

    with pytest.raises(ValueError) as e:
        Advert.create(title="title", price=10)
    assert str(e.value) == "price value must be more than 100"


def test_max_value_integerfield():
    class Advert(BaseModel):
        title = CharField(max_length=100)
        price = IntegerField(max_value=100)

    with pytest.raises(ValueError) as e:
        Advert.create(title="title", price=200)
    assert str(e.value) == "price value must be less than 100"


def test_invalid_type_integerfield():
    class Advert(BaseModel):
        title = CharField(max_length=100)
        price = IntegerField(min_value=100)

    with pytest.raises(ValueError) as e:
        Advert.create(title="title", price="string")
    assert str(e.value) == "price value must be int"


def test_invalid_model_attribute():
    class Advert(BaseModel):
        title = CharField(max_length=100)
        price = IntegerField(min_value=100)

    with pytest.raises(Exception) as e:
        Advert.create(title="title", price=200, bad_attribute="1")
    assert str(e.value) == "unknown field bad_attribute"
