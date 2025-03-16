import pytest
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.settings import settings
from app.core.database import Base
# from app.models import ProductModel, UserModel, ReviewModel, CartModel, CartItemsModel, OrderModel, OrderItemsModel

from app.models.products import ProductModel
from app.models.users import UserModel, ReviewModel
from app.models.orders import OrderModel, OrderItemsModel
from app.models.carts import CartModel, CartItemsModel



engine = create_async_engine(settings.DB_URL)
test_session = async_sessionmaker(
	bind=engine,
	expire_on_commit=False,
	autoflush=False
)

@pytest.fixture(scope='session', autouse=True)
async def setup_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
	yield
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope='session')
async def db_session():
	async with test_session() as session:
		yield session
		session.rollback()
		session.close()


# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()
