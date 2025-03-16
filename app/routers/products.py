from fastapi import APIRouter, Depends, HTTPException


from app.schemas import ProductSchema, IdSchema, ProductCreateSchema
from app.core.database import SessionDep
from app.repositories import ProductRepository

router = APIRouter(tags=['Products'])


@router.get("/products", response_model=list[ProductSchema])
async def get_products(session: SessionDep) -> list[ProductSchema]:
	result = await ProductRepository.get_products(session)
	# return [product for product in result]
	return result


@router.get("/products/{product_id}")
async def get_product(session: SessionDep, product_id: int) -> ProductSchema:
	result = await ProductRepository.get_product(session, product_id)
	if result is None:
		raise HTTPException(status_code=404, detail="Product not found")
	return result

@router.post("/products", response_model=ProductSchema)
async def create_product(session: SessionDep, product: ProductCreateSchema = Depends()) -> ProductSchema:
	result = await ProductRepository.create_product(session, product)
	return result