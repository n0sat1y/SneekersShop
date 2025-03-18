from fastapi import APIRouter, Depends, HTTPException

from app.core.database import SessionDep
from app.routers.deps import token_dep
from app.schemas import AddCartItemSchema, CartItemSchema
from app.repositories import CartRepository

router = APIRouter(tags=['Carts'])


@router.get('/cart')
async def get_cart(
	session: SessionDep,
	user = Depends(token_dep)
) -> list[CartItemSchema]:
	cart = await CartRepository.get_cart(session, user)
	return cart

@router.post('/cart')
async def add_to_cart(
	item: AddCartItemSchema,
	session: SessionDep,
	user = Depends(token_dep)
) -> CartItemSchema:
	cart_item = await CartRepository.get_cart_item(session, user, item)
	if cart_item:
		model_item = await CartRepository.update_quantity(session, cart_item, item.quantity)
	else:
		model_item = await CartRepository.add_cart_item(session=session, userId=user, item=item)
	return model_item
	
@router.delete('/cart')
async def delete_cart_item(
	item: AddCartItemSchema,
	session: SessionDep,
	user = Depends(token_dep)
):
	cart_item = await CartRepository.get_cart_item(session, user, item)
	if cart_item:
		await CartRepository.delete_cart_item(session, cart_item)
		return {'message': 'Item deleted'}
	raise HTTPException(status_code=404, detail='Item not found')