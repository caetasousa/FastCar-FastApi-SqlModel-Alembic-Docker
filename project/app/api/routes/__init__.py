from fastapi import APIRouter

from app.api.routes.car import router as car_router  


router = APIRouter()


router.include_router(car_router, prefix="/car", tags=["car"])