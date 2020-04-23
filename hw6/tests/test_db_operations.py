from hw6.fields import CharField
from hw6.fields import IntegerField
from hw6.main import BaseModel
from hw6.main import db


class Advert(BaseModel):
    title = CharField(max_length=100)
    price = IntegerField(min_value=0)


def setup():
    db.connect()


def test_select():
    db.create_tables([Advert])
    Advert.create(title="iPhone X", price=100)

    adverts = Advert.select()
    assert adverts[0].title == "iPhone X"
    assert adverts[0].price == 100
