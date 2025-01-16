from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

from internal.db_models.core import Base


class HistoryView(Base):

    __tablename__ = 'history_views'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id', ondelete='CASCADE'), nullable=False
    )
    counter_view: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0
    )

    user = relationship('User', back_populates='history_views')
    product = relationship('Product', back_populates='history_views')

    def __repr__(self):
        return f'{self.user_id} was view {self.product_id} -- {self.counter_view}'