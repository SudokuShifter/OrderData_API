from environs import Env

from core.config.jwt_config import JWTConfig
from core.config.db_config import DBConfig


def load_config_db(path: str | None = None) -> DBConfig:
    env = Env()
    env.read_env(path)
    return DBConfig(
        db_host=env.str("DATABASE_HOST"),
        db_port=env.str("DATABASE_PORT"),
        db_password=env.str("DATABASE_PWD"),
        db_user=env.str("PG_USER"),
        db_name=env.str("PG_NAME"),
    )


def load_config_jwt(path: str | None = None) -> JWTConfig:
    env = Env()
    env.read_env(path)
    return JWTConfig(
        secret=env.str("JWT_SECRET"),
        algorithm=env.str("JWT_ALGORITHM"),
    )