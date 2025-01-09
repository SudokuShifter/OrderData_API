from internal.models.core import IDMixCoreModel, CoreModel


class HistoryOrder(IDMixCoreModel):
    user_id: int
    product_id: int


class HistoryOrderCreate(CoreModel):
    user_id: int
    product_id: int