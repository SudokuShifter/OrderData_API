import uvicorn
from fastapi import FastAPI

from api.reg_auth import LoginRegister
from core.dependencies.database import session_manager
from internal.repository.users import UserRepository

app = FastAPI()

user_router = LoginRegister(rep=UserRepository)

app.include_router(user_router.router, prefix='/user', tags=['user'])

def start():
    uvicorn.run('main:app', host='127.0.0.1', port=8000)

if __name__ == '__main__':
    session_manager.init_db()
    start()
