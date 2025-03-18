import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.models import CartModel
from app.schemas import AddCartItemSchema


class CartRepository:	
	@classmethod
	async def add_cart_item(
		cls,
		session: AsyncSession,
		userId: int,
		item: AddCartItemSchema
	):
		try:
			cart_item = CartModel(
				userId=userId,
				**item.model_dump()
			)
			session.add(cart_item)
			await session.commit()
			await session.refresh(cart_item)
			return cart_item
		except Exception as e:
			await session.rollback()
			raise HTTPException(status_code=500, detail=str(e))
	
	@classmethod
	async def get_cart_item(cls,
		session: AsyncSession,
		userId: int,
		item: AddCartItemSchema	
	):
		try:
			stmt = select(CartModel).where(
				CartModel.userId == userId,
				CartModel.productId == item.productId,
				CartModel.size == item.size,
				CartModel.color == item.color
			)
			result = await session.execute(stmt)
			return result.scalar_one_or_none()
		except Exception as e:
			await session.rollback()
			raise HTTPException(status_code=500, detail=str(e))
	
	@classmethod
	async def update_quantity(cls, 
		session: AsyncSession, 
		cart_item: CartModel, 
		quantity: int
	):
		try:
			cart_item.quantity += quantity
			session.add(cart_item)
			await session.commit()
			await session.refresh(cart_item)
			return cart_item
		except Exception as e:
			await session.rollback()
			raise HTTPException(status_code=500, detail=str(e))
	
	@classmethod
	async def get_cart(cls, session: AsyncSession, userId: int):
		try:
			stmt = select(CartModel).where(CartModel.userId == userId)
			result = await session.execute(stmt)
			return result.scalars().all()
		except Exception as e:
				await session.rollback()
				raise HTTPException(status_code=500, detail=str(e))
	
	@classmethod
	async def delete_cart_item(
		cls,
		session: AsyncSession,
		item: CartModel
	):
		try:
			await session.delete(item)
			await session.commit()
			return None
		except Exception as e:
			await session.rollback()
			raise HTTPException(status_code=500, detail=str(e))

