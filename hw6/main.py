from hw6.fields import CharField
from hw6.fields import IntegerField
from hw6.simple_orm import Model
from hw6.simple_orm import SqliteDatabase

db = SqliteDatabase(":memory:")


class BaseModel(Model):
    class Meta:
        database = db


class Advert(BaseModel):
    title = CharField(max_length=180)
    price = IntegerField(min_value=0)

    def __str__(self):
        return f"{self.title} {self.price}"


if __name__ == "__main__":  # pragma: no cover
    db.connect()
    db.create_tables([Advert])

    Advert.create(title="iPhone X", price=100)

    adverts = Advert.select()
    assert adverts[0].title == "iPhone X"
    assert adverts[0].price == 100
