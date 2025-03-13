from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models import OrderModel, OrderItemsModel
from schemas import CreateOrderSchema
from repositories import ProductRepository


class OrderRepository:
	@classmethod
	async def get_orders(cls, session: AsyncSession, user_id: int):
		try:
			query = select(OrderModel).options(selectinload(OrderModel.order_items)).where(OrderModel.userId == user_id)
			result = await session.execute(query)
			return result.scalars().all()
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))
		
	@classmethod
	async def create_order(cls, 
		session: AsyncSession, 
		order: CreateOrderSchema,
		user_id: int):
		try:
			order_model = OrderModel(
				userId=user_id, 
				totalPrice=order.totalPrice,
				status=order.status
			)
			order_items = order.products
			products = []
			for product in order_items:
				product_id = await ProductRepository.get_product_by_name(session, product.name)
				item = OrderItemsModel(
					productId=product_id.id,
					quantity=product.quantity,
					color=product.color,
					size=product.size
				)
				products.append(item)
			order_model.order_items = products
			session.add(order_model)
			await session.commit()
			await session.refresh(order_model)
			return order_model
		except Exception as e:
			await session.rollback()
			raise HTTPException(status_code=500, detail=str(e))
		
	@classmethod
	async def get_order_by_id(cls, 
		session: AsyncSession, 
		order_id: int
		):
		order_query = (
			select(OrderModel)
			.options(selectinload(OrderModel.order_items))
			.where(OrderModel.id==order_id)
		)
		result = await session.execute(order_query)
		return result.scalars().first()