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
