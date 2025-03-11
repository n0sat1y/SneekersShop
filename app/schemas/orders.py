from datetime import datetime
from pydantic import BaseModel


class OrderItemSchema(BaseModel):
	itemId: int
	size: int
	color: str
	price: int
	category: str
	gender: str
	totalPrice: int
	name: str
	quantity: int

class OrderSchema(BaseModel):
	totalPrice: int
	products: list[OrderItemSchema]
	createdAt: datetime
	id: int
	user_id: int
	status: str