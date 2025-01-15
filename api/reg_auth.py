"""
Сигнатурные зависимости
"""
from crypt import methods
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies.database_session import get_db
import os
from api.core import ResponseManager
"""
JWT-зависимости
"""
from core.dependencies.JWT import JWTToken
from jwt import ExpiredSignatureError, InvalidTokenError

"""
Pydantic-модели
"""
from internal.models.user_pyd import UserCreate, UserIn, User


class LoginRegister(ResponseManager):
    """
    Класс LoginRegister отвечает за полный спектр возможностей юзера в рамках регистрации и авторизации
    """
    OAUTH2SCHEME = OAuth2PasswordBearer(tokenUrl="/login")

    def __init__(self, rep):
        self.router = APIRouter()
        self.rep = rep
        self.jwt = JWTToken()
        self.router.add_api_route('/register',
                                  self.register, methods=['POST'])
        self.router.add_api_route('/login',
                                  self.login, methods=['POST'])
        self.router.add_api_route('/logout',
                                  self.logout, methods=['POST']),
        self.router.add_api_route('/get_all_users',
                           self.get_all_users, methods=['GET'])


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


    @staticmethod
    async def is_admin(user: User = Depends(get_current_user)):
        if user:
            role = user.get('role')
            return True if role == 'admin' else False
        raise HTTPException(status_code=401, detail='Not authenticated')


    async def register(self, user: UserCreate,
                 response: Response, db_session: AsyncSession = Depends(get_db)):
        try:
            is_admin = True if (user.admin_token and
                                          user.admin_token == os.getenv('ADMIN_TOKEN')) else False
            res = await self.rep.register(user, db_session, is_admin)

            return LoginRegister.generate_response(True,
                                                   f'Success register with data: {res}',
                                                   response.headers)
        except Exception as e:
            raise HTTPException(status_code=400, detail=e.__str__())


    async def login(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
              response: Response, db_session: AsyncSession = Depends(get_db)):
        try:
            user = UserIn(email=form_data.username, password=form_data.password)
            user_in_db = await self.rep.login(user, db_session)
            if user_in_db:
                jwt_token = self.jwt.generate_token(
                    {'user_id': user_in_db.id,
                    'role': user_in_db.role,
                    'email': user_in_db.email
                     }
                )
                response.set_cookie('token', jwt_token, httponly=True)
                return LoginRegister.generate_response( True,
                                                        f'Success login with data: {user_in_db.email}'
                                                        f'and role: {user_in_db.role}',
                                                        response.headers)
        except Exception as e:
            raise HTTPException(status_code=401, detail=e.__str__())


    async def logout(self, response: Response):
        try:
            user = await self.get_current_user()
            response.set_cookie('token', 'None', httponly=True)
            return LoginRegister.generate_response(
                True,
                f'Success logout with data: {user.get("email")}',
                None
            )
        except Exception as e:
            raise HTTPException(status_code=401, detail=e.__str__())


    async def del_account(self, token: dict = Depends(get_current_user),
                          db_session: AsyncSession = Depends(get_db)):
        try:
            res = await self.rep.delete_account(token.get('username'), db_session)
            return LoginRegister.generate_response(
                res,
                'User was deleted',
                None
            )
        except Exception as e:
            raise HTTPException(status_code=401, detail=e.__str__())


    async def get_all_users(self, response: Response, is_admin: bool = Depends(is_admin),
                            session: AsyncSession = Depends(get_db)):
        try:
            result = await self.rep.get_all_users(is_admin, session)
            return LoginRegister.generate_response(
                True,
                result,
                response.headers
            )
        except Exception as e:
            raise HTTPException(status_code=403, detail=e.__str__())