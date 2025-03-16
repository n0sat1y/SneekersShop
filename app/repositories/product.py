from app.core.database import session
from app.models import ProductModel
from app.schemas import ProductCreateSchema

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class ProductRepository:
	@classmethod
	async def get_products(cls, session: AsyncSession):
		try:
			query = select(ProductModel)
			result = await session.execute(query)
			return result.scalars().all()
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))
	
	@classmethod
	async def get_product(cls, session: AsyncSession, product_id):
		try:
			query = select(ProductModel).where(ProductModel.id == product_id)
			result = await session.execute(query)
			return result.scalars().first()
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))
		
	@classmethod
	async def get_product_by_name(cls, session: AsyncSession, product_name: str):
		try:
			query = select(ProductModel).where(ProductModel.name == product_name)
			result = await session.execute(query)
			product = result.scalars().first()
			if not product:
				raise HTTPException(status_code=404, detail='Product not found')
			return product
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))
		
	@classmethod
	async def create_product(cls, session: AsyncSession, product: ProductCreateSchema):
		try:
			product_dict = product.model_dump()
			product_model = ProductModel(**product_dict)
			session.add(product_model)
			await session.commit()
			await session.refresh(product_model)
			return product_model
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))