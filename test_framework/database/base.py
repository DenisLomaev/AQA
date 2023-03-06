from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import url_db

BaseModel = declarative_base(name="BaseModel")


class DBCreateSession:
    def __init__(self):
        self.db_route: str = url_db

    def connect(self):
        return create_engine(self.db_route)

    def create_session(self):
        new_session = sessionmaker(self.connect(), autoflush=False, autocommit=False)
        return new_session()

    def close_session(self):
        self.create_session().close()
