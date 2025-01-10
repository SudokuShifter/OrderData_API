from core.config.db_config import DBConfig
from environs import Env


def load_config(path: str | None = None) -> DBConfig:
    env = Env()
    env.read_env('/home/zanid/OrderData_API/.env')
    return DBConfig(
        db_host=env.str("DATABASE_HOST"),
        db_port=env.str("DATABASE_PORT"),
        db_password=env.str("DATABASE_PWD"),
        db_user=env.str("PG_USER"),
        db_name=env.str("PG_NAME"),
    )
