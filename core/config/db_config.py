from dataclasses import dataclass
from environs import Env


@dataclass
class DBConfig:
    """
    Класс DBConfig, декорируемый дата-классом,
    для сигнатуры хранения переменных окружения базы данных
    """
    db_host: str
    db_port: str
    db_password: str
    db_user: str
    db_name: str


def load_config(path: str | None = None) -> DBConfig:
    env = Env()
    env.read_env(path)
    return DBConfig(
        db_host=env.str("DATABASE_HOST"),
        db_port=env.str("DATABASE_PORT"),
        db_password=env.str("DATABASE_PWD"),
        db_user=env.str("PG_USER"),
        db_name=env.str("PG_NAME"),
    )