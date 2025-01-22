from typing import ClassVar
from pydantic import BaseModel


class CoreModel(BaseModel):
    """
    Core-модель для pydantic-схем без id
    """
    pass


class IDMixCoreModel(BaseModel):
    """
    Core-модель для pydantic-схем с id
    """
    id: ClassVar[int]



