from sqlalchemy.orm import Session
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
        profile_photo_url=user.profile_photo_url,
        is_banned=False,
        is_superuser=user.is_superuser
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_code(code: str, db: Session):
    user = db.query(User).filter(User.code == code).first()
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
