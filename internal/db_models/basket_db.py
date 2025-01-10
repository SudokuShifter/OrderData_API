from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship, Mapped, MappedColumn
from internal.db_models.core import Base


class Basket(Base):

    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True)
