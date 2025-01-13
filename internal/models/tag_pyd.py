from typing import Optional
from internal.models.core import IDMixCoreModel, CoreModel

from pydantic import Field, ConfigDict



class Tag(IDMixCoreModel):

    model_config = ConfigDict(from_attributes=True)

    title: str = Field(
        str, min_length=1, max_length=100
    )
    description: str = None


class TagCreate(CoreModel):

    model_config = ConfigDict(from_attributes=True)

    title: str = Field(
        min_length=1, max_length=100
    )
    description: str = None