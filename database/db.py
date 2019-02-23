import database.models

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database:
    def __init__(self, db='postgresql://autist:pass@localhost:5432/sqlalchemy'):
        self.engine = create_engine(db, convert_unicode=True)

    def session_db(self):
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=False,
                                                 bind=self.engine))
        Base = declarative_base()
        Base.query = db_session.query_property()
