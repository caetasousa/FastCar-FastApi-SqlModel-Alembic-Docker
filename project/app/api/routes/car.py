from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session, init_db
from app.models import Car, CarCreate

router = APIRouter()

@router.post("/")
async def add_car(car: CarCreate, session: AsyncSession = Depends(get_session)):
    car = Car(modelo=car.modelo, placa=car.placa, ano=car.ano)
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car