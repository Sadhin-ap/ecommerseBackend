from fastapi import FastAPI
from app.controllers import admin_product_controllers
from app.database import Base, engine
from app.models import User
from app.controllers.user_controller import router as user_router
from app.controllers.auth_controller import router as auth_router
from app.controllers.admin import router as admin_router
from app.controllers.product_controller import router as product_router
from app.controllers.cart_controller import router as cart_router
from app. controllers.admin_product_controllers import router as admin_product_router


app = FastAPI(title="E-commerce API")
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(admin_router)
Base.metadata.create_all(bind=engine)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(admin_router)
app.include_router(admin_product_router)

