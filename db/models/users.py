from sqlalchemy import Column, String, Integer, Boolean

from db.base_class import Base

"""
Campos de los usuarios
id
mail
password
code
names
lastnames
is_banned
is_superuser
"""


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    names = Column(String, nullable=False)
    lastnames = Column(String, nullable=False)
    code = Column(String)
    is_banned = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
    profile_photo_url = Column(String, nullable=False)