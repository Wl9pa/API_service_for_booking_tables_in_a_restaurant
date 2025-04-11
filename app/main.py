from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers import tables, reservations
from app.backend.base import Base, engine

app = FastAPI()

app.include_router(tables.router)
app.include_router(reservations.router)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Создаём таблицы при старте (можно временно раскомментировать)
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     # Очищаем подключения при завершении
#     await engine.dispose()


# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "My app"}
