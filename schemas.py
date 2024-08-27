from pydantic import BaseModel
from typing import List, Optional


class RegisterModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "id": 5,
            "username": "Nodirbek",
            "email": "nodir@gmail.com",
            "password": "1234",
            "is_staff": False,
            "is_active": True,
        }


class LoginModel(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "username": "Nodirbek",
            "password": "1234",
        }


class ProductCreateModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[int]


class ProductListModel(BaseModel):
    name: Optional[str]
    price: Optional[int]


class OrderListModel(BaseModel):
    id: Optional[int]
    count: Optional[int]
    user_id: Optional[int]
    product_id: Optional[int]


class OrderCreateModel(BaseModel):
    id: Optional[int]
    count: Optional[int]
    user_id: Optional[int]
    product_id: Optional[int]


class UserOrderModel(BaseModel):
    id: Optional[int]
    product_id: Optional[int]
    order_id: Optional[int]
