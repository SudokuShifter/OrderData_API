from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from passlib.hash import pbkdf2_sha256
from typing import Sequence, cast

from internal.models.product_pyd import Product


class ProductRepository:

    """
    Класс ProductRepository реализует основную логику (CRUD) взаимодействия с моделью Product.
    """

    @staticmethod
    async def get_all_products(session: AsyncSession) -> Sequence[Product]:
        stmt = select(Product)
        result = await session.execute(stmt)
        return result.scalars().all()


    @staticmethod
    async def get_product(session: AsyncSession, product_id: int) -> Product:
        stmt = select(Product).where(Product.id == product_id) #type: ignore
        result = await session.execute(stmt)
        if result:
            return Product(**result.scalars().one())
        raise Exception('Product not found')


    @staticmethod
    async def create_product(session: AsyncSession, product: Product) -> Product:
        stmt = select(Product).filter(or_(Product.id == product.id, Product.name == product.name))
        if await session.scalar(stmt):
            raise Exception('Product already exists')
        new_product = Product(
            title=product.title,
            description=product.description,
            price=product.price,
            tag_id=product.tag_id
        )
        session.add(new_product)
        await session.commit()
        return new_product


    @staticmethod
    async def update_product(session: AsyncSession, product_id: int, product: Product) -> Product:
        stmt = select(Product).where(Product.id == product_id) #type: ignore
        product_old = await session.scalar(stmt)
        if not product_old:
            raise Exception('Product not found')
        for key, value in product:
            product_old(key=value)
        await session.commit()
        return product_old

