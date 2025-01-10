from internal.db_models.core import Base

from sqlalchemy.orm import Mapped, mapped_column, MappedColumn, relationship
from sqlalchemy import Integer, String, Numeric, ForeignKey


class Product(Base):

    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )
    price: Mapped[float] = mapped_column(
        Numeric(3, 2), nullable=False
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id'), nullable=False
    )

    tag = relationship('Tag', back_populates='products')
    orders = relationship('Order', back_populates='products')
    history_views = relationship('HistoryView', back_populates='product')