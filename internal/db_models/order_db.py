from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from internal.db_models.core import Base


class Order(Base):

    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id', ondelete='SET NULL'), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )

    products = relationship('Product', back_populates='orders')
    user = relationship('User', back_populates='orders')
