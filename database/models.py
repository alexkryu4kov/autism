from sqlalchemy import Column, Integer, String, Float, Time
from database.db import Database


class Picture(Database.declare_base()):
    __tablename__ = 'pictures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(Integer)
    category = Column(String(50))
    picture = Column(String(100))

    def __init__(self, id, level, category, picture):
        self.id = id
        self.level = level
        self.category = category
        self.picture = picture

    def __repr__(self):
        return f"<User(amount={self.name}, accuracy={self.category}', time={self.picture})>"


class User(Database.declare_base()):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    points = Column(Integer)
    all_points = Column(Integer)
    time = Column(Time)

    def __init__(self, email, amount, points, all_points, time):
        self.email = email
        self.amount = amount
        self.points = points
        self.all_points = all_points
        self.time = time
