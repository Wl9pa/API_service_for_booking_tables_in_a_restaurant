from __future__ import annotations
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.base import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String(50), nullable=False)
    table_id: Mapped[int] = mapped_column(Integer, ForeignKey('tables.id', ondelete='CASCADE'), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)

    table: Mapped["Table"] = relationship(back_populates="reservations")

    def __repr__(self) -> str:
        return (f"Бронирование(id={self.id}, клиент={self.customer_name}, "
                f"время={self.reservation_time}, продолжительность={self.duration_minutes})")
