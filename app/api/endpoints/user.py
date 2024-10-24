from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as usercrud
from app.schemas import schemas
from app.api.deps import get_db
from typing import List

router = APIRouter()

@router.post("/") #, response_model=schemas.User
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user)
    return usercrud.create_user(db=db, user=user)

@router.get("/", response_model=List[schemas.User]) # 
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    result = usercrud.get_users(db, skip=skip, limit=limit)
    if not result:
        raise HTTPException(status_code=404, detail="No users found")
    return result

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = usercrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if usercrud.delete_user(db=db, user_id=user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")