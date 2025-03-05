import pytest

from app.core.batabase import engine, Base, session_fabric
from app.core.settings import settings
from app.models import *

@pytest.fixture(scope='session', autouse=True)
async def startup_database():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)
		
		yield
		await conn.run_sync(Base.metadata.drop_all)

	
@pytest.fixture(scope='function')
async def session():
	async with session_fabric() as session:
		yield session
