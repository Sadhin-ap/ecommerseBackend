from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cart import Cart
from app.schemas.cart import CartCreate, CartRead,CartUpdate
from app.deps import get_logged_user

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=CartRead)
def add_to_cart(
    data: CartCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_logged_user)
):
    cart_item = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == data.product_id
    ).first()

    if cart_item:
        cart_item.quantity += data.quantity
        db.commit()
        db.refresh(cart_item)
        return cart_item

    new_cart = Cart(
        user_id=current_user.id,
        product_id=data.product_id,
        quantity=data.quantity
    )

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart

@router.get("/", response_model=list[CartRead])
def get_my_cart(
    db: Session = Depends(get_db),
    current_user = Depends(get_logged_user)
):
    return db.query(Cart).filter(
        Cart.user_id == current_user.id
    ).all()

@router.delete("/{cart_id}")
def remove_from_cart(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_logged_user)
):
    cart_item = db.query(Cart).filter(
        Cart.id == cart_id,
        Cart.user_id == current_user.id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(cart_item)
    db.commit()
    return {"message": "Item removed from cart"}

@router.put("/{cart_id}")
def edit_cart(
    cart_id: int,
    data: CartUpdate,
    db: Session = Depends(get_db)
):
    cart = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart item not found")

    # quantity = 0 → remove item
    if data.quantity <= 0:
        db.delete(cart)
        db.commit()
        return {"message": "Item removed from cart"}

    cart.quantity = data.quantity
    db.commit()
    db.refresh(cart)

    return cart

