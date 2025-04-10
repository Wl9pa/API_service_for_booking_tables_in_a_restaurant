from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.base import Base


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    seats: Mapped[int] = mapped_column(Integer, nullable=False)
    location: Mapped[str] = mapped_column(String(50), nullable=False)

    # Используем строковый литерал вместо импорта
    reservations: Mapped[List["Reservation"]] = relationship(
        back_populates="table",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Стол(id={self.id}, наименование={self.name}, места={self.seats})"
