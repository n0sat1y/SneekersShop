from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.database import SessionDep
from schemas import OrderItemSchema, OrderSchema
from utils import decode_jwt, validate_token_type
from repositories import OrderRepository

router = APIRouter(tags=['Orders'])
bearer = HTTPBearer()

@router.get('/orders')
async def get_user_orders(
	session: SessionDep,
	creds: HTTPAuthorizationCredentials = Depends(bearer),
	):
	decoded_token = decode_jwt(creds.credentials)
	token = validate_token_type(decoded_token, 'access')
	user_id = token.get('sub')
	if not user_id:
		raise HTTPException(status_code=401, detail='Invalid token')
	orders = await OrderRepository.get_orders(session, int(user_id))
	return orders

@router.post('/orders')
async def create_order(
	order: OrderSchema,
	creds: HTTPAuthorizationCredentials = Depends(bearer),
	):
	
	return order


