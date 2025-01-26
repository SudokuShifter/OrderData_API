from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from typing import Sequence

from internal.db_models.order_db import Order


class OrderRepository:
    """
    Класс OrderRepository отвечает за выполнение целевых задач Order-роутера
    """
    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[Order]:
        stmt = select(Order)
        result = await session.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> Sequence[Order]:
        stmt = select(Order).where(Order.user_id == user_id)
        result = await session.execute(stmt)
        return result.scalars().all()
