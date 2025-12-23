from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id:int
    is_active:bool
    is_admin: bool

    class Config:
        orm_mode=True