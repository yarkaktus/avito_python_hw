import sqlite3
from typing import List
from typing import Type

from hw6.fields import BaseField


class Model:
    def __init__(self, **fields):
        field_names = [mf.name for mf in self.fields()]

        for field, value in fields.items():
            if field not in field_names:
                raise AttributeError(f"unknown field {field}")
            setattr(self, field, value)

    @classmethod
    def create(cls, **fields) -> "Model":
        conn = cls.Meta.database.conn
        model_name = cls.__name__
        model = cls(**fields)

        field_values = []
        model_fields = model.fields()

        for model_field in model_fields:
            field_values.append(model_field.prepare_to_insert(model))

        sql_values = ",".join(field_values)

        sql_query = f"""
            INSERT INTO {model_name}
                 VALUES({sql_values})
        """
        conn.execute(sql_query)
        conn.commit()

        return model

    @classmethod
    def select(cls):
        conn = cls.Meta.database.conn
        model_name = cls.__name__

        sql_query = f"""
            SELECT * FROM {model_name}
        """
        cur = conn.cursor()

        cur.execute(sql_query)
        rows = cur.fetchall()
        result = []
        names = [description[0] for description in cur.description]
        for row in rows:
            model_obj = cls()
            for name, value in zip(names, row):
                model_obj.__setattr__(name, value)
            result.append(model_obj)
        return result

    @classmethod
    def fields(cls) -> List[BaseField]:
        return [
            cls.__dict__[item]
            for item in cls.__dict__
            if isinstance(cls.__dict__[item], BaseField)
        ]


class SqliteDatabase:
    def __init__(self, database: str) -> None:
        if database == ":memory:":
            self.database = database
        else:
            self.database = database

    def connect(self):
        self.conn = sqlite3.connect(self.database)

    def create_table(self, model: Type[Model]):
        model_name = model.__name__

        declare_fields = []
        for field in model.fields():
            declare_fields.append(f" {field.name} {field.field_db_type} ")

        sql_declare_fields = ",".join(declare_fields)
        sql_query = f"""
                CREATE TABLE {model_name}
                ({sql_declare_fields})
        """

        self.conn.execute(sql_query)

    def create_tables(self, models: List[Type[Model]]) -> None:
        for model in models:
            self.create_table(model)
