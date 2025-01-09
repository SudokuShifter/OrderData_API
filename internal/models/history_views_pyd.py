from internal.models.core import IDMixCoreModel, CoreModel


class HistoryView(IDMixCoreModel):
    user_id: int
    product_id: int


class HistoryViewCreate(CoreModel):
    user_id: int
    product_id: int