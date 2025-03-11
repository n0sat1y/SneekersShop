from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import OrderModel


class OrderRepository:
	@classmethod
	async def get_orders(cls, session: AsyncSession, user_id: int):
		try:
			query = select(OrderModel).where(OrderModel.userId == user_id)
			result = await session.execute(query)
			return result.scalars().all()
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))