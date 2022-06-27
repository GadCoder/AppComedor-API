from sqlalchemy.orm import  Session

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        code=user.code,
        names=user.names,
        lastnames=user.lastnames,
        is_banned=False,
        is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user