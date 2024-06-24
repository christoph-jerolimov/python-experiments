from typing import Optional

from sqlalchemy import func
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///test.db", echo=True)

SQLModel.metadata.create_all(engine)


with Session(engine) as session:
    countStatement = select(func.count()).select_from(Hero)
    count = session.scalar(countStatement)
    if count == 0:
        session.add_all(
            Hero(name="Deadpond", secret_name="Dive Wilson"),
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
            Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
        )
        session.commit()

    statement = select(Hero)
    for hero in session.exec(statement).all():
        print(hero)

    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(statement).one()
    print(hero)

    session.scalar(countStatement)
    print("Count:", count)
