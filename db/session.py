import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)  # database session


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
