import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship

from internal.db_models.core import Base


class RoleUserEnum(str, enum.Enum):
    ADMIN = 'admin'
    USER = 'user'


class User(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    first_name: Mapped[str] = mapped_column(
        String(50), nullable=False
    )
    second_name: Mapped[str] = mapped_column(
        String(50), nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True
    )
    password: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    role: Mapped[RoleUserEnum] = mapped_column(
        Enum(RoleUserEnum), nullable=False
    )

    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'User - {self.first_name} {self.second_name} with {self.email}'