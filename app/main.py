from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from router import router
from models import ProductModel, UserModel, ReviewModel
from core.batabase import start_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_db()  
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",  # localhost
        port=8000,
        reload=True  # enable auto-reload
    )