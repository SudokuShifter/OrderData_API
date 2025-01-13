from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, async_scoped_session
from core.config.core_config import load_config_db
from asyncio import current_task

from pkg.color_print import PrintColors


class DatabaseSessionManager:


    def __init__(self):
        self.engine: AsyncEngine | None = None
        self.session_marker = None
        self.session = None
        self._config = load_config_db()

    def init_db(self):
        if self.engine is not None:
            raise Exception('Database already initialized')

        self.engine = create_async_engine(
            url=f'postgresql+asyncpg://{self._config.db_user}:{self._config.db_password}'
                f'@{self._config.db_host}:{self._config.db_port}/{self._config.db_name}',
            pool_size=100, max_overflow=100, pool_pre_ping=True,
        )

        self.session_marker = async_sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        self.session = async_scoped_session(
            self.session_marker, scopefunc=current_task
        )
        print(PrintColors.OKGREEN + 'Database initialized' + PrintColors.ENDC)

    async def close(self):
        if self.engine is None:
            raise Exception('DatabaseSessionManager has not been initialized')
        await self.session.remove()
        await self.engine.dispose()


session_manager = DatabaseSessionManager()