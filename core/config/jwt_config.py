from dataclasses import dataclass



@dataclass
class JWTConfig:
    """
    Класс JWTConfig, декорируемый дата-классом,
    для сигнатуры формирования jwt-токенов для авторизации юзера
    """
    secret: str
    algorithm: str
