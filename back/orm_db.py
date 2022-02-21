
from peewee import *

conn = MySQLDatabase(database='mcgriefdb', username='root',
                     password='Uruk-hai_berserk1', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    user_id = AutoField(column_name='id')
    username = CharField(column_name='username', max_length=20)
    email = CharField(column_name='email', max_length=50)
    password = CharField(column_name='password', max_length=30)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class Meta:
    table_name = 'users'
