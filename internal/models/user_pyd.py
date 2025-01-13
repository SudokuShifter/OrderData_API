from internal.models.core import IDMixCoreModel, CoreModel

from pydantic import Field, EmailStr

from typing import Optional


class User(IDMixCoreModel):
    first_name: str = Field(
        min_length=1, max_length=100
    )
    last_name: str = Field(
        min_length=1, max_length=100
    )
    email: EmailStr
    phone: str


class UserCreate(CoreModel):
    first_name: str = Field(
        min_length=1, max_length=100
    )
    last_name: str = Field(
        min_length=1, max_length=100
    )
    email: EmailStr
    password: str
    phone: str
    admin_token: Optional[str] = None


class UserIn(CoreModel):
    email: EmailStr
    password: str
