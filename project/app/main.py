from fastapi import FastAPI
from app.api.routes import router as api_router


app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

app.include_router(api_router, prefix="/api")