from pydantic import BaseModel

class ProductSchema(BaseModel):
	id: int
	name: str
	description: str
	colors: list[str]
	category: str
	gender: str
	sizes: list[int]
	price: int
