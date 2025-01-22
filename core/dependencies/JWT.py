from datetime import datetime, timedelta

import jwt

from core.config.core_config import load_config_jwt


class JWTToken:
    """
    Класс JWTToken имеющий сигнатуру класса singleton, т.е. объект может быть лишь в единственном экземпляре,
    отвечает за генерацию и декодирование jwt-токенов для авторизации
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(JWTToken, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.config = load_config_jwt()


    def generate_token(self, data: dict):
        expire = datetime.utcnow() + timedelta(minutes=30)
        data.update({'exp': expire})
        return jwt.encode(data, self.config.secret, self.config.algorithm)

    def decode_token(self, token: str):
        payload = jwt.decode(token, self.config.secret, self.config.algorithm)
        return payload.get('sub')
