NoneType = type(None)


class BaseField:
    _field_db_type: str = None

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __str__(self):
        return f"{self.name} {self._field_db_type}"

    def __repr__(self):
        return self.__str__()

    def prepare_to_insert(self, instance) -> str:
        return str(instance.__dict__[self.name])

    @property
    def field_db_type(self):
        return self._field_db_type


class IntegerField(BaseField):
    _field_db_type = "int"

    def __init__(self, min_value: int = None, max_value: int = None):
        if not isinstance(min_value, (int, NoneType)):
            raise TypeError("max_value must be int")

        if not isinstance(max_value, (int, NoneType)):
            raise TypeError("max_value must be int")

        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} value must be int")

        if self.min_value is not None and self.min_value > value:
            raise ValueError(f"{self.name} value must be more than {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} value must be less than {self.max_value}")

        instance.__dict__[self.name] = value


class CharField(BaseField):
    _field_db_type = "varchar"

    def __init__(self, max_length: int):
        if not isinstance(max_length, int):
            raise TypeError("max_length must be int")
        self.max_length = max_length

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.name} value must be str")

        if len(value) > self.max_length:
            raise ValueError(
                f"length {self.name} must be less or equal {self.max_length}"
            )

        instance.__dict__[self.name] = value

    def prepare_to_insert(self, instance) -> str:
        return f"'{instance.__dict__[self.name]}'"

    @property
    def field_db_type(self) -> str:
        return self._field_db_type + f"({self.max_length})"
