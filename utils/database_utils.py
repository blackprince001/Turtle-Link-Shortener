from sqlalchemy.orm import Session
from turtle_link_shortener.database import engine, Base


def get_db():
    with Session(engine, autocommit=False, autoflush=False) as session:
        Base.metadata.create_all(bind=engine)
        yield session