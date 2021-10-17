from typing import Optional

from sqlmodel import Field, SQLModel


class CarBase(SQLModel):
    modelo: str
    placa: str
    ano: Optional[int] = None


class Car(CarBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CarRead(CarBase):
    id: int


class CarCreate(CarBase):
    pass


class CarUpdate(SQLModel):
    marca: Optional[str] = None
    placa: Optional[str] = None
    ano: Optional[int] = None
