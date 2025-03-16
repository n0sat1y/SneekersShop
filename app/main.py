from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from app.routers import router
from app.core.database import start_db, dispose_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await start_db()
    yield
    print('Disposing engine')
    await dispose_engine()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

origins = [
    # разрешенные источники
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    # сначапо все запрещаем    
    CORSMiddleware,
    # потом начинаем разрешать необходимое
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True
    )