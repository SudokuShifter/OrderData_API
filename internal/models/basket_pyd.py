from internal.models.core import IDMixCoreModel


class Basket(IDMixCoreModel):
    user_id: int
    product_id: int
