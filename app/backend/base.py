from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from environs import Env

env = Env()
env.read_env()

engine = create_async_engine(
    f"postgresql+asyncpg://{env.str('DB_NAME')}:"
    f"{env.str('DB_PASSWORD')}@{env.str('DB_HOST')}:"
    f"{env.str('DB_PORT')}/restaurant",
    echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
