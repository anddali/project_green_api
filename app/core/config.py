import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = "HS256"
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

settings = Settings()
