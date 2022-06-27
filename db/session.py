import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings


SQL_ALCHEMY_DATABASE_URL = settings.DATABASE_URL # URL de la base de datos
engine = create_engine(SQL_ALCHEMY_DATABASE_URL) # sqlalchemy engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #database session


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()