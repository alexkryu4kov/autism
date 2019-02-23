from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database:
    def __init__(self, db='postgresql://autist:pass@localhost:5432/postgres'):
        self.engine = create_engine(db, convert_unicode=True)

    @staticmethod
    def declare_base():
        return declarative_base()

    def session_db(self):
        db = create_engine(self.engine)
        session = sessionmaker(db)
        self.declare_base().metadata.create_all(db)
        return session()
