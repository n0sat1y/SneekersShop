from pydantic import BaseModel

class AddCartItemSchema(BaseModel):
	productId: int
	quantity: int
	color: str
	size: int

class CartItemSchema(AddCartItemSchema):
	id: int