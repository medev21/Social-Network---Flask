import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField(max_length = 100)
    joined_at = DateTimeField(default = datetime.datetime.now)
    is_admin = BooleanField(default = False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',) #the minus tells to order in descending order

    @classmethod #classmethod describes a method that belongs to a class that can create a class that belongs to
    def create_user(cls, username, email, password, admin=false): #cls instead of self
        try:
            cls.create(
            username = username,
            email = email,
            password = generate_password_hash(password),
            is_admin = admin
            )
        except IntegrityError:
            raise ValueError("User already exists")
