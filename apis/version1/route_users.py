from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.models.users import User
from schemas.users import UserCreate, ShowUser, ShowFullUser
from db.session import get_db
from db.repository.users import create_new_user, get_user_by_code
from apis.version1.route_login import get_current_user_from_token
from fastapi import status,HTTPException

router = APIRouter()


@router.post("/create-user/", response_model=ShowUser)
def create_user(user : UserCreate, db : Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_superuser:
        user = create_new_user(user=user, db=db)
        return user
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Usuario con codigo {current_user.code} no tiene autorizacion para crear nuevos usuarios"
        )


@router.get("/read-user", response_model=ShowFullUser)
def read_user_from_token(db : Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    user = get_user_by_code(current_user.code, db=db)
    return user





