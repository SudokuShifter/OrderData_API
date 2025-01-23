from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from passlib.hash import pbkdf2_sha256
from typing import List


class OrderRepository:

     @staticmethod
     async def get_all():
         pass