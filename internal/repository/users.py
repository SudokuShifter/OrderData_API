from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_

from passlib.hash import pbkdf2_sha256
from typing import List

from sqlalchemy.orm import session

from internal.models.user_pyd import UserCreate, UserIn
from internal.models.user_pyd import User as UserOut
from internal.db_models.user_db import User, RoleUserEnum


class UserRepository:
    """
    Класс UserRepository отвечает за выполнение целевых задач LoginRegister-роутера
    """
    @staticmethod
    async def register(user: UserIn, session: AsyncSession, is_admin: bool = False) -> UserOut:
        stmt = select(User).filter(or_(User.email == user.email, User.username == user.username))
        if await session.scalar(stmt):
            raise Exception("User already exists")
        new_user = User(
            username=user.username,
            real_name=user.real_name,
            email=user.email,
            password=pbkdf2_sha256.hash(user.password),
            role = RoleUserEnum.ADMIN if is_admin else RoleUserEnum.USER,
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


    @staticmethod
    async def login(user: UserIn, session: AsyncSession) -> User | Exception:
        stmt = select(User).where(User.username == user.username)
        user_in_db = await session.scalar(stmt)
        if user and pbkdf2_sha256.verify(user.password, user_in_db.password):
            return user_in_db
        raise Exception("User does not exist or incorrect data")

    @staticmethod
    async def delete_account(username: str, session: AsyncSession) -> bool | Exception:
        stmt = select(User).where(User.username == username)
        user = await session.scalar(stmt)
        if user:
            await session.delete(user)
            await session.commit()
            return True
        raise Exception("User does not exist")
