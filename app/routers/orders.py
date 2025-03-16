from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.database import SessionDep
from schemas import CreateItemOrderSchema, OrderSchema,CreateOrderSchema, OrderItemSchema
from utils import decode_jwt, validate_token_type
from repositories import OrderRepository, ProductRepository

from .deps import token_dep

router = APIRouter(tags=['Orders'])

async def serialize_order_data(session, order):
	order_item_list = []
	for item in order.order_items:
		product = await ProductRepository.get_product(session, item.productId)
		order_item_schema = OrderItemSchema(
			itemId=item.productId,
			size=item.size,
			color=item.color,
			price=product.price,
			category=product.category,
			gender=product.gender,
			# totalPrice=product.price,
			name=product.name,
			quantity=item.quantity
		)
		order_item_list.append(order_item_schema)
		order_schema = OrderSchema(
			id=order.id,
			userId=order.userId,
			totalPrice=order.totalPrice,
			status=order.status,
			createdAt=order.created_at,
			products=order_item_list
		)
	return order_schema


@router.get('/orders')
async def get_user_orders(
	session: SessionDep,
	user_id = Depends(token_dep)
	) -> list[OrderSchema]:
	
	orders = await OrderRepository.get_orders(session, user_id)
	order_list = [await serialize_order_data(session, order) for order in orders]
	return order_list

@router.get('/order')
async def get_order(
	session: SessionDep,
	order_id: int,
	user = Depends(token_dep)
) -> OrderSchema:
	order = await OrderRepository.get_order_by_id(session, order_id)
	if not order:
		raise HTTPException(status_code=404, detail='Order not found')
	order_schema = await serialize_order_data(session, order)
	return order_schema


@router.post('/order')
async def create_order(
	session: SessionDep,
	order: CreateOrderSchema,
	user_id = Depends(token_dep),
	):
	created_order = await OrderRepository.create_order(session, order, user_id)
	selected_order = await OrderRepository.get_order_by_id(session, created_order.id)
	return selected_order


