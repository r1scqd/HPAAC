"""Database module."""

from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from loguru import logger
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session, MappedAsDataclass, DeclarativeBase
from sqlalchemy_serializer import SerializerMixin


class Base(MappedAsDataclass, DeclarativeBase, SerializerMixin):
    ...


class Database:

    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True, echo_pool='debug')
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.commit()
            session.close()
