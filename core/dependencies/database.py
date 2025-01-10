from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, async_scoped_session
from core.config.core_config import load_config
from core.config.db_config import DBConfig
from asyncio import current_task


class DatabaseSessionManager:
    load_config()

    def __init__(self):
        self.engine: AsyncEngine | None = None
        self.session_marker = None
        self.session = None

    def init_db(self):
        self.engine = create_async_engine(
            url=f'postgresql+asyncpg://{DBConfig.db_user}:{DBConfig.db_password}'
                f'@{DBConfig.db_host}:{DBConfig.db_port}/{DBConfig.db_name}',
            pool_size=100, max_overflow=100, pool_pre_ping=True,
        )

        self.session_marker = async_sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        self.session = async_scoped_session(
            self.session_marker, scopefunc=current_task
        )

    def close(self):
        if self.engine is None:
            raise Exception('DatabaseSessionManager has not been initialized')
        await self.session.dispose()


session_manager = DatabaseSessionManager()