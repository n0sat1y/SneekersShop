from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from schemas import OrderItemSchema, OrderSchema

router = APIRouter(tags=['Orders'])
bearer = HTTPBearer()

@router.get('/orders')
async def get_orders(creds: HTTPAuthorizationCredentials = Depends(bearer)):
	pass

@router.post('/orders')
async def create_order(
	order: OrderSchema,
	creds: HTTPAuthorizationCredentials = Depends(bearer),
	):
	
	return order


