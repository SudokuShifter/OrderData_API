from internal.models.core import IDMixCoreModel, CoreModel

from pydantic import Field, EmailStr, ConfigDict

from typing import Optional


class User(IDMixCoreModel):

    model_config = ConfigDict(from_attributes=True)

    username: str = Field(
        min_length=1, max_length=100
    )
    real_name: str = Field(
        min_length=1, max_length=100
    )
    email: EmailStr


class UserCreate(CoreModel):

    model_config = ConfigDict(from_attributes=True)

    username: str = Field(
        min_length=1, max_length=100
    )
    real_name: str = Field(
        min_length=1, max_length=100
    )
    email: EmailStr
    password: str
    admin_token: Optional[str] = None


class UserIn(CoreModel):

    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    password: str

