from internal.models.core import IDMixCoreModel, CoreModel


class Order(IDMixCoreModel):
    user_id: int
    product_id: int


class OrderCreate(CoreModel):
    user_id: int
    product_id: int
