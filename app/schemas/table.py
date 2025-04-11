from pydantic import BaseModel


class TableBase(BaseModel):
    name: str
    seats: int
    location: str


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: int

    class Config:
        from_attributes = True
