from peewee import *

data_base = SqliteDatabase('gicar')


class Esquinas(Model):
    nodo = CharField
    way = CharField

    class Meta:
        database = data_base


def create_data_base():
    data_base.connect()
    data_base.create_table(Esquinas)
