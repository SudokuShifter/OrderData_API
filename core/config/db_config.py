from dataclasses import dataclass



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


