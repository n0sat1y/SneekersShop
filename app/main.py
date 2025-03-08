from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from router import router
from core.batabase import start_db, dispose_engine

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
        "main:app",  # localhost
        port=8000,
        reload=True  # enable auto-reload
    )