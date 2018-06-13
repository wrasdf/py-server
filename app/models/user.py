from . import db
from .base import BaseModel

class User(db.Model, BaseModel):
    """ The User model """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    logdate = db.Column(db.DateTime())


    def __init__(self, first_name, last_name, age=None):
        """ Create a new User """
        self.username = username
        self.password = password
        self.email = email
