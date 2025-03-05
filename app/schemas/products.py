from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
	name: str
	description: str
	colors: list[str]
	category: str
	gender: str
	sizes: list[int]
	price: int

class ProductSchema(ProductCreateSchema):
	id: int
	
class IdSchema(BaseModel):
	id: int
