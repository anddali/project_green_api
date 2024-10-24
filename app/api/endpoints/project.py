from typing import List
from app.crud import project as projectcrud
from app.crud import user as usercrud
from app.schemas import schemas
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.api.deps import get_db, verify_token
router = APIRouter()


# Read all projects
@router.get("/")
def read_projects(db: Session = Depends(get_db), payload = Depends(verify_token)):    
    projects = projectcrud.get_projects(db)
    if not projects:
       projects = []
    return projects

# Create a new project
@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db), payload = Depends(verify_token)):
    db_user = usercrud.get_user(db, project.user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return projectcrud.create_project(db, project)

# Get a project by ID
@router.get("/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db), payload = Depends(verify_token)):
    project = projectcrud.get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# Get all projects for a user
@router.get("/users/{user_id}/projects/", response_model=List[schemas.Project])
def get_user_projects(user_id: int, db: Session = Depends(get_db), payload = Depends(verify_token)):
    return projectcrud.get_projects_by_user(db, user_id)

# Delete a project by ID
@router.delete("/{project_id}/", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db), payload = Depends(verify_token)):
    project = projectcrud.delete_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


# Update a project by ID
@router.put("/{project_id}/", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db), payload = Depends(verify_token)):
    db_project = projectcrud.update_project(db, project_id, project)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project
