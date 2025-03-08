from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends

from .settings import settings

engine = create_async_engine(
	url=settings.DB_URL,
	# echo=True
)
session_fabric = async_sessionmaker(engine, expire_on_commit=False)

async def session():
	async with session_fabric() as session:
		yield session

SessionDep = Annotated[AsyncSession, Depends(session)]

class Base(DeclarativeBase):
	pass


async def start_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)


async def dispose_engine():
	await engine.dispose()
