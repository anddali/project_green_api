from fastapi import APIRouter
from app.api.endpoints import project, user, login

api_router = APIRouter()


api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(project.router, prefix="/projects", tags=["projects"])
api_router.include_router(login.router, prefix="/login", tags=["login"])