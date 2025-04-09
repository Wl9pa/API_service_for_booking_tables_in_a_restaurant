from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.base import async_session_maker, engine, Base


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
