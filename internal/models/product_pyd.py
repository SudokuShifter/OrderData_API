from typing import Optional
from internal.models.core import IDMixCoreModel, CoreModel

from pydantic import Field, ConfigDict


class Product(IDMixCoreModel):

    model_config = ConfigDict(from_attributes=True)

    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = Optional[str]
    price: float = Field(
        gt=0, lt=100
    )
    tag_id: int


class ProductCreate(CoreModel):

    model_config = ConfigDict(from_attributes=True)

    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = Optional[str]
    price: float = Field(
        gt=0, lt=100
    )
    tag_id: int
