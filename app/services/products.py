from repositories import ProductRepository
from core.batabase import session

from sqlalchemy.ext.asyncio import AsyncSession



class ProductServices:
	async def get_products(self):
		return await ProductRepository().get_products(session)
	
	async def get_product(self, product_id: int):
		return await ProductRepository().get_product(session, product_id)