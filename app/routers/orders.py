from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.database import SessionDep
from schemas import CreateItemOrderSchema, OrderSchema,CreateOrderSchema
from utils import decode_jwt, validate_token_type
from repositories import OrderRepository, ProductRepository

from .deps import token_dep

router = APIRouter(tags=['Orders'])


@router.get('/orders')
async def get_user_orders(
	session: SessionDep,
	user_id = Depends(token_dep)
	):
	
	orders = await OrderRepository.get_orders(session, user_id)
	return orders

@router.get('/order')
async def get_order(
	session: SessionDep,
	order_id: int,
	user = Depends(token_dep)
):
	order = await OrderRepository.get_order_by_id(session, order_id)
	if not order:
		raise HTTPException(status_code=404, detail='Order not found')
	return order



@router.post('/order')
async def create_order(
	session: SessionDep,
	order: CreateOrderSchema,
	user_id = Depends(token_dep),
	):
	created_order = await OrderRepository.create_order(session, order, user_id)
	selected_order = await OrderRepository.get_order_by_id(session, created_order.id)
	return selected_order


