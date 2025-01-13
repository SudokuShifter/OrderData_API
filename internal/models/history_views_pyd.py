from pydantic import ConfigDict

from internal.models.core import IDMixCoreModel, CoreModel


class HistoryView(IDMixCoreModel):

    model_config = ConfigDict(from_attributes=True)

    user_id: int
    product_id: int


class HistoryViewCreate(CoreModel):

    model_config = ConfigDict(from_attributes=True)

    user_id: int
    product_id: int