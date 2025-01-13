from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from passlib.hash import pbkdf2_sha256
from typing import List


from internal.models.user_pyd import UserCreate, UserIn
from internal.models.user_pyd import User as UserOut
from internal.db_models.user_db import User, RoleUserEnum


class UserRepository:

    @staticmethod
    async def register(user: UserIn, session: AsyncSession, role: RoleUserEnum = RoleUserEnum.USER) -> UserOut:
        stmt = select(User).where(User.email == user.email)
        if await session.scalar(stmt):
            raise Exception("User already exists")
        if role == RoleUserEnum.ADMIN:
            session.add(User(**user.dict(), role=RoleUserEnum.ADMIN))
        else:
            session.add(User(**user.dict(), role=RoleUserEnum.USER))
        await session.commit()
        return UserOut.from_orm(user)


