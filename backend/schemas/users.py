from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    code: str
    names: str
    lastnames: str


class ShowUser(BaseModel):
    email: EmailStr
    code: str
    is_banned: bool

    class Config(): # convert dict or non dict obj to json
        orm_mode = True
