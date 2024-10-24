from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas import schemas as user 
from typing import List


def create_user(db: Session, user: user.UserCreate):
    try:
        print(user)
        db_user = User(**user.dict(exclude={"password"}))
        db_user.hashed_password = user.hashed_password  # In reality, you should hash the password
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
        db.rollback()
        db_user = None
    return db_user

def create_google_user(db: Session, user: user.GoogleUserCreate):
    try:
        print(user)
        db_user = User(**user.dict())
        db_user.hashed_password = None  # In reality, you should hash the password
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
        db.rollback()
        db_user = None
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()