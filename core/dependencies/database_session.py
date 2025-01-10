from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import session_manager


async def get_db() -> AsyncIterator[AsyncSession]:
    session = session_manager.session()
    if session is None:
        raise Exception('DatabaseSessionManager has not been initialized')
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
