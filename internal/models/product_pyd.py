from typing import Optional
from internal.models.core import IDMixCoreModel, CoreModel

from pydantic import Field


class Product(IDMixCoreModel):
    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = Optional[str]
    price: float = Field(
        gt=0, lt=100
    )
    tag_id: int


class ProductCreate(CoreModel):
    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = Optional[str]
    price: float = Field(
        gt=0, lt=100
    )
    tag_id: int