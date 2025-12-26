from fastapi import Depends,HTTPException,status
from app.core.jwt import get_current_user
from app.models.user import User

def get_logged_user(user:User = Depends(get_current_user)):
    return user

def admin_required(current_user:User = Depends(get_logged_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource"
        )
    return current_user

def get_current_admin(current_user:User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access only"
        )
    return current_user