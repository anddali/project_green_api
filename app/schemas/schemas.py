# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Schema for a Project
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = ""

class ProjectCreate(ProjectBase):
    user_id: int

class Project(ProjectBase):
    id: int
    created_at: datetime
    user_id: int    

    class Config:
        from_attributes  = True

# Schema for a User
class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    hashed_password: str

class GoogleUserCreate(UserBase):
    google_id: str
    

class User(UserBase):
    id: int
    google_id: Optional[str] = None
    projects: List[Project] = []

    class Config:
        from_attributes  = True
