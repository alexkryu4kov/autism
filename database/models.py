from sqlalchemy import Column, Integer, String, Float, Time
from database.db import Database


class Picture(Database.declare_base()):
    __tablename__ = 'pictures'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    category = Column(String(50))
    picture = Column(String(100), unique=True)

    def __init__(self, id, name, category, picture):
        self.id = id
        self.name = name
        self.category = category
        self.picture = picture

    def __repr__(self):
        return f"<User(amount={self.name}, accuracy={self.category}', time={self.picture})>"


class Game(Database.declare_base()):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    accuracy = Column(Float)
    time = Column(Time)

    def __init__(self, amount, accuracy, time):
        self.amount = amount
        self.accuracy = accuracy
        self.time = time

    def __repr__(self):
        return f"<User(amount={self.amount}, accuracy={self.accuracy}', time={self.time})>"
