from abc import abstractmethod
from contextlib import contextmanager

import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import url_db
from test_framework.helpers.log import my_log


class BaseDB:
    _session = None

    def __init__(self):
        self.logger = my_log()

    @property
    @abstractmethod
    def host(self) -> str:
        """Должно быть реализовано дочерними классами"""

    @property
    @abstractmethod
    def database(self) -> str:
        """Должно быть реализовано дочерними классами"""

    @property
    @abstractmethod
    def user(self) -> str:
        """Должно быть реализовано дочерними классами"""

    @property
    @abstractmethod
    def password(self) -> str:
        """Должно быть реализовано дочерними классами"""

    def _new_session(self) -> sessionmaker:
        db_url = url_db.format(self.user, self.password, self.host, self.database)
        engine = create_engine(db_url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine, expire_on_commit=False)
        return session()

    def _get_session(self) -> sessionmaker:
        if not self._session:
            return self._new_session()
        return self._session  # type: ignore

    @contextmanager
    def create_session(self) -> sessionmaker:
        session = self._get_session()
        try:
            yield session
            session.commit()
        except psycopg2.Error as error:
            session.rollback()
            self._session = None
            self.logger.error("Error while get connection", error)
            raise
        finally:
            session.close()
