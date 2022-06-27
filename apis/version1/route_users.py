from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user
from fastapi import status,HTTPException
from core.hashing import Hasher
from db.repository.login import get_user

router = APIRouter()


@router.post("/create-user/", response_model=ShowUser)
def create_user(user : UserCreate, db : Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user



