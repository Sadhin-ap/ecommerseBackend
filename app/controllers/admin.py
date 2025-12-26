from fastapi import APIRouter, Depends
from app.deps import admin_required,get_current_admin
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/all-users")
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(admin_required)):
    users = db.query(User).all()
    return users

@router.get("/dashboard")
def admin_dashboard(admin = Depends(get_current_admin)):
    return{
        "message":"welcome Admin",
        "admin_name":admin.name
    }
