from internal.db_models.core import Base
from internal.db_models.product_db import Product

from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped



class Tag(Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False
    )
    description: Mapped[str] = mapped_column(
        String(255), nullable=True
    )

    products = relationship(Product, back_populates='tag')

    def __repr__(self):
        return f'Tag {self.title}: {self.description}'