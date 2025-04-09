from fastapi import FastAPI
from app.routers import tables, reservations
from app.backend.base import Base
from app.backend.deps import engine


app = FastAPI()


app.include_router(tables.router)
app.include_router(reservations.router)
