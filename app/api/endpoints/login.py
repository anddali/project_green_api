from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
import datetime
import os
import app.crud.user as usercrud
import app.schemas.schemas as schemas
from app.core.config import settings

router = APIRouter()
from app.api.deps import get_db




@router.post("/google")
async def google_login(data: dict, db: Session = Depends(get_db)):    
    try:
        # Specify the CLIENT_ID of the app that accesses the backend
        idinfo = id_token.verify_oauth2_token(data["token_id"], requests.Request(), settings.GOOGLE_CLIENT_ID)

        # ID token is valid, extract user info
        userid = idinfo["sub"]
        email = idinfo["email"]
        full_name = idinfo["name"]

        print(userid, email, full_name)
        print("Type of userid ", type(userid))

        # Create or find user in the database
        db_user = usercrud.get_user_by_email(db, email)
        print("User ", db_user)
        if not db_user:            
            db_user = usercrud.create_google_user(db, schemas.GoogleUserCreate(full_name=full_name, email=email, google_id=userid))  # In reality, you should hash the password
            print("Creating user ", db_user)
       
        
        

        # Create JWT token
        jwt_payload = {
            "user_id" : db_user.id,
            "google_id": userid,
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(jwt_payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

        return {"token": token, "user_id": db_user.id, "email": email}
    except ValueError:
        # Invalid token
        raise HTTPException(status_code=400, detail="Invalid Google token")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))