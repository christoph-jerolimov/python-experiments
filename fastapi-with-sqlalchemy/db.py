from sqlalchemy import create_engine, String, Boolean, func
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped,
    sessionmaker,
    Session,
)
from pydantic import BaseModel
from typing import Iterable, Optional


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    done: Mapped[bool] = mapped_column(Boolean, default=False)


class NewTodo(BaseModel):
    name: str
    done: Optional[bool] = None


class UpdateTodo(BaseModel):
    name: Optional[str] = None
    done: Optional[bool] = None


class TodoResponse(BaseModel):
    id: int
    name: str
    done: bool


connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///test.db", connect_args=connect_args, echo=True)
sessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        if session.query(func.count()).select_from(Todo).scalar() == 0:
            session.add(Todo(name="todo a", done=False))
            session.add(Todo(name="todo b", done=False))
            session.add(Todo(name="todo c", done=False))
            session.add(Todo(name="done", done=True))
            session.commit()


def get_session() -> Iterable[Session]:
    session = sessionFactory()
    try:
        yield session
    finally:
        session.close()
