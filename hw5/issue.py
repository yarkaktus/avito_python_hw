import keyword
from typing import Any

from hw5.color_style_codes import BackgroundColorCode
from hw5.color_style_codes import TextColorCode
from hw5.color_style_codes import TextStyleCode


class ColorizeMixin:
    """
    Миксин для цветного форматирования вывода
    """

    TEXT_COLOR_CODE = TextColorCode.BLACK
    TEXT_STYLE_CODE = TextStyleCode.BRIGHT
    BACKGROUND_COLOR_CODE = BackgroundColorCode.RED

    NORMILIZE_COLOR_TEMPLATE = "\033[0;0;0m"

    def __repr__(self) -> str:
        return "\033[{tsc};{tcc};{bcc}m{text}{normilized}".format(
            tsc=self.TEXT_STYLE_CODE,
            tcc=self.TEXT_COLOR_CODE,
            bcc=self.BACKGROUND_COLOR_CODE,
            text=super().__repr__(),
            normilized=self.NORMILIZE_COLOR_TEMPLATE,
        )


class Advert(object):
    """
    Класс для динамического создания атрибута классов из словаря.

    title - обязательный ключ словаря.
    """

    def __init__(self, data: dict, main_level=True):

        if main_level:
            if not isinstance(data, dict):
                raise ValueError("data must be instance of dict")

            if "title" not in data:
                raise ValueError("Can't find key 'title'")

            if "price" in data:
                price = data["price"]
                if not isinstance(price, (int, float)):
                    raise ValueError("price must be instance of float or int")

                if price < 0:
                    raise ValueError("price can't be less than 0")
            else:
                data["price"] = 0

        self.data = self.prepare_dict(data)
        self.main_level = main_level

    @classmethod
    def prepare_dict(cls, data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("data must be instance of dict")

        new_data = {}
        for key, value in data.items():
            if keyword.iskeyword(key):
                key += '_'

            if isinstance(value, dict):
                new_data[key] = cls.prepare_dict(value)
            else:
                new_data[key] = value
        return new_data

    def __getattr__(self, item: str) -> Any:
        if keyword.iskeyword(item):
            item += '_'

        if item not in self.data:
            raise AttributeError

        value = self.data[item]
        if isinstance(value, dict):
            return Advert(value, main_level=False)
        return value

    def __repr__(self) -> str:
        if self.main_level:
            return f"{self.title} | {self.price} ₽"
        return str(self.data)


class ColorizedAdvert(ColorizeMixin, Advert):
    pass


if __name__ == "__main__":  # pragma: no cover
    iphone_advert = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"],
        },
    }
    advert = Advert(iphone_advert)
    print(advert)

    dog_advert = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"},
    }
    color_advert = ColorizedAdvert(dog_advert)
    print(color_advert)
    print(getattr(color_advert, 'class'))
    print(getattr(color_advert, 'class_'))
    print(color_advert.location)

    color_advert.TEXT_COLOR_CODE = 36
    color_advert.TEXT_STYLE_CODE = 1
    color_advert.BACKGROUND_COLOR_CODE = 43
    print(color_advert)
