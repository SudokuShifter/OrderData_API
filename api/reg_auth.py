"""
Сигнатурные зависимости
"""
from http.client import responses
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies.database_session import get_db
import os

from internal.db_models.user_db import RoleUserEnum

"""
JWT-зависимости
"""
from core.dependencies.JWT import JWTToken
from jwt import ExpiredSignatureError, InvalidTokenError

"""
Pydantic-модели
"""
from internal.models.tag_pyd import TagCreate
from internal.models.history_views_pyd import HistoryViewCreate
from internal.models.user_pyd import UserCreate, UserIn
from internal.models.product_pyd import ProductCreate



class LoginRegister:
    """
    Класс LoginRegister отвечает за полный спектр возможностей юзера в рамках регистрации и авторизации
    """
    OAUTH2SCHEME = OAuth2PasswordBearer(tokenUrl="/login")

    def __init__(self, rep):
        self.router = APIRouter()
        self.rep = rep
        self.jwt = JWTToken()
        self.router.add_api_route('/register',
                                  self.register, methods=["POST"])

    @staticmethod
    async def get_token_from_cookies(request: Request):
        token = request.cookies.get("token")
        if not token:
            raise HTTPException(401, detail='Not authenticated')
        return token


    async def get_current_user(self, token: str = Depends(get_token_from_cookies)):
        try:
            payload = self.jwt.decode_token(token)
            user = {
                'id': payload.get('id'),
                'user': payload.get('user'),
                'role': payload.get('role')
                }
            return user if user else None

        except ExpiredSignatureError:
            raise ExpiredSignatureError('Token expired')

        except InvalidTokenError:
            raise InvalidTokenError('Invalid token')


    async def register(self, user: UserCreate,
                 response: Response, db_session: AsyncSession = Depends(get_db)):
        try:
            role = RoleUserEnum.ADMIN if (user.admin_token and
                                          user.admin_token == os.getenv('ADMIN_TOKEN')) else RoleUserEnum.USER
            res = await self.rep.register(user, db_session, role)

            return JSONResponse(content={'success': True,
                                         'detail': f'Success register with data: {res}'},
                                headers=response.headers)
        except HTTPException:
            raise HTTPException(status_code=400, detail='Invalid credentials')


    async def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
              response: Response, db_session: AsyncSession = Depends(get_db)):
        pass