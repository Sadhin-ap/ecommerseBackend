from pydantic import BaseModel

class CartBase(BaseModel):
    product_id: int
    quantity: int = 1


class CartCreate(CartBase):
    pass

class CartUpdate(BaseModel):
    quantity:int


class CartRead(CartBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class CartItemRead(BaseModel):
    id: int
    product_id: int
    product_name: str
    price: float
    quantity: int
    subtotal: float

