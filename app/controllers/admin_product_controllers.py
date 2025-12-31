from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductRead
from app.deps import admin_required

router = APIRouter(
    prefix="/admin/products",
    tags=["Admin Products"]
)


@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin = Depends(admin_required)
):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
