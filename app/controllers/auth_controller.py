from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.auth import LoginSchema
from app.core.security import verify_password
from app.core.jwt import create_access_token, create_refresh_token
from fastapi.security import OAuth2PasswordRequestForm

router =APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/login")
def login(data:OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(
        data={"sub":user.email}
    )


    refresh_token = create_refresh_token({"sub": user.email})

    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

from app.core.jwt import verify_token, create_access_token

@router.post("/refresh")
def refresh_access_token(token: str):
    payload = verify_token(token)
    email = payload.get("sub")

    if not email:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({"sub": email})

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }
