from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.responses import JSONResponse

from jwt import ExpiredSignatureError, InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession



class LoginRegister:

    OAUTH2SCHEME = OAuth2PasswordBearer(tokenUrl="/login")

    def __init__(self, rep):
        self.router = APIRouter()
        self.rep = rep

    @staticmethod
    def get_token_from_cookies(request: Request):
        token = request.cookies.get("token")
        if not token:
            raise HTTPException(401, detail='Not authenticated')
        return token

    @staticmethod
    def get_current_user(token: str = Depends(get_token_from_cookies)):
        pass