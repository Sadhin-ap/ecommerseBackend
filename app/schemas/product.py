from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True   
        
