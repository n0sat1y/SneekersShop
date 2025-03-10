from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from routers import router
from core.database import start_db, dispose_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await start_db()
    yield
    print('Disposing engine')
    await dispose_engine()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True
    )