from datetime import datetime
import uuid
from pydantic import BaseModel


class OrderItemSchema(BaseModel):
	itemId: int
	size: int
	color: str
	price: int
	category: str
	gender: str
	# totalPrice: int
	name: str
	quantity: int

class OrderSchema(BaseModel):
	totalPrice: int
	products: list[OrderItemSchema]
	createdAt: datetime
	id: uuid.UUID
	userId: uuid.UUID
	status: str

class CreateItemOrderSchema(BaseModel):
	size: int
	color: str
	name: str
	quantity: int

class CreateOrderSchema(BaseModel):
	products: list[CreateItemOrderSchema]
	totalPrice: int
	status: str