from core.batabase import session
from models import ProductModel

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class ProductRepository:
	@classmethod
	async def get_products(cls, session: AsyncSession):
		query = select(ProductModel)
		result = await session.execute(query)
		return result.scalars().all()
	
	@classmethod
	async def get_product(cls, session: AsyncSession, product_id: int):
		query = select(ProductModel).where(ProductModel.id == product_id)
		result = await session.execute(query)
		return result.scalars().first()