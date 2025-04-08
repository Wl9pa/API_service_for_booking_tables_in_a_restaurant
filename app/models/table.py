from sqlalchemy import Column, Integer, String
from app.backend.base import Base
from sqlalchemy.orm import relationship


class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    seats = Column(Integer)
    location = Column(String)

    reservations = relationship("Reservation")
