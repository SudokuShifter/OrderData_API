from pydantic import ConfigDict

from internal.models.core import IDMixCoreModel, CoreModel


class Order(IDMixCoreModel):

    model_config = ConfigDict(from_attributes=True)

    user_id: int
    product_id: int

    config = ConfigDict(from_attributes=True)


class OrderCreate(CoreModel):

    model_config = ConfigDict(from_attributes=True)

    user_id: int
    product_id: int
