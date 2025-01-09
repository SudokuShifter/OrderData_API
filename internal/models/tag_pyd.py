from typing import Optional
from internal.models.core import IDMixCoreModel, CoreModel

from pydantic import Field


class Tag(IDMixCoreModel):
    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = Optional[str]


class TagCreate(CoreModel):
    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = Optional[str]