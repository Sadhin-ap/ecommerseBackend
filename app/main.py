from fastapi import FastAPI
from app.database import Base, engine
from app.schemas.user import UserRead
from app.models import User
from app.controllers.user_controller import router as user_router
from app.controllers.auth_controller import router as auth_router

app = FastAPI(title="E-commerce API")
app.include_router(user_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

# @app.get("/")
# def home():
#     return {"message": "Database & User table ready"}




# @app.get("/test-schema")
# def test_schema():
#     fake_user = UserRead(
#         id=1,
#         name="Sadhin",
#         email="sadhin@example.com",
#         is_active=True,
#         is_admin=False
#     )
#     return fake_user
