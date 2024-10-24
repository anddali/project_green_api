from fastapi import FastAPI
from app.db.database import engine
from app.models import models
from app.api.api import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# allow all cors
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "vIBE API is running"}
