from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select

from app.backend.deps import get_db
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.table import TableCreate, Table

from app.models.table import Table as DBTable

router = APIRouter(prefix='/tables', tags=['tables'])


@router.get('/', response_model=list[Table])
async def get_tables(skip: Annotated[int, 0] = 0, limit: Annotated[int, 100] = 100,
                     db: Annotated[AsyncSession, Depends(get_db)] = None):
    result = await db.execute(select(DBTable).offset(skip).limit(limit))
    return result.scalars().all()
