from fastapi import APIRouter, Depends, status, HTTPException
from app.backend.deps import get_db
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession



router = APIRouter(prefix='/tables', tags=['tables'])
